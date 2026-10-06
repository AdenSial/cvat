
# Annotation Analytics — Plan

 Branch: dev-test01

## Goal

Add annotation analytics to CVAT by providing an authenticated API endpoint that returns annotation counts grouped by class for a task, and a web page that displays those counts as a graph.

## Order of Work

### 1. Understand the existing CVAT structure

Inspect the existing Django backend, task/job/annotation models, authentication and permission mechanisms, and the frontend structure.

### 2. Create the backend Django app

Create the required Django app named `test` and identify the correct place for the analytics endpoint.

### 3. Implement the annotation count API

Add an API endpoint that:

* accepts a task identifier;
* verifies that the requester is logged in;
* verifies that the requester has access to the task;
* reads annotation data from the database;
* returns the number of annotations for each class.

### 4. Verify the API

Test the endpoint against a task containing known COCO annotations and verify that the returned counts match the database data.

### 5. Build the frontend page

Add a page/component in the existing CVAT web interface that calls the analytics endpoint and displays the returned counts.

### 6. Handle failure cases

Implement clear frontend states for:

* no annotations/data;
* failed API request.

### 7. Measure endpoint performance

Choose a measurable response-time target, run five measurements under documented conditions, calculate the median and spread, and record the raw results.

### 8. Add one grouping/filter

Add one useful grouping or filter beyond the basic per-class count. The choice will be based on what can be implemented cleanly within the remaining time.

### 9. Real-time updates

Only after the earlier requirements are working, investigate updating the graph over WebSocket when annotations change and recovering from a dropped connection.

### 10. Document the final decision

If the real-time portion is reached, document the approach chosen, an approach considered and rejected, and the cost of rejecting it.

## Time Allocation

| Work                                            | Planned Time |
| ----------------------------------------------- | -----------: |
| Repository exploration and setup                |       30 min |
| Backend/API                                     |         2 hr |
| API verification and authentication/permissions |         1 hr |
| Frontend graph and states                       |       1.5 hr |
| Performance measurement                         |       45 min |
| Filter/grouping                                 |       45 min |
| WebSocket/reconnection, if time remains         |         1 hr |
| Final testing, documentation and recording      |       30 min |

## Initial Scope Decision

The first priority is requirements 1–4 because they are the minimum assessed floor. Real-time WebSocket updates and reconnection will not be started until the basic API, graph, empty state and error state are working.

The implementation will stay contained within the required `test` Django app and the necessary frontend files.

## Sample Data

Use the COCO 2017 validation dataset supplied by the assessment.

## Commits


