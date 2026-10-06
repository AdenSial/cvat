# Definition of Done

This checklist defines the evidence required to consider the assessment complete. An item is only considered done when its evidence is recorded.

| #  | Requirement                                                                                                  | Status | Evidence                                                                                                |
| -- | ------------------------------------------------------------------------------------------------------------ | ------ | ------------------------------------------------------------------------------------------------------- |
| 1  | API endpoint returns annotation counts grouped by class for a task from the database.                        | [ ]    |                                                                                                         |
| 2  | API result has been checked against a known task and database result.                                        | [ ]    | Task #1 currently contains 1090 `LabeledShape` records; database grouping result will be recorded here. |
| 3  | Authenticated user with access to the task can call the endpoint successfully.                               | [ ]    |                                                                                                         |
| 4  | Unauthenticated request is refused by CVAT authentication.                                                   | [ ]    |                                                                                                         |
| 5  | Authenticated user without access to the task is refused by CVAT task permissions.                           | [ ]    |                                                                                                         |
| 6  | A web interface page calls the annotation statistics endpoint.                                               | [ ]    |                                                                                                         |
| 7  | Annotation counts are displayed as a graph.                                                                  | [ ]    |                                                                                                         |
| 8  | The page has a clear empty/no-data state.                                                                    | [ ]    |                                                                                                         |
| 9  | The page has a clear failed-request/error state.                                                             | [ ]    |                                                                                                         |
| 10 | API response-time objective is measured using five runs with raw output, median and spread recorded.         | [ ]    | `docs/OBJECTIVES.md`                                                                                    |
| 11 | Response-time target is reported as met or missed with an explanation.                                       | [ ]    | `docs/OBJECTIVES.md`                                                                                    |
| 12 | One useful filter or grouping beyond the plain per-class count is implemented and its purpose is documented. | [ ]    |                                                                                                         |
| 13 | Graph updates live when annotations change over WebSocket.                                                   | [ ]    |                                                                                                         |
| 14 | Page recovers after the WebSocket connection drops and reconnects.                                           | [ ]    |                                                                                                         |
| 15 | Final work is split across meaningful commits rather than one large final commit.                            | [ ]    | `git log --oneline`                                                                                     |
| 16 | All unfinished requirements are explicitly listed with a reason.                                             | [ ]    | Final section below                                                                                     |

## Known Validation Data

The primary validation task is:

* Task ID: `1`
* Task name: `COCO Analytics Test`
* Frames: `135`
* Job ID: `1`
* LabeledShape records: `1090`

The initial database grouping was verified manually before implementation. The result will be used as the reference for validating the API.

## Completion Notes

This section will be completed at the end of the assessment.

### Finished

To be completed.

### Not Finished

To be completed. Each unfinished requirement will include the reason it was not reached.

### Final Evidence

Relevant commit SHAs, API test output, timing output, screenshots or URLs will be recorded here.
