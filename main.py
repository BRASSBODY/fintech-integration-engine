from enum import Enum
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field

app = FastAPI(
    title="FinTech Integration Middleware",
    description="Webhook Receiver and Payload Transformation Service",
    version="1.0.0",
)


class VendorStatus(str, Enum):
    SUCCESS = "SUCCESS"
    FAILED = "FAILED"
    PENDING = "PENDING"


class ExternalPaymentPayload(BaseModel):
    vendor_transaction_id: str = Field(..., example="TXN-VENDOR-99812")
    user_reference: str = Field(..., example="USR-4421")
    amount_in_kobo: int = Field(..., gt=0, example=500000)
    currency: str = Field(default="NGN", example="NGN")
    status: VendorStatus
    signature: str = Field(..., example="a8f9c123d4e5f667")


class InternalPaymentEvent(BaseModel):
    transaction_id: str
    user_id: str
    amount_naira: float
    status: str
    is_processed: bool = False


@app.post(
    "/webhook/v1/payments",
    status_code=status.HTTP_202_ACCEPTED,
    summary="Receive external payment callbacks",
)
async def receive_payment_webhook(payload: ExternalPaymentPayload):
    if payload.currency != "NGN":
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Unsupported currency: {payload.currency}. Only NGN is accepted.",
        )

    internal_event = InternalPaymentEvent(
        transaction_id=payload.vendor_transaction_id,
        user_id=payload.user_reference,
        amount_naira=payload.amount_in_kobo / 100.0,
        status=payload.status.value,
    )

    print(f"\n[INTEGRATION ENGINE] Received Webhook Payload:")
    print(f" -> Vendor Txn ID : {payload.vendor_transaction_id}")
    print(f" -> Converted Amt  : NGN {internal_event.amount_naira:,.2f}")
    print(f" -> Status         : {internal_event.status}")

    return {
        "status": "accepted",
        "message": "Webhook received and queued for integration processing.",
        "internal_reference": internal_event.transaction_id,
    }


@app.get("/health", status_code=status.HTTP_200_OK)
async def health_check():
    return {"status": "healthy", "service": "integration-middleware"}