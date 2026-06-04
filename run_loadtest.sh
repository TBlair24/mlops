#!/bin/bash
set -e

echo "Starting Flask app in background..."
gunicorn --bind 0.0.0.0:8080 app:app --daemon

echo "Waiting for app to start..."
sleep 5

echo "Running load test..."
locust -f locustfile.py \
    --host=http://localhost:8080 \
    --headless \
    --users 20 \
    --spawn-rate 5 \
    --run-time 60s \
    --csv=loadtest_results

echo ""
echo "=== Load Test Results ==="
cat loadtest_results_stats.csv
echo ""

# Fail if any requests failed
FAILURES=$(tail -1 loadtest_results_stats.csv | awk -F',' '{print $4}')
if [ "$FAILURES" != "0" ] && [ "$FAILURES" != "Failure Count"];
then
    echo "Load test had $FAILURES failures. Failing the test."
    exit 1
fi

    echo "Load test completed successfully with no failures."
