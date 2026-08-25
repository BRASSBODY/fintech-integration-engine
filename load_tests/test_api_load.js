// load_tests/test_api_load.js
import http from 'k6/http';
import { check, sleep } from 'k6';

// 1. CONFIGURATION OPTIONS
export const options = {
  // Ramp up to 10 virtual users over 10s, hold for 20s, ramp down over 10s
  stages: [
    { duration: '10s', target: 10 },
    { duration: '20s', target: 10 },
    { duration: '10s', target: 0 },
  ],
  // Performance Thresholds (SLA validation)
  thresholds: {
    http_req_duration: ['p(95)<500'], // 95% of requests must complete below 500ms
    http_req_failed: ['rate<0.01'],   // Error rate must be under 1%
  },
};

// 2. VIRTUAL USER WORKFLOW
export default function () {
  const res = http.get('https://jsonplaceholder.typicode.com/posts/1');

  // Functional assertions on response
  check(res, {
    'status is 200': (r) => r.status === 200,
    'transaction time OK': (r) => r.timings.duration < 500,
  });

  sleep(1); // 1-second think time between requests
}