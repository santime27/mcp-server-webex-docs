# Webex Messaging: All APIs Documentation & Schema Reference

This document is an automated structured reference of all API endpoints under **Webex Messaging: All APIs**, including OpenAPI specifications, HTTP methods, paths, parameters, request body schemas, and response schemas.

## Table of Contents

- [1. Attachment Actions](#1-attachment-actions)
- [2. ECM folder linking](#2-ecm-folder-linking)
- [3. Events](#3-events)
- [4. Hybrid Data Security (HDS)](#4-hybrid-data-security-hds)
- [5. Memberships](#5-memberships)
- [6. Messages](#6-messages)
- [7. People](#7-people)
- [8. Room Tabs](#8-room-tabs)
- [9. Rooms](#9-rooms)
- [10. Team Memberships](#10-team-memberships)
- [11. Teams](#11-teams)
- [12. Webhooks](#12-webhooks)

---

## 1. Attachment Actions

### 1.1 Attachment Actions: Create an Attachment Action

**Endpoint:** `POST /attachment/actions`

Create a new attachment action.

#### Request Body Schema

```json
{
  "type": "object",
  "required": [
    "type",
    "messageId",
    "inputs"
  ],
  "properties": {
    "type": {
      "type": "string",
      "enum": [
        "submit"
      ],
      "description": "The type of action to perform. Valid values are 'submit'"
    },
    "messageId": {
      "type": "string",
      "example": "GFyazovL3VzL1BFT1BMRS80MDNlZmUwNy02Yzc3LTQyY2UtOWI4NC",
      "description": "The ID of the message which contains the attachment."
    },
    "inputs": {
      "type": "object",
      "properties": {
        "Name": {
          "type": "string",
          "example": "John Andersen"
        },
        "Url": {
          "type": "string",
          "example": "https://example.com"
        },
        "Email": {
          "type": "string",
          "example": "john.andersen@example.com"
        },
        "Tel": {
          "type": "string",
          "example": "+1 408 555 7209"
        }
      },
      "description": "The attachment action's inputs."
    }
  },
  "$$ref": "#/components/schemas/SubmitCardAction"
}
```

#### Responses

- **`202`** — Accepted
  ```json
  {
    "type": "object",
    "required": [
      "type",
      "messageId"
    ],
    "properties": {
      "id": {
        "type": "string",
        "example": "Y2lzY29zcGFyazovL3VzL0NBTExTLzU0MUFFMzBFLUUyQzUtNERENi04NTM4LTgzOTRDODYzM0I3MQo",
        "description": "A unique identifier for the action."
      },
      "personId": {
        "type": "string",
        "example": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS83MTZlOWQxYy1jYTQ0LTRmZ",
        "description": "The ID of the person who performed the action."
      },
      "roomId": {
        "type": "string",
        "example": "L3VzL1BFT1BMRS80MDNlZmUwNy02Yzc3LTQyY2UtOWI",
        "description": "The ID of the room in which the action was performed."
      },
      "type": {
        "type": "string",
        "enum": [
          "submit"
        ],
        "description": "The type of action performed."
      },
      "messageId": {
        "type": "string",
        "example": "GFyazovL3VzL1BFT1BMRS80MDNlZmUwNy02Yzc3LTQyY2UtOWI4NC",
        "description": "The parent message on which the attachment action was performed."
      },
      "inputs": {
        "type": "object",
        "properties": {
          "Name": {
            "type": "string",
            "example": "John Andersen"
          },
          "Url": {
            "type": "string",
            "example": "https://example.com"
          },
          "Email": {
            "type": "string",
            "example": "john.andersen@example.com"
          },
          "Tel": {
            "type": "string",
            "example": "+1 408 555 7209"
          }
        },
        "description": "The action's inputs."
      },
      "created": {
        "type": "string",
        "example": "2016-05-10T19:41:00.100Z",
        "description": "The date and time the action was created."
      }
    },
    "$$ref": "#/components/schemas/AttachmentActivity"
  }
  ```
- **`400`** — Bad Request
- **`401`** — Unauthorized: Authentication credentials were missing or incorrect.
- **`403`** — Forbidden: The request is understood, but it has been refused or access is not allowed.
- **`404`** — Not Found
- **`405`** — Method Not Allowed: The request was made to a resource using an HTTP request method that is not supported.
- **`409`** — Conflict: The request could not be processed because it conflicts with some established rule of the system. For example, a person may not be added to a room more than once.
- **`410`** — Gone: The requested resource is no longer available.
- **`415`** — Unsupported Media Type: The request was made to a resource without specifying a media type or used a media type that is not supported.
- **`423`** — Locked: The requested resource is temporarily unavailable. A Retry-After header may be present that specifies how many seconds you need to wait before attempting the request again.
- **`428`** — Precondition Required: File(s) cannot be scanned for malware and need to be force downloaded.
- **`429`** — Too Many Requests: Too many requests have been sent in a given amount of time and the request has been rate limited. A Retry-After header should be present that specifies how many seconds you need to wait before a successful request can be made.
- **`500`** — Internal Server Error: Something went wrong on the server. If the issue persists, feel free to contact the [Webex Developer Support team](/explore/support).
- **`502`** — Bad Gateway: The server received an invalid response from an upstream server while processing the request. Try again later.
- **`503`** — Service Unavailable: Server is overloaded with requests. Try again later.
- **`504`** — Gateway Timeout: An upstream server failed to respond on time. If your query uses max parameter, please try to reduce it.

---

### 1.2 Attachment Actions: Get Attachment Action Details

**Endpoint:** `GET /attachment/actions/{id}`

Shows details for a attachment action, by ID.

Specify the attachment action ID in the `id` URI parameter.

#### Parameters

| Name | In | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| `id` | `path` | `string` | Yes | A unique identifier for the attachment action. |

#### Responses

- **`200`** — OK
  ```json
  {
    "type": "object",
    "required": [
      "type",
      "messageId"
    ],
    "properties": {
      "id": {
        "type": "string",
        "example": "Y2lzY29zcGFyazovL3VzL0NBTExTLzU0MUFFMzBFLUUyQzUtNERENi04NTM4LTgzOTRDODYzM0I3MQo",
        "description": "A unique identifier for the action."
      },
      "personId": {
        "type": "string",
        "example": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS83MTZlOWQxYy1jYTQ0LTRmZ",
        "description": "The ID of the person who performed the action."
      },
      "roomId": {
        "type": "string",
        "example": "L3VzL1BFT1BMRS80MDNlZmUwNy02Yzc3LTQyY2UtOWI",
        "description": "The ID of the room in which the action was performed."
      },
      "type": {
        "type": "string",
        "enum": [
          "submit"
        ],
        "description": "The type of action performed."
      },
      "messageId": {
        "type": "string",
        "example": "GFyazovL3VzL1BFT1BMRS80MDNlZmUwNy02Yzc3LTQyY2UtOWI4NC",
        "description": "The parent message on which the attachment action was performed."
      },
      "inputs": {
        "type": "object",
        "properties": {
          "Name": {
            "type": "string",
            "example": "John Andersen"
          },
          "Url": {
            "type": "string",
            "example": "https://example.com"
          },
          "Email": {
            "type": "string",
            "example": "john.andersen@example.com"
          },
          "Tel": {
            "type": "string",
            "example": "+1 408 555 7209"
          }
        },
        "description": "The action's inputs."
      },
      "created": {
        "type": "string",
        "example": "2016-05-10T19:41:00.100Z",
        "description": "The date and time the action was created."
      }
    },
    "$$ref": "#/components/schemas/AttachmentActivity"
  }
  ```
- **`400`** — Bad Request: The request was invalid or cannot be otherwise served. An accompanying error message will explain further.
- **`401`** — Unauthorized: Authentication credentials were missing or incorrect.
- **`403`** — Forbidden: The request is understood, but it has been refused or access is not allowed.
- **`404`** — Not Found: The URI requested is invalid or the resource requested, such as a user, does not exist. Also returned when the requested format is not supported by the requested method.
- **`405`** — Method Not Allowed: The request was made to a resource using an HTTP request method that is not supported.
- **`409`** — Conflict: The request could not be processed because it conflicts with some established rule of the system. For example, a person may not be added to a room more than once.
- **`410`** — Gone: The requested resource is no longer available.
- **`415`** — Unsupported Media Type: The request was made to a resource without specifying a media type or used a media type that is not supported.
- **`423`** — Locked: The requested resource is temporarily unavailable. A Retry-After header may be present that specifies how many seconds you need to wait before attempting the request again.
- **`428`** — Precondition Required: File(s) cannot be scanned for malware and need to be force downloaded.
- **`429`** — Too Many Requests: Too many requests have been sent in a given amount of time and the request has been rate limited. A Retry-After header should be present that specifies how many seconds you need to wait before a successful request can be made.
- **`500`** — Internal Server Error: Something went wrong on the server. If the issue persists, feel free to contact the [Webex Developer Support team](/explore/support).
- **`502`** — Bad Gateway: The server received an invalid response from an upstream server while processing the request. Try again later.
- **`503`** — Service Unavailable: Server is overloaded with requests. Try again later.
- **`504`** — Gateway Timeout: An upstream server failed to respond on time. If your query uses max parameter, please try to reduce it.

---

## 2. ECM folder linking

### 2.1 ECM folder linking: Create an ECM folder configuration

**Endpoint:** `POST /room/linkedFolders`

Adds an existing ECM folder to a room as (default or reference) file storage. There is no data validation happening for the request. Please ensure the correct `driveId` and `itemId.` These can be collected from the MS Graph API. The `contentUrl` and `displayName` are used only for user convenience. The folder will be configured with the MS folder name as `displayName`, and the `contentURL` may be updated or corrected as needed. To assess final configuration, please make a GET request on the linkedFolder.

#### Request Body Schema

```json
{
  "type": "object",
  "required": [
    "roomId",
    "contentUrl",
    "displayName",
    "driveId",
    "itemId",
    "defaultFolder"
  ],
  "properties": {
    "roomId": {
      "type": "string",
      "example": "Y2lzY29zcGFyazovL3VzL1JPT00vYmJjZWIxYWQtNDNmMS0zYjU4LTkxNDctZjE0YmIwYzRkMTU0",
      "description": "A unique identifier for the room."
    },
    "contentUrl": {
      "type": "string",
      "example": "https://cisco-my.sharepoint.com/personal/naalluri/123",
      "description": "URL of the ECM folder."
    },
    "displayName": {
      "type": "string",
      "example": "OneDrive folder for shared documents",
      "description": "This should match the folder name in the ECM backend."
    },
    "driveId": {
      "type": "string",
      "example": "123",
      "description": "Sharepoint or OneDrive drive id. It can be queried via MS Graph APIs."
    },
    "itemId": {
      "type": "string",
      "example": "456",
      "description": "Sharepoint or OneDrive item id. It can be queried via MS Graph APIs."
    },
    "defaultFolder": {
      "type": "string",
      "example": "false",
      "description": "Makes the folder the default storage for the space."
    }
  }
}
```

#### Responses

- **`200`** — OK
  ```json
  {
    "type": "object",
    "required": [
      "driveId",
      "itemId",
      "displayName"
    ],
    "properties": {
      "id": {
        "type": "string",
        "example": "Y2lzY29zcGFyazovL3VybjpURUFNOnVzLWVhc3QtMl9hL1RBQlMvZDg1ZTYwNj",
        "description": "A unique identifier for the folder."
      },
      "roomId": {
        "type": "string",
        "example": "Y2lzY29zcGFyazovL3VzL1JPT00vYmJjZWIxYWQtNDNmMS0zYjU4LTkxNDctZjE0YmIwYzRkMTU0",
        "description": "A unique identifier for the room to which the folder should be linked to."
      },
      "roomType": {
        "type": "string",
        "enum": [
          "direct",
          "group"
        ],
        "description": "The room type.\n * `direct` - 1:1 room\n * `group` - group room\n"
      },
      "driveId": {
        "type": "string",
        "example": "123",
        "description": "Sharepoint or OneDrive drive id. It can be queried via MS Graph APIs."
      },
      "itemId": {
        "type": "string",
        "example": "456",
        "description": "Sharepoint or OneDrive item id. It can be queried via MS Graph APIs."
      },
      "defaultFolder": {
        "type": "string",
        "example": "false",
        "description": "Indicates if this is the default content storage for the room."
      },
      "displayName": {
        "type": "string",
        "example": "OneDrive folder for shared documents",
        "description": "This should match the folder name in the ECM backend."
      },
      "contentUrl": {
        "type": "string",
        "example": "https://cisco-my.sharepoint.com/personal/naalluri/123",
        "description": "Folder's content URL."
      },
      "creatorId": {
        "type": "string",
        "example": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS9mNWIzNjE4Ny1jOGRkLTQ3MjctOGIyZi1mOWM0NDdmMjkwNDY",
        "description": "The person ID of the person who created this folder link."
      },
      "created": {
        "type": "string",
        "example": "2015-10-18T14:26:16.203Z",
        "description": "The date and time when the folder link was created."
      }
    },
    "$$ref": "#/components/schemas/ECMFolder"
  }
  ```
- **`400`** — Bad Request: The request was invalid or cannot be otherwise served. An accompanying error message will explain further.
- **`401`** — Unauthorized: Authentication credentials were missing or incorrect.
- **`403`** — Forbidden: The request is understood, but it has been refused or access is not allowed.
- **`404`** — Not Found: The URI requested is invalid or the resource requested, such as a user, does not exist. Also returned when the requested format is not supported by the requested method.
- **`405`** — Method Not Allowed: The request was made to a resource using an HTTP request method that is not supported.
- **`409`** — Conflict: The request could not be processed because it conflicts with some established rule of the system. For example, a person may not be added to a room more than once.
- **`410`** — Gone: The requested resource is no longer available.
- **`415`** — Unsupported Media Type: The request was made to a resource without specifying a media type or used a media type that is not supported.
- **`423`** — Locked: The requested resource is temporarily unavailable. A Retry-After header may be present that specifies how many seconds you need to wait before attempting the request again.
- **`428`** — Precondition Required: File(s) cannot be scanned for malware and need to be force downloaded.
- **`429`** — Too Many Requests: Too many requests have been sent in a given amount of time and the request has been rate limited. A Retry-After header should be present that specifies how many seconds you need to wait before a successful request can be made.
- **`500`** — Internal Server Error: Something went wrong on the server. If the issue persists, feel free to contact the [Webex Developer Support team](/explore/support).
- **`502`** — Bad Gateway: The server received an invalid response from an upstream server while processing the request. Try again later.
- **`503`** — Service Unavailable: Server is overloaded with requests. Try again later.
- **`504`** — Gateway Timeout: An upstream server failed to respond on time. If your query uses max parameter, please try to reduce it.

---

### 2.2 ECM folder linking: Get ECM Folder Details

**Endpoint:** `GET /room/linkedFolders/{id}`

Get details for a room ECM folder with the specified folder id.

#### Parameters

| Name | In | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| `id` | `path` | `string` | Yes | The unique identifier for the folder. |

#### Responses

- **`200`** — OK
  ```json
  {
    "type": "object",
    "required": [
      "driveId",
      "itemId",
      "displayName"
    ],
    "properties": {
      "id": {
        "type": "string",
        "example": "Y2lzY29zcGFyazovL3VybjpURUFNOnVzLWVhc3QtMl9hL1RBQlMvZDg1ZTYwNj",
        "description": "A unique identifier for the folder."
      },
      "roomId": {
        "type": "string",
        "example": "Y2lzY29zcGFyazovL3VzL1JPT00vYmJjZWIxYWQtNDNmMS0zYjU4LTkxNDctZjE0YmIwYzRkMTU0",
        "description": "A unique identifier for the room to which the folder should be linked to."
      },
      "roomType": {
        "type": "string",
        "enum": [
          "direct",
          "group"
        ],
        "description": "The room type.\n * `direct` - 1:1 room\n * `group` - group room\n"
      },
      "driveId": {
        "type": "string",
        "example": "123",
        "description": "Sharepoint or OneDrive drive id. It can be queried via MS Graph APIs."
      },
      "itemId": {
        "type": "string",
        "example": "456",
        "description": "Sharepoint or OneDrive item id. It can be queried via MS Graph APIs."
      },
      "defaultFolder": {
        "type": "string",
        "example": "false",
        "description": "Indicates if this is the default content storage for the room."
      },
      "displayName": {
        "type": "string",
        "example": "OneDrive folder for shared documents",
        "description": "This should match the folder name in the ECM backend."
      },
      "contentUrl": {
        "type": "string",
        "example": "https://cisco-my.sharepoint.com/personal/naalluri/123",
        "description": "Folder's content URL."
      },
      "creatorId": {
        "type": "string",
        "example": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS9mNWIzNjE4Ny1jOGRkLTQ3MjctOGIyZi1mOWM0NDdmMjkwNDY",
        "description": "The person ID of the person who created this folder link."
      },
      "created": {
        "type": "string",
        "example": "2015-10-18T14:26:16.203Z",
        "description": "The date and time when the folder link was created."
      }
    },
    "$$ref": "#/components/schemas/ECMFolder"
  }
  ```
- **`400`** — Bad Request: The request was invalid or cannot be otherwise served. An accompanying error message will explain further.
- **`401`** — Unauthorized: Authentication credentials were missing or incorrect.
- **`403`** — Forbidden: The request is understood, but it has been refused or access is not allowed.
- **`404`** — Not Found: The URI requested is invalid or the resource requested, such as a user, does not exist. Also returned when the requested format is not supported by the requested method.
- **`405`** — Method Not Allowed: The request was made to a resource using an HTTP request method that is not supported.
- **`409`** — Conflict: The request could not be processed because it conflicts with some established rule of the system. For example, a person may not be added to a room more than once.
- **`410`** — Gone: The requested resource is no longer available.
- **`415`** — Unsupported Media Type: The request was made to a resource without specifying a media type or used a media type that is not supported.
- **`423`** — Locked: The requested resource is temporarily unavailable. A Retry-After header may be present that specifies how many seconds you need to wait before attempting the request again.
- **`428`** — Precondition Required: File(s) cannot be scanned for malware and need to be force downloaded.
- **`429`** — Too Many Requests: Too many requests have been sent in a given amount of time and the request has been rate limited. A Retry-After header should be present that specifies how many seconds you need to wait before a successful request can be made.
- **`500`** — Internal Server Error: Something went wrong on the server. If the issue persists, feel free to contact the [Webex Developer Support team](/explore/support).
- **`502`** — Bad Gateway: The server received an invalid response from an upstream server while processing the request. Try again later.
- **`503`** — Service Unavailable: Server is overloaded with requests. Try again later.
- **`504`** — Gateway Timeout: An upstream server failed to respond on time. If your query uses max parameter, please try to reduce it.

---

### 2.3 ECM folder linking: List ECM folder

**Endpoint:** `GET /room/linkedFolders`

Lists the ECM folder of a room specified by the `roomId` query parameter.

#### Parameters

| Name | In | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| `roomId` | `query` | `string` | Yes | ID of the room for which to list the ECM folder. |

#### Responses

- **`200`** — OK
  ```json
  {
    "type": "object",
    "properties": {
      "items": {
        "type": "array",
        "items": {
          "type": "object",
          "required": [
            "driveId",
            "itemId",
            "displayName"
          ],
          "properties": {
            "id": {
              "type": "string",
              "example": "Y2lzY29zcGFyazovL3VybjpURUFNOnVzLWVhc3QtMl9hL1RBQlMvZDg1ZTYwNj",
              "description": "A unique identifier for the folder."
            },
            "roomId": {
              "type": "string",
              "example": "Y2lzY29zcGFyazovL3VzL1JPT00vYmJjZWIxYWQtNDNmMS0zYjU4LTkxNDctZjE0YmIwYzRkMTU0",
              "description": "A unique identifier for the room to which the folder should be linked to."
            },
            "roomType": {
              "type": "string",
              "enum": [
                "direct",
                "group"
              ],
              "description": "The room type.\n * `direct` - 1:1 room\n * `group` - group room\n"
            },
            "driveId": {
              "type": "string",
              "example": "123",
              "description": "Sharepoint or OneDrive drive id. It can be queried via MS Graph APIs."
            },
            "itemId": {
              "type": "string",
              "example": "456",
              "description": "Sharepoint or OneDrive item id. It can be queried via MS Graph APIs."
            },
            "defaultFolder": {
              "type": "string",
              "example": "false",
              "description": "Indicates if this is the default content storage for the room."
            },
            "displayName": {
              "type": "string",
              "example": "OneDrive folder for shared documents",
              "description": "This should match the folder name in the ECM backend."
            },
            "contentUrl": {
              "type": "string",
              "example": "https://cisco-my.sharepoint.com/personal/naalluri/123",
              "description": "Folder's content URL."
            },
            "creatorId": {
              "type": "string",
              "example": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS9mNWIzNjE4Ny1jOGRkLTQ3MjctOGIyZi1mOWM0NDdmMjkwNDY",
              "description": "The person ID of the person who created this folder link."
            },
            "created": {
              "type": "string",
              "example": "2015-10-18T14:26:16.203Z",
              "description": "The date and time when the folder link was created."
            }
          },
          "$$ref": "#/components/schemas/ECMFolder"
        }
      }
    },
    "$$ref": "#/components/schemas/ECMFolderCollectionResponse"
  }
  ```
- **`400`** — Bad Request: The request was invalid or cannot be otherwise served. An accompanying error message will explain further.
- **`401`** — Unauthorized: Authentication credentials were missing or incorrect.
- **`403`** — Forbidden: The request is understood, but it has been refused or access is not allowed.
- **`404`** — Not Found: The URI requested is invalid or the resource requested, such as a user, does not exist. Also returned when the requested format is not supported by the requested method.
- **`405`** — Method Not Allowed: The request was made to a resource using an HTTP request method that is not supported.
- **`409`** — Conflict: The request could not be processed because it conflicts with some established rule of the system. For example, a person may not be added to a room more than once.
- **`410`** — Gone: The requested resource is no longer available.
- **`415`** — Unsupported Media Type: The request was made to a resource without specifying a media type or used a media type that is not supported.
- **`423`** — Locked: The requested resource is temporarily unavailable. A Retry-After header may be present that specifies how many seconds you need to wait before attempting the request again.
- **`428`** — Precondition Required: File(s) cannot be scanned for malware and need to be force downloaded.
- **`429`** — Too Many Requests: Too many requests have been sent in a given amount of time and the request has been rate limited. A Retry-After header should be present that specifies how many seconds you need to wait before a successful request can be made.
- **`500`** — Internal Server Error: Something went wrong on the server. If the issue persists, feel free to contact the [Webex Developer Support team](/explore/support).
- **`502`** — Bad Gateway: The server received an invalid response from an upstream server while processing the request. Try again later.
- **`503`** — Service Unavailable: Server is overloaded with requests. Try again later.
- **`504`** — Gateway Timeout: An upstream server failed to respond on time. If your query uses max parameter, please try to reduce it.

---

### 2.4 ECM folder linking: Unlink an ECM linked folder

**Endpoint:** `DELETE /room/linkedFolders/{id}`

Unlinks the room-linked folder with the specified ID from the space.

#### Parameters

| Name | In | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| `id` | `path` | `string` | Yes | The unique identifier for the folder to disassociate from the space. |

#### Responses

- **`204`** — No Content
- **`400`** — Bad Request: The request was invalid or cannot be otherwise served. An accompanying error message will explain further.
- **`401`** — Unauthorized: Authentication credentials were missing or incorrect.
- **`403`** — Forbidden: The request is understood, but it has been refused or access is not allowed.
- **`404`** — Not Found: The URI requested is invalid or the resource requested, such as a user, does not exist. Also returned when the requested format is not supported by the requested method.
- **`405`** — Method Not Allowed: The request was made to a resource using an HTTP request method that is not supported.
- **`409`** — Conflict: The request could not be processed because it conflicts with some established rule of the system. For example, a person may not be added to a room more than once.
- **`410`** — Gone: The requested resource is no longer available.
- **`415`** — Unsupported Media Type: The request was made to a resource without specifying a media type or used a media type that is not supported.
- **`423`** — Locked: The requested resource is temporarily unavailable. A Retry-After header may be present that specifies how many seconds you need to wait before attempting the request again.
- **`428`** — Precondition Required: File(s) cannot be scanned for malware and need to be force downloaded.
- **`429`** — Too Many Requests: Too many requests have been sent in a given amount of time and the request has been rate limited. A Retry-After header should be present that specifies how many seconds you need to wait before a successful request can be made.
- **`500`** — Internal Server Error: Something went wrong on the server. If the issue persists, feel free to contact the [Webex Developer Support team](/explore/support).
- **`502`** — Bad Gateway: The server received an invalid response from an upstream server while processing the request. Try again later.
- **`503`** — Service Unavailable: Server is overloaded with requests. Try again later.
- **`504`** — Gateway Timeout: An upstream server failed to respond on time. If your query uses max parameter, please try to reduce it.

---

### 2.5 ECM folder linking: Update an ECM Linked Folder

**Endpoint:** `PUT /room/linkedFolders/{id}`

Updates the configuration of the specified Room folder. There is no data validation happening for the request. Please ensure the correct `driveId` and `itemId.` These can be collected from the MS Graph API. The `contentUrl` and `displayName` are used only for user convenience. The folder will be configured with the MS folder name as `displayName`, and the `contentURL` may be updated or corrected as needed. To assess final configuration, please make a GET request on the linkedFolder.

#### Parameters

| Name | In | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| `id` | `path` | `string` | Yes | The unique identifier for the room folder. |

#### Request Body Schema

```json
{
  "type": "object",
  "required": [
    "roomId",
    "contentUrl",
    "displayName",
    "driveId",
    "itemId",
    "defaultFolder"
  ],
  "properties": {
    "roomId": {
      "type": "string",
      "example": "Y2lzY29zcGFyazovL3VzL1JPT00vYmJjZWIxYWQtNDNmMS0zYjU4LTkxNDctZjE0YmIwYzRkMTU0",
      "description": "ID of the room that contains the room tab in question."
    },
    "contentUrl": {
      "type": "string",
      "example": "https://cisco-my.sharepoint.com/personal/naalluri/123",
      "description": "Content URL of the folder."
    },
    "displayName": {
      "type": "string",
      "example": "OneDrive folder for shared documents",
      "description": "This should match the folder name in the ECM backend."
    },
    "driveId": {
      "type": "string",
      "example": "123",
      "description": "Sharepoint or OneDrive drive id. It can be queried via MS Graph APIs."
    },
    "itemId": {
      "type": "string",
      "example": "456",
      "description": "Sharepoint or OneDrive item id. It can be queried via MS Graph APIs."
    },
    "defaultFolder": {
      "type": "string",
      "example": "false",
      "description": "Makes the folder the default storage for the space."
    }
  }
}
```

#### Responses

- **`200`** — OK
  ```json
  {
    "type": "object",
    "required": [
      "driveId",
      "itemId",
      "displayName"
    ],
    "properties": {
      "id": {
        "type": "string",
        "example": "Y2lzY29zcGFyazovL3VybjpURUFNOnVzLWVhc3QtMl9hL1RBQlMvZDg1ZTYwNj",
        "description": "A unique identifier for the folder."
      },
      "roomId": {
        "type": "string",
        "example": "Y2lzY29zcGFyazovL3VzL1JPT00vYmJjZWIxYWQtNDNmMS0zYjU4LTkxNDctZjE0YmIwYzRkMTU0",
        "description": "A unique identifier for the room to which the folder should be linked to."
      },
      "roomType": {
        "type": "string",
        "enum": [
          "direct",
          "group"
        ],
        "description": "The room type.\n * `direct` - 1:1 room\n * `group` - group room\n"
      },
      "driveId": {
        "type": "string",
        "example": "123",
        "description": "Sharepoint or OneDrive drive id. It can be queried via MS Graph APIs."
      },
      "itemId": {
        "type": "string",
        "example": "456",
        "description": "Sharepoint or OneDrive item id. It can be queried via MS Graph APIs."
      },
      "defaultFolder": {
        "type": "string",
        "example": "false",
        "description": "Indicates if this is the default content storage for the room."
      },
      "displayName": {
        "type": "string",
        "example": "OneDrive folder for shared documents",
        "description": "This should match the folder name in the ECM backend."
      },
      "contentUrl": {
        "type": "string",
        "example": "https://cisco-my.sharepoint.com/personal/naalluri/123",
        "description": "Folder's content URL."
      },
      "creatorId": {
        "type": "string",
        "example": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS9mNWIzNjE4Ny1jOGRkLTQ3MjctOGIyZi1mOWM0NDdmMjkwNDY",
        "description": "The person ID of the person who created this folder link."
      },
      "created": {
        "type": "string",
        "example": "2015-10-18T14:26:16.203Z",
        "description": "The date and time when the folder link was created."
      }
    },
    "$$ref": "#/components/schemas/ECMFolder"
  }
  ```
- **`400`** — Bad Request: The request was invalid or cannot be otherwise served. An accompanying error message will explain further.
- **`401`** — Unauthorized: Authentication credentials were missing or incorrect.
- **`403`** — Forbidden: The request is understood, but it has been refused or access is not allowed.
- **`404`** — Not Found: The URI requested is invalid or the resource requested, such as a user, does not exist. Also returned when the requested format is not supported by the requested method.
- **`405`** — Method Not Allowed: The request was made to a resource using an HTTP request method that is not supported.
- **`409`** — Conflict: The request could not be processed because it conflicts with some established rule of the system. For example, a person may not be added to a room more than once.
- **`410`** — Gone: The requested resource is no longer available.
- **`415`** — Unsupported Media Type: The request was made to a resource without specifying a media type or used a media type that is not supported.
- **`423`** — Locked: The requested resource is temporarily unavailable. A Retry-After header may be present that specifies how many seconds you need to wait before attempting the request again.
- **`428`** — Precondition Required: File(s) cannot be scanned for malware and need to be force downloaded.
- **`429`** — Too Many Requests: Too many requests have been sent in a given amount of time and the request has been rate limited. A Retry-After header should be present that specifies how many seconds you need to wait before a successful request can be made.
- **`500`** — Internal Server Error: Something went wrong on the server. If the issue persists, feel free to contact the [Webex Developer Support team](/explore/support).
- **`502`** — Bad Gateway: The server received an invalid response from an upstream server while processing the request. Try again later.
- **`503`** — Service Unavailable: Server is overloaded with requests. Try again later.
- **`504`** — Gateway Timeout: An upstream server failed to respond on time. If your query uses max parameter, please try to reduce it.

---

## 3. Events

### 3.1 Events: Get Event Details

**Endpoint:** `GET /events/{eventId}`

Shows details for an event, by event ID.

Specify the event ID in the `eventId` parameter in the URI.

#### Parameters

| Name | In | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| `eventId` | `path` | `string` | Yes | The unique identifier for the event. |

#### Responses

- **`200`** — OK
  ```json
  {
    "type": "object",
    "required": [
      "id",
      "resource",
      "type",
      "actorId",
      "orgId",
      "created",
      "data"
    ],
    "properties": {
      "id": {
        "type": "string",
        "example": "Y2lzY29zcGFyazovL3VzL0VWRU5UL2JiY2ViMWFkLTQzZjEtM2I1OC05MTQ3LWYxNGJiMGM0ZDE1NAo",
        "description": "The unique identifier for the event."
      },
      "resource": {
        "type": "string",
        "enum": [
          "attachmentActions",
          "businessTexts",
          "call_records",
          "convergedRecordings",
          "file_transcodings",
          "files",
          "meetingMessages",
          "meetings",
          "meetingTranscripts",
          "memberships",
          "messages",
          "rooms",
          "tabs"
        ],
        "description": " * `attachmentActions` - State changed on a card attachment\n * `businessTexts` - A user sent or received a SMS message\n * `call_records` - A Webex call was made to/from a user\n * `convergedRecordings` - A Webex call was recorded for a user\n * `file_transcodings` - State change on a file preview\n * `files` - State changed on a file download\n * `meetingMessages` - State changed on a meeting message, i.e. message exchanged as part of a meeting\n * `meetings` - State change on a meeting ( here combined with type = 'ended' )\n * `meetingTranscripts` - State change on a automatic transcript resource for Webex Assistant\n * `memberships` - State changed on a memberships resource\n * `messages` - State changed on a messages resource\n * `rooms` - State changed on a space classification\n * `tabs` - State changed on a room tabs in a space\n",
        "$$ref": "#/components/schemas/EventResourceEnum"
      },
      "type": {
        "type": "string",
        "enum": [
          "created",
          "updated",
          "deleted",
          "ended"
        ],
        "description": " * `created` - The resource has been created\n * `updated` - A property on the resource has been updated\n * `deleted` - The resource has been deleted\n * `ended` - The meeting has ended\n",
        "$$ref": "#/components/schemas/EventTypeEnum"
      },
      "appId": {
        "type": "string",
        "example": "null",
        "description": "The ID of the application for the event."
      },
      "actorId": {
        "type": "string",
        "example": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS9mNWIzNjE4Ny1jOGRkLTQ3MjctOGIyZi1mOWM0NDdmMjkwNDY",
        "description": "The ID of the person who performed the action."
      },
      "orgId": {
        "type": "string",
        "example": "OTZhYmMyYWEtM2RjYy0xMWU1LWExNTItZmUzNDgxOWNkYzlh",
        "description": "The ID of the organization for the event."
      },
      "created": {
        "type": "string",
        "example": "2016-05-16T21:34:59.324Z",
        "description": "The date and time of the event."
      },
      "data": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string",
            "example": "Y2lzY29zcGFyazovL3VzL01FU1NBR0UvOTJkYjNiZTAtNDNiZC0xMWU2LThhZTktZGQ1YjNkZmM1NjVk"
          },
          "roomId": {
            "type": "string",
            "example": "Y2lzY29zcGFyazovL3VzL1JPT00vYmJjZWIxYWQtNDNmMS0zYjU4LTkxNDctZjE0YmIwYzRkMTU0"
          },
          "roomType": {
            "type": "string",
            "example": "group"
          },
          "orgId": {
            "type": "string",
            "example": "Y2lzY29zcGFyazovL3VzL09SR0FOSVpBVElPTi9jZTg2MWZiYS02ZTJmLTQ5ZjktOWE4NC1iMzU0MDA4ZmFjOWU"
          },
          "text": {
            "type": "string",
            "example": "PROJECT UPDATE - A new project plan has been published on Box: http://box.com/s/lf5vj. The PM for this project is Mike C. and the Engineering Manager is Jane W."
          },
          "personId": {
            "type": "string",
            "example": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS9mNWIzNjE4Ny1jOGRkLTQ3MjctOGIyZi1mOWM0NDdmMjkwNDY"
          },
          "personEmail": {
            "type": "string",
            "example": "matt@example.com"
          },
          "meetingId": {
            "type": "string",
            "example": "16ce696f75844d24b2d4fab04b4419af_I_183979003076423608"
          },
          "creatorId": {
            "type": "string",
            "example": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS82YWE2ZGE5OS0xYzdlLTQ4MWItODY3YS03MWY2NTIwNDk0MzM"
          },
          "host": {
            "type": "object",
            "properties": {},
            "description": "The meeting's host data."
          },
          "attendees": {
            "type": "array",
            "items": {},
            "description": "Common Identity (CI) authenticated meeting attendees."
          },
          "transcriptionEnabled": {
            "type": "string",
            "example": "yes",
            "description": "Indicates whether or not the Voice Assistant was enabled during the meeting. If `true` a transcript should be available a couple minutes after the meeting ended at the [meetingTranscripts resource](/docs/api/v1/meeting-transcripts)."
          },
          "recordingEnabled": {
            "type": "string",
            "example": "yes",
            "description": "Indicates if recording was enabled for all or parts of the meeting. If `true` a recording should be available shortly after the meeting ended at the [recordings resource](/docs/api/v1/recordings)."
          },
          "hasPostMeetingsChat": {
            "type": "string",
            "example": "yes",
            "description": "Indicates if chat messages were exchanged during the meeting in the meetings client (not the unified client). If `true` these messages can be accessed by a compliance officer at the [postMeetingsChat](/docs/api/v1/meetings-chat) resource. Meetings chat collection must be custom enabled."
          },
          "corelationId": {
            "type": "string",
            "example": "fdda8613-d34b-424c-8c6a-44ff2e19379c",
            "description": "Telephony; The corelation id."
          },
          "callType": {
            "type": "string",
            "example": "SIP_ENTERPRISE",
            "description": "Telephony; call types (examples `VIDEO_DIALIN`,`VIDEO_DIALOUT`,`CASCADE`,`HYBRID_CASCADE`,`PSTN_SIP`,`PSTN_DIALIN`,`PSTN_DIALOUT`,`PSTN_ONLY_DIALIN`,`PSTN_ONLY_DIALOUT`,`H323`,`H323_IP`,`SIP_ENTERPRISE`,`SIP_MOBILE`,`SIP_NATIONAL`,`SIP_INTERNATIONAL`,`SIP_EMERGENCY`,`SIP_OPERATOR`,`SIP_SHORTCODE`,`SIP_TOLLFREE`,`SIP_PREMIUM`,`SIP_URI`,`SIP_INBOUND`,`UNKNOWN`,`ZTM`,`SIP_MEETING`)."
          },
          "userId": {
            "type": "string",
            "example": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS8zZjEwMTU1NC04ZGJjLTQyMmUtOGEzZC1kYTk1YTI3NWZlNzU",
            "description": "Telephony; user id of the CDR owner."
          },
          "userType": {
            "type": "string",
            "example": "User",
            "description": "Telephony; The type of user (`User`,`Anchor`,`AutomatedAttendantBasic`,`AutomatedAttendantStandard`,`AutomatedAttendantVideo`,`BroadworksAnywhere`,`CallCenterBasic`,`CallCenterPremium`,`CallCenterStandard`,`CollaborateBridge`,`ContactCenterAdaptor`,`FindMeFollowMe`,`FlexibleSeatingHost`,`GroupCall`,`GroupPaging`,`HuntGroup`,`LocalGateway`,`MeetMeConference`,`Place`,`RoutePoint`,`SystemVoicePortal`,`VoiceMailGroup`,`VoiceMailRetrieval`,`VoiceXML`,`VirtualLine`,`Unknown`)."
          },
          "callDirection": {
            "type": "string",
            "example": "ORIGINTATING",
            "description": "Telephony; `ORIGINATING` or `TERMINATING`."
          },
          "isCallAnswered": {
            "type": "string",
            "example": "true",
            "description": "Telephony; indicates if the call was answered."
          },
          "callDurationSeconds": {
            "type": "string",
            "example": "192",
            "description": "Telephony; duration of call in seconds."
          },
          "callStartTime": {
            "type": "string",
            "example": "2023-02-08T06:12:43.976Z",
            "description": "Telephony; ISO 8601."
          },
          "callAnswerTime": {
            "type": "string",
            "example": "2023-02-08T06:12:47.012Z",
            "description": "Telephony; ISO 8601."
          },
          "callTransferTime": {
            "type": "string",
            "example": "2023-02-08T06:15:19.112Z",
            "description": "Telephony; ISO 8601."
          },
          "callingNumber": {
            "type": "string",
            "example": "910481234",
            "description": "Telephony; originating number."
          },
          "callingLineId": {
            "type": "string",
            "example": "211",
            "description": "Telephony."
          },
          "calledNumber": {
            "type": "string",
            "example": "4089671221",
            "description": "Telephony; destination number."
          },
          "calledLineId": {
            "type": "string",
            "example": "219",
            "description": "Telephony"
          },
          "dialedDigits": {
            "type": "string",
            "example": "123",
            "description": "Telephony"
          },
          "callRedirectingNumber": {
            "type": "string",
            "description": "Telephony"
          },
          "callRedirectedReason": {
            "type": "string",
            "description": "Telephony"
          },
          "created": {
            "type": "string",
            "example": "2016-05-16T21:34:59.324Z"
          },
          "type": {
            "type": "string",
            "example": "direct",
            "description": "Message type `direct` or `group` message."
          },
          "breakoutSessionId": {
            "type": "string",
            "example": "d66a4a90-4f50-11ef-bc94-f5c71646dc71",
            "description": "The breakout session Id in cases where the action happened in a meeting's brakout session, for example a `meetingMessage`."
          },
          "recipients": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "personId": {
                  "type": "string",
                  "example": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS9lOGYwOTIwOC00ZjUxLTExZWYtOTQ4My1iYTA3NjE2MzY4NmQ",
                  "description": "The personId of the recipient"
                },
                "personEmail": {
                  "type": "string",
                  "example": "johndoe@simplistic.com",
                  "description": "The personEmail"
                },
                "guestDisplayName": {
                  "type": "string",
                  "example": "John Wayne",
                  "description": "Guests, who are unauthenticated users, have a guestDisplayName"
                },
                "guestEmail": {
                  "type": "string",
                  "example": "jwayne@mailinator.com",
                  "description": "Guests, who are unauthenticated users, have a guestEmail"
                }
              },
              "$$ref": "#/components/schemas/Recipient"
            },
            "description": "The recipients list for directed meetingMessages."
          }
        },
        "description": "The event's data representation. This object will contain the event's `resource`, such as [memberships](/docs/api/v1/memberships/get-membership-details), [messages](/docs/api/v1/messages/get-message-details), [meetings](/docs/api/v1/meetings), [meetingMessages](/docs/api/v1/meetingMessages), [tabs](/docs/api/v1/room-tabs), [rooms](/docs/api/v1/space-classifications) or [attachmentActions](/docs/api/v1/attachment-actions) at the time the event took place."
      }
    },
    "$$ref": "#/components/schemas/Event"
  }
  ```
- **`400`** — Bad Request: The request was invalid or cannot be otherwise served. An accompanying error message will explain further.
- **`401`** — Unauthorized: Authentication credentials were missing or incorrect.
- **`403`** — Forbidden: The request is understood, but it has been refused or access is not allowed.
- **`404`** — Not Found: The URI requested is invalid or the resource requested, such as a user, does not exist. Also returned when the requested format is not supported by the requested method.
- **`405`** — Method Not Allowed: The request was made to a resource using an HTTP request method that is not supported.
- **`409`** — Conflict: The request could not be processed because it conflicts with some established rule of the system. For example, a person may not be added to a room more than once.
- **`410`** — Gone: The requested resource is no longer available.
- **`415`** — Unsupported Media Type: The request was made to a resource without specifying a media type or used a media type that is not supported.
- **`423`** — Locked: The requested resource is temporarily unavailable. A Retry-After header may be present that specifies how many seconds you need to wait before attempting the request again.
- **`428`** — Precondition Required: File(s) cannot be scanned for malware and need to be force downloaded.
- **`429`** — Too Many Requests: Too many requests have been sent in a given amount of time and the request has been rate limited. A Retry-After header should be present that specifies how many seconds you need to wait before a successful request can be made.
- **`500`** — Internal Server Error: Something went wrong on the server. If the issue persists, feel free to contact the [Webex Developer Support team](/explore/support).
- **`502`** — Bad Gateway: The server received an invalid response from an upstream server while processing the request. Try again later.
- **`503`** — Service Unavailable: Server is overloaded with requests. Try again later.
- **`504`** — Gateway Timeout: An upstream server failed to respond on time. If your query uses max parameter, please try to reduce it.

---

### 3.2 Events: List Events

**Endpoint:** `GET /events`

List events in your organization. Several query parameters are available to filter the events returned in the response.

Long result sets will be split into [pages](/docs/basics#pagination).

#### Parameters

| Name | In | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| `resource` | `query` | `string` | No | List events with a specific resource type. |
| `type` | `query` | `string` | No | List events with a specific event type. |
| `actorId` | `query` | `string` | No | List events performed by this person, by person ID. |
| `from` | `query` | `string` | No | List events which occurred after a specific date and time. |
| `to` | `query` | `string` | No | List events that occurred before a specific date and time. If not specified, events up to the present time will be listed. Cannot be set to a future date relative to the current time. |
| `max` | `query` | `number` | No | Limit the maximum number of events in the response. Value must be between 1 and 1000, inclusive. |
| `serviceType` | `query` | `string` | No | List events for a specific service type. This parameter is only applicable and mandatory when resource is set to `convergedRecordings`. |

#### Responses

- **`200`** — OK
  ```json
  {
    "type": "object",
    "properties": {
      "items": {
        "type": "array",
        "items": {
          "type": "object",
          "required": [
            "id",
            "resource",
            "type",
            "actorId",
            "orgId",
            "created",
            "data"
          ],
          "properties": {
            "id": {
              "type": "string",
              "example": "Y2lzY29zcGFyazovL3VzL0VWRU5UL2JiY2ViMWFkLTQzZjEtM2I1OC05MTQ3LWYxNGJiMGM0ZDE1NAo",
              "description": "The unique identifier for the event."
            },
            "resource": {
              "type": "string",
              "enum": [
                "attachmentActions",
                "businessTexts",
                "call_records",
                "convergedRecordings",
                "file_transcodings",
                "files",
                "meetingMessages",
                "meetings",
                "meetingTranscripts",
                "memberships",
                "messages",
                "rooms",
                "tabs"
              ],
              "description": " * `attachmentActions` - State changed on a card attachment\n * `businessTexts` - A user sent or received a SMS message\n * `call_records` - A Webex call was made to/from a user\n * `convergedRecordings` - A Webex call was recorded for a user\n * `file_transcodings` - State change on a file preview\n * `files` - State changed on a file download\n * `meetingMessages` - State changed on a meeting message, i.e. message exchanged as part of a meeting\n * `meetings` - State change on a meeting ( here combined with type = 'ended' )\n * `meetingTranscripts` - State change on a automatic transcript resource for Webex Assistant\n * `memberships` - State changed on a memberships resource\n * `messages` - State changed on a messages resource\n * `rooms` - State changed on a space classification\n * `tabs` - State changed on a room tabs in a space\n",
              "$$ref": "#/components/schemas/EventResourceEnum"
            },
            "type": {
              "type": "string",
              "enum": [
                "created",
                "updated",
                "deleted",
                "ended"
              ],
              "description": " * `created` - The resource has been created\n * `updated` - A property on the resource has been updated\n * `deleted` - The resource has been deleted\n * `ended` - The meeting has ended\n",
              "$$ref": "#/components/schemas/EventTypeEnum"
            },
            "appId": {
              "type": "string",
              "example": "null",
              "description": "The ID of the application for the event."
            },
            "actorId": {
              "type": "string",
              "example": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS9mNWIzNjE4Ny1jOGRkLTQ3MjctOGIyZi1mOWM0NDdmMjkwNDY",
              "description": "The ID of the person who performed the action."
            },
            "orgId": {
              "type": "string",
              "example": "OTZhYmMyYWEtM2RjYy0xMWU1LWExNTItZmUzNDgxOWNkYzlh",
              "description": "The ID of the organization for the event."
            },
            "created": {
              "type": "string",
              "example": "2016-05-16T21:34:59.324Z",
              "description": "The date and time of the event."
            },
            "data": {
              "type": "object",
              "properties": {
                "id": {
                  "type": "string",
                  "example": "Y2lzY29zcGFyazovL3VzL01FU1NBR0UvOTJkYjNiZTAtNDNiZC0xMWU2LThhZTktZGQ1YjNkZmM1NjVk"
                },
                "roomId": {
                  "type": "string",
                  "example": "Y2lzY29zcGFyazovL3VzL1JPT00vYmJjZWIxYWQtNDNmMS0zYjU4LTkxNDctZjE0YmIwYzRkMTU0"
                },
                "roomType": {
                  "type": "string",
                  "example": "group"
                },
                "orgId": {
                  "type": "string",
                  "example": "Y2lzY29zcGFyazovL3VzL09SR0FOSVpBVElPTi9jZTg2MWZiYS02ZTJmLTQ5ZjktOWE4NC1iMzU0MDA4ZmFjOWU"
                },
                "text": {
                  "type": "string",
                  "example": "PROJECT UPDATE - A new project plan has been published on Box: http://box.com/s/lf5vj. The PM for this project is Mike C. and the Engineering Manager is Jane W."
                },
                "personId": {
                  "type": "string",
                  "example": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS9mNWIzNjE4Ny1jOGRkLTQ3MjctOGIyZi1mOWM0NDdmMjkwNDY"
                },
                "personEmail": {
                  "type": "string",
                  "example": "matt@example.com"
                },
                "meetingId": {
                  "type": "string",
                  "example": "16ce696f75844d24b2d4fab04b4419af_I_183979003076423608"
                },
                "creatorId": {
                  "type": "string",
                  "example": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS82YWE2ZGE5OS0xYzdlLTQ4MWItODY3YS03MWY2NTIwNDk0MzM"
                },
                "host": {
                  "type": "object",
                  "properties": {},
                  "description": "The meeting's host data."
                },
                "attendees": {
                  "type": "array",
                  "items": {},
                  "description": "Common Identity (CI) authenticated meeting attendees."
                },
                "transcriptionEnabled": {
                  "type": "string",
                  "example": "yes",
                  "description": "Indicates whether or not the Voice Assistant was enabled during the meeting. If `true` a transcript should be available a couple minutes after the meeting ended at the [meetingTranscripts resource](/docs/api/v1/meeting-transcripts)."
                },
                "recordingEnabled": {
                  "type": "string",
                  "example": "yes",
                  "description": "Indicates if recording was enabled for all or parts of the meeting. If `true` a recording should be available shortly after the meeting ended at the [recordings resource](/docs/api/v1/recordings)."
                },
                "hasPostMeetingsChat": {
                  "type": "string",
                  "example": "yes",
                  "description": "Indicates if chat messages were exchanged during the meeting in the meetings client (not the unified client). If `true` these messages can be accessed by a compliance officer at the [postMeetingsChat](/docs/api/v1/meetings-chat) resource. Meetings chat collection must be custom enabled."
                },
                "corelationId": {
                  "type": "string",
                  "example": "fdda8613-d34b-424c-8c6a-44ff2e19379c",
                  "description": "Telephony; The corelation id."
                },
                "callType": {
                  "type": "string",
                  "example": "SIP_ENTERPRISE",
                  "description": "Telephony; call types (examples `VIDEO_DIALIN`,`VIDEO_DIALOUT`,`CASCADE`,`HYBRID_CASCADE`,`PSTN_SIP`,`PSTN_DIALIN`,`PSTN_DIALOUT`,`PSTN_ONLY_DIALIN`,`PSTN_ONLY_DIALOUT`,`H323`,`H323_IP`,`SIP_ENTERPRISE`,`SIP_MOBILE`,`SIP_NATIONAL`,`SIP_INTERNATIONAL`,`SIP_EMERGENCY`,`SIP_OPERATOR`,`SIP_SHORTCODE`,`SIP_TOLLFREE`,`SIP_PREMIUM`,`SIP_URI`,`SIP_INBOUND`,`UNKNOWN`,`ZTM`,`SIP_MEETING`)."
                },
                "userId": {
                  "type": "string",
                  "example": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS8zZjEwMTU1NC04ZGJjLTQyMmUtOGEzZC1kYTk1YTI3NWZlNzU",
                  "description": "Telephony; user id of the CDR owner."
                },
                "userType": {
                  "type": "string",
                  "example": "User",
                  "description": "Telephony; The type of user (`User`,`Anchor`,`AutomatedAttendantBasic`,`AutomatedAttendantStandard`,`AutomatedAttendantVideo`,`BroadworksAnywhere`,`CallCenterBasic`,`CallCenterPremium`,`CallCenterStandard`,`CollaborateBridge`,`ContactCenterAdaptor`,`FindMeFollowMe`,`FlexibleSeatingHost`,`GroupCall`,`GroupPaging`,`HuntGroup`,`LocalGateway`,`MeetMeConference`,`Place`,`RoutePoint`,`SystemVoicePortal`,`VoiceMailGroup`,`VoiceMailRetrieval`,`VoiceXML`,`VirtualLine`,`Unknown`)."
                },
                "callDirection": {
                  "type": "string",
                  "example": "ORIGINTATING",
                  "description": "Telephony; `ORIGINATING` or `TERMINATING`."
                },
                "isCallAnswered": {
                  "type": "string",
                  "example": "true",
                  "description": "Telephony; indicates if the call was answered."
                },
                "callDurationSeconds": {
                  "type": "string",
                  "example": "192",
                  "description": "Telephony; duration of call in seconds."
                },
                "callStartTime": {
                  "type": "string",
                  "example": "2023-02-08T06:12:43.976Z",
                  "description": "Telephony; ISO 8601."
                },
                "callAnswerTime": {
                  "type": "string",
                  "example": "2023-02-08T06:12:47.012Z",
                  "description": "Telephony; ISO 8601."
                },
                "callTransferTime": {
                  "type": "string",
                  "example": "2023-02-08T06:15:19.112Z",
                  "description": "Telephony; ISO 8601."
                },
                "callingNumber": {
                  "type": "string",
                  "example": "910481234",
                  "description": "Telephony; originating number."
                },
                "callingLineId": {
                  "type": "string",
                  "example": "211",
                  "description": "Telephony."
                },
                "calledNumber": {
                  "type": "string",
                  "example": "4089671221",
                  "description": "Telephony; destination number."
                },
                "calledLineId": {
                  "type": "string",
                  "example": "219",
                  "description": "Telephony"
                },
                "dialedDigits": {
                  "type": "string",
                  "example": "123",
                  "description": "Telephony"
                },
                "callRedirectingNumber": {
                  "type": "string",
                  "description": "Telephony"
                },
                "callRedirectedReason": {
                  "type": "string",
                  "description": "Telephony"
                },
                "created": {
                  "type": "string",
                  "example": "2016-05-16T21:34:59.324Z"
                },
                "type": {
                  "type": "string",
                  "example": "direct",
                  "description": "Message type `direct` or `group` message."
                },
                "breakoutSessionId": {
                  "type": "string",
                  "example": "d66a4a90-4f50-11ef-bc94-f5c71646dc71",
                  "description": "The breakout session Id in cases where the action happened in a meeting's brakout session, for example a `meetingMessage`."
                },
                "recipients": {
                  "type": "array",
                  "items": {
                    "type": "object",
                    "properties": {
                      "personId": {
                        "type": "string",
                        "example": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS9lOGYwOTIwOC00ZjUxLTExZWYtOTQ4My1iYTA3NjE2MzY4NmQ",
                        "description": "The personId of the recipient"
                      },
                      "personEmail": {
                        "type": "string",
                        "example": "johndoe@simplistic.com",
                        "description": "The personEmail"
                      },
                      "guestDisplayName": {
                        "type": "string",
                        "example": "John Wayne",
                        "description": "Guests, who are unauthenticated users, have a guestDisplayName"
                      },
                      "guestEmail": {
                        "type": "string",
                        "example": "jwayne@mailinator.com",
                        "description": "Guests, who are unauthenticated users, have a guestEmail"
                      }
                    },
                    "$$ref": "#/components/schemas/Recipient"
                  },
                  "description": "The recipients list for directed meetingMessages."
                }
              },
              "description": "The event's data representation. This object will contain the event's `resource`, such as [memberships](/docs/api/v1/memberships/get-membership-details), [messages](/docs/api/v1/messages/get-message-details), [meetings](/docs/api/v1/meetings), [meetingMessages](/docs/api/v1/meetingMessages), [tabs](/docs/api/v1/room-tabs), [rooms](/docs/api/v1/space-classifications) or [attachmentActions](/docs/api/v1/attachment-actions) at the time the event took place."
            }
          },
          "$$ref": "#/components/schemas/Event"
        }
      }
    },
    "$$ref": "#/components/schemas/EventCollectionResponse"
  }
  ```
- **`400`** — Bad Request: The request was invalid or cannot be otherwise served. An accompanying error message will explain further.
- **`401`** — Unauthorized: Authentication credentials were missing or incorrect.
- **`403`** — Forbidden: The request is understood, but it has been refused or access is not allowed.
- **`404`** — Not Found: The URI requested is invalid or the resource requested, such as a user, does not exist. Also returned when the requested format is not supported by the requested method.
- **`405`** — Method Not Allowed: The request was made to a resource using an HTTP request method that is not supported.
- **`409`** — Conflict: The request could not be processed because it conflicts with some established rule of the system. For example, a person may not be added to a room more than once.
- **`410`** — Gone: The requested resource is no longer available.
- **`415`** — Unsupported Media Type: The request was made to a resource without specifying a media type or used a media type that is not supported.
- **`423`** — Locked: The requested resource is temporarily unavailable. A Retry-After header may be present that specifies how many seconds you need to wait before attempting the request again.
- **`428`** — Precondition Required: File(s) cannot be scanned for malware and need to be force downloaded.
- **`429`** — Too Many Requests: Too many requests have been sent in a given amount of time and the request has been rate limited. A Retry-After header should be present that specifies how many seconds you need to wait before a successful request can be made.
- **`500`** — Internal Server Error: Something went wrong on the server. If the issue persists, feel free to contact the [Webex Developer Support team](/explore/support).
- **`502`** — Bad Gateway: The server received an invalid response from an upstream server while processing the request. Try again later.
- **`503`** — Service Unavailable: Server is overloaded with requests. Try again later.
- **`504`** — Gateway Timeout: An upstream server failed to respond on time. If your query uses max parameter, please try to reduce it.

---

## 4. Hybrid Data Security (HDS)

### 4.1 Hybrid Data Security (HDS): Get alarms for an Hybrid Data Security node

**Endpoint:** `GET /hds/nodes/{nodeId}/alarms`

Returns the alarm details for a single Hybrid Data Security node for the provided time range (last 24 hours).
To obtain the Node ID needed for this API, use the [List nodes for an Hybrid Data Security cluster API](</docs/api/v1/hds/list-hds-cluster-nodes>)

#### Parameters

| Name | In | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| `nodeId` | `path` | `string` | Yes | Unique ID of the Hybrid Data Security node. |
| `from` | `query` | `string` | Yes | The start date and time of the requested data in any [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) compliant format. |
| `to` | `query` | `string` | Yes | The end date and time of the requested data in any [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) compliant format. |

#### Responses

- **`200`** — OK
  ```json
  {
    "type": "object",
    "properties": {
      "context": {
        "type": "object",
        "properties": {
          "orgId": {
            "type": "string",
            "example": "Y2lzY29zcGFyazovL3VzL0hZQlJJRF9DTFVTVEVSLzFlYjY1ZmRmLTk2NDMtNDE3Zi05OTc0LWFkNzJVGNG",
            "description": "Unique ID of the organization."
          },
          "clusterId": {
            "type": "string",
            "example": "Y2lzY29zcGFyazovL3VzL0hZQlJJRF9DTFVTVEVSLzFlYjY1ZmRmLTk2NDMtNDE3Zi05OTc0LWFkNzJjYWUwZTEwZjpiMzdmNTgzYy1kZGRjLTQyOGItODJlNS1jYmU2ODFkYjQ5xxx",
            "description": "Unique ID of the cluster."
          },
          "clusterName": {
            "type": "string",
            "example": "San Jose",
            "description": "Name of the cluster."
          },
          "nodeId": {
            "type": "string",
            "example": "Y2lzY29zcGFyazovL3VzL0hZQlJJRF9DTFVTVEVSLzM2ZDg5NGY3LTJiNTctNDNjMS1hY2VlLWQ0N2U2Nzc2MTQxNDo0NjdiNGIxZC1jZWI2LTQwN2EtYWZmOC1mMjIxZmFiNzhjyyy",
            "description": "Unique ID of the node."
          },
          "host": {
            "type": "string",
            "example": "10.196.5.82",
            "description": "Host name or IP of the Hybrid Data Security node."
          }
        },
        "description": "Metadata information about the node for which alarms are being retrieved."
      },
      "alarms": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "alarmId": {
              "type": "string",
              "example": "AUTH_WARN.expiring-60",
              "description": "Unique identifier of the alarm."
            },
            "alarmName": {
              "type": "string",
              "example": "Hybrid Data Security Machine Accounts Expiring in 60 days",
              "description": "Name of the alarm."
            },
            "alarmSeverity": {
              "type": "string",
              "example": "Warning",
              "description": "Severity level of the alarm."
            },
            "alarmDetails": {
              "type": "string",
              "example": "Expiration Details",
              "description": "Additional details about the alarm."
            },
            "possibleRemediation": {
              "type": "string",
              "example": "Refresh Hybrid Data Security Machine Accounts using Hybrid Data Security Setup Tool",
              "description": "Suggested remediation steps for the alarm."
            },
            "currentStatus": {
              "type": "string",
              "example": "Active",
              "description": "Current status of the alarm."
            },
            "occurrences": {
              "type": "object",
              "properties": {
                "total": {
                  "type": "string",
                  "example": "4",
                  "description": "Total number of occurrences of the alarm."
                },
                "details": {
                  "type": "array",
                  "items": {
                    "type": "object",
                    "properties": {
                      "raisedAt": {
                        "type": "string",
                        "format": "date-time",
                        "example": "2025-06-14T15:53:00Z",
                        "description": "Timestamp when the alarm was raised."
                      },
                      "clearedAt": {
                        "type": "string",
                        "format": "date-time",
                        "example": "2025-06-15T15:53:00Z",
                        "description": "Timestamp when the alarm was cleared."
                      }
                    },
                    "$$ref": "#/components/schemas/alarmOccurrence"
                  },
                  "description": "List of individual alarm occurrence details."
                }
              },
              "description": "Occurrence details of the alarm."
            }
          },
          "$$ref": "#/components/schemas/nodeAlarm"
        },
        "description": "List of alarms raised for the node."
      },
      "timeRange": {
        "type": "object",
        "properties": {
          "from": {
            "type": "string",
            "format": "date-time",
            "example": "2025-06-15T15:53:00Z",
            "description": "Start time of the requested data range."
          },
          "to": {
            "type": "string",
            "format": "date-time",
            "example": "2025-06-16T15:53:00Z",
            "description": "End time of the requested data range."
          }
        },
        "description": "The time range for the alarms data."
      }
    },
    "$$ref": "#/components/schemas/nodeAlarmsResponse"
  }
  ```
- **`400`** — Bad Request: The request was invalid or could not be processed. An accompanying error message will provide more details.
- **`401`** — Unauthorized: Authentication credentials were missing or incorrect.
- **`403`** — Forbidden: The request was understood, but it has been refused or access is not allowed.
- **`404`** — Not Found: The requested URI is invalid, or the resource requested (such as a user) does not exist. This response is also returned when the requested format is not supported by the requested method.
- **`405`** — Method Not Allowed: The request was made to a resource using an HTTP method that is not supported.
- **`409`** — Conflict: The request could not be processed because it conflicts with some established rule of the system. For example, a person may not be added to a room more than once.
- **`410`** — Gone: The requested resource is no longer available.
- **`415`** — Unsupported Media Type: The request was made to a resource without specifying a media type, or with a media type that is not supported.
- **`423`** — Locked: The requested resource is temporarily unavailable. A Retry-After header may be present to indicate how many seconds you should wait before attempting the request again.
- **`428`** — Precondition Required: The file(s) cannot be scanned for malware and must be force downloaded.
- **`429`** — Too Many Requests: Too many requests have been sent in a given period of time and the request has been rate limited. A Retry-After header should be present that specifies how many seconds you need to wait before a successful request can be made.
- **`500`** — Internal Server Error: Something went wrong on the server. If the issue persists, please contact the [Webex Developer Support team](/explore/support).
- **`502`** — Bad Gateway: The server received an invalid response from an upstream server while processing the request. Try again later.
- **`503`** — Service Unavailable: Server is overloaded with requests. Try again later.
- **`504`** — Gateway Timeout: An upstream server failed to respond in time. If your query uses the max parameter, please try reducing its value.

---

### 4.2 Hybrid Data Security (HDS): Get availability details for Hybrid Data Security cluster

**Endpoint:** `GET /hds/clusters/{clusterId}/availability`

Get the availability details for an Hybrid Data Security cluster, where each segment specifies the start and end times, as well as the number of online, offline, and total nodes within that segment.
To obtain the Cluster ID needed for this API, use the [Get organization details API](</docs/api/v1/hds/get-organization-details>)

#### Parameters

| Name | In | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| `clusterId` | `path` | `string` | Yes | Unique ID of the Hybrid Data Security cluster. |
| `from` | `query` | `string` | Yes | The start date and time of the requested data in any [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) compliant format. The 'from' value cannot be later than the 'to' value, and it cannot be more than 1 day older than the current date and time. |
| `to` | `query` | `string` | Yes | The end date and time of the requested data in any [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) compliant format. |

#### Responses

- **`200`** — OK
  ```json
  {
    "type": "object",
    "properties": {
      "context": {
        "type": "object",
        "properties": {
          "orgId": {
            "type": "string",
            "example": "Y2lzY29zcGFyazovL3VzL09SR0FOSVpBVElPTi8yYzNjOWY5NS03M2Q5LTQ0NjAtYTY2OC0wNDcxNjJmZjFiYWQ",
            "description": "Unique ID of the organization."
          },
          "clusterId": {
            "type": "string",
            "example": "Y2lzY29zcGFyazovL3VzL0hZQlJJRF9DTFVTVEVSLzJjM2M5Zjk1LTczZDktNDQ2MC1hNjY4LTA0NzE2MmZmMWJhZDpiMzdmNTgzYy1kZGRjLTQyOGItODJlNS1jYmU2ODFkYjQ5NjI=",
            "description": "Unique ID of the cluster."
          },
          "clusterName": {
            "type": "string",
            "example": "San Jose",
            "description": "Name of the cluster."
          }
        },
        "description": "Metadata information about the cluster for which availability details are being retrieved."
      },
      "availabilitySegments": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "segmentStartTime": {
              "type": "string",
              "format": "date-time",
              "example": "2026-01-01T00:00:00Z",
              "description": "Start time of the availability segment."
            },
            "segmentEndTime": {
              "type": "string",
              "format": "date-time",
              "example": "2026-01-02T00:00:00Z",
              "description": "End time of the availability segment."
            },
            "noOfOnlineNodes": {
              "type": "integer",
              "example": 1,
              "description": "Number of online nodes in the cluster in the segment."
            },
            "noOfOfflineNodes": {
              "type": "integer",
              "example": 1,
              "description": "Number of offline nodes in the cluster in the segment."
            },
            "totalNodes": {
              "type": "integer",
              "example": 2,
              "description": "Total number of nodes in the cluster in the segment."
            }
          },
          "$$ref": "#/components/schemas/availabilitySegment"
        },
        "description": "List of availability segments for the cluster."
      },
      "timeRange": {
        "type": "object",
        "properties": {
          "from": {
            "type": "string",
            "format": "date-time",
            "example": "2025-06-15T15:53:00Z",
            "description": "Start time of the requested data range."
          },
          "to": {
            "type": "string",
            "format": "date-time",
            "example": "2025-06-17T15:53:00Z",
            "description": "End time of the requested data range."
          }
        },
        "description": "The time range for the availability data."
      }
    },
    "$$ref": "#/components/schemas/clustersAvailabilityDetailsResponse"
  }
  ```
- **`400`** — Bad Request: The request was invalid or could not be processed. An accompanying error message will provide more details.
- **`401`** — Unauthorized: Authentication credentials were missing or incorrect.
- **`403`** — Forbidden: The request was understood, but it has been refused or access is not allowed.
- **`404`** — Not Found: The requested URI is invalid, or the resource requested (such as a user) does not exist. This response is also returned when the requested format is not supported by the requested method.
- **`405`** — Method Not Allowed: The request was made to a resource using an HTTP method that is not supported.
- **`409`** — Conflict: The request could not be processed because it conflicts with some established rule of the system. For example, a person may not be added to a room more than once.
- **`410`** — Gone: The requested resource is no longer available.
- **`415`** — Unsupported Media Type: The request was made to a resource without specifying a media type, or with a media type that is not supported.
- **`423`** — Locked: The requested resource is temporarily unavailable. A Retry-After header may be present to indicate how many seconds you should wait before attempting the request again.
- **`428`** — Precondition Required: The file(s) cannot be scanned for malware and must be force downloaded.
- **`429`** — Too Many Requests: Too many requests have been sent in a given period of time and the request has been rate limited. A Retry-After header should be present that specifies how many seconds you need to wait before a successful request can be made.
- **`500`** — Internal Server Error: Something went wrong on the server. If the issue persists, please contact the [Webex Developer Support team](/explore/support).
- **`502`** — Bad Gateway: The server received an invalid response from an upstream server while processing the request. Try again later.
- **`503`** — Service Unavailable: Server is overloaded with requests. Try again later.
- **`504`** — Gateway Timeout: An upstream server failed to respond in time. If your query uses the max parameter, please try reducing its value.

---

### 4.3 Hybrid Data Security (HDS): Get cluster details

**Endpoint:** `GET /hds/clusters/{clusterId}`

Retrieve details for a specific Hybrid Data Security cluster, such as the cluster name, cluster status, upgrade schedule, and Hybrid Data Security nodes in the cluster.
To obtain the Cluster ID needed for this API, use the [Get organization details API](</docs/api/v1/hds/get-organization-details>)

#### Parameters

| Name | In | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| `clusterId` | `path` | `string` | Yes | Unique ID of the Hybrid Data Security cluster. |

#### Responses

- **`200`** — OK
  ```json
  {
    "type": "object",
    "properties": {
      "context": {
        "type": "object",
        "properties": {
          "orgId": {
            "type": "string",
            "example": "Y2lzY29zcGFyazovL3VzL09SR0FOSVpBVElPTi8yYzNjOWY5NS03M2Q5LTQ0NjAtYTY2OC0wNDcxNjJmZjFiYWQ=",
            "description": "Unique ID of the organization."
          }
        },
        "description": "Metadata information about the organization for which the cluster details are being retrieved."
      },
      "clusterId": {
        "type": "string",
        "example": "Y2lzY29zcGFyazovL3VzL0hZQlJJRF9DTFVTVEVSLzJjM2M5Zjk1LTczZDktNDQ2MC1hNjY4LTA0NzE2MmZmMWJhZDpmMWJmMGI1MC0yMDUyLTQ3ZmUtYjg3ZC01MTFjMmZlNzQ3MWI",
        "description": "Unique ID of the cluster."
      },
      "clusterName": {
        "type": "string",
        "example": "Bangalore",
        "description": "Name of the cluster."
      },
      "clusterStatus": {
        "type": "string",
        "example": "Operational",
        "description": "Current status of the cluster."
      },
      "releaseChannel": {
        "type": "string",
        "example": "beta",
        "description": "Release channel of the cluster."
      },
      "upgradeSchedule": {
        "type": "object",
        "properties": {
          "scheduleDays": {
            "type": "array",
            "items": {
              "type": "string",
              "example": "sunday"
            },
            "description": "Days of the week when upgrades are scheduled."
          },
          "scheduleTime": {
            "type": "string",
            "example": "02:00",
            "description": "Time of the day when upgrades are scheduled."
          },
          "scheduleTimeZone": {
            "type": "string",
            "example": "Asia/Kolkata",
            "description": "Time zone for the scheduled upgrade time."
          },
          "nextUpgradeTime": {
            "type": "string",
            "example": "2025-07-25T20:30:00Z",
            "description": "Next scheduled upgrade time."
          }
        },
        "description": "Upgrade schedule details of the cluster."
      }
    },
    "$$ref": "#/components/schemas/clusterDetailsResponse"
  }
  ```
- **`400`** — Bad Request: The request was invalid or could not be processed. An accompanying error message will provide more details.
- **`401`** — Unauthorized: Authentication credentials were missing or incorrect.
- **`403`** — Forbidden: The request was understood, but it has been refused or access is not allowed.
- **`404`** — Not Found: The requested URI is invalid, or the resource requested (such as a user) does not exist. This response is also returned when the requested format is not supported by the requested method.
- **`405`** — Method Not Allowed: The request was made to a resource using an HTTP method that is not supported.
- **`409`** — Conflict: The request could not be processed because it conflicts with some established rule of the system. For example, a person may not be added to a room more than once.
- **`410`** — Gone: The requested resource is no longer available.
- **`415`** — Unsupported Media Type: The request was made to a resource without specifying a media type, or with a media type that is not supported.
- **`423`** — Locked: The requested resource is temporarily unavailable. A Retry-After header may be present to indicate how many seconds you should wait before attempting the request again.
- **`428`** — Precondition Required: The file(s) cannot be scanned for malware and must be force downloaded.
- **`429`** — Too Many Requests: Too many requests have been sent in a given period of time and the request has been rate limited. A Retry-After header should be present that specifies how many seconds you need to wait before a successful request can be made.
- **`500`** — Internal Server Error: Something went wrong on the server. If the issue persists, please contact the [Webex Developer Support team](/explore/support).
- **`502`** — Bad Gateway: The server received an invalid response from an upstream server while processing the request. Try again later.
- **`503`** — Service Unavailable: Server is overloaded with requests. Try again later.
- **`504`** — Gateway Timeout: An upstream server failed to respond in time. If your query uses the max parameter, please try reducing its value.

---

### 4.4 Hybrid Data Security (HDS): Get database details for the Hybrid Data Security organization

**Endpoint:** `GET /hds/organizations/{organizationId}/database`

Retrieve details of database information for an Hybrid Data Security organization, such as database type and version used.
To obtain the Organization ID needed for this API, use the [Organizations API](</docs/api/v1/organizations/list-organizations>)

#### Parameters

| Name | In | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| `organizationId` | `path` | `string` | Yes | Unique ID of the Hybrid Data Security organization |

#### Responses

- **`200`** — OK
  ```json
  {
    "type": "object",
    "properties": {
      "context": {
        "type": "object",
        "properties": {
          "orgId": {
            "type": "string",
            "example": "Y2lzY29zcGFyazovL3VzL09SR0FOSVpBVElPTi8yYzNjOWY5NS03M2Q5LTQ0NjAtYTY2OC0wNDcxNjJmZjFiYWQ=",
            "description": "Unique ID of the organization."
          }
        },
        "description": "Context for the response payload."
      },
      "databaseType": {
        "type": "string",
        "example": "PostgreSQL",
        "description": "Type of the database."
      },
      "databaseVersion": {
        "type": "string",
        "example": "PostgreSQL 16.9 (Ubuntu 16.9-1.pgdg24.04+1) on x86_64-pc-linux-gnu, compiled by gcc (Ubuntu 13.3.0-6ubuntu2~24.04) 13.3.0, 64-bit",
        "description": "Version of the database."
      }
    },
    "$$ref": "#/components/schemas/databaseDetailsResponse"
  }
  ```
- **`400`** — Bad Request: The request was invalid or could not be processed. An accompanying error message will provide more details.
- **`401`** — Unauthorized: Authentication credentials were missing or incorrect.
- **`403`** — Forbidden: The request was understood, but it has been refused or access is not allowed.
- **`404`** — Not Found: The requested URI is invalid, or the resource requested (such as a user) does not exist. This response is also returned when the requested format is not supported by the requested method.
- **`405`** — Method Not Allowed: The request was made to a resource using an HTTP method that is not supported.
- **`409`** — Conflict: The request could not be processed because it conflicts with some established rule of the system. For example, a person may not be added to a room more than once.
- **`410`** — Gone: The requested resource is no longer available.
- **`415`** — Unsupported Media Type: The request was made to a resource without specifying a media type, or with a media type that is not supported.
- **`423`** — Locked: The requested resource is temporarily unavailable. A Retry-After header may be present to indicate how many seconds you should wait before attempting the request again.
- **`428`** — Precondition Required: The file(s) cannot be scanned for malware and must be force downloaded.
- **`429`** — Too Many Requests: Too many requests have been sent in a given period of time and the request has been rate limited. A Retry-After header should be present that specifies how many seconds you need to wait before a successful request can be made.
- **`500`** — Internal Server Error: Something went wrong on the server. If the issue persists, please contact the [Webex Developer Support team](/explore/support).
- **`502`** — Bad Gateway: The server received an invalid response from an upstream server while processing the request. Try again later.
- **`503`** — Service Unavailable: Server is overloaded with requests. Try again later.
- **`504`** — Gateway Timeout: An upstream server failed to respond in time. If your query uses the max parameter, please try reducing its value.

---

### 4.5 Hybrid Data Security (HDS): Get Multi-Tenant Hybrid Data Security organization details

**Endpoint:** `GET /hds/organizations/{organizationId}/tenants`

Retrieve details of Multi-Tenant Hybrid Data Security organization such as Organization Name and ID, CMK state and state of Tenants Organizations.
To obtain the Organization ID needed for this API, use the [Organizations API](</docs/api/v1/organizations/list-organizations>)

#### Parameters

| Name | In | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| `organizationId` | `path` | `string` | Yes | Unique ID of the Hybrid Data Security organization. |

#### Responses

- **`200`** — Ok
  ```json
  {
    "type": "object",
    "properties": {
      "context": {
        "type": "object",
        "properties": {
          "partnerOrgId": {
            "type": "string",
            "example": "Y2lzY29zcGFyazovL3VzL0hZQlJJRF9DTFVTVEVSLzFlYjY1ZmRmLTk2NDMtNDE3Zi05OTc0LWFkNzJjYWUwZTEwZjpiMzdmNTgzYy1kZGRjLTQyOGItODJlNS1jYmU2ODFkYjQ5NjI",
            "description": "Unique ID of the partner organization."
          }
        },
        "description": "Metadata information about the response payload."
      },
      "tenants": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "tenantOrgId": {
              "type": "string",
              "example": "Y2lzY29zcGFyazovL3VzL0hZQlJJRF9DTFVTVEVSLzFlYjY1ZmRmLTk2NDMtNDE3Zi05OTc0LWFCGCGCGH",
              "description": "Unique ID of the tenant organization."
            },
            "tenantOrgName": {
              "type": "string",
              "example": "abcd",
              "description": "Name of the tenant organization."
            },
            "cmkState": {
              "type": "string",
              "example": "CMK Managed",
              "description": "Customer Managed Key (CMK) state of the tenant organization."
            },
            "tenantOrgState": {
              "type": "string",
              "example": "Setup complete",
              "description": "Current state of the tenant organization."
            }
          },
          "$$ref": "#/components/schemas/tenantDetails"
        },
        "description": "List of tenant organizations under the partner organization."
      }
    },
    "$$ref": "#/components/schemas/multiTenantHDSOrgDetailsResponse"
  }
  ```
- **`400`** — Bad Request: The request was invalid or could not be processed. An accompanying error message will provide more details.
- **`401`** — Unauthorized: Authentication credentials were missing or incorrect.
- **`403`** — Forbidden: The request was understood, but it has been refused or access is not allowed.
- **`404`** — Not Found: The requested URI is invalid, or the resource requested (such as a user) does not exist. This response is also returned when the requested format is not supported by the requested method.
- **`405`** — Method Not Allowed: The request was made to a resource using an HTTP method that is not supported.
- **`409`** — Conflict: The request could not be processed because it conflicts with some established rule of the system. For example, a person may not be added to a room more than once.
- **`410`** — Gone: The requested resource is no longer available.
- **`415`** — Unsupported Media Type: The request was made to a resource without specifying a media type, or with a media type that is not supported.
- **`423`** — Locked: The requested resource is temporarily unavailable. A Retry-After header may be present to indicate how many seconds you should wait before attempting the request again.
- **`428`** — Precondition Required: The file(s) cannot be scanned for malware and must be force downloaded.
- **`429`** — Too Many Requests: Too many requests have been sent in a given period of time and the request has been rate limited. A Retry-After header should be present that specifies how many seconds you need to wait before a successful request can be made.
- **`500`** — Internal Server Error: Something went wrong on the server. If the issue persists, please contact the [Webex Developer Support team](/explore/support).
- **`502`** — Bad Gateway: The server received an invalid response from an upstream server while processing the request. Try again later.
- **`503`** — Service Unavailable: Server is overloaded with requests. Try again later.
- **`504`** — Gateway Timeout: An upstream server failed to respond in time. If your query uses the max parameter, please try reducing its value.

---

### 4.6 Hybrid Data Security (HDS): Get node details

**Endpoint:** `GET /hds/nodes/{nodeId}`

Retrieve details for a specific Hybrid Data Security node, such as host name, release version, proxy details, deployment and build type, availability details, etc.
To obtain the Node ID needed for this API, use the [Get cluster details API](</docs/api/v1/hds/get-cluster-details>)

#### Parameters

| Name | In | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| `nodeId` | `path` | `string` | Yes | Unique ID of the Hybrid Data Security node |

#### Responses

- **`200`** — Ok
  ```json
  {
    "type": "object",
    "properties": {
      "context": {
        "type": "object",
        "properties": {
          "orgId": {
            "type": "string",
            "example": "Y2lzY29zcGFyazovL3VzL0hZQlJJRF9DTFVTVEVSLzFlYjY1ZmRmLTk2NDMtNDE3Zi05OTc0LWFkNzJVGNG",
            "description": "Unique ID of the organization."
          },
          "clusterId": {
            "type": "string",
            "example": "Y2lzY29zcGFyazovL3VzL0hZQlJJRF9DTFVTVEVSLzFlYjY1ZmRmLTk2NDMtNDE3Zi05OTc0LWFkNzJjYWUwZTEwZjpiMzdmNTgzYy1kZGRjLTQyOGItODJlNS1jYmU2ODFkYjQ5NjI",
            "description": "Unique ID of the cluster."
          },
          "clusterName": {
            "type": "string",
            "example": "San Jose",
            "description": "Name of the cluster."
          }
        },
        "description": "Metadata information about the cluster to which the node belongs."
      },
      "nodeId": {
        "type": "string",
        "example": "Y2lzY29zcGFyazovL3VzL0hZQlJJRF9DTFVTVEVSLzM2ZDg5NGY3LTJiNTctNDNjMS1hY2VlLWQ0N2U2Nzc2MTQxNDo0NjdiNGIxZC1jZWI2LTQwN2EtYWZmOC1mMjIxZmFiNzhjNzI",
        "description": "Unique ID of the connector/node."
      },
      "host": {
        "type": "string",
        "example": "xyz.abc.com",
        "description": "Host Name or Host IP of the Hybrid Data Security node."
      },
      "availabilityDetails": {
        "type": "object",
        "properties": {
          "nodeAvailability": {
            "type": "string",
            "example": "Online",
            "description": "Current availability of the Hybrid Data Security node."
          },
          "hdsHealthStatus": {
            "type": "string",
            "example": "Healthy / Unhealthy",
            "description": "Health status of the Hybrid Data Security node."
          },
          "hdsUnhealthyReasons": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "example": [
              "kms unhealthy",
              "avalon unhealthy"
            ],
            "description": "List of reasons for unhealthy status of the Hybrid Data Security node."
          }
        },
        "description": "Availability and health details of the Hybrid Data Security node."
      },
      "releaseVersion": {
        "type": "string",
        "example": "2025.07.16.7042",
        "description": "The release version of the Hybrid Data Security node."
      },
      "proxyType": {
        "type": "string",
        "example": "Explicit",
        "description": "Proxy type used by the Hybrid Data Security node."
      },
      "proxyStatus": {
        "type": "string",
        "example": "Enabled",
        "description": "Current proxy status of the Hybrid Data Security node."
      },
      "maintenanceMode": {
        "type": "string",
        "example": "On",
        "description": "On indicates that the node is in maintenance mode, and Off indicates that the node is not in maintenance mode."
      },
      "ntpSync": {
        "type": "string",
        "example": "active",
        "description": "NTP sync status of the Hybrid Data Security node."
      },
      "ovaDeploymentType": {
        "type": "string",
        "example": "Large",
        "description": "Deployment type of the Hybrid Data Security node."
      },
      "ovaBuildType": {
        "type": "string",
        "example": "Dev",
        "description": "Build type of the Hybrid Data Security node."
      }
    },
    "$$ref": "#/components/schemas/nodeDetailsResponse"
  }
  ```
- **`400`** — Bad Request: The request was invalid or could not be processed. An accompanying error message will provide more details.
- **`401`** — Unauthorized: Authentication credentials were missing or incorrect.
- **`403`** — Forbidden: The request was understood, but it has been refused or access is not allowed.
- **`404`** — Not Found: The requested URI is invalid, or the resource requested (such as a user) does not exist. This response is also returned when the requested format is not supported by the requested method.
- **`405`** — Method Not Allowed: The request was made to a resource using an HTTP method that is not supported.
- **`409`** — Conflict: The request could not be processed because it conflicts with some established rule of the system. For example, a person may not be added to a room more than once.
- **`410`** — Gone: The requested resource is no longer available.
- **`415`** — Unsupported Media Type: The request was made to a resource without specifying a media type, or with a media type that is not supported.
- **`423`** — Locked: The requested resource is temporarily unavailable. A Retry-After header may be present to indicate how many seconds you should wait before attempting the request again.
- **`428`** — Precondition Required: The file(s) cannot be scanned for malware and must be force downloaded.
- **`429`** — Too Many Requests: Too many requests have been sent in a given period of time and the request has been rate limited. A Retry-After header should be present that specifies how many seconds you need to wait before a successful request can be made.
- **`500`** — Internal Server Error: Something went wrong on the server. If the issue persists, please contact the [Webex Developer Support team](/explore/support).
- **`502`** — Bad Gateway: The server received an invalid response from an upstream server while processing the request. Try again later.
- **`503`** — Service Unavailable: Server is overloaded with requests. Try again later.
- **`504`** — Gateway Timeout: An upstream server failed to respond in time. If your query uses the max parameter, please try reducing its value.

---

### 4.7 Hybrid Data Security (HDS): Get organization details

**Endpoint:** `GET /hds/organizations/{organizationId}`

Retrieve details for an Hybrid Data Security organization, such as the organization name, type of organization.
To obtain the Organization ID needed for this API, use the [Organizations API](</docs/api/v1/organizations/list-organizations>)

#### Parameters

| Name | In | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| `organizationId` | `path` | `string` | Yes | Unique ID of the Hybrid Data Security organization. |

#### Responses

- **`200`** — Ok
  ```json
  {
    "type": "object",
    "properties": {
      "orgId": {
        "type": "string",
        "example": "Y2lzY29zcGFyazovL3VzL09SR0FOSVpBVElPTi8yYzNjOWY5NS03M2Q5LTQ0NjAtYTY2OC0wNDcxNjJmZjFiYWQ",
        "description": "Unique ID of the organization."
      },
      "orgName": {
        "type": "string",
        "example": "HDS_Demo",
        "description": "Name of the organization."
      },
      "orgType": {
        "type": "string",
        "example": "Single Tenant",
        "description": "Type of the organization."
      },
      "orgMode": {
        "type": "string",
        "example": "Production",
        "description": "Mode of the organization."
      }
    },
    "$$ref": "#/components/schemas/orgDetailsResponse"
  }
  ```
- **`400`** — Bad Request: The request was invalid or could not be processed. An accompanying error message will provide more details.
- **`401`** — Unauthorized: Authentication credentials were missing or incorrect.
- **`403`** — Forbidden: The request was understood, but it has been refused or access is not allowed.
- **`404`** — Not Found: The requested URI is invalid, or the resource requested (such as a user) does not exist. This response is also returned when the requested format is not supported by the requested method.
- **`405`** — Method Not Allowed: The request was made to a resource using an HTTP method that is not supported.
- **`409`** — Conflict: The request could not be processed because it conflicts with some established rule of the system. For example, a person may not be added to a room more than once.
- **`410`** — Gone: The requested resource is no longer available.
- **`415`** — Unsupported Media Type: The request was made to a resource without specifying a media type, or with a media type that is not supported.
- **`423`** — Locked: The requested resource is temporarily unavailable. A Retry-After header may be present to indicate how many seconds you should wait before attempting the request again.
- **`428`** — Precondition Required: The file(s) cannot be scanned for malware and must be force downloaded.
- **`429`** — Too Many Requests: Too many requests have been sent in a given period of time and the request has been rate limited. A Retry-After header should be present that specifies how many seconds you need to wait before a successful request can be made.
- **`500`** — Internal Server Error: Something went wrong on the server. If the issue persists, please contact the [Webex Developer Support team](/explore/support).
- **`502`** — Bad Gateway: The server received an invalid response from an upstream server while processing the request. Try again later.
- **`503`** — Service Unavailable: Server is overloaded with requests. Try again later.
- **`504`** — Gateway Timeout: An upstream server failed to respond in time. If your query uses the max parameter, please try reducing its value.

---

### 4.8 Hybrid Data Security (HDS): Get resource usage for an Hybrid Data Security node

**Endpoint:** `GET /hds/nodes/{nodeId}/resourceUsage`

Retrieve CPU, memory, and disk resource usage details for a specific Hybrid Data Security node over the requested time range.
To obtain the Node ID needed for this API, use the [List nodes for an Hybrid Data Security cluster API](</docs/api/v1/hds/list-hds-cluster-nodes>)

#### Parameters

| Name | In | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| `nodeId` | `path` | `string` | Yes | Unique ID of the Hybrid Data Security node. |
| `from` | `query` | `string` | Yes | The start date and time of the requested data in any [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) compliant format. |
| `to` | `query` | `string` | Yes | The end date and time of the requested data in any [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) compliant format. |

#### Responses

- **`200`** — OK
  ```json
  {
    "type": "object",
    "properties": {
      "context": {
        "type": "object",
        "properties": {
          "orgId": {
            "type": "string",
            "example": "Y2lzY29zcGFyazovL3VzL0hZQlJJRF9DTFVTVEVSLzFlYjY1ZmRmLTk2NDMtNDE3Zi05OTc0LWFkNzJVGNG",
            "description": "Unique ID of the organization."
          },
          "clusterId": {
            "type": "string",
            "example": "Y2lzY29zcGFyazovL3VzL0hZQlJJRF9DTFVTVEVSLzFlYjY1ZmRmLTk2NDMtNDE3Zi05OTc0LWFkNzJjYWUwZTEwZjpiMzdmNTgzYy1kZGRjLTQyOGItODJlNS1jYmU2ODFkYjQ5NjI",
            "description": "Unique ID of the cluster."
          },
          "clusterName": {
            "type": "string",
            "example": "cluster-1",
            "description": "Name of the cluster."
          },
          "nodeId": {
            "type": "string",
            "example": "Y2lzY29zcGFyazovL3VzL0hZQlJJRF9DTFVTVEVSLzFlYjY1ZmRmLTk2NDMtNDE3Zi05OTc0LWFkNzJjYWUwZTEwZjpiMzdmNTgzYy1kZGRjLTQyOGItODJlNS1jYmU2ODFkYjQ5NjI",
            "description": "Unique ID of the node."
          },
          "host": {
            "type": "string",
            "example": "xyz.abc.com",
            "description": "Host name or IP address of the Hybrid Data Security node."
          }
        },
        "description": "Metadata information about the node for which resource usage is being retrieved."
      },
      "resourceUsage": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "startTime": {
              "type": "string",
              "format": "date-time",
              "example": "2025-06-15T15:00:00Z",
              "description": "Start time of the resource usage segment."
            },
            "endTime": {
              "type": "string",
              "format": "date-time",
              "example": "2025-06-15T15:10:00Z",
              "description": "End time of the resource usage segment."
            },
            "cpuUsage": {
              "type": "object",
              "properties": {
                "peakCpuUsagePercent": {
                  "type": "number",
                  "example": 30.78,
                  "description": "Peak CPU usage percentage in the segment."
                },
                "averageCpuUsagePercent": {
                  "type": "number",
                  "example": 8.9,
                  "description": "Average CPU usage percentage in the segment."
                }
              },
              "description": "CPU usage details for the segment."
            },
            "memoryUsage": {
              "type": "object",
              "properties": {
                "totalMemoryUsageInMB": {
                  "type": "number",
                  "example": 7454,
                  "description": "Total memory available on the node in MB."
                },
                "peakMemoryUsageInMB": {
                  "type": "number",
                  "example": 6075,
                  "description": "Peak memory usage in MB in the segment."
                },
                "peakMemoryUsagePercent": {
                  "type": "number",
                  "example": 81.5,
                  "description": "Peak memory usage percentage in the segment."
                },
                "averageMemoryUsageInMB": {
                  "type": "number",
                  "example": 6042,
                  "description": "Average memory usage in MB in the segment."
                },
                "averageMemoryUsagePercent": {
                  "type": "number",
                  "example": 81.06,
                  "description": "Average memory usage percentage in the segment."
                }
              },
              "description": "Memory usage details for the segment."
            },
            "diskUsage": {
              "type": "object",
              "properties": {
                "totalDiskSpaceUsageInMB": {
                  "type": "number",
                  "example": 37308,
                  "description": "Total disk space available on the node in MB."
                },
                "peakDiskSpaceUsageInMB": {
                  "type": "number",
                  "example": 18874,
                  "description": "Peak disk space usage in MB in the segment."
                },
                "peakDiskUsagePercent": {
                  "type": "number",
                  "example": 50.59,
                  "description": "Peak disk usage percentage in the segment."
                },
                "averageDiskUsage": {
                  "type": "number",
                  "example": 18874,
                  "description": "Average disk usage in MB in the segment."
                },
                "averageDiskUsagePercent": {
                  "type": "number",
                  "example": 50.59,
                  "description": "Average disk usage percentage in the segment."
                }
              },
              "description": "Disk usage details for the segment."
            }
          },
          "$$ref": "#/components/schemas/nodeResourceUsageSegment"
        },
        "description": "List of resource usage segments over the requested time range."
      },
      "timeRange": {
        "type": "object",
        "properties": {
          "from": {
            "type": "string",
            "format": "date-time",
            "example": "2025-06-15T15:00:00Z",
            "description": "Start time of the requested data range."
          },
          "to": {
            "type": "string",
            "format": "date-time",
            "example": "2025-06-15T15:20:00Z",
            "description": "End time of the requested data range."
          }
        },
        "description": "The time range for the resource usage data."
      }
    },
    "$$ref": "#/components/schemas/nodeResourceUsageResponse"
  }
  ```
- **`400`** — Bad Request: The request was invalid or could not be processed. An accompanying error message will provide more details.
- **`401`** — Unauthorized: Authentication credentials were missing or incorrect.
- **`403`** — Forbidden: The request was understood, but it has been refused or access is not allowed.
- **`404`** — Not Found: The requested URI is invalid, or the resource requested (such as a user) does not exist. This response is also returned when the requested format is not supported by the requested method.
- **`405`** — Method Not Allowed: The request was made to a resource using an HTTP method that is not supported.
- **`409`** — Conflict: The request could not be processed because it conflicts with some established rule of the system. For example, a person may not be added to a room more than once.
- **`410`** — Gone: The requested resource is no longer available.
- **`415`** — Unsupported Media Type: The request was made to a resource without specifying a media type, or with a media type that is not supported.
- **`423`** — Locked: The requested resource is temporarily unavailable. A Retry-After header may be present to indicate how many seconds you should wait before attempting the request again.
- **`428`** — Precondition Required: The file(s) cannot be scanned for malware and must be force downloaded.
- **`429`** — Too Many Requests: Too many requests have been sent in a given period of time and the request has been rate limited. A Retry-After header should be present that specifies how many seconds you need to wait before a successful request can be made.
- **`500`** — Internal Server Error: Something went wrong on the server. If the issue persists, please contact the [Webex Developer Support team](/explore/support).
- **`502`** — Bad Gateway: The server received an invalid response from an upstream server while processing the request. Try again later.
- **`503`** — Service Unavailable: Server is overloaded with requests. Try again later.
- **`504`** — Gateway Timeout: An upstream server failed to respond in time. If your query uses the max parameter, please try reducing its value.

---

### 4.9 Hybrid Data Security (HDS): Get test results for Hybrid Data Security node

**Endpoint:** `GET /hds/testResults/nodes/{nodeId}/networkTest`

Get the latest results of the network tests triggered for a single Hybrid Data Security node. The test results are generated as part of the Network Test execution on the node. The network tests include the Bandwidth Test, DNS Resolution Test, and HTTPS Connectivity Test.
 The results from the latest test run are provided, covering up to the past 90 days if available.
To obtain the Node ID needed for this API, use the [Get cluster details API](</docs/api/v1/hds/get-cluster-details>)

#### Parameters

| Name | In | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| `nodeId` | `path` | `string` | Yes | Unique ID of the Hybrid Data Security node. |
| `triggerType` | `query` | `string` | No | Trigger type. |

#### Responses

- **`200`** — OK
  ```json
  {
    "type": "object",
    "properties": {
      "context": {
        "type": "object",
        "properties": {
          "orgId": {
            "type": "string",
            "example": "Y2lzY29zcGFyazovL3VzL0hZQlJJRF9DTFVTVEVSLzFlYjY1ZmRmLTk2NDMtNDE3Zi05OTc0LWFkNzJVGNG",
            "description": "Unique ID of the organization."
          },
          "clusterId": {
            "type": "string",
            "example": "Y2lzY29zcGFyazovL3VzL0hZQlJJRF9DTFVTVEVSLzJjM2M5Zjk1LTczZDktNDQ2MC1hNjY4LTA0NzE2MmZmMWJhZDpmMWJmMGI1MC0yMDUyLTQ3ZmUtYjg3ZC01MTFjMmZlNzQ3MWI=",
            "description": "Unique ID of the cluster."
          },
          "clusterName": {
            "type": "string",
            "example": "hds_bangalore",
            "description": "Name of the cluster."
          },
          "nodeId": {
            "type": "string",
            "example": "Y2lzY29zcGFyazovL3VzL0hZQlJJRF9DT05ORUNUT1IvMmMzYzlmOTUtNzNkOS00NDYwLWE2NjgtMDQ3MTYyZmYxYmFkOjE1NmRmNzg5Yzg1NTRkNTVhMjc1ZGY5OTc4Zjk5MDJk",
            "description": "Unique ID of the node."
          },
          "hostName": {
            "type": "string",
            "example": "abc.xyz.com",
            "description": "Hostname of the Hybrid Data Security node."
          },
          "hostIP": {
            "type": "string",
            "example": "10.196.5.82",
            "description": "IP address of the Hybrid Data Security node."
          }
        },
        "description": "Metadata information about the node for which network test results are being retrieved."
      },
      "testResults": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "timestamp": {
              "type": "string",
              "format": "date-time",
              "example": "2025-06-15T15:53:00Z",
              "description": "Timestamp when the test was triggered."
            },
            "triggerType": {
              "type": "string",
              "example": "OnDemand",
              "description": "Type of trigger for the test."
            },
            "result": {
              "type": "array",
              "items": {
                "type": "object",
                "properties": {
                  "type": {
                    "type": "string",
                    "example": "DNSResolutionTest",
                    "description": "Type of network test."
                  },
                  "results": {
                    "type": "array",
                    "items": {
                      "type": "object",
                      "properties": {
                        "serviceType": {
                          "type": "string",
                          "example": "WebexCloud",
                          "description": "Type of service."
                        },
                        "services": {
                          "type": "array",
                          "items": {
                            "type": "object",
                            "properties": {
                              "serviceName": {
                                "type": "string",
                                "example": "idBroker",
                                "description": "Name of the service."
                              },
                              "testResult": {
                                "type": "string",
                                "example": "Success",
                                "description": "Result of the test for the service."
                              },
                              "failureDetails": {
                                "type": "object",
                                "properties": {
                                  "possibleFailureReason": {
                                    "type": "array",
                                    "items": {
                                      "type": "string"
                                    },
                                    "example": [
                                      "DNS Resolution issue detected in the Hybrid Data Security Node [Error Code: 1302]."
                                    ],
                                    "description": "List of possible reasons for the test failure."
                                  },
                                  "possibleRemediation": {
                                    "type": "array",
                                    "items": {
                                      "type": "string"
                                    },
                                    "example": [
                                      "Please ensure that the configured DNS Servers are correct and healthy, and verify the network settings are adhering to the Hybrid Data Security Deployment Guide."
                                    ],
                                    "description": "List of suggested remediation steps."
                                  }
                                },
                                "description": "Failure details for a failed network test, present only when testResult is Failed.",
                                "$$ref": "#/components/schemas/networkTestFailureDetails"
                              }
                            },
                            "$$ref": "#/components/schemas/singleServiceTestResult"
                          },
                          "description": "List of individual service test results."
                        }
                      },
                      "$$ref": "#/components/schemas/serviceTestResults"
                    },
                    "description": "List of service type test results."
                  }
                },
                "$$ref": "#/components/schemas/networkTestTypeResult"
              },
              "description": "List of results per test type."
            }
          },
          "$$ref": "#/components/schemas/networkTestResult"
        },
        "description": "List of network test results."
      }
    },
    "$$ref": "#/components/schemas/networkTestsResultsResponse"
  }
  ```
- **`400`** — Bad Request: The request was invalid or could not be processed. An accompanying error message will provide more details.
- **`401`** — Unauthorized: Authentication credentials were missing or incorrect.
- **`403`** — Forbidden: The request was understood, but it has been refused or access is not allowed.
- **`404`** — Not Found: The requested URI is invalid, or the resource requested (such as a user) does not exist. This response is also returned when the requested format is not supported by the requested method.
- **`405`** — Method Not Allowed: The request was made to a resource using an HTTP method that is not supported.
- **`409`** — Conflict: The request could not be processed because it conflicts with some established rule of the system. For example, a person may not be added to a room more than once.
- **`410`** — Gone: The requested resource is no longer available.
- **`415`** — Unsupported Media Type: The request was made to a resource without specifying a media type, or with a media type that is not supported.
- **`423`** — Locked: The requested resource is temporarily unavailable. A Retry-After header may be present to indicate how many seconds you should wait before attempting the request again.
- **`428`** — Precondition Required: The file(s) cannot be scanned for malware and must be force downloaded.
- **`429`** — Too Many Requests: Too many requests have been sent in a given period of time and the request has been rate limited. A Retry-After header should be present that specifies how many seconds you need to wait before a successful request can be made.
- **`500`** — Internal Server Error: Something went wrong on the server. If the issue persists, please contact the [Webex Developer Support team](/explore/support).
- **`502`** — Bad Gateway: The server received an invalid response from an upstream server while processing the request. Try again later.
- **`503`** — Service Unavailable: Server is overloaded with requests. Try again later.
- **`504`** — Gateway Timeout: An upstream server failed to respond in time. If your query uses the max parameter, please try reducing its value.

---

### 4.10 Hybrid Data Security (HDS): List clusters for an Hybrid Data Security organization

**Endpoint:** `GET /hds/organizations/{organizationId}/clusters`

Retrieve a list of all clusters for a specific Hybrid Data Security organization, including cluster status, release channel, and upgrade schedule details.
To obtain the Organization ID needed for this API, use the [Organizations API](</docs/api/v1/organizations/list-organizations>)

#### Parameters

| Name | In | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| `organizationId` | `path` | `string` | Yes | Unique ID of the Hybrid Data Security organization. |

#### Responses

- **`200`** — OK
  ```json
  {
    "type": "object",
    "properties": {
      "clusters": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "context": {
              "type": "object",
              "properties": {
                "orgId": {
                  "type": "string",
                  "example": "Y2lzY29zcGFyazovL3VzL09SR0FOSVpBVElPTi8yYzNjOWY5NS03M2Q5LTQ0NjAtYTY2OC0wNDcxNjJmZjFiYWQ=",
                  "description": "Unique ID of the organization."
                }
              },
              "description": "Metadata information about the organization for which the cluster details are being retrieved."
            },
            "clusterId": {
              "type": "string",
              "example": "Y2lzY29zcGFyazovL3VzL0hZQlJJRF9DTFVTVEVSLzJjM2M5Zjk1LTczZDktNDQ2MC1hNjY4LTA0NzE2MmZmMWJhZDpmMWJmMGI1MC0yMDUyLTQ3ZmUtYjg3ZC01MTFjMmZlNzQ3MWI",
              "description": "Unique ID of the cluster."
            },
            "clusterName": {
              "type": "string",
              "example": "Bangalore",
              "description": "Name of the cluster."
            },
            "clusterStatus": {
              "type": "string",
              "example": "Operational",
              "description": "Current status of the cluster."
            },
            "releaseChannel": {
              "type": "string",
              "example": "beta",
              "description": "Release channel of the cluster."
            },
            "upgradeSchedule": {
              "type": "object",
              "properties": {
                "scheduleDays": {
                  "type": "array",
                  "items": {
                    "type": "string",
                    "example": "sunday"
                  },
                  "description": "Days of the week when upgrades are scheduled."
                },
                "scheduleTime": {
                  "type": "string",
                  "example": "02:00",
                  "description": "Time of the day when upgrades are scheduled."
                },
                "scheduleTimeZone": {
                  "type": "string",
                  "example": "Asia/Kolkata",
                  "description": "Time zone for the scheduled upgrade time."
                },
                "nextUpgradeTime": {
                  "type": "string",
                  "example": "2025-07-25T20:30:00Z",
                  "description": "Next scheduled upgrade time."
                }
              },
              "description": "Upgrade schedule details of the cluster."
            }
          },
          "$$ref": "#/components/schemas/clusterDetailsResponse"
        },
        "description": "List of clusters in the organization."
      }
    },
    "$$ref": "#/components/schemas/orgClustersResponse"
  }
  ```
- **`400`** — The request was invalid or could not be processed. An accompanying error message will provide more details.
- **`401`** — Unauthorized: Authentication credentials were missing or incorrect.
- **`403`** — Forbidden: The request was understood, but it has been refused or access is not allowed.
- **`404`** — Not Found: The requested URI is invalid, or the resource requested (such as a user) does not exist. This response is also returned when the requested format is not supported by the requested method.
- **`405`** — Method Not Allowed: The request was made to a resource using an HTTP method that is not supported.
- **`409`** — Conflict: The request could not be processed because it conflicts with some established rule of the system. For example, a person may not be added to a room more than once.
- **`410`** — Gone: The requested resource is no longer available.
- **`415`** — Unsupported Media Type: The request was made to a resource without specifying a media type, or with a media type that is not supported.
- **`423`** — Locked: The requested resource is temporarily unavailable. A Retry-After header may be present to indicate how many seconds you should wait before attempting the request again.
- **`428`** — Precondition Required: The file(s) cannot be scanned for malware and must be force downloaded.
- **`429`** — Too Many Requests: Too many requests have been sent in a given period of time and the request has been rate limited. A Retry-After header should be present that specifies how many seconds you need to wait before a successful request can be made.
- **`500`** — Internal Server Error: Something went wrong on the server. If the issue persists, please contact the [Webex Developer Support team](/explore/support).
- **`502`** — Bad Gateway: The server received an invalid response from an upstream server while processing the request. Try again later.
- **`503`** — Service Unavailable: Server is overloaded with requests. Try again later.
- **`504`** — Gateway Timeout: An upstream server failed to respond in time. If your query uses the max parameter, please try reducing its value.

---

### 4.11 Hybrid Data Security (HDS): List nodes for an Hybrid Data Security cluster

**Endpoint:** `GET /hds/clusters/{clusterId}/nodes`

Retrieve a list of all nodes for a specific Hybrid Data Security cluster, including availability, proxy details, deployment type, and release version.
To obtain the Cluster ID needed for this API, use the [List clusters for an Hybrid Data Security organization API](</docs/api/v1/hds/list-hds-organization-clusters>)

#### Parameters

| Name | In | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| `clusterId` | `path` | `string` | Yes | Unique ID of the Hybrid Data Security cluster. |

#### Responses

- **`200`** — OK
  ```json
  {
    "type": "object",
    "properties": {
      "nodes": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "context": {
              "type": "object",
              "properties": {
                "orgId": {
                  "type": "string",
                  "example": "Y2lzY29zcGFyazovL3VzL0hZQlJJRF9DTFVTVEVSLzFlYjY1ZmRmLTk2NDMtNDE3Zi05OTc0LWFkNzJVGNG",
                  "description": "Unique ID of the organization."
                },
                "clusterId": {
                  "type": "string",
                  "example": "Y2lzY29zcGFyazovL3VzL0hZQlJJRF9DTFVTVEVSLzFlYjY1ZmRmLTk2NDMtNDE3Zi05OTc0LWFkNzJjYWUwZTEwZjpiMzdmNTgzYy1kZGRjLTQyOGItODJlNS1jYmU2ODFkYjQ5NjI",
                  "description": "Unique ID of the cluster."
                },
                "clusterName": {
                  "type": "string",
                  "example": "San Jose",
                  "description": "Name of the cluster."
                }
              },
              "description": "Metadata information about the cluster to which the node belongs."
            },
            "nodeId": {
              "type": "string",
              "example": "Y2lzY29zcGFyazovL3VzL0hZQlJJRF9DTFVTVEVSLzM2ZDg5NGY3LTJiNTctNDNjMS1hY2VlLWQ0N2U2Nzc2MTQxNDo0NjdiNGIxZC1jZWI2LTQwN2EtYWZmOC1mMjIxZmFiNzhjNzI",
              "description": "Unique ID of the connector/node."
            },
            "host": {
              "type": "string",
              "example": "xyz.abc.com",
              "description": "Host Name or Host IP of the Hybrid Data Security node."
            },
            "availabilityDetails": {
              "type": "object",
              "properties": {
                "nodeAvailability": {
                  "type": "string",
                  "example": "Online",
                  "description": "Current availability of the Hybrid Data Security node."
                },
                "hdsHealthStatus": {
                  "type": "string",
                  "example": "Healthy / Unhealthy",
                  "description": "Health status of the Hybrid Data Security node."
                },
                "hdsUnhealthyReasons": {
                  "type": "array",
                  "items": {
                    "type": "string"
                  },
                  "example": [
                    "kms unhealthy",
                    "avalon unhealthy"
                  ],
                  "description": "List of reasons for unhealthy status of the Hybrid Data Security node."
                }
              },
              "description": "Availability and health details of the Hybrid Data Security node."
            },
            "releaseVersion": {
              "type": "string",
              "example": "2025.07.16.7042",
              "description": "The release version of the Hybrid Data Security node."
            },
            "proxyType": {
              "type": "string",
              "example": "Explicit",
              "description": "Proxy type used by the Hybrid Data Security node."
            },
            "proxyStatus": {
              "type": "string",
              "example": "Enabled",
              "description": "Current proxy status of the Hybrid Data Security node."
            },
            "maintenanceMode": {
              "type": "string",
              "example": "On",
              "description": "On indicates that the node is in maintenance mode, and Off indicates that the node is not in maintenance mode."
            },
            "ntpSync": {
              "type": "string",
              "example": "active",
              "description": "NTP sync status of the Hybrid Data Security node."
            },
            "ovaDeploymentType": {
              "type": "string",
              "example": "Large",
              "description": "Deployment type of the Hybrid Data Security node."
            },
            "ovaBuildType": {
              "type": "string",
              "example": "Dev",
              "description": "Build type of the Hybrid Data Security node."
            }
          },
          "$$ref": "#/components/schemas/nodeDetailsResponse"
        },
        "description": "List of nodes in the cluster."
      }
    },
    "$$ref": "#/components/schemas/clusterNodesResponse"
  }
  ```
- **`400`** — Bad Request: The request was invalid or could not be processed. An accompanying error message will provide more details.
- **`401`** — Unauthorized: Authentication credentials were missing or incorrect.
- **`403`** — Forbidden: The request was understood, but it has been refused or access is not allowed.
- **`404`** — Not Found: The requested URI is invalid, or the resource requested (such as a user) does not exist. This response is also returned when the requested format is not supported by the requested method.
- **`405`** — Method Not Allowed: The request was made to a resource using an HTTP method that is not supported.
- **`409`** — Conflict: The request could not be processed because it conflicts with some established rule of the system. For example, a person may not be added to a room more than once.
- **`410`** — Gone: The requested resource is no longer available.
- **`415`** — Unsupported Media Type: The request was made to a resource without specifying a media type, or with a media type that is not supported.
- **`423`** — Locked: The requested resource is temporarily unavailable. A Retry-After header may be present to indicate how many seconds you should wait before attempting the request again.
- **`428`** — Precondition Required: The file(s) cannot be scanned for malware and must be force downloaded.
- **`429`** — Too Many Requests: Too many requests have been sent in a given period of time and the request has been rate limited. A Retry-After header should be present that specifies how many seconds you need to wait before a successful request can be made.
- **`500`** — Internal Server Error: Something went wrong on the server. If the issue persists, please contact the [Webex Developer Support team](/explore/support).
- **`502`** — Bad Gateway: The server received an invalid response from an upstream server while processing the request. Try again later.
- **`503`** — Service Unavailable: Server is overloaded with requests. Try again later.
- **`504`** — Gateway Timeout: An upstream server failed to respond in time. If your query uses the max parameter, please try reducing its value.

---

## 5. Memberships

### 5.1 Memberships: Create a Membership

**Endpoint:** `POST /memberships`

Add someone to a room by Person ID or email address, optionally making them a moderator. Compliance Officers cannot add people to empty (team) spaces.

#### Request Body Schema

```json
{
  "type": "object",
  "required": [
    "roomId"
  ],
  "properties": {
    "roomId": {
      "type": "string",
      "example": "Y2lzY29zcGFyazovL3VzL1JPT00vYmJjZWIxYWQtNDNmMS0zYjU4LTkxNDctZjE0YmIwYzRkMTU0",
      "description": "The room ID."
    },
    "personId": {
      "type": "string",
      "example": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS9mNWIzNjE4Ny1jOGRkLTQ3MjctOGIyZi1mOWM0NDdmMjkwNDY",
      "description": "The person ID."
    },
    "personEmail": {
      "type": "string",
      "example": "john.andersen@example.com",
      "description": "The email address of the person."
    },
    "isModerator": {
      "type": "boolean",
      "example": true,
      "description": "Whether or not the participant is a room moderator."
    }
  }
}
```

#### Responses

- **`200`** — OK
  ```json
  {
    "type": "object",
    "properties": {
      "id": {
        "type": "string",
        "example": "Y2lzY29zcGFyazovL3VzL01FTUJFUlNISVAvMGQwYzkxYjYtY2U2MC00NzI1LWI2ZDAtMzQ1NWQ1ZDExZWYzOmNkZTFkZDQwLTJmMGQtMTFlNS1iYTljLTdiNjU1NmQyMjA3Yg",
        "description": "A unique identifier for the membership."
      },
      "roomId": {
        "type": "string",
        "example": "Y2lzY29zcGFyazovL3VzL1JPT00vYmJjZWIxYWQtNDNmMS0zYjU4LTkxNDctZjE0YmIwYzRkMTU0",
        "description": "The room ID."
      },
      "personId": {
        "type": "string",
        "example": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS9mNWIzNjE4Ny1jOGRkLTQ3MjctOGIyZi1mOWM0NDdmMjkwNDY",
        "description": "The person ID."
      },
      "personEmail": {
        "type": "string",
        "example": "john.andersen@example.com",
        "description": "The email address of the person."
      },
      "personDisplayName": {
        "type": "string",
        "example": "John Andersen",
        "description": "The display name of the person."
      },
      "personOrgId": {
        "type": "string",
        "example": "Y2lzY29zcGFyazovL3VzL09SR0FOSVpBVElPTi85NmFiYzJhYS0zZGNjLTExZTUtYTE1Mi1mZTM0ODE5Y2RjOWE",
        "description": "The organization ID of the person."
      },
      "isModerator": {
        "type": "boolean",
        "example": true,
        "description": "Whether or not the participant is a room moderator."
      },
      "isRoomHidden": {
        "type": "boolean",
        "description": "Whether or not the direct type room is hidden in the Webex clients."
      },
      "roomType": {
        "type": "string",
        "enum": [
          "direct",
          "group"
        ],
        "description": "The type of room the membership is associated with.\n * `direct` - 1:1 room.\n * `group` - Group room.\n"
      },
      "isMonitor": {
        "type": "boolean",
        "description": "Whether or not the participant is a monitoring bot (deprecated)."
      },
      "created": {
        "type": "string",
        "example": "2015-10-18T14:26:16.203Z",
        "description": "The date and time when the membership was created."
      }
    },
    "$$ref": "#/components/schemas/Membership"
  }
  ```
- **`400`** — Bad Request: The request was invalid or cannot be otherwise served. An accompanying error message will explain further.
- **`401`** — Unauthorized: Authentication credentials were missing or incorrect.
- **`403`** — Forbidden: The request is understood, but it has been refused or access is not allowed.
- **`404`** — Not Found: The URI requested is invalid or the resource requested, such as a user, does not exist. Also returned when the requested format is not supported by the requested method.
- **`405`** — Method Not Allowed: The request was made to a resource using an HTTP request method that is not supported.
- **`409`** — Conflict: The request could not be processed because it conflicts with some established rule of the system. For example, a person may not be added to a room more than once.
- **`410`** — Gone: The requested resource is no longer available.
- **`415`** — Unsupported Media Type: The request was made to a resource without specifying a media type or used a media type that is not supported.
- **`423`** — Locked: The requested resource is temporarily unavailable. A Retry-After header may be present that specifies how many seconds you need to wait before attempting the request again.
- **`428`** — Precondition Required: File(s) cannot be scanned for malware and need to be force downloaded.
- **`429`** — Too Many Requests: Too many requests have been sent in a given amount of time and the request has been rate limited. A Retry-After header should be present that specifies how many seconds you need to wait before a successful request can be made.
- **`500`** — Internal Server Error: Something went wrong on the server. If the issue persists, feel free to contact the [Webex Developer Support team](/explore/support).
- **`502`** — Bad Gateway: The server received an invalid response from an upstream server while processing the request. Try again later.
- **`503`** — Service Unavailable: Server is overloaded with requests. Try again later.
- **`504`** — Gateway Timeout: An upstream server failed to respond on time. If your query uses max parameter, please try to reduce it.

---

### 5.2 Memberships: Delete a Membership

**Endpoint:** `DELETE /memberships/{membershipId}`

Deletes a membership by ID.

Specify the membership ID in the `membershipId` URI parameter.

The membership for the last moderator of a [Team](/docs/api/v1/teams)'s General space may not be deleted; [promote another user](/docs/api/v1/team-memberships/update-a-team-membership) to team moderator first.

#### Parameters

| Name | In | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| `membershipId` | `path` | `string` | Yes | The unique identifier for the membership. |

#### Responses

- **`204`** — No Content
- **`400`** — Bad Request: The request was invalid or cannot be otherwise served. An accompanying error message will explain further.
- **`401`** — Unauthorized: Authentication credentials were missing or incorrect.
- **`403`** — Forbidden: The request is understood, but it has been refused or access is not allowed.
- **`404`** — Not Found: The URI requested is invalid or the resource requested, such as a user, does not exist. Also returned when the requested format is not supported by the requested method.
- **`405`** — Method Not Allowed: The request was made to a resource using an HTTP request method that is not supported.
- **`409`** — Conflict: The request could not be processed because it conflicts with some established rule of the system. For example, a person may not be added to a room more than once.
- **`410`** — Gone: The requested resource is no longer available.
- **`415`** — Unsupported Media Type: The request was made to a resource without specifying a media type or used a media type that is not supported.
- **`423`** — Locked: The requested resource is temporarily unavailable. A Retry-After header may be present that specifies how many seconds you need to wait before attempting the request again.
- **`428`** — Precondition Required: File(s) cannot be scanned for malware and need to be force downloaded.
- **`429`** — Too Many Requests: Too many requests have been sent in a given amount of time and the request has been rate limited. A Retry-After header should be present that specifies how many seconds you need to wait before a successful request can be made.
- **`500`** — Internal Server Error: Something went wrong on the server. If the issue persists, feel free to contact the [Webex Developer Support team](/explore/support).
- **`502`** — Bad Gateway: The server received an invalid response from an upstream server while processing the request. Try again later.
- **`503`** — Service Unavailable: Server is overloaded with requests. Try again later.
- **`504`** — Gateway Timeout: An upstream server failed to respond on time. If your query uses max parameter, please try to reduce it.

---

### 5.3 Memberships: Get Membership Details

**Endpoint:** `GET /memberships/{membershipId}`

Get details for a membership by ID.

Specify the membership ID in the `membershipId` URI parameter.

#### Parameters

| Name | In | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| `membershipId` | `path` | `string` | Yes | The unique identifier for the membership. |

#### Responses

- **`200`** — OK
  ```json
  {
    "type": "object",
    "properties": {
      "id": {
        "type": "string",
        "example": "Y2lzY29zcGFyazovL3VzL01FTUJFUlNISVAvMGQwYzkxYjYtY2U2MC00NzI1LWI2ZDAtMzQ1NWQ1ZDExZWYzOmNkZTFkZDQwLTJmMGQtMTFlNS1iYTljLTdiNjU1NmQyMjA3Yg",
        "description": "A unique identifier for the membership."
      },
      "roomId": {
        "type": "string",
        "example": "Y2lzY29zcGFyazovL3VzL1JPT00vYmJjZWIxYWQtNDNmMS0zYjU4LTkxNDctZjE0YmIwYzRkMTU0",
        "description": "The room ID."
      },
      "personId": {
        "type": "string",
        "example": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS9mNWIzNjE4Ny1jOGRkLTQ3MjctOGIyZi1mOWM0NDdmMjkwNDY",
        "description": "The person ID."
      },
      "personEmail": {
        "type": "string",
        "example": "john.andersen@example.com",
        "description": "The email address of the person."
      },
      "personDisplayName": {
        "type": "string",
        "example": "John Andersen",
        "description": "The display name of the person."
      },
      "personOrgId": {
        "type": "string",
        "example": "Y2lzY29zcGFyazovL3VzL09SR0FOSVpBVElPTi85NmFiYzJhYS0zZGNjLTExZTUtYTE1Mi1mZTM0ODE5Y2RjOWE",
        "description": "The organization ID of the person."
      },
      "isModerator": {
        "type": "boolean",
        "example": true,
        "description": "Whether or not the participant is a room moderator."
      },
      "isRoomHidden": {
        "type": "boolean",
        "description": "Whether or not the direct type room is hidden in the Webex clients."
      },
      "roomType": {
        "type": "string",
        "enum": [
          "direct",
          "group"
        ],
        "description": "The type of room the membership is associated with.\n * `direct` - 1:1 room.\n * `group` - Group room.\n"
      },
      "isMonitor": {
        "type": "boolean",
        "description": "Whether or not the participant is a monitoring bot (deprecated)."
      },
      "created": {
        "type": "string",
        "example": "2015-10-18T14:26:16.203Z",
        "description": "The date and time when the membership was created."
      }
    },
    "$$ref": "#/components/schemas/Membership"
  }
  ```
- **`400`** — Bad Request: The request was invalid or cannot be otherwise served. An accompanying error message will explain further.
- **`401`** — Unauthorized: Authentication credentials were missing or incorrect.
- **`403`** — Forbidden: The request is understood, but it has been refused or access is not allowed.
- **`404`** — Not Found: The URI requested is invalid or the resource requested, such as a user, does not exist. Also returned when the requested format is not supported by the requested method.
- **`405`** — Method Not Allowed: The request was made to a resource using an HTTP request method that is not supported.
- **`409`** — Conflict: The request could not be processed because it conflicts with some established rule of the system. For example, a person may not be added to a room more than once.
- **`410`** — Gone: The requested resource is no longer available.
- **`415`** — Unsupported Media Type: The request was made to a resource without specifying a media type or used a media type that is not supported.
- **`423`** — Locked: The requested resource is temporarily unavailable. A Retry-After header may be present that specifies how many seconds you need to wait before attempting the request again.
- **`428`** — Precondition Required: File(s) cannot be scanned for malware and need to be force downloaded.
- **`429`** — Too Many Requests: Too many requests have been sent in a given amount of time and the request has been rate limited. A Retry-After header should be present that specifies how many seconds you need to wait before a successful request can be made.
- **`500`** — Internal Server Error: Something went wrong on the server. If the issue persists, feel free to contact the [Webex Developer Support team](/explore/support).
- **`502`** — Bad Gateway: The server received an invalid response from an upstream server while processing the request. Try again later.
- **`503`** — Service Unavailable: Server is overloaded with requests. Try again later.
- **`504`** — Gateway Timeout: An upstream server failed to respond on time. If your query uses max parameter, please try to reduce it.

---

### 5.4 Memberships: List Memberships

**Endpoint:** `GET /memberships`

Lists all room memberships. By default, lists memberships for rooms to which the authenticated user belongs.

Use query parameters to filter the response.

Use `roomId` to list memberships for a room, by ID.

**NOTE**: For moderated team spaces, the list of memberships will include only the space moderators if the user is a team member but not a direct participant of the space.

Use either `personId` or `personEmail` to filter the results. The `roomId` parameter is required when using these parameters.

When the requester is a compliance officer, they can query by `personId` or `personEmail` **WITHOUT** specifying a `roomId`. The response will include **ALL** memberships for the user where a space is owned by an org to which the user belongs.

Long result sets will be split into [pages](/docs/basics#pagination).

#### Parameters

| Name | In | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| `roomId` | `query` | `string` | No | List memberships associated with a room, by ID. |
| `personId` | `query` | `string` | No | List memberships associated with a person, by ID. The `roomId` parameter is required when using this parameter. |
| `personEmail` | `query` | `string` | No | List memberships associated with a person, by email address. The `roomId` parameter is required when using this parameter. |
| `max` | `query` | `number` | No | Limit the maximum number of memberships in the response. |

#### Responses

- **`200`** — OK
  ```json
  {
    "type": "object",
    "properties": {
      "items": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "id": {
              "type": "string",
              "example": "Y2lzY29zcGFyazovL3VzL01FTUJFUlNISVAvMGQwYzkxYjYtY2U2MC00NzI1LWI2ZDAtMzQ1NWQ1ZDExZWYzOmNkZTFkZDQwLTJmMGQtMTFlNS1iYTljLTdiNjU1NmQyMjA3Yg",
              "description": "A unique identifier for the membership."
            },
            "roomId": {
              "type": "string",
              "example": "Y2lzY29zcGFyazovL3VzL1JPT00vYmJjZWIxYWQtNDNmMS0zYjU4LTkxNDctZjE0YmIwYzRkMTU0",
              "description": "The room ID."
            },
            "personId": {
              "type": "string",
              "example": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS9mNWIzNjE4Ny1jOGRkLTQ3MjctOGIyZi1mOWM0NDdmMjkwNDY",
              "description": "The person ID."
            },
            "personEmail": {
              "type": "string",
              "example": "john.andersen@example.com",
              "description": "The email address of the person."
            },
            "personDisplayName": {
              "type": "string",
              "example": "John Andersen",
              "description": "The display name of the person."
            },
            "personOrgId": {
              "type": "string",
              "example": "Y2lzY29zcGFyazovL3VzL09SR0FOSVpBVElPTi85NmFiYzJhYS0zZGNjLTExZTUtYTE1Mi1mZTM0ODE5Y2RjOWE",
              "description": "The organization ID of the person."
            },
            "isModerator": {
              "type": "boolean",
              "example": true,
              "description": "Whether or not the participant is a room moderator."
            },
            "isRoomHidden": {
              "type": "boolean",
              "description": "Whether or not the direct type room is hidden in the Webex clients."
            },
            "roomType": {
              "type": "string",
              "enum": [
                "direct",
                "group"
              ],
              "description": "The type of room the membership is associated with.\n * `direct` - 1:1 room.\n * `group` - Group room.\n"
            },
            "isMonitor": {
              "type": "boolean",
              "description": "Whether or not the participant is a monitoring bot (deprecated)."
            },
            "created": {
              "type": "string",
              "example": "2015-10-18T14:26:16.203Z",
              "description": "The date and time when the membership was created."
            }
          },
          "$$ref": "#/components/schemas/Membership"
        }
      }
    },
    "$$ref": "#/components/schemas/MembershipCollectionResponse"
  }
  ```
- **`400`** — Bad Request: The request was invalid or cannot be otherwise served. An accompanying error message will explain further.
- **`401`** — Unauthorized: Authentication credentials were missing or incorrect.
- **`403`** — Forbidden: The request is understood, but it has been refused or access is not allowed.
- **`404`** — Not Found: The URI requested is invalid or the resource requested, such as a user, does not exist. Also returned when the requested format is not supported by the requested method.
- **`405`** — Method Not Allowed: The request was made to a resource using an HTTP request method that is not supported.
- **`409`** — Conflict: The request could not be processed because it conflicts with some established rule of the system. For example, a person may not be added to a room more than once.
- **`410`** — Gone: The requested resource is no longer available.
- **`415`** — Unsupported Media Type: The request was made to a resource without specifying a media type or used a media type that is not supported.
- **`423`** — Locked: The requested resource is temporarily unavailable. A Retry-After header may be present that specifies how many seconds you need to wait before attempting the request again.
- **`428`** — Precondition Required: File(s) cannot be scanned for malware and need to be force downloaded.
- **`429`** — Too Many Requests: Too many requests have been sent in a given amount of time and the request has been rate limited. A Retry-After header should be present that specifies how many seconds you need to wait before a successful request can be made.
- **`500`** — Internal Server Error: Something went wrong on the server. If the issue persists, feel free to contact the [Webex Developer Support team](/explore/support).
- **`502`** — Bad Gateway: The server received an invalid response from an upstream server while processing the request. Try again later.
- **`503`** — Service Unavailable: Server is overloaded with requests. Try again later.
- **`504`** — Gateway Timeout: An upstream server failed to respond on time. If your query uses max parameter, please try to reduce it.

---

### 5.5 Memberships: Update a Membership

**Endpoint:** `PUT /memberships/{membershipId}`

Updates properties for a membership by ID.

Specify the membership ID in the `membershipId` URI parameter.

#### Parameters

| Name | In | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| `membershipId` | `path` | `string` | Yes | The unique identifier for the membership. |

#### Request Body Schema

```json
{
  "type": "object",
  "required": [
    "isModerator",
    "isRoomHidden"
  ],
  "properties": {
    "isModerator": {
      "type": "boolean",
      "example": true,
      "description": "Whether or not the participant is a room moderator."
    },
    "isRoomHidden": {
      "type": "boolean",
      "description": "When set to true, hides direct spaces in the teams client. Any new message will make the room visible again."
    }
  }
}
```

#### Responses

- **`200`** — OK
  ```json
  {
    "type": "object",
    "properties": {
      "id": {
        "type": "string",
        "example": "Y2lzY29zcGFyazovL3VzL01FTUJFUlNISVAvMGQwYzkxYjYtY2U2MC00NzI1LWI2ZDAtMzQ1NWQ1ZDExZWYzOmNkZTFkZDQwLTJmMGQtMTFlNS1iYTljLTdiNjU1NmQyMjA3Yg",
        "description": "A unique identifier for the membership."
      },
      "roomId": {
        "type": "string",
        "example": "Y2lzY29zcGFyazovL3VzL1JPT00vYmJjZWIxYWQtNDNmMS0zYjU4LTkxNDctZjE0YmIwYzRkMTU0",
        "description": "The room ID."
      },
      "personId": {
        "type": "string",
        "example": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS9mNWIzNjE4Ny1jOGRkLTQ3MjctOGIyZi1mOWM0NDdmMjkwNDY",
        "description": "The person ID."
      },
      "personEmail": {
        "type": "string",
        "example": "john.andersen@example.com",
        "description": "The email address of the person."
      },
      "personDisplayName": {
        "type": "string",
        "example": "John Andersen",
        "description": "The display name of the person."
      },
      "personOrgId": {
        "type": "string",
        "example": "Y2lzY29zcGFyazovL3VzL09SR0FOSVpBVElPTi85NmFiYzJhYS0zZGNjLTExZTUtYTE1Mi1mZTM0ODE5Y2RjOWE",
        "description": "The organization ID of the person."
      },
      "isModerator": {
        "type": "boolean",
        "example": true,
        "description": "Whether or not the participant is a room moderator."
      },
      "isRoomHidden": {
        "type": "boolean",
        "description": "Whether or not the direct type room is hidden in the Webex clients."
      },
      "roomType": {
        "type": "string",
        "enum": [
          "direct",
          "group"
        ],
        "description": "The type of room the membership is associated with.\n * `direct` - 1:1 room.\n * `group` - Group room.\n"
      },
      "isMonitor": {
        "type": "boolean",
        "description": "Whether or not the participant is a monitoring bot (deprecated)."
      },
      "created": {
        "type": "string",
        "example": "2015-10-18T14:26:16.203Z",
        "description": "The date and time when the membership was created."
      }
    },
    "$$ref": "#/components/schemas/Membership"
  }
  ```
- **`400`** — Bad Request: The request was invalid or cannot be otherwise served. An accompanying error message will explain further.
- **`401`** — Unauthorized: Authentication credentials were missing or incorrect.
- **`403`** — Forbidden: The request is understood, but it has been refused or access is not allowed.
- **`404`** — Not Found: The URI requested is invalid or the resource requested, such as a user, does not exist. Also returned when the requested format is not supported by the requested method.
- **`405`** — Method Not Allowed: The request was made to a resource using an HTTP request method that is not supported.
- **`409`** — Conflict: The request could not be processed because it conflicts with some established rule of the system. For example, a person may not be added to a room more than once.
- **`410`** — Gone: The requested resource is no longer available.
- **`415`** — Unsupported Media Type: The request was made to a resource without specifying a media type or used a media type that is not supported.
- **`423`** — Locked: The requested resource is temporarily unavailable. A Retry-After header may be present that specifies how many seconds you need to wait before attempting the request again.
- **`428`** — Precondition Required: File(s) cannot be scanned for malware and need to be force downloaded.
- **`429`** — Too Many Requests: Too many requests have been sent in a given amount of time and the request has been rate limited. A Retry-After header should be present that specifies how many seconds you need to wait before a successful request can be made.
- **`500`** — Internal Server Error: Something went wrong on the server. If the issue persists, feel free to contact the [Webex Developer Support team](/explore/support).
- **`502`** — Bad Gateway: The server received an invalid response from an upstream server while processing the request. Try again later.
- **`503`** — Service Unavailable: Server is overloaded with requests. Try again later.
- **`504`** — Gateway Timeout: An upstream server failed to respond on time. If your query uses max parameter, please try to reduce it.

---

## 6. Messages

### 6.1 Messages: Create a Message

**Endpoint:** `POST /messages`

Post a plain text or [rich text](/docs/basics#formatting-messages) message, and optionally, a [file attachment](/docs/basics#message-attachments) attachment, to a room.

The `files` parameter is an array, which accepts multiple values to allow for future expansion, but currently only one file may be included with the message. File previews are only rendered for attachments of 1MB or less.

#### Request Body Schema

```json
{
  "type": "object",
  "properties": {
    "roomId": {
      "type": "string",
      "example": "Y2lzY29zcGFyazovL3VzL1JPT00vYmJjZWIxYWQtNDNmMS0zYjU4LTkxNDctZjE0YmIwYzRkMTU0",
      "description": "The room ID of the message."
    },
    "parentId": {
      "type": "string",
      "example": "Y2lzY29zcGFyazovL3VzL01FU1NBR0UvZWM1ZTIzZjAtN2RhMS0xMWU5LTg2NTgtZTkzYzNiODZjZmFm",
      "description": "The parent message to reply to."
    },
    "toPersonId": {
      "type": "string",
      "example": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS9mMDZkNzFhNS0wODMzLTRmYTUtYTcyYS1jYzg5YjI1ZWVlMmX",
      "description": "The person ID of the recipient when sending a private 1:1 message."
    },
    "toPersonEmail": {
      "type": "string",
      "example": "julie@example.com",
      "description": "The email address of the recipient when sending a private 1:1 message."
    },
    "text": {
      "type": "string",
      "example": "PROJECT UPDATE - A new project plan has been published on Box: http://box.com/s/lf5vj. The PM for this project is Mike C. and the Engineering Manager is Jane W.",
      "description": "The message, in plain text. If `markdown` is specified this parameter may be *optionally* used to provide alternate text for UI clients that do not support rich text. The maximum message length is 7439 bytes."
    },
    "markdown": {
      "type": "string",
      "example": "**PROJECT UPDATE** A new project plan has been published [on Box](http://box.com/s/lf5vj). The PM for this project is <@personEmail:mike@example.com> and the Engineering Manager is <@personEmail:jane@example.com>.",
      "description": "The message, in Markdown format. The maximum message length is 7439 bytes."
    },
    "files": {
      "type": "array",
      "items": {
        "type": "string",
        "example": "http://www.example.com/images/media.png"
      },
      "description": "The public URL to a binary file to be posted into the room. Only one file is allowed per message. Uploaded files are automatically converted into a format that all Webex clients can render. For the supported media types and the behavior of uploads, see the [Message Attachments Guide](/docs/basics#message-attachments)."
    },
    "attachments": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "contentType": {
            "type": "string",
            "example": "application/vnd.microsoft.card.adaptive",
            "description": "The content type of the attachment."
          },
          "content": {
            "type": "object",
            "required": [
              "type",
              "version"
            ],
            "properties": {
              "type": {
                "type": "string",
                "example": "AdaptiveCard",
                "description": "Must be `AdaptiveCard`."
              },
              "version": {
                "type": "string",
                "example": "1.0",
                "description": "Adaptive Card schema version."
              },
              "body": {
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "type": {
                      "type": "string",
                      "example": "TextBlock"
                    },
                    "text": {
                      "type": "string",
                      "example": "Adaptive Cards"
                    },
                    "size": {
                      "type": "string",
                      "example": "large"
                    }
                  }
                },
                "description": "The card's elements."
              },
              "actions": {
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "type": {
                      "type": "string",
                      "example": "Action.OpenUrl"
                    },
                    "url": {
                      "type": "string",
                      "example": "http://adaptivecards.io"
                    },
                    "title": {
                      "type": "string",
                      "example": "Learn More"
                    }
                  }
                },
                "description": "The card's actions."
              }
            },
            "$$ref": "#/components/schemas/AdaptiveCard"
          }
        },
        "$$ref": "#/components/schemas/Attachment"
      },
      "description": "Content attachments to attach to the message. Only one card per message is supported. See the [Cards Guide](/docs/buttons-and-cards) for more information."
    }
  }
}
```

#### Responses

- **`200`** — OK
  ```json
  {
    "type": "object",
    "properties": {
      "id": {
        "type": "string",
        "example": "Y2lzY29zcGFyazovL3VzL01FU1NBR0UvOTJkYjNiZTAtNDNiZC0xMWU2LThhZTktZGQ1YjNkZmM1NjVk",
        "description": "The unique identifier for the message."
      },
      "parentId": {
        "type": "string",
        "example": "Y2lzY29zcGFyazovL3VzL01FU1NBR0UvOTJkYjNiZTAtNDNiZC0xMWU2LThhZTktZGQ1YjNkZmM1NjVk",
        "description": "The unique identifier for the parent message."
      },
      "roomId": {
        "type": "string",
        "example": "Y2lzY29zcGFyazovL3VzL1JPT00vYmJjZWIxYWQtNDNmMS0zYjU4LTkxNDctZjE0YmIwYzRkMTU0",
        "description": "The room ID of the message."
      },
      "roomType": {
        "type": "string",
        "enum": [
          "direct",
          "group"
        ],
        "description": "The type of room.\n * `direct` - 1:1 room\n * `group` - group room\n"
      },
      "toPersonId": {
        "type": "string",
        "example": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS9mMDZkNzFhNS0wODMzLTRmYTUtYTcyYS1jYzg5YjI1ZWVlMmX",
        "description": "The person ID of the recipient when sending a private 1:1 message."
      },
      "toPersonEmail": {
        "type": "string",
        "example": "julie@example.com",
        "description": "The email address of the recipient when sending a private 1:1 message."
      },
      "text": {
        "type": "string",
        "example": "PROJECT UPDATE - A new project plan has been published om http://example.com/s/lf5vj. The PM for this project is Mike C. and the Engineering Manager is Jane W.",
        "description": "The message, in plain text. If `markdown` is specified this parameter may be *optionally* used to provide alternate text for UI clients that do not support rich text."
      },
      "markdown": {
        "type": "string",
        "example": "**PROJECT UPDATE** A new project plan has been published on <http://box.com/s/lf5vj>. The PM for this project is <@personEmail:mike@example.com> and the Engineering Manager is <@personEmail:jane@example.com>.",
        "description": "The message, in Markdown format."
      },
      "html": {
        "type": "string",
        "example": "<p><strong>PROJECT UPDATE</strong> A new project plan has been published <a href=\\\"http://example.com/s/lf5vj\\\" rel=\\\"nofollow\\\">here</a>. The PM for this project is mike@example.com and the Engineering Manager is jane@example.com.</p>",
        "description": "The text content of the message, in HTML format. This read-only property is used by the Webex clients."
      },
      "files": {
        "type": "array",
        "items": {
          "type": "string",
          "example": "http://www.example.com/images/media.png"
        },
        "description": "Public URLs for files attached to the message. For the supported media types and the behavior of file uploads, see [Message Attachments](/docs/basics#message-attachments)."
      },
      "personId": {
        "type": "string",
        "example": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS9mNWIzNjE4Ny1jOGRkLTQ3MjctOGIyZi1mOWM0NDdmMjkwNDY",
        "description": "The person ID of the message author."
      },
      "personEmail": {
        "type": "string",
        "example": "matt@example.com",
        "description": "The email address of the message author."
      },
      "mentionedPeople": {
        "type": "array",
        "items": {
          "type": "string",
          "example": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS8yNDlmNzRkOS1kYjhhLTQzY2EtODk2Yi04NzllZDI0MGFjNTM,Y2lzY29zcGFyazovL3VzL1BFT1BMRS83YWYyZjcyYy0xZDk1LTQxZjAtYTcxNi00MjlmZmNmYmM0ZDg"
        },
        "description": "People IDs for anyone mentioned in the message."
      },
      "mentionedGroups": {
        "type": "array",
        "items": {
          "type": "string",
          "example": "all"
        },
        "description": "Group names for the groups mentioned in the message."
      },
      "attachments": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "contentType": {
              "type": "string",
              "example": "application/vnd.microsoft.card.adaptive",
              "description": "The content type of the attachment."
            },
            "content": {
              "type": "object",
              "required": [
                "type",
                "version"
              ],
              "properties": {
                "type": {
                  "type": "string",
                  "example": "AdaptiveCard",
                  "description": "Must be `AdaptiveCard`."
                },
                "version": {
                  "type": "string",
                  "example": "1.0",
                  "description": "Adaptive Card schema version."
                },
                "body": {
                  "type": "array",
                  "items": {
                    "type": "object",
                    "properties": {
                      "type": {
                        "type": "string",
                        "example": "TextBlock"
                      },
                      "text": {
                        "type": "string",
                        "example": "Adaptive Cards"
                      },
                      "size": {
                        "type": "string",
                        "example": "large"
                      }
                    }
                  },
                  "description": "The card's elements."
                },
                "actions": {
                  "type": "array",
                  "items": {
                    "type": "object",
                    "properties": {
                      "type": {
                        "type": "string",
                        "example": "Action.OpenUrl"
                      },
                      "url": {
                        "type": "string",
                        "example": "http://adaptivecards.io"
                      },
                      "title": {
                        "type": "string",
                        "example": "Learn More"
                      }
                    }
                  },
                  "description": "The card's actions."
                }
              },
              "$$ref": "#/components/schemas/AdaptiveCard"
            }
          },
          "$$ref": "#/components/schemas/Attachment"
        },
        "description": "Message content attachments attached to the message. See the [Cards Guide](/docs/buttons-and-cards) for more information."
      },
      "created": {
        "type": "string",
        "example": "2015-10-18T14:26:16+00:00",
        "description": "The date and time the message was created."
      },
      "updated": {
        "type": "string",
        "example": "2015-10-18T14:27:16+00:00",
        "description": "The date and time that the message was last edited by the author. This field is only present when the message contents have changed."
      },
      "isVoiceClip": {
        "type": "boolean",
        "description": "True if the audio file is a voice clip recorded by the client; false if the audio file is a standard audio file not posted using the voice clip feature."
      }
    },
    "$$ref": "#/components/schemas/Message"
  }
  ```
- **`400`** — Bad Request: The request was invalid or cannot be otherwise served. An accompanying error message will explain further.
- **`401`** — Unauthorized: Authentication credentials were missing or incorrect.
- **`403`** — Forbidden: The request is understood, but it has been refused or access is not allowed.
- **`404`** — Not Found: The URI requested is invalid or the resource requested, such as a user, does not exist. Also returned when the requested format is not supported by the requested method.
- **`405`** — Method Not Allowed: The request was made to a resource using an HTTP request method that is not supported.
- **`409`** — Conflict: The request could not be processed because it conflicts with some established rule of the system. For example, a person may not be added to a room more than once.
- **`410`** — Gone: The requested resource is no longer available.
- **`415`** — Unsupported Media Type: The request was made to a resource without specifying a media type or used a media type that is not supported.
- **`423`** — Locked: The requested resource is temporarily unavailable. A Retry-After header may be present that specifies how many seconds you need to wait before attempting the request again.
- **`428`** — Precondition Required: File(s) cannot be scanned for malware and need to be force downloaded.
- **`429`** — Too Many Requests: Too many requests have been sent in a given amount of time and the request has been rate limited. A Retry-After header should be present that specifies how many seconds you need to wait before a successful request can be made.
- **`500`** — Internal Server Error: Something went wrong on the server. If the issue persists, feel free to contact the [Webex Developer Support team](/explore/support).
- **`502`** — Bad Gateway: The server received an invalid response from an upstream server while processing the request. Try again later.
- **`503`** — Service Unavailable: Server is overloaded with requests. Try again later.
- **`504`** — Gateway Timeout: An upstream server failed to respond on time. If your query uses max parameter, please try to reduce it.

---

### 6.2 Messages: Delete a Message

**Endpoint:** `DELETE /messages/{messageId}`

Delete a message, by message ID.

Specify the message ID in the `messageId` parameter in the URI.

#### Parameters

| Name | In | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| `messageId` | `path` | `string` | Yes | The unique identifier for the message. |

#### Responses

- **`204`** — No Content
- **`400`** — Bad Request: The request was invalid or cannot be otherwise served. An accompanying error message will explain further.
- **`401`** — Unauthorized: Authentication credentials were missing or incorrect.
- **`403`** — Forbidden: The request is understood, but it has been refused or access is not allowed.
- **`404`** — Not Found: The URI requested is invalid or the resource requested, such as a user, does not exist. Also returned when the requested format is not supported by the requested method.
- **`405`** — Method Not Allowed: The request was made to a resource using an HTTP request method that is not supported.
- **`409`** — Conflict: The request could not be processed because it conflicts with some established rule of the system. For example, a person may not be added to a room more than once.
- **`410`** — Gone: The requested resource is no longer available.
- **`415`** — Unsupported Media Type: The request was made to a resource without specifying a media type or used a media type that is not supported.
- **`423`** — Locked: The requested resource is temporarily unavailable. A Retry-After header may be present that specifies how many seconds you need to wait before attempting the request again.
- **`428`** — Precondition Required: File(s) cannot be scanned for malware and need to be force downloaded.
- **`429`** — Too Many Requests: Too many requests have been sent in a given amount of time and the request has been rate limited. A Retry-After header should be present that specifies how many seconds you need to wait before a successful request can be made.
- **`500`** — Internal Server Error: Something went wrong on the server. If the issue persists, feel free to contact the [Webex Developer Support team](/explore/support).
- **`502`** — Bad Gateway: The server received an invalid response from an upstream server while processing the request. Try again later.
- **`503`** — Service Unavailable: Server is overloaded with requests. Try again later.
- **`504`** — Gateway Timeout: An upstream server failed to respond on time. If your query uses max parameter, please try to reduce it.

---

### 6.3 Messages: Edit a Message

**Endpoint:** `PUT /messages/{messageId}`

Update a message you have posted not more than 10 times.

Specify the `messageId` of the message you want to edit.

Edits of messages containing files or attachments are not currently supported.
If a user attempts to edit a message containing files or attachments a `400 Bad Request` will be returned by the API with a message stating that the feature is currently unsupported.

There is also a maximum number of times a user can edit a message. The maximum currently supported is 10 edits per message.
    If a user attempts to edit a message greater that the maximum times allowed the API will return 400 Bad Request with a message stating the edit limit has been reached.

While only the `roomId` and `text` or `markdown` attributes are *required* in the request body, a common pattern for editing message is to first call `GET /messages/{id}` for the message you wish to edit and to then update the `text` or `markdown` attribute accordingly, passing the updated message object in the request body of the `PUT /messages/{id}` request.
When this pattern is used on a message that included markdown, the `html` attribute must be deleted prior to making the `PUT` request.

#### Parameters

| Name | In | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| `messageId` | `path` | `string` | Yes | The unique identifier for the message. |

#### Request Body Schema

```json
{
  "type": "object",
  "required": [
    "roomId"
  ],
  "properties": {
    "roomId": {
      "type": "string",
      "example": "Y2lzY29zcGFyazovL3VzL1JPT00vYmJjZWIxYWQtNDNmMS0zYjU4LTkxNDctZjE0YmIwYzRkMTU0",
      "description": "The room ID of the message."
    },
    "text": {
      "type": "string",
      "example": "PROJECT UPDATE - A new project plan has been published on http://example.com/s/lf5vj. The PM for this project is Mike C. and the Engineering Manager is Jane W.",
      "description": "The message, in plain text. If `markdown` is specified this parameter may be *optionally* used to provide alternate text for UI clients that do not support rich text. The maximum message length is 7439 bytes."
    },
    "markdown": {
      "type": "string",
      "example": "**PROJECT UPDATE** A new project plan has been published on <http://example.com/s/lf5vj>. The PM for this project is <@personEmail:mike@example.com> and the Engineering Manager is <@personEmail:jane@example.com>.",
      "description": "The message, in Markdown format. If this attribute is set ensure that the request does NOT contain an `html` attribute."
    }
  }
}
```

#### Responses

- **`200`** — OK
  ```json
  {
    "type": "object",
    "properties": {
      "id": {
        "type": "string",
        "example": "Y2lzY29zcGFyazovL3VzL01FU1NBR0UvOTJkYjNiZTAtNDNiZC0xMWU2LThhZTktZGQ1YjNkZmM1NjVk",
        "description": "The unique identifier for the message."
      },
      "parentId": {
        "type": "string",
        "example": "Y2lzY29zcGFyazovL3VzL01FU1NBR0UvOTJkYjNiZTAtNDNiZC0xMWU2LThhZTktZGQ1YjNkZmM1NjVk",
        "description": "The unique identifier for the parent message."
      },
      "roomId": {
        "type": "string",
        "example": "Y2lzY29zcGFyazovL3VzL1JPT00vYmJjZWIxYWQtNDNmMS0zYjU4LTkxNDctZjE0YmIwYzRkMTU0",
        "description": "The room ID of the message."
      },
      "roomType": {
        "type": "string",
        "enum": [
          "direct",
          "group"
        ],
        "description": "The type of room.\n * `direct` - 1:1 room\n * `group` - group room\n"
      },
      "text": {
        "type": "string",
        "example": "PROJECT UPDATE - A new project plan has been published on http://example.com/s/lf5vj. The PM for this project is Mike C. and the Engineering Manager is Jane W.",
        "description": "The message, in plain text. If `markdown` is specified this parameter may be *optionally* used to provide alternate text for UI clients that do not support rich text."
      },
      "markdown": {
        "type": "string",
        "example": "**PROJECT UPDATE** A new project plan has been published on <http://example.com/s/lf5vj>. The PM for this project is <@personEmail:mike@example.com> and the Engineering Manager is <@personEmail:jane@example.com>.",
        "description": "The message, in Markdown format."
      },
      "html": {
        "type": "string",
        "example": "<p><strong>PROJECT UPDATE</strong> A new project plan has been published <a href=\\\"http://example.com/s/lf5vj\\\" rel=\\\"nofollow\\\">here</a>. The PM for this project is mike@example.com and the Engineering Manager is jane@example.com.</p>",
        "description": "The text content of the message, in HTML format. This read-only property is used by the Webex clients."
      },
      "files": {
        "type": "array",
        "items": {
          "type": "string",
          "example": "http://www.example.com/images/media.png"
        },
        "description": "Public URLs for files attached to the message. For the supported media types and the behavior of file uploads, see [Message Attachments](/docs/basics#message-attachments)."
      },
      "personId": {
        "type": "string",
        "example": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS9mNWIzNjE4Ny1jOGRkLTQ3MjctOGIyZi1mOWM0NDdmMjkwNDY",
        "description": "The person ID of the message author."
      },
      "personEmail": {
        "type": "string",
        "example": "matt@example.com",
        "description": "The email address of the message author."
      },
      "mentionedPeople": {
        "type": "array",
        "items": {
          "type": "string",
          "example": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS8yNDlmNzRkOS1kYjhhLTQzY2EtODk2Yi04NzllZDI0MGFjNTM,Y2lzY29zcGFyazovL3VzL1BFT1BMRS83YWYyZjcyYy0xZDk1LTQxZjAtYTcxNi00MjlmZmNmYmM0ZDg"
        },
        "description": "People IDs for anyone mentioned in the message."
      },
      "mentionedGroups": {
        "type": "array",
        "items": {
          "type": "string",
          "example": "all"
        },
        "description": "Group names for the groups mentioned in the message."
      },
      "attachments": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "contentType": {
              "type": "string",
              "example": "application/vnd.microsoft.card.adaptive",
              "description": "The content type of the attachment."
            },
            "content": {
              "type": "object",
              "required": [
                "type",
                "version"
              ],
              "properties": {
                "type": {
                  "type": "string",
                  "example": "AdaptiveCard",
                  "description": "Must be `AdaptiveCard`."
                },
                "version": {
                  "type": "string",
                  "example": "1.0",
                  "description": "Adaptive Card schema version."
                },
                "body": {
                  "type": "array",
                  "items": {
                    "type": "object",
                    "properties": {
                      "type": {
                        "type": "string",
                        "example": "TextBlock"
                      },
                      "text": {
                        "type": "string",
                        "example": "Adaptive Cards"
                      },
                      "size": {
                        "type": "string",
                        "example": "large"
                      }
                    }
                  },
                  "description": "The card's elements."
                },
                "actions": {
                  "type": "array",
                  "items": {
                    "type": "object",
                    "properties": {
                      "type": {
                        "type": "string",
                        "example": "Action.OpenUrl"
                      },
                      "url": {
                        "type": "string",
                        "example": "http://adaptivecards.io"
                      },
                      "title": {
                        "type": "string",
                        "example": "Learn More"
                      }
                    }
                  },
                  "description": "The card's actions."
                }
              },
              "$$ref": "#/components/schemas/AdaptiveCard"
            }
          },
          "$$ref": "#/components/schemas/Attachment"
        },
        "description": "Message content attachments attached to the message. See the [Cards Guide](/docs/buttons-and-cards) for more information."
      },
      "created": {
        "type": "string",
        "example": "2015-10-18T14:26:16+00:00",
        "description": "The date and time the message was created."
      },
      "updated": {
        "type": "string",
        "example": "2015-10-18T14:27:16+00:00",
        "description": "The date and time that the message was last edited by the author. This field is only present when the message contents have changed."
      },
      "isVoiceClip": {
        "type": "boolean",
        "description": "`true` if the audio file is a voice clip recorded by the client; `false` if the audio file is a standard audio file not posted using the voice clip feature."
      }
    },
    "$$ref": "#/components/schemas/ListMessage"
  }
  ```
- **`400`** — Bad Request: The request was invalid or cannot be otherwise served. An accompanying error message will explain further.
- **`401`** — Unauthorized: Authentication credentials were missing or incorrect.
- **`403`** — Forbidden: The request is understood, but it has been refused or access is not allowed.
- **`404`** — Not Found: The URI requested is invalid or the resource requested, such as a user, does not exist. Also returned when the requested format is not supported by the requested method.
- **`405`** — Method Not Allowed: The request was made to a resource using an HTTP request method that is not supported.
- **`409`** — Conflict: The request could not be processed because it conflicts with some established rule of the system. For example, a person may not be added to a room more than once.
- **`410`** — Gone: The requested resource is no longer available.
- **`415`** — Unsupported Media Type: The request was made to a resource without specifying a media type or used a media type that is not supported.
- **`423`** — Locked: The requested resource is temporarily unavailable. A Retry-After header may be present that specifies how many seconds you need to wait before attempting the request again.
- **`428`** — Precondition Required: File(s) cannot be scanned for malware and need to be force downloaded.
- **`429`** — Too Many Requests: Too many requests have been sent in a given amount of time and the request has been rate limited. A Retry-After header should be present that specifies how many seconds you need to wait before a successful request can be made.
- **`500`** — Internal Server Error: Something went wrong on the server. If the issue persists, feel free to contact the [Webex Developer Support team](/explore/support).
- **`502`** — Bad Gateway: The server received an invalid response from an upstream server while processing the request. Try again later.
- **`503`** — Service Unavailable: Server is overloaded with requests. Try again later.
- **`504`** — Gateway Timeout: An upstream server failed to respond on time. If your query uses max parameter, please try to reduce it.

---

### 6.4 Messages: Get Message Details

**Endpoint:** `GET /messages/{messageId}`

Show details for a message, by message ID.

Specify the message ID in the `messageId` parameter in the URI.

#### Parameters

| Name | In | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| `messageId` | `path` | `string` | Yes | The unique identifier for the message. |

#### Responses

- **`200`** — OK
  ```json
  {
    "type": "object",
    "properties": {
      "id": {
        "type": "string",
        "example": "Y2lzY29zcGFyazovL3VzL01FU1NBR0UvOTJkYjNiZTAtNDNiZC0xMWU2LThhZTktZGQ1YjNkZmM1NjVk",
        "description": "The unique identifier for the message."
      },
      "parentId": {
        "type": "string",
        "example": "Y2lzY29zcGFyazovL3VzL01FU1NBR0UvOTJkYjNiZTAtNDNiZC0xMWU2LThhZTktZGQ1YjNkZmM1NjVk",
        "description": "The unique identifier for the parent message."
      },
      "roomId": {
        "type": "string",
        "example": "Y2lzY29zcGFyazovL3VzL1JPT00vYmJjZWIxYWQtNDNmMS0zYjU4LTkxNDctZjE0YmIwYzRkMTU0",
        "description": "The room ID of the message."
      },
      "roomType": {
        "type": "string",
        "enum": [
          "direct",
          "group"
        ],
        "description": "The type of room.\n * `direct` - 1:1 room\n * `group` - group room\n"
      },
      "text": {
        "type": "string",
        "example": "PROJECT UPDATE - A new project plan has been published on http://example.com/s/lf5vj. The PM for this project is Mike C. and the Engineering Manager is Jane W.",
        "description": "The message, in plain text. If `markdown` is specified this parameter may be *optionally* used to provide alternate text for UI clients that do not support rich text."
      },
      "markdown": {
        "type": "string",
        "example": "**PROJECT UPDATE** A new project plan has been published on <http://example.com/s/lf5vj>. The PM for this project is <@personEmail:mike@example.com> and the Engineering Manager is <@personEmail:jane@example.com>.",
        "description": "The message, in Markdown format."
      },
      "html": {
        "type": "string",
        "example": "<p><strong>PROJECT UPDATE</strong> A new project plan has been published <a href=\\\"http://example.com/s/lf5vj\\\" rel=\\\"nofollow\\\">here</a>. The PM for this project is mike@example.com and the Engineering Manager is jane@example.com.</p>",
        "description": "The text content of the message, in HTML format. This read-only property is used by the Webex clients."
      },
      "files": {
        "type": "array",
        "items": {
          "type": "string",
          "example": "http://www.example.com/images/media.png"
        },
        "description": "Public URLs for files attached to the message. For the supported media types and the behavior of file uploads, see [Message Attachments](/docs/basics#message-attachments)."
      },
      "personId": {
        "type": "string",
        "example": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS9mNWIzNjE4Ny1jOGRkLTQ3MjctOGIyZi1mOWM0NDdmMjkwNDY",
        "description": "The person ID of the message author."
      },
      "personEmail": {
        "type": "string",
        "example": "matt@example.com",
        "description": "The email address of the message author."
      },
      "mentionedPeople": {
        "type": "array",
        "items": {
          "type": "string",
          "example": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS8yNDlmNzRkOS1kYjhhLTQzY2EtODk2Yi04NzllZDI0MGFjNTM,Y2lzY29zcGFyazovL3VzL1BFT1BMRS83YWYyZjcyYy0xZDk1LTQxZjAtYTcxNi00MjlmZmNmYmM0ZDg"
        },
        "description": "People IDs for anyone mentioned in the message."
      },
      "mentionedGroups": {
        "type": "array",
        "items": {
          "type": "string",
          "example": "all"
        },
        "description": "Group names for the groups mentioned in the message."
      },
      "attachments": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "contentType": {
              "type": "string",
              "example": "application/vnd.microsoft.card.adaptive",
              "description": "The content type of the attachment."
            },
            "content": {
              "type": "object",
              "required": [
                "type",
                "version"
              ],
              "properties": {
                "type": {
                  "type": "string",
                  "example": "AdaptiveCard",
                  "description": "Must be `AdaptiveCard`."
                },
                "version": {
                  "type": "string",
                  "example": "1.0",
                  "description": "Adaptive Card schema version."
                },
                "body": {
                  "type": "array",
                  "items": {
                    "type": "object",
                    "properties": {
                      "type": {
                        "type": "string",
                        "example": "TextBlock"
                      },
                      "text": {
                        "type": "string",
                        "example": "Adaptive Cards"
                      },
                      "size": {
                        "type": "string",
                        "example": "large"
                      }
                    }
                  },
                  "description": "The card's elements."
                },
                "actions": {
                  "type": "array",
                  "items": {
                    "type": "object",
                    "properties": {
                      "type": {
                        "type": "string",
                        "example": "Action.OpenUrl"
                      },
                      "url": {
                        "type": "string",
                        "example": "http://adaptivecards.io"
                      },
                      "title": {
                        "type": "string",
                        "example": "Learn More"
                      }
                    }
                  },
                  "description": "The card's actions."
                }
              },
              "$$ref": "#/components/schemas/AdaptiveCard"
            }
          },
          "$$ref": "#/components/schemas/Attachment"
        },
        "description": "Message content attachments attached to the message. See the [Cards Guide](/docs/buttons-and-cards) for more information."
      },
      "created": {
        "type": "string",
        "example": "2015-10-18T14:26:16+00:00",
        "description": "The date and time the message was created."
      },
      "updated": {
        "type": "string",
        "example": "2015-10-18T14:27:16+00:00",
        "description": "The date and time that the message was last edited by the author. This field is only present when the message contents have changed."
      },
      "isVoiceClip": {
        "type": "boolean",
        "description": "`true` if the audio file is a voice clip recorded by the client; `false` if the audio file is a standard audio file not posted using the voice clip feature."
      }
    },
    "$$ref": "#/components/schemas/ListMessage"
  }
  ```
- **`400`** — Bad Request: The request was invalid or cannot be otherwise served. An accompanying error message will explain further.
- **`401`** — Unauthorized: Authentication credentials were missing or incorrect.
- **`403`** — Forbidden: The request is understood, but it has been refused or access is not allowed.
- **`404`** — Not Found: The URI requested is invalid or the resource requested, such as a user, does not exist. Also returned when the requested format is not supported by the requested method.
- **`405`** — Method Not Allowed: The request was made to a resource using an HTTP request method that is not supported.
- **`409`** — Conflict: The request could not be processed because it conflicts with some established rule of the system. For example, a person may not be added to a room more than once.
- **`410`** — Gone: The requested resource is no longer available.
- **`415`** — Unsupported Media Type: The request was made to a resource without specifying a media type or used a media type that is not supported.
- **`423`** — Locked: The requested resource is temporarily unavailable. A Retry-After header may be present that specifies how many seconds you need to wait before attempting the request again.
- **`428`** — Precondition Required: File(s) cannot be scanned for malware and need to be force downloaded.
- **`429`** — Too Many Requests: Too many requests have been sent in a given amount of time and the request has been rate limited. A Retry-After header should be present that specifies how many seconds you need to wait before a successful request can be made.
- **`500`** — Internal Server Error: Something went wrong on the server. If the issue persists, feel free to contact the [Webex Developer Support team](/explore/support).
- **`502`** — Bad Gateway: The server received an invalid response from an upstream server while processing the request. Try again later.
- **`503`** — Service Unavailable: Server is overloaded with requests. Try again later.
- **`504`** — Gateway Timeout: An upstream server failed to respond on time. If your query uses max parameter, please try to reduce it.

---

### 6.5 Messages: List Direct Messages

**Endpoint:** `GET /messages/direct`

List all messages in a 1:1 (direct) room. Use the `personId` or `personEmail` query parameter to specify the room. Each message will include content attachments if present.

The list sorts the messages in descending order by creation date.

#### Parameters

| Name | In | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| `parentId` | `query` | `string` | No | List messages with a parent, by ID. |
| `personId` | `query` | `string` | No | List messages in a 1:1 room, by person ID. |
| `personEmail` | `query` | `string` | No | List messages in a 1:1 room, by person email. |

#### Responses

- **`200`** — OK
  ```json
  {
    "type": "object",
    "properties": {
      "items": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "id": {
              "type": "string",
              "example": "Y2lzY29zcGFyazovL3VzL01FU1NBR0UvOTJkYjNiZTAtNDNiZC0xMWU2LThhZTktZGQ1YjNkZmM1NjVk",
              "description": "The unique identifier for the message."
            },
            "parentId": {
              "type": "string",
              "example": "Y2lzY29zcGFyazovL3VzL01FU1NBR0UvOTJkYjNiZTAtNDNiZC0xMWU2LThhZTktZGQ1YjNkZmM1NjVk",
              "description": "The unique identifier for the parent message."
            },
            "roomId": {
              "type": "string",
              "example": "Y2lzY29zcGFyazovL3VzL1JPT00vODQxZjY5MjAtNDdlZC00NmE0LWI2YmItZTVjM2M1YTc3Yzgy",
              "description": "The room ID of the message."
            },
            "roomType": {
              "type": "string",
              "example": "direct",
              "description": "The type of room. Will always be `direct`."
            },
            "text": {
              "type": "string",
              "example": "Hey there, what do you think of this project update presentation (http://sharepoint.example.com/presentation.pptx)?",
              "description": "The message, in plain text. If `markdown` is specified this parameter may be *optionally* used to provide alternate text for UI clients that do not support rich text."
            },
            "markdown": {
              "type": "string",
              "example": "Hey there, what do you think of [this project update presentation](http://sharepoint.example.com/presentation.pptx)?",
              "description": "The message, in Markdown format."
            },
            "html": {
              "type": "string",
              "example": "<p>Hey there, what do you think of <a href=\\\"http://sharepoint.example.com/presentation.pptx\\\" rel=\\\"nofollow\\\">this project update presentation</a>?</p>",
              "description": "The text content of the message, in HTML format. This read-only property is used by the Webex clients."
            },
            "files": {
              "type": "array",
              "items": {
                "type": "string",
                "example": "http://www.example.com/images/media.png"
              },
              "description": "Public URLs for files attached to the message. For the supported media types and the behavior of file uploads, see [Message Attachments](/docs/api/basics#message-attachments)."
            },
            "personId": {
              "type": "string",
              "example": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS9mNWIzNjE4Ny1jOGRkLTQ3MjctOGIyZi1mOWM0NDdmMjkwNDY",
              "description": "The person ID of the message author."
            },
            "personEmail": {
              "type": "string",
              "example": "matt@example.com",
              "description": "The email address of the message author."
            },
            "attachments": {
              "type": "array",
              "items": {
                "type": "object",
                "properties": {
                  "contentType": {
                    "type": "string",
                    "example": "application/vnd.microsoft.card.adaptive",
                    "description": "The content type of the attachment."
                  },
                  "content": {
                    "type": "object",
                    "required": [
                      "type",
                      "version"
                    ],
                    "properties": {
                      "type": {
                        "type": "string",
                        "example": "AdaptiveCard",
                        "description": "Must be `AdaptiveCard`."
                      },
                      "version": {
                        "type": "string",
                        "example": "1.0",
                        "description": "Adaptive Card schema version."
                      },
                      "body": {
                        "type": "array",
                        "items": {
                          "type": "object",
                          "properties": {
                            "type": {
                              "type": "string",
                              "example": "TextBlock"
                            },
                            "text": {
                              "type": "string",
                              "example": "Adaptive Cards"
                            },
                            "size": {
                              "type": "string",
                              "example": "large"
                            }
                          }
                        },
                        "description": "The card's elements."
                      },
                      "actions": {
                        "type": "array",
                        "items": {
                          "type": "object",
                          "properties": {
                            "type": {
                              "type": "string",
                              "example": "Action.OpenUrl"
                            },
                            "url": {
                              "type": "string",
                              "example": "http://adaptivecards.io"
                            },
                            "title": {
                              "type": "string",
                              "example": "Learn More"
                            }
                          }
                        },
                        "description": "The card's actions."
                      }
                    },
                    "$$ref": "#/components/schemas/AdaptiveCard"
                  }
                },
                "$$ref": "#/components/schemas/Attachment"
              },
              "description": "Message content attachments attached to the message. See the [Cards Guide](/docs/buttons-and-cards) for more information."
            },
            "created": {
              "type": "string",
              "example": "2015-10-18T14:26:16+00:00",
              "description": "The date and time the message was created."
            },
            "updated": {
              "type": "string",
              "example": "2015-10-18T14:27:16+00:00",
              "description": "The date and time that the message was last edited by the author. This field is only present when the message contents have changed."
            },
            "isVoiceClip": {
              "type": "boolean",
              "description": "True if the audio file is a voice clip recorded by the client; false if the audio file is a standard audio file not posted using the voice clip feature."
            }
          },
          "$$ref": "#/components/schemas/DirectMessage"
        }
      }
    },
    "$$ref": "#/components/schemas/DirectMessageCollectionResponse"
  }
  ```
- **`400`** — Bad Request: The request was invalid or cannot be otherwise served. An accompanying error message will explain further.
- **`401`** — Unauthorized: Authentication credentials were missing or incorrect.
- **`403`** — Forbidden: The request is understood, but it has been refused or access is not allowed.
- **`404`** — Not Found: The URI requested is invalid or the resource requested, such as a user, does not exist. Also returned when the requested format is not supported by the requested method.
- **`405`** — Method Not Allowed: The request was made to a resource using an HTTP request method that is not supported.
- **`409`** — Conflict: The request could not be processed because it conflicts with some established rule of the system. For example, a person may not be added to a room more than once.
- **`410`** — Gone: The requested resource is no longer available.
- **`415`** — Unsupported Media Type: The request was made to a resource without specifying a media type or used a media type that is not supported.
- **`423`** — Locked: The requested resource is temporarily unavailable. A Retry-After header may be present that specifies how many seconds you need to wait before attempting the request again.
- **`428`** — Precondition Required: File(s) cannot be scanned for malware and need to be force downloaded.
- **`429`** — Too Many Requests: Too many requests have been sent in a given amount of time and the request has been rate limited. A Retry-After header should be present that specifies how many seconds you need to wait before a successful request can be made.
- **`500`** — Internal Server Error: Something went wrong on the server. If the issue persists, feel free to contact the [Webex Developer Support team](/explore/support).
- **`502`** — Bad Gateway: The server received an invalid response from an upstream server while processing the request. Try again later.
- **`503`** — Service Unavailable: Server is overloaded with requests. Try again later.
- **`504`** — Gateway Timeout: An upstream server failed to respond on time. If your query uses max parameter, please try to reduce it.

---

### 6.6 Messages: List Messages

**Endpoint:** `GET /messages`

Lists all messages in a room.  Each message will include content attachments if present.

The list sorts the messages in descending order by creation date.

Long result sets will be split into [pages](/docs/basics#pagination).

#### Parameters

| Name | In | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| `roomId` | `query` | `string` | Yes | List messages in a room, by ID. |
| `parentId` | `query` | `string` | No | List messages with a parent, by ID. |
| `mentionedPeople` | `query` | `array` | No | List messages with these people mentioned, by ID. Use `me` as a shorthand for the current API user. Only `me` or the person ID of the current user may be specified. Bots must include this parameter to list messages in group rooms (spaces). |
| `before` | `query` | `string` | No | List messages sent before a date and time. |
| `beforeMessage` | `query` | `string` | No | List messages sent before a message, by ID. |
| `max` | `query` | `number` | No | Limit the maximum number of messages in the response. Cannot exceed 100 if used with `mentionedPeople`. |

#### Responses

- **`200`** — OK
  ```json
  {
    "type": "object",
    "properties": {
      "items": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "id": {
              "type": "string",
              "example": "Y2lzY29zcGFyazovL3VzL01FU1NBR0UvOTJkYjNiZTAtNDNiZC0xMWU2LThhZTktZGQ1YjNkZmM1NjVk",
              "description": "The unique identifier for the message."
            },
            "parentId": {
              "type": "string",
              "example": "Y2lzY29zcGFyazovL3VzL01FU1NBR0UvOTJkYjNiZTAtNDNiZC0xMWU2LThhZTktZGQ1YjNkZmM1NjVk",
              "description": "The unique identifier for the parent message."
            },
            "roomId": {
              "type": "string",
              "example": "Y2lzY29zcGFyazovL3VzL1JPT00vYmJjZWIxYWQtNDNmMS0zYjU4LTkxNDctZjE0YmIwYzRkMTU0",
              "description": "The room ID of the message."
            },
            "roomType": {
              "type": "string",
              "enum": [
                "direct",
                "group"
              ],
              "description": "The type of room.\n * `direct` - 1:1 room\n * `group` - group room\n"
            },
            "text": {
              "type": "string",
              "example": "PROJECT UPDATE - A new project plan has been published on http://example.com/s/lf5vj. The PM for this project is Mike C. and the Engineering Manager is Jane W.",
              "description": "The message, in plain text. If `markdown` is specified this parameter may be *optionally* used to provide alternate text for UI clients that do not support rich text."
            },
            "markdown": {
              "type": "string",
              "example": "**PROJECT UPDATE** A new project plan has been published on <http://example.com/s/lf5vj>. The PM for this project is <@personEmail:mike@example.com> and the Engineering Manager is <@personEmail:jane@example.com>.",
              "description": "The message, in Markdown format."
            },
            "html": {
              "type": "string",
              "example": "<p><strong>PROJECT UPDATE</strong> A new project plan has been published <a href=\\\"http://example.com/s/lf5vj\\\" rel=\\\"nofollow\\\">here</a>. The PM for this project is mike@example.com and the Engineering Manager is jane@example.com.</p>",
              "description": "The text content of the message, in HTML format. This read-only property is used by the Webex clients."
            },
            "files": {
              "type": "array",
              "items": {
                "type": "string",
                "example": "http://www.example.com/images/media.png"
              },
              "description": "Public URLs for files attached to the message. For the supported media types and the behavior of file uploads, see [Message Attachments](/docs/basics#message-attachments)."
            },
            "personId": {
              "type": "string",
              "example": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS9mNWIzNjE4Ny1jOGRkLTQ3MjctOGIyZi1mOWM0NDdmMjkwNDY",
              "description": "The person ID of the message author."
            },
            "personEmail": {
              "type": "string",
              "example": "matt@example.com",
              "description": "The email address of the message author."
            },
            "mentionedPeople": {
              "type": "array",
              "items": {
                "type": "string",
                "example": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS8yNDlmNzRkOS1kYjhhLTQzY2EtODk2Yi04NzllZDI0MGFjNTM,Y2lzY29zcGFyazovL3VzL1BFT1BMRS83YWYyZjcyYy0xZDk1LTQxZjAtYTcxNi00MjlmZmNmYmM0ZDg"
              },
              "description": "People IDs for anyone mentioned in the message."
            },
            "mentionedGroups": {
              "type": "array",
              "items": {
                "type": "string",
                "example": "all"
              },
              "description": "Group names for the groups mentioned in the message."
            },
            "attachments": {
              "type": "array",
              "items": {
                "type": "object",
                "properties": {
                  "contentType": {
                    "type": "string",
                    "example": "application/vnd.microsoft.card.adaptive",
                    "description": "The content type of the attachment."
                  },
                  "content": {
                    "type": "object",
                    "required": [
                      "type",
                      "version"
                    ],
                    "properties": {
                      "type": {
                        "type": "string",
                        "example": "AdaptiveCard",
                        "description": "Must be `AdaptiveCard`."
                      },
                      "version": {
                        "type": "string",
                        "example": "1.0",
                        "description": "Adaptive Card schema version."
                      },
                      "body": {
                        "type": "array",
                        "items": {
                          "type": "object",
                          "properties": {
                            "type": {
                              "type": "string",
                              "example": "TextBlock"
                            },
                            "text": {
                              "type": "string",
                              "example": "Adaptive Cards"
                            },
                            "size": {
                              "type": "string",
                              "example": "large"
                            }
                          }
                        },
                        "description": "The card's elements."
                      },
                      "actions": {
                        "type": "array",
                        "items": {
                          "type": "object",
                          "properties": {
                            "type": {
                              "type": "string",
                              "example": "Action.OpenUrl"
                            },
                            "url": {
                              "type": "string",
                              "example": "http://adaptivecards.io"
                            },
                            "title": {
                              "type": "string",
                              "example": "Learn More"
                            }
                          }
                        },
                        "description": "The card's actions."
                      }
                    },
                    "$$ref": "#/components/schemas/AdaptiveCard"
                  }
                },
                "$$ref": "#/components/schemas/Attachment"
              },
              "description": "Message content attachments attached to the message. See the [Cards Guide](/docs/buttons-and-cards) for more information."
            },
            "created": {
              "type": "string",
              "example": "2015-10-18T14:26:16+00:00",
              "description": "The date and time the message was created."
            },
            "updated": {
              "type": "string",
              "example": "2015-10-18T14:27:16+00:00",
              "description": "The date and time that the message was last edited by the author. This field is only present when the message contents have changed."
            },
            "isVoiceClip": {
              "type": "boolean",
              "description": "`true` if the audio file is a voice clip recorded by the client; `false` if the audio file is a standard audio file not posted using the voice clip feature."
            }
          },
          "$$ref": "#/components/schemas/ListMessage"
        }
      }
    },
    "$$ref": "#/components/schemas/ListMessageCollectionResponse"
  }
  ```
- **`400`** — Bad Request: The request was invalid or cannot be otherwise served. An accompanying error message will explain further.
- **`401`** — Unauthorized: Authentication credentials were missing or incorrect.
- **`403`** — Forbidden: The request is understood, but it has been refused or access is not allowed.
- **`404`** — Not Found: The URI requested is invalid or the resource requested, such as a user, does not exist. Also returned when the requested format is not supported by the requested method.
- **`405`** — Method Not Allowed: The request was made to a resource using an HTTP request method that is not supported.
- **`409`** — Conflict: The request could not be processed because it conflicts with some established rule of the system. For example, a person may not be added to a room more than once.
- **`410`** — Gone: The requested resource is no longer available.
- **`415`** — Unsupported Media Type: The request was made to a resource without specifying a media type or used a media type that is not supported.
- **`423`** — Locked: The requested resource is temporarily unavailable. A Retry-After header may be present that specifies how many seconds you need to wait before attempting the request again.
- **`428`** — Precondition Required: File(s) cannot be scanned for malware and need to be force downloaded.
- **`429`** — Too Many Requests: Too many requests have been sent in a given amount of time and the request has been rate limited. A Retry-After header should be present that specifies how many seconds you need to wait before a successful request can be made.
- **`500`** — Internal Server Error: Something went wrong on the server. If the issue persists, feel free to contact the [Webex Developer Support team](/explore/support).
- **`502`** — Bad Gateway: The server received an invalid response from an upstream server while processing the request. Try again later.
- **`503`** — Service Unavailable: Server is overloaded with requests. Try again later.
- **`504`** — Gateway Timeout: An upstream server failed to respond on time. If your query uses max parameter, please try to reduce it.

---

## 7. People

### 7.1 People: Create a Person

**Endpoint:** `POST /people`

Create a new user account for a given organization. Only an admin can create a new user account.

At least one of the following body parameters is required to create a new user: `displayName`, `firstName`, `lastName`.

Currently, users may have only one email address associated with their account. The `emails` parameter is an array, which accepts multiple values to allow for future expansion, but currently only one email address will be used for the new user.

Admin users can include `Webex calling` (BroadCloud) user details in the response by specifying `callingData` parameter as true. It may happen that the POST request with calling data returns a 400 status, but the person was created still. One way to get into this state is if an invalid phone number is assigned to a user. The people API aggregates calls to several other microservices, and one may have failed. A best practice is to check if the user exists before retrying. This can be done with the user's email address and a GET /people.

When doing attendee management, append `#attendee` to the `siteUrl` parameter (e.g. `mysite.webex.com#attendee`) to make the new user an attendee for a site.

**NOTES**:

* For creating a `Webex Calling` user, you must provide `phoneNumbers` or `extension`, `locationId`, and `licenses` string in the same request.

* `SipAddresses` are asigned via an asynchronous process. This means that the POST response may not show the SIPAddresses immediately. Instead you can verify them with a separate GET to /people, after they were newly configured.

* When assigning multiple licenses in a single request, the system will assign all valid and available licenses. If any requested licenses cannot be assigned, the operation will continue with the remaining licenses. As a result, it is possible that not all requested licenses are assigned to the user.

#### Parameters

| Name | In | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| `callingData` | `query` | `boolean` | No | Include Webex Calling user details in the response. |
| `minResponse` | `query` | `boolean` | No | Set to `true` to improve performance by omitting person details and returning only the ID in the response when successful. If unsuccessful the response will have optional error details. |

#### Request Body Schema

```json
{
  "type": "object",
  "required": [
    "emails"
  ],
  "properties": {
    "emails": {
      "type": "array",
      "items": {
        "type": "string",
        "example": "john.andersen@example.com"
      },
      "description": "The email addresses of the person. Only one email address is allowed per person."
    },
    "phoneNumbers": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "type": {
            "type": "string",
            "enum": [
              "work"
            ],
            "description": "The type of phone number. Valid values are 'work'"
          },
          "value": {
            "type": "string",
            "example": "408 526 7209",
            "description": "The phone number."
          }
        }
      },
      "description": "Phone numbers for the person. Only settable for Webex Calling. Requires a Webex Calling license."
    },
    "extension": {
      "type": "string",
      "example": "133",
      "description": "Webex Calling extension of the person. This is only settable for a person with a Webex Calling license."
    },
    "locationId": {
      "type": "string",
      "example": "Y2lzY29zcGFyazovL3VzL0xPQ0FUSU9OLzYzNzE1",
      "description": "The ID of the location for this person."
    },
    "displayName": {
      "type": "string",
      "example": "John Andersen",
      "description": "The full name of the person."
    },
    "firstName": {
      "type": "string",
      "example": "John",
      "description": "The first name of the person."
    },
    "lastName": {
      "type": "string",
      "example": "Andersen",
      "description": "The last name of the person."
    },
    "avatar": {
      "type": "string",
      "example": "https://1efa7a94ed21783e352-c62266528714497a17239ececf39e9e2.ssl.cf1.rackcdn.com/V1~54c844c89e678e5a7b16a306bc2897b9~wx29yGtlTpilEFlYzqPKag==~1600",
      "description": "The URL to the person's avatar in PNG format."
    },
    "orgId": {
      "type": "string",
      "example": "Y2lzY29zcGFyazovL3VzL09SR0FOSVpBVElPTi85NmFiYzJhYS0zZGNjLTExZTUtYTE1Mi1mZTM0ODE5Y2RjOWE",
      "description": "The ID of the organization to which this person belongs."
    },
    "roles": {
      "type": "array",
      "items": {
        "type": "string",
        "example": "Y2lzY29zcGFyazovL3VzL1JPTEUvOTZhYmMyYWEtM2RjYy0xMWU1LWExNTItZmUzNDgxOWNkYzlh,Y2lzY29zcGFyazovL3VzL1JPTEUvOTZhYmMyYWEtM2RjYy0xMWU1LWIyNjMtMGY0NTkyYWRlZmFi"
      },
      "description": "An array of role strings representing the roles to which this admin user belongs."
    },
    "licenses": {
      "type": "array",
      "items": {
        "type": "string",
        "example": "Y2lzY29zcGFyazovL3VzL0xJQ0VOU0UvOTZhYmMyYWEtM2RjYy0xMWU1LWExNTItZmUzNDgxOWNkYzlh,Y2lzY29zcGFyazovL3VzL0xJQ0VOU0UvOTZhYmMyYWEtM2RjYy0xMWU1LWIyNjMtMGY0NTkyYWRlZmFi"
      },
      "description": "An array of license strings allocated to this person."
    },
    "department": {
      "type": "string",
      "example": "Sales",
      "description": "The business department the user belongs to."
    },
    "manager": {
      "type": "string",
      "example": "John Duarte",
      "description": "A manager identifier."
    },
    "managerId": {
      "type": "string",
      "example": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS80ZGEzYTI0OC05YjBhLTQxMDgtODU0NC1iNTQwMzEyZTU2M2E",
      "description": "Person ID of the manager."
    },
    "title": {
      "type": "string",
      "example": "GM",
      "description": "The person's title."
    },
    "addresses": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "type": {
            "type": "string",
            "example": "work",
            "description": "The type of address."
          },
          "country": {
            "type": "string",
            "example": "US",
            "description": "The user's country."
          },
          "locality": {
            "type": "string",
            "example": "Milpitas",
            "description": "The user's locality, often city."
          },
          "region": {
            "type": "string",
            "example": "California",
            "description": "The user's region, often state."
          },
          "streetAddress": {
            "type": "string",
            "example": "1099 Bird Ave.",
            "description": "The user's street."
          },
          "postalCode": {
            "type": "string",
            "example": "99212",
            "description": "The user's postal or zip code."
          }
        }
      },
      "description": "A person's addresses."
    },
    "siteUrls": {
      "type": "array",
      "items": {
        "type": "string",
        "example": "mysite.webex.com#attendee"
      },
      "description": "One or several site names where this user has an attendee role. Append `#attendee` to the sitename (e.g.: `mysite.webex.com#attendee`)."
    }
  }
}
```

#### Responses

- **`200`** — OK
  ```json
  {
    "type": "object",
    "properties": {
      "id": {
        "type": "string",
        "example": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS9mNWIzNjE4Ny1jOGRkLTQ3MjctOGIyZi1mOWM0NDdmMjkwNDY",
        "description": "A unique identifier for the person."
      },
      "emails": {
        "type": "array",
        "items": {
          "type": "string",
          "example": "john.andersen@example.com"
        },
        "description": "The email addresses of the person."
      },
      "phoneNumbers": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "type": {
              "type": "string",
              "enum": [
                "work",
                "work_extension",
                "mobile",
                "fax"
              ],
              "description": "The type of phone number.\n * `work` - Work phone number of the person.\n * `work_extension` - Work extension of the person. For the Webex Calling person, the value will have a routing prefix along with the extension.\n * `mobile` - Mobile number of the person.\n * `fax` - FAX number of the person.\n"
            },
            "value": {
              "type": "string",
              "example": "+1 408 526 7209",
              "description": "The phone number."
            },
            "primary": {
              "type": "boolean",
              "example": true,
              "description": "Primary number for the person."
            }
          }
        },
        "description": "Phone numbers for the person."
      },
      "extension": {
        "type": "string",
        "example": "133",
        "description": "The Webex Calling extension for the person. Only applies to a person with a Webex Calling license."
      },
      "locationId": {
        "type": "string",
        "example": "Y2lzY29zcGFyazovL3VzL0xPQ0FUSU9OLzYzNzE1",
        "description": "The ID of the location for this person retrieved from BroadCloud."
      },
      "displayName": {
        "type": "string",
        "example": "John Andersen",
        "description": "The full name of the person."
      },
      "nickName": {
        "type": "string",
        "example": "John",
        "description": "The nickname of the person if configured. If no nickname is configured for the person, this field will not be present."
      },
      "firstName": {
        "type": "string",
        "example": "John",
        "description": "The first name of the person."
      },
      "lastName": {
        "type": "string",
        "example": "Andersen",
        "description": "The last name of the person."
      },
      "avatar": {
        "type": "string",
        "example": "https://1efa7a94ed21783e352-c62266528714497a17239ececf39e9e2.ssl.cf1.rackcdn.com/V1~54c844c89e678e5a7b16a306bc2897b9~wx29yGtlTpilEFlYzqPKag==~1600",
        "description": "The URL to the person's avatar in PNG format."
      },
      "orgId": {
        "type": "string",
        "example": "Y2lzY29zcGFyazovL3VzL09SR0FOSVpBVElPTi85NmFiYzJhYS0zZGNjLTExZTUtYTE1Mi1mZTM0ODE5Y2RjOWE",
        "description": "The ID of the organization to which this person belongs."
      },
      "roles": {
        "type": "array",
        "items": {
          "type": "string",
          "example": "Y2lzY29zcGFyazovL3VzL1JPTEUvOTZhYmMyYWEtM2RjYy0xMWU1LWExNTItZmUzNDgxOWNkYzlh,Y2lzY29zcGFyazovL3VzL1JPTEUvOTZhYmMyYWEtM2RjYy0xMWU1LWIyNjMtMGY0NTkyYWRlZmFi"
        },
        "description": "An array of role strings representing the roles to which this admin user belongs."
      },
      "licenses": {
        "type": "array",
        "items": {
          "type": "string",
          "example": "Y2lzY29zcGFyazovL3VzL0xJQ0VOU0UvOTZhYmMyYWEtM2RjYy0xMWU1LWExNTItZmUzNDgxOWNkYzlh,Y2lzY29zcGFyazovL3VzL0xJQ0VOU0UvOTZhYmMyYWEtM2RjYy0xMWU1LWIyNjMtMGY0NTkyYWRlZmFi"
        },
        "description": "An array of license strings allocated to this person."
      },
      "department": {
        "type": "string",
        "example": "Sales",
        "description": "The business department the user belongs to."
      },
      "manager": {
        "type": "string",
        "example": "John Duarte",
        "description": "A manager identifier."
      },
      "managerId": {
        "type": "string",
        "example": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS80ZGEzYTI0OC05YjBhLTQxMDgtODU0NC1iNTQwMzEyZTU2M2E",
        "description": "Person ID of the manager."
      },
      "title": {
        "type": "string",
        "example": "GM",
        "description": "The person's title."
      },
      "addresses": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "type": {
              "type": "string",
              "example": "work",
              "description": "The type of address."
            },
            "country": {
              "type": "string",
              "example": "US",
              "description": "The user's country."
            },
            "locality": {
              "type": "string",
              "example": "Milpitas",
              "description": "The user's locality, often city."
            },
            "region": {
              "type": "string",
              "example": "California",
              "description": "The user's region, often state."
            },
            "streetAddress": {
              "type": "string",
              "example": "1099 Bird Ave.",
              "description": "The user's street."
            },
            "postalCode": {
              "type": "string",
              "example": "99212",
              "description": "The user's postal or zip code."
            }
          }
        },
        "description": "A person's addresses."
      },
      "created": {
        "type": "string",
        "example": "2015-10-18T14:26:16.000Z",
        "description": "The date and time the person was created."
      },
      "lastModified": {
        "type": "string",
        "example": "2015-10-18T14:26:16.000Z",
        "description": "The date and time the person was last changed."
      },
      "timezone": {
        "type": "string",
        "example": "America/Denver",
        "description": "The time zone of the person if configured. If no timezone is configured on the account, this field will not be present."
      },
      "lastActivity": {
        "type": "string",
        "example": "2015-10-18T14:26:16.028Z",
        "description": "The date and time of the person's last activity within Webex. This will only be returned for people within your organization or an organization you manage. Presence information will not be shown if the authenticated user has [disabled status sharing](https://help.webex.com/nkzs6wl/)."
      },
      "siteUrls": {
        "type": "array",
        "items": {
          "type": "string",
          "example": "mysite.webex.com#attendee"
        },
        "description": "One or several site names where this user has a role (host or attendee)."
      },
      "sipAddresses": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "type": {
              "type": "string",
              "enum": [
                "personal-room",
                "enterprise",
                "cloud-calling"
              ],
              "description": "The type of SIP address.\n * `personal-room` - Personal room address.\n * `enterprise` - Enterprise address.\n * `cloud-calling` - Cloud calling address.\n"
            },
            "value": {
              "type": "string",
              "example": "testuser5@mycompany.webex.com",
              "description": "The SIP address."
            },
            "primary": {
              "type": "boolean",
              "description": "Primary SIP address of the person."
            }
          }
        },
        "description": "The user's SIP addresses. Read-only."
      },
      "xmppFederationJid": {
        "type": "string",
        "example": "user@example.com",
        "description": "Identifier for intra-domain federation with other XMPP based messenger systems."
      },
      "status": {
        "type": "string",
        "enum": [
          "active",
          "call",
          "DoNotDisturb",
          "inactive",
          "meeting",
          "OutOfOffice",
          "pending",
          "presenting",
          "unknown"
        ],
        "description": "The current presence status of the person. This will only be returned for people within your organization or an organization you manage. Presence information will not be shown if the authenticated user has [disabled status sharing](https://help.webex.com/nkzs6wl/). Presence status is different from Control Hub's \"Last Service Access Time\" which indicates the last time an oAuth token was issued for this user.\n * `active` - Active within the last 10 minutes.\n * `call` - The user is in a call.\n * `DoNotDisturb` - The user has manually set their status to \"Do Not Disturb\".\n * `inactive` - Last activity occurred more than 10 minutes ago.\n * `meeting` - The user is in a meeting.\n * `OutOfOffice` - The user or a Hybrid Calendar service has indicated that they are \"Out of Office\".\n * `pending` - The user has never logged in; a status cannot be determined.\n * `presenting` - The user is sharing content.\n * `unknown` - The user\u2019s status could not be determined.\n"
      },
      "invitePending": {
        "type": "string",
        "enum": [
          "true",
          "false"
        ],
        "description": "Whether or not an invite is pending for the user to complete account activation. This property is only returned if the authenticated user is an admin user for the person's organization.\n * `true` - The person has been invited to Webex but has not created an account.\n * `false` - An invite is not pending for this person.\n"
      },
      "loginEnabled": {
        "type": "string",
        "enum": [
          "true",
          "false"
        ],
        "description": "Whether or not the user is allowed to use Webex. This property is only returned if the authenticated user is an admin user for the person's organization.\n * `true` - The person _can_ log into Webex.\n * `false` - The person _cannot_ log into Webex.\n"
      },
      "type": {
        "type": "string",
        "enum": [
          "person",
          "bot",
          "appuser"
        ],
        "description": "The type of person account, such as person or bot.\n * `person` - Account belongs to a person.\n * `bot` - Account is a bot user.\n * `appuser` - Account is a [guest user](/docs/guest-issuer).\n"
      }
    },
    "$$ref": "#/components/schemas/Person"
  }
  ```
- **`400`** — Bad Request: The request was invalid or cannot be otherwise served. An accompanying error message will explain further.
- **`401`** — Unauthorized: Authentication credentials were missing or incorrect.
- **`403`** — Forbidden: The request is understood, but it has been refused or access is not allowed.
- **`404`** — Not Found: The URI requested is invalid or the resource requested, such as a user, does not exist. Also returned when the requested format is not supported by the requested method.
- **`405`** — Method Not Allowed: The request was made to a resource using an HTTP request method that is not supported.
- **`409`** — Conflict: The request could not be processed because it conflicts with some established rule of the system. For example, a person may not be added to a room more than once.
- **`410`** — Gone: The requested resource is no longer available.
- **`415`** — Unsupported Media Type: The request was made to a resource without specifying a media type or used a media type that is not supported.
- **`423`** — Locked: The requested resource is temporarily unavailable. A Retry-After header may be present that specifies how many seconds you need to wait before attempting the request again.
- **`428`** — Precondition Required: File(s) cannot be scanned for malware and need to be force downloaded.
- **`429`** — Too Many Requests: Too many requests have been sent in a given amount of time and the request has been rate limited. A Retry-After header should be present that specifies how many seconds you need to wait before a successful request can be made.
- **`500`** — Internal Server Error: Something went wrong on the server. If the issue persists, feel free to contact the [Webex Developer Support team](/explore/support).
- **`502`** — Bad Gateway: The server received an invalid response from an upstream server while processing the request. Try again later.
- **`503`** — Service Unavailable: Server is overloaded with requests. Try again later.
- **`504`** — Gateway Timeout: An upstream server failed to respond on time. If your query uses max parameter, please try to reduce it.

---

### 7.2 People: Delete a Person

**Endpoint:** `DELETE /people/{personId}`

Remove a person from the system.

**Required Administrator Roles:**

The following administrators have permission to use this API:

**Customer Organization:**
- Full administrator
- User administrator

**Partner/External Access:**
- External full administrator

**Note:** External read-only administrators, provisioning administrators, and device administrators cannot delete users.

Specify the person ID in the `personId` parameter in the URI.

#### Parameters

| Name | In | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| `personId` | `path` | `string` | Yes | A unique identifier for the person. |

#### Responses

- **`204`** — No Content
- **`400`** — Bad Request: The request was invalid or cannot be otherwise served. An accompanying error message will explain further.
- **`401`** — Unauthorized: Authentication credentials were missing or incorrect.
- **`403`** — Forbidden: The request is understood, but it has been refused or access is not allowed.
- **`404`** — Not Found: The URI requested is invalid or the resource requested, such as a user, does not exist. Also returned when the requested format is not supported by the requested method.
- **`405`** — Method Not Allowed: The request was made to a resource using an HTTP request method that is not supported.
- **`409`** — Conflict: The request could not be processed because it conflicts with some established rule of the system. For example, a person may not be added to a room more than once.
- **`410`** — Gone: The requested resource is no longer available.
- **`415`** — Unsupported Media Type: The request was made to a resource without specifying a media type or used a media type that is not supported.
- **`423`** — Locked: The requested resource is temporarily unavailable. A Retry-After header may be present that specifies how many seconds you need to wait before attempting the request again.
- **`428`** — Precondition Required: File(s) cannot be scanned for malware and need to be force downloaded.
- **`429`** — Too Many Requests: Too many requests have been sent in a given amount of time and the request has been rate limited. A Retry-After header should be present that specifies how many seconds you need to wait before a successful request can be made.
- **`500`** — Internal Server Error: Something went wrong on the server. If the issue persists, feel free to contact the [Webex Developer Support team](/explore/support).
- **`502`** — Bad Gateway: The server received an invalid response from an upstream server while processing the request. Try again later.
- **`503`** — Service Unavailable: Server is overloaded with requests. Try again later.
- **`504`** — Gateway Timeout: An upstream server failed to respond on time. If your query uses max parameter, please try to reduce it.

---

### 7.3 People: Get My Own Details

**Endpoint:** `GET /people/me`

Get profile details for the authenticated user. This is the same as GET `/people/{personId}` using the Person ID associated with your Auth token.

Admin users can include `Webex Calling` (BroadCloud) user details in the response by specifying `callingData` parameter as true.

#### Parameters

| Name | In | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| `callingData` | `query` | `boolean` | No | Include Webex Calling user details in the response. |

#### Responses

- **`200`** — OK
  ```json
  {
    "type": "object",
    "properties": {
      "id": {
        "type": "string",
        "example": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS9mNWIzNjE4Ny1jOGRkLTQ3MjctOGIyZi1mOWM0NDdmMjkwNDY",
        "description": "A unique identifier for the person."
      },
      "emails": {
        "type": "array",
        "items": {
          "type": "string",
          "example": "john.andersen@example.com"
        },
        "description": "The email addresses of the person."
      },
      "phoneNumbers": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "type": {
              "type": "string",
              "enum": [
                "work",
                "work_extension",
                "mobile",
                "fax"
              ],
              "description": "The type of phone number.\n * `work` - Work phone number of the person.\n * `work_extension` - Work extension of the person. For the Webex Calling person, the value will have a routing prefix along with the extension.\n * `mobile` - Mobile number of the person.\n * `fax` - FAX number of the person.\n"
            },
            "value": {
              "type": "string",
              "example": "+1 408 526 7209",
              "description": "The phone number."
            },
            "primary": {
              "type": "boolean",
              "example": true,
              "description": "Primary number for the person."
            }
          }
        },
        "description": "Phone numbers for the person."
      },
      "extension": {
        "type": "string",
        "example": "133",
        "description": "The Webex Calling extension for the person. Only applies to a person with a Webex Calling license."
      },
      "locationId": {
        "type": "string",
        "example": "Y2lzY29zcGFyazovL3VzL0xPQ0FUSU9OLzYzNzE1",
        "description": "The ID of the location for this person retrieved from BroadCloud."
      },
      "displayName": {
        "type": "string",
        "example": "John Andersen",
        "description": "The full name of the person."
      },
      "nickName": {
        "type": "string",
        "example": "John",
        "description": "The nickname of the person if configured. If no nickname is configured for the person, this field will not be present."
      },
      "firstName": {
        "type": "string",
        "example": "John",
        "description": "The first name of the person."
      },
      "lastName": {
        "type": "string",
        "example": "Andersen",
        "description": "The last name of the person."
      },
      "avatar": {
        "type": "string",
        "example": "https://1efa7a94ed21783e352-c62266528714497a17239ececf39e9e2.ssl.cf1.rackcdn.com/V1~54c844c89e678e5a7b16a306bc2897b9~wx29yGtlTpilEFlYzqPKag==~1600",
        "description": "The URL to the person's avatar in PNG format."
      },
      "orgId": {
        "type": "string",
        "example": "Y2lzY29zcGFyazovL3VzL09SR0FOSVpBVElPTi85NmFiYzJhYS0zZGNjLTExZTUtYTE1Mi1mZTM0ODE5Y2RjOWE",
        "description": "The ID of the organization to which this person belongs."
      },
      "roles": {
        "type": "array",
        "items": {
          "type": "string",
          "example": "Y2lzY29zcGFyazovL3VzL1JPTEUvOTZhYmMyYWEtM2RjYy0xMWU1LWExNTItZmUzNDgxOWNkYzlh,Y2lzY29zcGFyazovL3VzL1JPTEUvOTZhYmMyYWEtM2RjYy0xMWU1LWIyNjMtMGY0NTkyYWRlZmFi"
        },
        "description": "An array of role strings representing the roles to which this admin user belongs."
      },
      "licenses": {
        "type": "array",
        "items": {
          "type": "string",
          "example": "Y2lzY29zcGFyazovL3VzL0xJQ0VOU0UvOTZhYmMyYWEtM2RjYy0xMWU1LWExNTItZmUzNDgxOWNkYzlh,Y2lzY29zcGFyazovL3VzL0xJQ0VOU0UvOTZhYmMyYWEtM2RjYy0xMWU1LWIyNjMtMGY0NTkyYWRlZmFi"
        },
        "description": "An array of license strings allocated to this person."
      },
      "department": {
        "type": "string",
        "example": "Sales",
        "description": "The business department the user belongs to."
      },
      "manager": {
        "type": "string",
        "example": "John Duarte",
        "description": "A manager identifier."
      },
      "managerId": {
        "type": "string",
        "example": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS80ZGEzYTI0OC05YjBhLTQxMDgtODU0NC1iNTQwMzEyZTU2M2E",
        "description": "Person ID of the manager."
      },
      "title": {
        "type": "string",
        "example": "GM",
        "description": "The person's title."
      },
      "addresses": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "type": {
              "type": "string",
              "example": "work",
              "description": "The type of address."
            },
            "country": {
              "type": "string",
              "example": "US",
              "description": "The user's country."
            },
            "locality": {
              "type": "string",
              "example": "Milpitas",
              "description": "The user's locality, often city."
            },
            "region": {
              "type": "string",
              "example": "California",
              "description": "The user's region, often state."
            },
            "streetAddress": {
              "type": "string",
              "example": "1099 Bird Ave.",
              "description": "The user's street."
            },
            "postalCode": {
              "type": "string",
              "example": "99212",
              "description": "The user's postal or zip code."
            }
          }
        },
        "description": "A person's addresses."
      },
      "created": {
        "type": "string",
        "example": "2015-10-18T14:26:16.000Z",
        "description": "The date and time the person was created."
      },
      "lastModified": {
        "type": "string",
        "example": "2015-10-18T14:26:16.000Z",
        "description": "The date and time the person was last changed."
      },
      "timezone": {
        "type": "string",
        "example": "America/Denver",
        "description": "The time zone of the person if configured. If no timezone is configured on the account, this field will not be present."
      },
      "lastActivity": {
        "type": "string",
        "example": "2015-10-18T14:26:16.028Z",
        "description": "The date and time of the person's last activity within Webex. This will only be returned for people within your organization or an organization you manage. Presence information will not be shown if the authenticated user has [disabled status sharing](https://help.webex.com/nkzs6wl/)."
      },
      "siteUrls": {
        "type": "array",
        "items": {
          "type": "string",
          "example": "mysite.webex.com#attendee"
        },
        "description": "One or several site names where this user has a role (host or attendee)."
      },
      "sipAddresses": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "type": {
              "type": "string",
              "enum": [
                "personal-room",
                "enterprise",
                "cloud-calling"
              ],
              "description": "The type of SIP address.\n * `personal-room` - Personal room address.\n * `enterprise` - Enterprise address.\n * `cloud-calling` - Cloud calling address.\n"
            },
            "value": {
              "type": "string",
              "example": "testuser5@mycompany.webex.com",
              "description": "The SIP address."
            },
            "primary": {
              "type": "boolean",
              "description": "Primary SIP address of the person."
            }
          }
        },
        "description": "The user's SIP addresses. Read-only."
      },
      "xmppFederationJid": {
        "type": "string",
        "example": "user@example.com",
        "description": "Identifier for intra-domain federation with other XMPP based messenger systems."
      },
      "status": {
        "type": "string",
        "enum": [
          "active",
          "call",
          "DoNotDisturb",
          "inactive",
          "meeting",
          "OutOfOffice",
          "pending",
          "presenting",
          "unknown"
        ],
        "description": "The current presence status of the person. This will only be returned for people within your organization or an organization you manage. Presence information will not be shown if the authenticated user has [disabled status sharing](https://help.webex.com/nkzs6wl/). Presence status is different from Control Hub's \"Last Service Access Time\" which indicates the last time an oAuth token was issued for this user.\n * `active` - Active within the last 10 minutes.\n * `call` - The user is in a call.\n * `DoNotDisturb` - The user has manually set their status to \"Do Not Disturb\".\n * `inactive` - Last activity occurred more than 10 minutes ago.\n * `meeting` - The user is in a meeting.\n * `OutOfOffice` - The user or a Hybrid Calendar service has indicated that they are \"Out of Office\".\n * `pending` - The user has never logged in; a status cannot be determined.\n * `presenting` - The user is sharing content.\n * `unknown` - The user\u2019s status could not be determined.\n"
      },
      "invitePending": {
        "type": "string",
        "enum": [
          "true",
          "false"
        ],
        "description": "Whether or not an invite is pending for the user to complete account activation. This property is only returned if the authenticated user is an admin user for the person's organization.\n * `true` - The person has been invited to Webex but has not created an account.\n * `false` - An invite is not pending for this person.\n"
      },
      "loginEnabled": {
        "type": "string",
        "enum": [
          "true",
          "false"
        ],
        "description": "Whether or not the user is allowed to use Webex. This property is only returned if the authenticated user is an admin user for the person's organization.\n * `true` - The person _can_ log into Webex.\n * `false` - The person _cannot_ log into Webex.\n"
      },
      "type": {
        "type": "string",
        "enum": [
          "person",
          "bot",
          "appuser"
        ],
        "description": "The type of person account, such as person or bot.\n * `person` - Account belongs to a person.\n * `bot` - Account is a bot user.\n * `appuser` - Account is a [guest user](/docs/guest-issuer).\n"
      }
    },
    "$$ref": "#/components/schemas/Person"
  }
  ```
- **`400`** — Bad Request: The request was invalid or cannot be otherwise served. An accompanying error message will explain further.
- **`401`** — Unauthorized: Authentication credentials were missing or incorrect.
- **`403`** — Forbidden: The request is understood, but it has been refused or access is not allowed.
- **`404`** — Not Found: The URI requested is invalid or the resource requested, such as a user, does not exist. Also returned when the requested format is not supported by the requested method.
- **`405`** — Method Not Allowed: The request was made to a resource using an HTTP request method that is not supported.
- **`409`** — Conflict: The request could not be processed because it conflicts with some established rule of the system. For example, a person may not be added to a room more than once.
- **`410`** — Gone: The requested resource is no longer available.
- **`415`** — Unsupported Media Type: The request was made to a resource without specifying a media type or used a media type that is not supported.
- **`423`** — Locked: The requested resource is temporarily unavailable. A Retry-After header may be present that specifies how many seconds you need to wait before attempting the request again.
- **`428`** — Precondition Required: File(s) cannot be scanned for malware and need to be force downloaded.
- **`429`** — Too Many Requests: Too many requests have been sent in a given amount of time and the request has been rate limited. A Retry-After header should be present that specifies how many seconds you need to wait before a successful request can be made.
- **`500`** — Internal Server Error: Something went wrong on the server. If the issue persists, feel free to contact the [Webex Developer Support team](/explore/support).
- **`502`** — Bad Gateway: The server received an invalid response from an upstream server while processing the request. Try again later.
- **`503`** — Service Unavailable: Server is overloaded with requests. Try again later.
- **`504`** — Gateway Timeout: An upstream server failed to respond on time. If your query uses max parameter, please try to reduce it.

---

### 7.4 People: Get Person Details

**Endpoint:** `GET /people/{personId}`

Shows details for a person, by ID.

Response properties associated with a user's presence status, such as `status` or `lastActivity`, will only be displayed for people within your organization or an organization you manage. Presence information will not be shown if the authenticated user has [disabled status sharing](https://help.webex.com/nkzs6wl/).

Admin users can include `Webex Calling` (BroadCloud) user details in the response by specifying `callingData` parameter as `true`.

Specify the person ID in the `personId` parameter in the URI.

#### Parameters

| Name | In | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| `personId` | `path` | `string` | Yes | A unique identifier for the person. |
| `callingData` | `query` | `boolean` | No | Include Webex Calling user details in the response. |

#### Responses

- **`200`** — OK
  ```json
  {
    "type": "object",
    "properties": {
      "id": {
        "type": "string",
        "example": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS9mNWIzNjE4Ny1jOGRkLTQ3MjctOGIyZi1mOWM0NDdmMjkwNDY",
        "description": "A unique identifier for the person."
      },
      "emails": {
        "type": "array",
        "items": {
          "type": "string",
          "example": "john.andersen@example.com"
        },
        "description": "The email addresses of the person."
      },
      "phoneNumbers": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "type": {
              "type": "string",
              "enum": [
                "work",
                "work_extension",
                "mobile",
                "fax"
              ],
              "description": "The type of phone number.\n * `work` - Work phone number of the person.\n * `work_extension` - Work extension of the person. For the Webex Calling person, the value will have a routing prefix along with the extension.\n * `mobile` - Mobile number of the person.\n * `fax` - FAX number of the person.\n"
            },
            "value": {
              "type": "string",
              "example": "+1 408 526 7209",
              "description": "The phone number."
            },
            "primary": {
              "type": "boolean",
              "example": true,
              "description": "Primary number for the person."
            }
          }
        },
        "description": "Phone numbers for the person."
      },
      "extension": {
        "type": "string",
        "example": "133",
        "description": "The Webex Calling extension for the person. Only applies to a person with a Webex Calling license."
      },
      "locationId": {
        "type": "string",
        "example": "Y2lzY29zcGFyazovL3VzL0xPQ0FUSU9OLzYzNzE1",
        "description": "The ID of the location for this person retrieved from BroadCloud."
      },
      "displayName": {
        "type": "string",
        "example": "John Andersen",
        "description": "The full name of the person."
      },
      "nickName": {
        "type": "string",
        "example": "John",
        "description": "The nickname of the person if configured. If no nickname is configured for the person, this field will not be present."
      },
      "firstName": {
        "type": "string",
        "example": "John",
        "description": "The first name of the person."
      },
      "lastName": {
        "type": "string",
        "example": "Andersen",
        "description": "The last name of the person."
      },
      "avatar": {
        "type": "string",
        "example": "https://1efa7a94ed21783e352-c62266528714497a17239ececf39e9e2.ssl.cf1.rackcdn.com/V1~54c844c89e678e5a7b16a306bc2897b9~wx29yGtlTpilEFlYzqPKag==~1600",
        "description": "The URL to the person's avatar in PNG format."
      },
      "orgId": {
        "type": "string",
        "example": "Y2lzY29zcGFyazovL3VzL09SR0FOSVpBVElPTi85NmFiYzJhYS0zZGNjLTExZTUtYTE1Mi1mZTM0ODE5Y2RjOWE",
        "description": "The ID of the organization to which this person belongs."
      },
      "roles": {
        "type": "array",
        "items": {
          "type": "string",
          "example": "Y2lzY29zcGFyazovL3VzL1JPTEUvOTZhYmMyYWEtM2RjYy0xMWU1LWExNTItZmUzNDgxOWNkYzlh,Y2lzY29zcGFyazovL3VzL1JPTEUvOTZhYmMyYWEtM2RjYy0xMWU1LWIyNjMtMGY0NTkyYWRlZmFi"
        },
        "description": "An array of role strings representing the roles to which this admin user belongs."
      },
      "licenses": {
        "type": "array",
        "items": {
          "type": "string",
          "example": "Y2lzY29zcGFyazovL3VzL0xJQ0VOU0UvOTZhYmMyYWEtM2RjYy0xMWU1LWExNTItZmUzNDgxOWNkYzlh,Y2lzY29zcGFyazovL3VzL0xJQ0VOU0UvOTZhYmMyYWEtM2RjYy0xMWU1LWIyNjMtMGY0NTkyYWRlZmFi"
        },
        "description": "An array of license strings allocated to this person."
      },
      "department": {
        "type": "string",
        "example": "Sales",
        "description": "The business department the user belongs to."
      },
      "manager": {
        "type": "string",
        "example": "John Duarte",
        "description": "A manager identifier."
      },
      "managerId": {
        "type": "string",
        "example": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS80ZGEzYTI0OC05YjBhLTQxMDgtODU0NC1iNTQwMzEyZTU2M2E",
        "description": "Person ID of the manager."
      },
      "title": {
        "type": "string",
        "example": "GM",
        "description": "The person's title."
      },
      "addresses": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "type": {
              "type": "string",
              "example": "work",
              "description": "The type of address."
            },
            "country": {
              "type": "string",
              "example": "US",
              "description": "The user's country."
            },
            "locality": {
              "type": "string",
              "example": "Milpitas",
              "description": "The user's locality, often city."
            },
            "region": {
              "type": "string",
              "example": "California",
              "description": "The user's region, often state."
            },
            "streetAddress": {
              "type": "string",
              "example": "1099 Bird Ave.",
              "description": "The user's street."
            },
            "postalCode": {
              "type": "string",
              "example": "99212",
              "description": "The user's postal or zip code."
            }
          }
        },
        "description": "A person's addresses."
      },
      "created": {
        "type": "string",
        "example": "2015-10-18T14:26:16.000Z",
        "description": "The date and time the person was created."
      },
      "lastModified": {
        "type": "string",
        "example": "2015-10-18T14:26:16.000Z",
        "description": "The date and time the person was last changed."
      },
      "timezone": {
        "type": "string",
        "example": "America/Denver",
        "description": "The time zone of the person if configured. If no timezone is configured on the account, this field will not be present."
      },
      "lastActivity": {
        "type": "string",
        "example": "2015-10-18T14:26:16.028Z",
        "description": "The date and time of the person's last activity within Webex. This will only be returned for people within your organization or an organization you manage. Presence information will not be shown if the authenticated user has [disabled status sharing](https://help.webex.com/nkzs6wl/)."
      },
      "siteUrls": {
        "type": "array",
        "items": {
          "type": "string",
          "example": "mysite.webex.com#attendee"
        },
        "description": "One or several site names where this user has a role (host or attendee)."
      },
      "sipAddresses": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "type": {
              "type": "string",
              "enum": [
                "personal-room",
                "enterprise",
                "cloud-calling"
              ],
              "description": "The type of SIP address.\n * `personal-room` - Personal room address.\n * `enterprise` - Enterprise address.\n * `cloud-calling` - Cloud calling address.\n"
            },
            "value": {
              "type": "string",
              "example": "testuser5@mycompany.webex.com",
              "description": "The SIP address."
            },
            "primary": {
              "type": "boolean",
              "description": "Primary SIP address of the person."
            }
          }
        },
        "description": "The user's SIP addresses. Read-only."
      },
      "xmppFederationJid": {
        "type": "string",
        "example": "user@example.com",
        "description": "Identifier for intra-domain federation with other XMPP based messenger systems."
      },
      "status": {
        "type": "string",
        "enum": [
          "active",
          "call",
          "DoNotDisturb",
          "inactive",
          "meeting",
          "OutOfOffice",
          "pending",
          "presenting",
          "unknown"
        ],
        "description": "The current presence status of the person. This will only be returned for people within your organization or an organization you manage. Presence information will not be shown if the authenticated user has [disabled status sharing](https://help.webex.com/nkzs6wl/). Presence status is different from Control Hub's \"Last Service Access Time\" which indicates the last time an oAuth token was issued for this user.\n * `active` - Active within the last 10 minutes.\n * `call` - The user is in a call.\n * `DoNotDisturb` - The user has manually set their status to \"Do Not Disturb\".\n * `inactive` - Last activity occurred more than 10 minutes ago.\n * `meeting` - The user is in a meeting.\n * `OutOfOffice` - The user or a Hybrid Calendar service has indicated that they are \"Out of Office\".\n * `pending` - The user has never logged in; a status cannot be determined.\n * `presenting` - The user is sharing content.\n * `unknown` - The user\u2019s status could not be determined.\n"
      },
      "invitePending": {
        "type": "string",
        "enum": [
          "true",
          "false"
        ],
        "description": "Whether or not an invite is pending for the user to complete account activation. This property is only returned if the authenticated user is an admin user for the person's organization.\n * `true` - The person has been invited to Webex but has not created an account.\n * `false` - An invite is not pending for this person.\n"
      },
      "loginEnabled": {
        "type": "string",
        "enum": [
          "true",
          "false"
        ],
        "description": "Whether or not the user is allowed to use Webex. This property is only returned if the authenticated user is an admin user for the person's organization.\n * `true` - The person _can_ log into Webex.\n * `false` - The person _cannot_ log into Webex.\n"
      },
      "type": {
        "type": "string",
        "enum": [
          "person",
          "bot",
          "appuser"
        ],
        "description": "The type of person account, such as person or bot.\n * `person` - Account belongs to a person.\n * `bot` - Account is a bot user.\n * `appuser` - Account is a [guest user](/docs/guest-issuer).\n"
      }
    },
    "$$ref": "#/components/schemas/Person"
  }
  ```
- **`400`** — Bad Request: The request was invalid or cannot be otherwise served. An accompanying error message will explain further.
- **`401`** — Unauthorized: Authentication credentials were missing or incorrect.
- **`403`** — Forbidden: The request is understood, but it has been refused or access is not allowed.
- **`404`** — Not Found: The URI requested is invalid or the resource requested, such as a user, does not exist. Also returned when the requested format is not supported by the requested method.
- **`405`** — Method Not Allowed: The request was made to a resource using an HTTP request method that is not supported.
- **`409`** — Conflict: The request could not be processed because it conflicts with some established rule of the system. For example, a person may not be added to a room more than once.
- **`410`** — Gone: The requested resource is no longer available.
- **`415`** — Unsupported Media Type: The request was made to a resource without specifying a media type or used a media type that is not supported.
- **`423`** — Locked: The requested resource is temporarily unavailable. A Retry-After header may be present that specifies how many seconds you need to wait before attempting the request again.
- **`428`** — Precondition Required: File(s) cannot be scanned for malware and need to be force downloaded.
- **`429`** — Too Many Requests: Too many requests have been sent in a given amount of time and the request has been rate limited. A Retry-After header should be present that specifies how many seconds you need to wait before a successful request can be made.
- **`500`** — Internal Server Error: Something went wrong on the server. If the issue persists, feel free to contact the [Webex Developer Support team](/explore/support).
- **`502`** — Bad Gateway: The server received an invalid response from an upstream server while processing the request. Try again later.
- **`503`** — Service Unavailable: Server is overloaded with requests. Try again later.
- **`504`** — Gateway Timeout: An upstream server failed to respond on time. If your query uses max parameter, please try to reduce it.

---

### 7.5 People: List People

**Endpoint:** `GET /people`

List people in your organization. For most users, either the `email` or `displayName` parameter is required. Admin users can omit these fields and list all users in their organization.

Response properties associated with a user's presence status, such as `status` or `lastActivity`, will only be returned for people within your organization or an organization you manage. Presence information will not be returned if the authenticated user has [disabled status sharing](https://help.webex.com/nkzs6wl/). Calling /people frequently to poll `status` information for a large set of users will quickly lead to `429` errors and throttling of such requests and is therefore discouraged.

Admin users can include `Webex Calling` (BroadCloud) user details in the response by specifying `callingData` parameter as `true`. Admin users can list all users in a location. Admin users will receive an enriched payload with additional administrative fields like `licenses`,`roles`, `locations` etc. These fields are shown when accessing a user via GET /people/{id}, not when doing a GET /people?id=

Lookup by `email` is only supported for people within the same org or where a partner admin relationship is in place.

Lookup by `roles` is only supported for Admin users for the people within the same org.

Long result sets will be split into [pages](/docs/basics#pagination).

#### Parameters

| Name | In | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| `email` | `query` | `string` | No | List people with this email address. For non-admin requests, either this or `displayName` are required. With the exception of partner admins and a managed org relationship, people lookup by email is only available for users in the same org. |
| `displayName` | `query` | `string` | No | List people whose name starts with this string. For non-admin requests, either this or email are required. |
| `id` | `query` | `string` | No | List people by ID. Accepts up to 85 person IDs separated by commas. If this parameter is provided then presence information (such as the `lastActivity` or `status` properties) will not be included in the response. |
| `orgId` | `query` | `string` | No | List people in this organization. Only admin users of another organization (such as partners) may use this parameter. |
| `roles` | `query` | `string` | No | List of roleIds separated by commas. |
| `callingData` | `query` | `boolean` | No | Include Webex Calling user details in the response. |
| `locationId` | `query` | `string` | No | List people present in this location. |
| `max` | `query` | `number` | No | Limit the maximum number of people in the response. If `callingData`=true, then `max` will not be more than 100. If `locationId` is specified then `max` will not be more than 50. |
| `excludeStatus` | `query` | `boolean` | No | Omit people status/availability to enhance query performance. |

#### Responses

- **`200`** — OK
  ```json
  {
    "type": "object",
    "properties": {
      "items": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "id": {
              "type": "string",
              "example": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS9mNWIzNjE4Ny1jOGRkLTQ3MjctOGIyZi1mOWM0NDdmMjkwNDY",
              "description": "A unique identifier for the person."
            },
            "emails": {
              "type": "array",
              "items": {
                "type": "string",
                "example": "john.andersen@example.com"
              },
              "description": "The email addresses of the person."
            },
            "phoneNumbers": {
              "type": "array",
              "items": {
                "type": "object",
                "properties": {
                  "type": {
                    "type": "string",
                    "enum": [
                      "work",
                      "work_extension",
                      "mobile",
                      "fax"
                    ],
                    "description": "The type of phone number.\n * `work` - Work phone number of the person.\n * `work_extension` - Work extension of the person. For the Webex Calling person, the value will have a routing prefix along with the extension.\n * `mobile` - Mobile number of the person.\n * `fax` - FAX number of the person.\n"
                  },
                  "value": {
                    "type": "string",
                    "example": "+1 408 526 7209",
                    "description": "The phone number."
                  },
                  "primary": {
                    "type": "boolean",
                    "example": true,
                    "description": "Primary number for the person."
                  }
                }
              },
              "description": "Phone numbers for the person."
            },
            "extension": {
              "type": "string",
              "example": "133",
              "description": "The Webex Calling extension for the person. Only applies to a person with a Webex Calling license."
            },
            "locationId": {
              "type": "string",
              "example": "Y2lzY29zcGFyazovL3VzL0xPQ0FUSU9OLzYzNzE1",
              "description": "The ID of the location for this person retrieved from BroadCloud."
            },
            "displayName": {
              "type": "string",
              "example": "John Andersen",
              "description": "The full name of the person."
            },
            "nickName": {
              "type": "string",
              "example": "John",
              "description": "The nickname of the person if configured. If no nickname is configured for the person, this field will not be present."
            },
            "firstName": {
              "type": "string",
              "example": "John",
              "description": "The first name of the person."
            },
            "lastName": {
              "type": "string",
              "example": "Andersen",
              "description": "The last name of the person."
            },
            "avatar": {
              "type": "string",
              "example": "https://1efa7a94ed21783e352-c62266528714497a17239ececf39e9e2.ssl.cf1.rackcdn.com/V1~54c844c89e678e5a7b16a306bc2897b9~wx29yGtlTpilEFlYzqPKag==~1600",
              "description": "The URL to the person's avatar in PNG format."
            },
            "orgId": {
              "type": "string",
              "example": "Y2lzY29zcGFyazovL3VzL09SR0FOSVpBVElPTi85NmFiYzJhYS0zZGNjLTExZTUtYTE1Mi1mZTM0ODE5Y2RjOWE",
              "description": "The ID of the organization to which this person belongs."
            },
            "roles": {
              "type": "array",
              "items": {
                "type": "string",
                "example": "Y2lzY29zcGFyazovL3VzL1JPTEUvOTZhYmMyYWEtM2RjYy0xMWU1LWExNTItZmUzNDgxOWNkYzlh,Y2lzY29zcGFyazovL3VzL1JPTEUvOTZhYmMyYWEtM2RjYy0xMWU1LWIyNjMtMGY0NTkyYWRlZmFi"
              },
              "description": "An array of role strings representing the roles to which this admin user belongs."
            },
            "licenses": {
              "type": "array",
              "items": {
                "type": "string",
                "example": "Y2lzY29zcGFyazovL3VzL0xJQ0VOU0UvOTZhYmMyYWEtM2RjYy0xMWU1LWExNTItZmUzNDgxOWNkYzlh,Y2lzY29zcGFyazovL3VzL0xJQ0VOU0UvOTZhYmMyYWEtM2RjYy0xMWU1LWIyNjMtMGY0NTkyYWRlZmFi"
              },
              "description": "An array of license strings allocated to this person."
            },
            "department": {
              "type": "string",
              "example": "Sales",
              "description": "The business department the user belongs to."
            },
            "manager": {
              "type": "string",
              "example": "John Duarte",
              "description": "A manager identifier."
            },
            "managerId": {
              "type": "string",
              "example": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS80ZGEzYTI0OC05YjBhLTQxMDgtODU0NC1iNTQwMzEyZTU2M2E",
              "description": "Person ID of the manager."
            },
            "title": {
              "type": "string",
              "example": "GM",
              "description": "The person's title."
            },
            "addresses": {
              "type": "array",
              "items": {
                "type": "object",
                "properties": {
                  "type": {
                    "type": "string",
                    "example": "work",
                    "description": "The type of address."
                  },
                  "country": {
                    "type": "string",
                    "example": "US",
                    "description": "The user's country."
                  },
                  "locality": {
                    "type": "string",
                    "example": "Milpitas",
                    "description": "The user's locality, often city."
                  },
                  "region": {
                    "type": "string",
                    "example": "California",
                    "description": "The user's region, often state."
                  },
                  "streetAddress": {
                    "type": "string",
                    "example": "1099 Bird Ave.",
                    "description": "The user's street."
                  },
                  "postalCode": {
                    "type": "string",
                    "example": "99212",
                    "description": "The user's postal or zip code."
                  }
                }
              },
              "description": "A person's addresses."
            },
            "created": {
              "type": "string",
              "example": "2015-10-18T14:26:16.000Z",
              "description": "The date and time the person was created."
            },
            "lastModified": {
              "type": "string",
              "example": "2015-10-18T14:26:16.000Z",
              "description": "The date and time the person was last changed."
            },
            "timezone": {
              "type": "string",
              "example": "America/Denver",
              "description": "The time zone of the person if configured. If no timezone is configured on the account, this field will not be present."
            },
            "lastActivity": {
              "type": "string",
              "example": "2015-10-18T14:26:16.028Z",
              "description": "The date and time of the person's last activity within Webex. This will only be returned for people within your organization or an organization you manage. Presence information will not be shown if the authenticated user has [disabled status sharing](https://help.webex.com/nkzs6wl/)."
            },
            "siteUrls": {
              "type": "array",
              "items": {
                "type": "string",
                "example": "mysite.webex.com#attendee"
              },
              "description": "One or several site names where this user has a role (host or attendee)."
            },
            "sipAddresses": {
              "type": "array",
              "items": {
                "type": "object",
                "properties": {
                  "type": {
                    "type": "string",
                    "enum": [
                      "personal-room",
                      "enterprise",
                      "cloud-calling"
                    ],
                    "description": "The type of SIP address.\n * `personal-room` - Personal room address.\n * `enterprise` - Enterprise address.\n * `cloud-calling` - Cloud calling address.\n"
                  },
                  "value": {
                    "type": "string",
                    "example": "testuser5@mycompany.webex.com",
                    "description": "The SIP address."
                  },
                  "primary": {
                    "type": "boolean",
                    "description": "Primary SIP address of the person."
                  }
                }
              },
              "description": "The user's SIP addresses. Read-only."
            },
            "xmppFederationJid": {
              "type": "string",
              "example": "user@example.com",
              "description": "Identifier for intra-domain federation with other XMPP based messenger systems."
            },
            "status": {
              "type": "string",
              "enum": [
                "active",
                "call",
                "DoNotDisturb",
                "inactive",
                "meeting",
                "OutOfOffice",
                "pending",
                "presenting",
                "unknown"
              ],
              "description": "The current presence status of the person. This will only be returned for people within your organization or an organization you manage. Presence information will not be shown if the authenticated user has [disabled status sharing](https://help.webex.com/nkzs6wl/). Presence status is different from Control Hub's \"Last Service Access Time\" which indicates the last time an oAuth token was issued for this user.\n * `active` - Active within the last 10 minutes.\n * `call` - The user is in a call.\n * `DoNotDisturb` - The user has manually set their status to \"Do Not Disturb\".\n * `inactive` - Last activity occurred more than 10 minutes ago.\n * `meeting` - The user is in a meeting.\n * `OutOfOffice` - The user or a Hybrid Calendar service has indicated that they are \"Out of Office\".\n * `pending` - The user has never logged in; a status cannot be determined.\n * `presenting` - The user is sharing content.\n * `unknown` - The user\u2019s status could not be determined.\n"
            },
            "invitePending": {
              "type": "string",
              "enum": [
                "true",
                "false"
              ],
              "description": "Whether or not an invite is pending for the user to complete account activation. This property is only returned if the authenticated user is an admin user for the person's organization.\n * `true` - The person has been invited to Webex but has not created an account.\n * `false` - An invite is not pending for this person.\n"
            },
            "loginEnabled": {
              "type": "string",
              "enum": [
                "true",
                "false"
              ],
              "description": "Whether or not the user is allowed to use Webex. This property is only returned if the authenticated user is an admin user for the person's organization.\n * `true` - The person _can_ log into Webex.\n * `false` - The person _cannot_ log into Webex.\n"
            },
            "type": {
              "type": "string",
              "enum": [
                "person",
                "bot",
                "appuser"
              ],
              "description": "The type of person account, such as person or bot.\n * `person` - Account belongs to a person.\n * `bot` - Account is a bot user.\n * `appuser` - Account is a [guest user](/docs/guest-issuer).\n"
            }
          },
          "$$ref": "#/components/schemas/Person"
        },
        "description": "An array of person objects."
      },
      "notFoundIds": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "An array of person IDs that could not be found."
      }
    },
    "$$ref": "#/components/schemas/PersonCollectionResponse"
  }
  ```
- **`400`** — Bad Request: The request was invalid or cannot be otherwise served. An accompanying error message will explain further.
- **`401`** — Unauthorized: Authentication credentials were missing or incorrect.
- **`403`** — Forbidden: The request is understood, but it has been refused or access is not allowed.
- **`404`** — Not Found: The URI requested is invalid or the resource requested, such as a user, does not exist. Also returned when the requested format is not supported by the requested method.
- **`405`** — Method Not Allowed: The request was made to a resource using an HTTP request method that is not supported.
- **`409`** — Conflict: The request could not be processed because it conflicts with some established rule of the system. For example, a person may not be added to a room more than once.
- **`410`** — Gone: The requested resource is no longer available.
- **`415`** — Unsupported Media Type: The request was made to a resource without specifying a media type or used a media type that is not supported.
- **`423`** — Locked: The requested resource is temporarily unavailable. A Retry-After header may be present that specifies how many seconds you need to wait before attempting the request again.
- **`428`** — Precondition Required: File(s) cannot be scanned for malware and need to be force downloaded.
- **`429`** — Too Many Requests: Too many requests have been sent in a given amount of time and the request has been rate limited. A Retry-After header should be present that specifies how many seconds you need to wait before a successful request can be made.
- **`500`** — Internal Server Error: Something went wrong on the server. If the issue persists, feel free to contact the [Webex Developer Support team](/explore/support).
- **`502`** — Bad Gateway: The server received an invalid response from an upstream server while processing the request. Try again later.
- **`503`** — Service Unavailable: Server is overloaded with requests. Try again later.
- **`504`** — Gateway Timeout: An upstream server failed to respond on time. If your query uses max parameter, please try to reduce it.

---

### 7.6 People: Update a Person

**Endpoint:** `PUT /people/{personId}`

Update details for a person, by ID.

Specify the person ID in the `personId` parameter in the URI. Only an admin can update a person details.

Include all details for the person. This action expects all user details to be present in the request. A common approach is to first [GET the person's details](/docs/api/v1/people/get-person-details), make changes, then PUT both the changed and unchanged values.

Admin users can include `Webex Calling` (BroadCloud) user details in the response by specifying `callingData` parameter as true.

When doing attendee management, to update a user from host role to an attendee for a site append `#attendee` to the respective `siteUrl` and remove the meeting host license for this site from the license array.
To update a person from an attendee role to a host for a site, add the meeting license for this site in the meeting array, and remove that site from the `siteurl` parameter.

To remove the attendee privilege for a user on a meeting site, remove the `sitename#attendee` from the `siteUrl`s array. The `showAllTypes` parameter must be set to `true`.

**NOTE**:

* When assigning a Webex Calling license, either a telephone number or extension must already be assigned to the person or provided in the request payload.

* When `callingData` is set to `true`, a Webex Calling license must be included in the `licenses` array.

* The `locationId` can only be set when assigning a calling license to a user. It cannot be changed if a user is already an existing calling user.

* The `extension` field should be used to update the Webex Calling extension for a person. The extension value should not include the location routing prefix. The `work_extension` type in the `phoneNumbers` object as seen in the response payload of [List People](/docs/api/v1/people/list-people) or [Get Person Details](/docs/api/v1/people/get-person-details), cannot be used to set the Webex Calling extension for a person.

* When updating a user with multiple email addresses using a PUT request, ensure that the primary email address is listed first in the array. Note that the order of email addresses returned by a GET request is not guaranteed..

* The People API is a combination of several microservices, each responsible for specific attributes of a person. As a result, a PUT request that returns an error response code may still have altered some values of the person's data. Therefore, it is recommended to perform a GET request after encountering an error to verify the current state of the resource. 

* Some licenses are implicitly assigned by the system and cannot be admin controlled. They are necessary for the baseline function of the Webex system. If you get an error about implicitly assigned licensed that cannot be removed, please ensure you have the corresponding license in your PUT request.

* When assigning multiple licenses in a single request, the system will assign all valid and available licenses. If any requested licenses cannot be assigned, the operation will continue with the remaining licenses. As a result, it is possible that not all requested licenses are assigned to the user.

#### Parameters

| Name | In | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| `personId` | `path` | `string` | Yes | A unique identifier for the person. |
| `callingData` | `query` | `boolean` | No | Include Webex Calling user details in the response. |
| `showAllTypes` | `query` | `boolean` | No | Include additional user data like `#attendee` role. |
| `minResponse` | `query` | `boolean` | No | Set to `true` to improve performance by omitting person details in the response. If unsuccessful the response will have optional error details. |

#### Request Body Schema

```json
{
  "type": "object",
  "required": [
    "displayName"
  ],
  "properties": {
    "emails": {
      "type": "array",
      "items": {
        "type": "string",
        "example": "john.andersen@example.com"
      },
      "description": "The email addresses of the person. Only one email address is allowed per person."
    },
    "phoneNumbers": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "type": {
            "type": "string",
            "enum": [
              "work"
            ],
            "description": "The type of phone number. Valid values are 'work'"
          },
          "value": {
            "type": "string",
            "example": "408 526 7209",
            "description": "The phone number."
          }
        }
      },
      "description": "Phone numbers for the person. Can only be set for Webex Calling. Needs a Webex Calling license."
    },
    "extension": {
      "type": "string",
      "example": "133",
      "description": "Webex Calling extension of the person. This is only settable for a person with a Webex Calling license."
    },
    "locationId": {
      "type": "string",
      "example": "Y2lzY29zcGFyazovL3VzL0xPQ0FUSU9OLzYzNzE1",
      "description": "The ID of the location for this person."
    },
    "displayName": {
      "type": "string",
      "example": "John Andersen",
      "description": "The full name of the person."
    },
    "firstName": {
      "type": "string",
      "example": "John",
      "description": "The first name of the person."
    },
    "lastName": {
      "type": "string",
      "example": "Andersen",
      "description": "The last name of the person."
    },
    "nickName": {
      "type": "string",
      "example": "John",
      "description": "The nickname of the person if configured. This cannot be overwritten and instead will be set to the firstName automatically in update requests."
    },
    "avatar": {
      "type": "string",
      "example": "https://1efa7a94ed21783e352-c62266528714497a17239ececf39e9e2.ssl.cf1.rackcdn.com/V1~54c844c89e678e5a7b16a306bc2897b9~wx29yGtlTpilEFlYzqPKag==~1600",
      "description": "The URL to the person's avatar in PNG format."
    },
    "orgId": {
      "type": "string",
      "example": "Y2lzY29zcGFyazovL3VzL09SR0FOSVpBVElPTi85NmFiYzJhYS0zZGNjLTExZTUtYTE1Mi1mZTM0ODE5Y2RjOWE",
      "description": "The ID of the organization to which this person belongs."
    },
    "roles": {
      "type": "array",
      "items": {
        "type": "string",
        "example": "Y2lzY29zcGFyazovL3VzL1JPTEUvOTZhYmMyYWEtM2RjYy0xMWU1LWExNTItZmUzNDgxOWNkYzlh,Y2lzY29zcGFyazovL3VzL1JPTEUvOTZhYmMyYWEtM2RjYy0xMWU1LWIyNjMtMGY0NTkyYWRlZmFi"
      },
      "description": "An array of role strings representing the roles to which this admin user belongs."
    },
    "licenses": {
      "type": "array",
      "items": {
        "type": "string",
        "example": "Y2lzY29zcGFyazovL3VzL0xJQ0VOU0UvOTZhYmMyYWEtM2RjYy0xMWU1LWExNTItZmUzNDgxOWNkYzlh,Y2lzY29zcGFyazovL3VzL0xJQ0VOU0UvOTZhYmMyYWEtM2RjYy0xMWU1LWIyNjMtMGY0NTkyYWRlZmFi"
      },
      "description": "An array of license strings allocated to this person."
    },
    "department": {
      "type": "string",
      "example": "Sales",
      "description": "The business department the user belongs to."
    },
    "manager": {
      "type": "string",
      "example": "John Duarte",
      "description": "A manager identifier."
    },
    "managerId": {
      "type": "string",
      "example": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS80ZGEzYTI0OC05YjBhLTQxMDgtODU0NC1iNTQwMzEyZTU2M2E",
      "description": "Person ID of the manager."
    },
    "title": {
      "type": "string",
      "example": "GM",
      "description": "The person's title."
    },
    "addresses": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "type": {
            "type": "string",
            "example": "work",
            "description": "The type of address."
          },
          "country": {
            "type": "string",
            "example": "US",
            "description": "The user's country."
          },
          "locality": {
            "type": "string",
            "example": "Milpitas",
            "description": "The user's locality, often city."
          },
          "region": {
            "type": "string",
            "example": "California",
            "description": "The user's region, often state."
          },
          "streetAddress": {
            "type": "string",
            "example": "1099 Bird Ave.",
            "description": "The user's street."
          },
          "postalCode": {
            "type": "string",
            "example": "99212",
            "description": "The user's postal or zip code."
          }
        }
      },
      "description": "A person's addresses."
    },
    "siteUrls": {
      "type": "array",
      "items": {
        "type": "string",
        "example": "mysite.webex.com#attendee"
      },
      "description": "One or several site names where this user has a role (host or attendee). Append `#attendee` to the site name to designate the attendee role on that site."
    },
    "loginEnabled": {
      "type": "boolean",
      "example": true,
      "description": "Whether or not the user is allowed to use Webex. This property is only accessible if the authenticated user is an admin user for the person's organization."
    }
  }
}
```

#### Responses

- **`200`** — OK
  ```json
  {
    "type": "object",
    "properties": {
      "id": {
        "type": "string",
        "example": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS9mNWIzNjE4Ny1jOGRkLTQ3MjctOGIyZi1mOWM0NDdmMjkwNDY",
        "description": "A unique identifier for the person."
      },
      "emails": {
        "type": "array",
        "items": {
          "type": "string",
          "example": "john.andersen@example.com"
        },
        "description": "The email addresses of the person."
      },
      "phoneNumbers": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "type": {
              "type": "string",
              "enum": [
                "work",
                "work_extension",
                "mobile",
                "fax"
              ],
              "description": "The type of phone number.\n * `work` - Work phone number of the person.\n * `work_extension` - Work extension of the person. For the Webex Calling person, the value will have a routing prefix along with the extension.\n * `mobile` - Mobile number of the person.\n * `fax` - FAX number of the person.\n"
            },
            "value": {
              "type": "string",
              "example": "+1 408 526 7209",
              "description": "The phone number."
            },
            "primary": {
              "type": "boolean",
              "example": true,
              "description": "Primary number for the person."
            }
          }
        },
        "description": "Phone numbers for the person."
      },
      "extension": {
        "type": "string",
        "example": "133",
        "description": "The Webex Calling extension for the person. Only applies to a person with a Webex Calling license."
      },
      "locationId": {
        "type": "string",
        "example": "Y2lzY29zcGFyazovL3VzL0xPQ0FUSU9OLzYzNzE1",
        "description": "The ID of the location for this person retrieved from BroadCloud."
      },
      "displayName": {
        "type": "string",
        "example": "John Andersen",
        "description": "The full name of the person."
      },
      "nickName": {
        "type": "string",
        "example": "John",
        "description": "The nickname of the person if configured. If no nickname is configured for the person, this field will not be present."
      },
      "firstName": {
        "type": "string",
        "example": "John",
        "description": "The first name of the person."
      },
      "lastName": {
        "type": "string",
        "example": "Andersen",
        "description": "The last name of the person."
      },
      "avatar": {
        "type": "string",
        "example": "https://1efa7a94ed21783e352-c62266528714497a17239ececf39e9e2.ssl.cf1.rackcdn.com/V1~54c844c89e678e5a7b16a306bc2897b9~wx29yGtlTpilEFlYzqPKag==~1600",
        "description": "The URL to the person's avatar in PNG format."
      },
      "orgId": {
        "type": "string",
        "example": "Y2lzY29zcGFyazovL3VzL09SR0FOSVpBVElPTi85NmFiYzJhYS0zZGNjLTExZTUtYTE1Mi1mZTM0ODE5Y2RjOWE",
        "description": "The ID of the organization to which this person belongs."
      },
      "roles": {
        "type": "array",
        "items": {
          "type": "string",
          "example": "Y2lzY29zcGFyazovL3VzL1JPTEUvOTZhYmMyYWEtM2RjYy0xMWU1LWExNTItZmUzNDgxOWNkYzlh,Y2lzY29zcGFyazovL3VzL1JPTEUvOTZhYmMyYWEtM2RjYy0xMWU1LWIyNjMtMGY0NTkyYWRlZmFi"
        },
        "description": "An array of role strings representing the roles to which this admin user belongs."
      },
      "licenses": {
        "type": "array",
        "items": {
          "type": "string",
          "example": "Y2lzY29zcGFyazovL3VzL0xJQ0VOU0UvOTZhYmMyYWEtM2RjYy0xMWU1LWExNTItZmUzNDgxOWNkYzlh,Y2lzY29zcGFyazovL3VzL0xJQ0VOU0UvOTZhYmMyYWEtM2RjYy0xMWU1LWIyNjMtMGY0NTkyYWRlZmFi"
        },
        "description": "An array of license strings allocated to this person."
      },
      "department": {
        "type": "string",
        "example": "Sales",
        "description": "The business department the user belongs to."
      },
      "manager": {
        "type": "string",
        "example": "John Duarte",
        "description": "A manager identifier."
      },
      "managerId": {
        "type": "string",
        "example": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS80ZGEzYTI0OC05YjBhLTQxMDgtODU0NC1iNTQwMzEyZTU2M2E",
        "description": "Person ID of the manager."
      },
      "title": {
        "type": "string",
        "example": "GM",
        "description": "The person's title."
      },
      "addresses": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "type": {
              "type": "string",
              "example": "work",
              "description": "The type of address."
            },
            "country": {
              "type": "string",
              "example": "US",
              "description": "The user's country."
            },
            "locality": {
              "type": "string",
              "example": "Milpitas",
              "description": "The user's locality, often city."
            },
            "region": {
              "type": "string",
              "example": "California",
              "description": "The user's region, often state."
            },
            "streetAddress": {
              "type": "string",
              "example": "1099 Bird Ave.",
              "description": "The user's street."
            },
            "postalCode": {
              "type": "string",
              "example": "99212",
              "description": "The user's postal or zip code."
            }
          }
        },
        "description": "A person's addresses."
      },
      "created": {
        "type": "string",
        "example": "2015-10-18T14:26:16.000Z",
        "description": "The date and time the person was created."
      },
      "lastModified": {
        "type": "string",
        "example": "2015-10-18T14:26:16.000Z",
        "description": "The date and time the person was last changed."
      },
      "timezone": {
        "type": "string",
        "example": "America/Denver",
        "description": "The time zone of the person if configured. If no timezone is configured on the account, this field will not be present."
      },
      "lastActivity": {
        "type": "string",
        "example": "2015-10-18T14:26:16.028Z",
        "description": "The date and time of the person's last activity within Webex. This will only be returned for people within your organization or an organization you manage. Presence information will not be shown if the authenticated user has [disabled status sharing](https://help.webex.com/nkzs6wl/)."
      },
      "siteUrls": {
        "type": "array",
        "items": {
          "type": "string",
          "example": "mysite.webex.com#attendee"
        },
        "description": "One or several site names where this user has a role (host or attendee)."
      },
      "sipAddresses": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "type": {
              "type": "string",
              "enum": [
                "personal-room",
                "enterprise",
                "cloud-calling"
              ],
              "description": "The type of SIP address.\n * `personal-room` - Personal room address.\n * `enterprise` - Enterprise address.\n * `cloud-calling` - Cloud calling address.\n"
            },
            "value": {
              "type": "string",
              "example": "testuser5@mycompany.webex.com",
              "description": "The SIP address."
            },
            "primary": {
              "type": "boolean",
              "description": "Primary SIP address of the person."
            }
          }
        },
        "description": "The user's SIP addresses. Read-only."
      },
      "xmppFederationJid": {
        "type": "string",
        "example": "user@example.com",
        "description": "Identifier for intra-domain federation with other XMPP based messenger systems."
      },
      "status": {
        "type": "string",
        "enum": [
          "active",
          "call",
          "DoNotDisturb",
          "inactive",
          "meeting",
          "OutOfOffice",
          "pending",
          "presenting",
          "unknown"
        ],
        "description": "The current presence status of the person. This will only be returned for people within your organization or an organization you manage. Presence information will not be shown if the authenticated user has [disabled status sharing](https://help.webex.com/nkzs6wl/). Presence status is different from Control Hub's \"Last Service Access Time\" which indicates the last time an oAuth token was issued for this user.\n * `active` - Active within the last 10 minutes.\n * `call` - The user is in a call.\n * `DoNotDisturb` - The user has manually set their status to \"Do Not Disturb\".\n * `inactive` - Last activity occurred more than 10 minutes ago.\n * `meeting` - The user is in a meeting.\n * `OutOfOffice` - The user or a Hybrid Calendar service has indicated that they are \"Out of Office\".\n * `pending` - The user has never logged in; a status cannot be determined.\n * `presenting` - The user is sharing content.\n * `unknown` - The user\u2019s status could not be determined.\n"
      },
      "invitePending": {
        "type": "string",
        "enum": [
          "true",
          "false"
        ],
        "description": "Whether or not an invite is pending for the user to complete account activation. This property is only returned if the authenticated user is an admin user for the person's organization.\n * `true` - The person has been invited to Webex but has not created an account.\n * `false` - An invite is not pending for this person.\n"
      },
      "loginEnabled": {
        "type": "string",
        "enum": [
          "true",
          "false"
        ],
        "description": "Whether or not the user is allowed to use Webex. This property is only returned if the authenticated user is an admin user for the person's organization.\n * `true` - The person _can_ log into Webex.\n * `false` - The person _cannot_ log into Webex.\n"
      },
      "type": {
        "type": "string",
        "enum": [
          "person",
          "bot",
          "appuser"
        ],
        "description": "The type of person account, such as person or bot.\n * `person` - Account belongs to a person.\n * `bot` - Account is a bot user.\n * `appuser` - Account is a [guest user](/docs/guest-issuer).\n"
      }
    },
    "$$ref": "#/components/schemas/Person"
  }
  ```
- **`204`** — No Content
- **`400`** — Bad Request: The request was invalid or cannot be otherwise served. An accompanying error message will explain further.
- **`401`** — Unauthorized: Authentication credentials were missing or incorrect.
- **`403`** — Forbidden: The request is understood, but it has been refused or access is not allowed.
- **`404`** — Not Found: The URI requested is invalid or the resource requested, such as a user, does not exist. Also returned when the requested format is not supported by the requested method.
- **`405`** — Method Not Allowed: The request was made to a resource using an HTTP request method that is not supported.
- **`409`** — Conflict: The request could not be processed because it conflicts with some established rule of the system. For example, a person may not be added to a room more than once.
- **`410`** — Gone: The requested resource is no longer available.
- **`415`** — Unsupported Media Type: The request was made to a resource without specifying a media type or used a media type that is not supported.
- **`423`** — Locked: The requested resource is temporarily unavailable. A Retry-After header may be present that specifies how many seconds you need to wait before attempting the request again.
- **`428`** — Precondition Required: File(s) cannot be scanned for malware and need to be force downloaded.
- **`429`** — Too Many Requests: Too many requests have been sent in a given amount of time and the request has been rate limited. A Retry-After header should be present that specifies how many seconds you need to wait before a successful request can be made.
- **`500`** — Internal Server Error: Something went wrong on the server. If the issue persists, feel free to contact the [Webex Developer Support team](/explore/support).
- **`502`** — Bad Gateway: The server received an invalid response from an upstream server while processing the request. Try again later.
- **`503`** — Service Unavailable: Server is overloaded with requests. Try again later.
- **`504`** — Gateway Timeout: An upstream server failed to respond on time. If your query uses max parameter, please try to reduce it.

---

## 8. Room Tabs

### 8.1 Room Tabs: Create a Room Tab

**Endpoint:** `POST /room/tabs`

Add a tab with a specified URL to a room.

#### Request Body Schema

```json
{
  "type": "object",
  "required": [
    "roomId",
    "contentUrl",
    "displayName"
  ],
  "properties": {
    "roomId": {
      "type": "string",
      "example": "Y2lzY29zcGFyazovL3VzL1JPT00vYmJjZWIxYWQtNDNmMS0zYjU4LTkxNDctZjE0YmIwYzRkMTU0",
      "description": "A unique identifier for the room."
    },
    "contentUrl": {
      "type": "string",
      "example": "https://www.cisco.com",
      "description": "URL of the Room Tab. Must use `https` protocol."
    },
    "displayName": {
      "type": "string",
      "example": "Cisco HomePage",
      "description": "User-friendly name for the room tab."
    }
  }
}
```

#### Responses

- **`200`** — OK
  ```json
  {
    "type": "object",
    "required": [
      "displayName"
    ],
    "properties": {
      "id": {
        "type": "string",
        "example": "Y2lzY29zcGFyazovL3VzL01FTUJFUlNISVAvMGQwYzkxYjYtY2U2MC00NzI1LWI2ZDAtMzQ1NWQ1ZDExZWYzOmNkZTFkZDQwLTJmMGQtMTFlNS1iYTljLTdiNjU1NmQyMjA3Yg",
        "description": "A unique identifier for the Room Tab."
      },
      "roomId": {
        "type": "string",
        "example": "Y2lzY29zcGFyazovL3VzL1JPT00vYmJjZWIxYWQtNDNmMS0zYjU4LTkxNDctZjE0YmIwYzRkMTU0",
        "description": "A unique identifier for the room containing the room tab."
      },
      "roomType": {
        "type": "string",
        "enum": [
          "direct",
          "group"
        ],
        "description": "The room type.\n * `direct` - 1:1 room\n * `group` - group room\n"
      },
      "displayName": {
        "type": "string",
        "example": "Cisco HomePage",
        "description": "User-friendly name for the room tab."
      },
      "contentUrl": {
        "type": "string",
        "example": "https://www.cisco.com",
        "description": "Room Tab's content URL."
      },
      "creatorId": {
        "type": "string",
        "example": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS9mNWIzNjE4Ny1jOGRkLTQ3MjctOGIyZi1mOWM0NDdmMjkwNDY",
        "description": "The person ID of the person who created this Room Tab."
      },
      "created": {
        "type": "string",
        "example": "2015-10-18T14:26:16.203Z",
        "description": "The date and time when the Room Tab was created."
      }
    },
    "$$ref": "#/components/schemas/RoomTab"
  }
  ```
- **`400`** — Bad Request: The request was invalid or cannot be otherwise served. An accompanying error message will explain further.
- **`401`** — Unauthorized: Authentication credentials were missing or incorrect.
- **`403`** — Forbidden: The request is understood, but it has been refused or access is not allowed.
- **`404`** — Not Found: The URI requested is invalid or the resource requested, such as a user, does not exist. Also returned when the requested format is not supported by the requested method.
- **`405`** — Method Not Allowed: The request was made to a resource using an HTTP request method that is not supported.
- **`409`** — Conflict: The request could not be processed because it conflicts with some established rule of the system. For example, a person may not be added to a room more than once.
- **`410`** — Gone: The requested resource is no longer available.
- **`415`** — Unsupported Media Type: The request was made to a resource without specifying a media type or used a media type that is not supported.
- **`423`** — Locked: The requested resource is temporarily unavailable. A Retry-After header may be present that specifies how many seconds you need to wait before attempting the request again.
- **`428`** — Precondition Required: File(s) cannot be scanned for malware and need to be force downloaded.
- **`429`** — Too Many Requests: Too many requests have been sent in a given amount of time and the request has been rate limited. A Retry-After header should be present that specifies how many seconds you need to wait before a successful request can be made.
- **`500`** — Internal Server Error: Something went wrong on the server. If the issue persists, feel free to contact the [Webex Developer Support team](/explore/support).
- **`502`** — Bad Gateway: The server received an invalid response from an upstream server while processing the request. Try again later.
- **`503`** — Service Unavailable: Server is overloaded with requests. Try again later.
- **`504`** — Gateway Timeout: An upstream server failed to respond on time. If your query uses max parameter, please try to reduce it.

---

### 8.2 Room Tabs: Delete a Room Tab

**Endpoint:** `DELETE /room/tabs/{id}`

Deletes a Room Tab with the specified ID.

#### Parameters

| Name | In | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| `id` | `path` | `string` | Yes | The unique identifier for the Room Tab to delete. |

#### Responses

- **`204`** — No Content
- **`400`** — Bad Request: The request was invalid or cannot be otherwise served. An accompanying error message will explain further.
- **`401`** — Unauthorized: Authentication credentials were missing or incorrect.
- **`403`** — Forbidden: The request is understood, but it has been refused or access is not allowed.
- **`404`** — Not Found: The URI requested is invalid or the resource requested, such as a user, does not exist. Also returned when the requested format is not supported by the requested method.
- **`405`** — Method Not Allowed: The request was made to a resource using an HTTP request method that is not supported.
- **`409`** — Conflict: The request could not be processed because it conflicts with some established rule of the system. For example, a person may not be added to a room more than once.
- **`410`** — Gone: The requested resource is no longer available.
- **`415`** — Unsupported Media Type: The request was made to a resource without specifying a media type or used a media type that is not supported.
- **`423`** — Locked: The requested resource is temporarily unavailable. A Retry-After header may be present that specifies how many seconds you need to wait before attempting the request again.
- **`428`** — Precondition Required: File(s) cannot be scanned for malware and need to be force downloaded.
- **`429`** — Too Many Requests: Too many requests have been sent in a given amount of time and the request has been rate limited. A Retry-After header should be present that specifies how many seconds you need to wait before a successful request can be made.
- **`500`** — Internal Server Error: Something went wrong on the server. If the issue persists, feel free to contact the [Webex Developer Support team](/explore/support).
- **`502`** — Bad Gateway: The server received an invalid response from an upstream server while processing the request. Try again later.
- **`503`** — Service Unavailable: Server is overloaded with requests. Try again later.
- **`504`** — Gateway Timeout: An upstream server failed to respond on time. If your query uses max parameter, please try to reduce it.

---

### 8.3 Room Tabs: Get Room Tab Details

**Endpoint:** `GET /room/tabs/{id}`

Get details for a Room Tab with the specified room tab ID.

#### Parameters

| Name | In | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| `id` | `path` | `string` | Yes | The unique identifier for the Room Tab. |

#### Responses

- **`200`** — OK
  ```json
  {
    "type": "object",
    "required": [
      "displayName"
    ],
    "properties": {
      "id": {
        "type": "string",
        "example": "Y2lzY29zcGFyazovL3VzL01FTUJFUlNISVAvMGQwYzkxYjYtY2U2MC00NzI1LWI2ZDAtMzQ1NWQ1ZDExZWYzOmNkZTFkZDQwLTJmMGQtMTFlNS1iYTljLTdiNjU1NmQyMjA3Yg",
        "description": "A unique identifier for the Room Tab."
      },
      "roomId": {
        "type": "string",
        "example": "Y2lzY29zcGFyazovL3VzL1JPT00vYmJjZWIxYWQtNDNmMS0zYjU4LTkxNDctZjE0YmIwYzRkMTU0",
        "description": "A unique identifier for the room containing the room tab."
      },
      "roomType": {
        "type": "string",
        "enum": [
          "direct",
          "group"
        ],
        "description": "The room type.\n * `direct` - 1:1 room\n * `group` - group room\n"
      },
      "displayName": {
        "type": "string",
        "example": "Cisco HomePage",
        "description": "User-friendly name for the room tab."
      },
      "contentUrl": {
        "type": "string",
        "example": "https://www.cisco.com",
        "description": "Room Tab's content URL."
      },
      "creatorId": {
        "type": "string",
        "example": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS9mNWIzNjE4Ny1jOGRkLTQ3MjctOGIyZi1mOWM0NDdmMjkwNDY",
        "description": "The person ID of the person who created this Room Tab."
      },
      "created": {
        "type": "string",
        "example": "2015-10-18T14:26:16.203Z",
        "description": "The date and time when the Room Tab was created."
      }
    },
    "$$ref": "#/components/schemas/RoomTab"
  }
  ```
- **`400`** — Bad Request: The request was invalid or cannot be otherwise served. An accompanying error message will explain further.
- **`401`** — Unauthorized: Authentication credentials were missing or incorrect.
- **`403`** — Forbidden: The request is understood, but it has been refused or access is not allowed.
- **`404`** — Not Found: The URI requested is invalid or the resource requested, such as a user, does not exist. Also returned when the requested format is not supported by the requested method.
- **`405`** — Method Not Allowed: The request was made to a resource using an HTTP request method that is not supported.
- **`409`** — Conflict: The request could not be processed because it conflicts with some established rule of the system. For example, a person may not be added to a room more than once.
- **`410`** — Gone: The requested resource is no longer available.
- **`415`** — Unsupported Media Type: The request was made to a resource without specifying a media type or used a media type that is not supported.
- **`423`** — Locked: The requested resource is temporarily unavailable. A Retry-After header may be present that specifies how many seconds you need to wait before attempting the request again.
- **`428`** — Precondition Required: File(s) cannot be scanned for malware and need to be force downloaded.
- **`429`** — Too Many Requests: Too many requests have been sent in a given amount of time and the request has been rate limited. A Retry-After header should be present that specifies how many seconds you need to wait before a successful request can be made.
- **`500`** — Internal Server Error: Something went wrong on the server. If the issue persists, feel free to contact the [Webex Developer Support team](/explore/support).
- **`502`** — Bad Gateway: The server received an invalid response from an upstream server while processing the request. Try again later.
- **`503`** — Service Unavailable: Server is overloaded with requests. Try again later.
- **`504`** — Gateway Timeout: An upstream server failed to respond on time. If your query uses max parameter, please try to reduce it.

---

### 8.4 Room Tabs: List Room Tabs

**Endpoint:** `GET /room/tabs`

Lists all Room Tabs of a room specified by the `roomId` query parameter.

#### Parameters

| Name | In | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| `roomId` | `query` | `string` | Yes | ID of the room for which to list room tabs. |

#### Responses

- **`200`** — OK
  ```json
  {
    "type": "object",
    "properties": {
      "items": {
        "type": "array",
        "items": {
          "type": "object",
          "required": [
            "displayName"
          ],
          "properties": {
            "id": {
              "type": "string",
              "example": "Y2lzY29zcGFyazovL3VzL01FTUJFUlNISVAvMGQwYzkxYjYtY2U2MC00NzI1LWI2ZDAtMzQ1NWQ1ZDExZWYzOmNkZTFkZDQwLTJmMGQtMTFlNS1iYTljLTdiNjU1NmQyMjA3Yg",
              "description": "A unique identifier for the Room Tab."
            },
            "roomId": {
              "type": "string",
              "example": "Y2lzY29zcGFyazovL3VzL1JPT00vYmJjZWIxYWQtNDNmMS0zYjU4LTkxNDctZjE0YmIwYzRkMTU0",
              "description": "A unique identifier for the room containing the room tab."
            },
            "roomType": {
              "type": "string",
              "enum": [
                "direct",
                "group"
              ],
              "description": "The room type.\n * `direct` - 1:1 room\n * `group` - group room\n"
            },
            "displayName": {
              "type": "string",
              "example": "Cisco HomePage",
              "description": "User-friendly name for the room tab."
            },
            "contentUrl": {
              "type": "string",
              "example": "https://www.cisco.com",
              "description": "Room Tab's content URL."
            },
            "creatorId": {
              "type": "string",
              "example": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS9mNWIzNjE4Ny1jOGRkLTQ3MjctOGIyZi1mOWM0NDdmMjkwNDY",
              "description": "The person ID of the person who created this Room Tab."
            },
            "created": {
              "type": "string",
              "example": "2015-10-18T14:26:16.203Z",
              "description": "The date and time when the Room Tab was created."
            }
          },
          "$$ref": "#/components/schemas/RoomTab"
        }
      }
    },
    "$$ref": "#/components/schemas/RoomTabsCollectionResponse"
  }
  ```
- **`400`** — Bad Request: The request was invalid or cannot be otherwise served. An accompanying error message will explain further.
- **`401`** — Unauthorized: Authentication credentials were missing or incorrect.
- **`403`** — Forbidden: The request is understood, but it has been refused or access is not allowed.
- **`404`** — Not Found: The URI requested is invalid or the resource requested, such as a user, does not exist. Also returned when the requested format is not supported by the requested method.
- **`405`** — Method Not Allowed: The request was made to a resource using an HTTP request method that is not supported.
- **`409`** — Conflict: The request could not be processed because it conflicts with some established rule of the system. For example, a person may not be added to a room more than once.
- **`410`** — Gone: The requested resource is no longer available.
- **`415`** — Unsupported Media Type: The request was made to a resource without specifying a media type or used a media type that is not supported.
- **`423`** — Locked: The requested resource is temporarily unavailable. A Retry-After header may be present that specifies how many seconds you need to wait before attempting the request again.
- **`428`** — Precondition Required: File(s) cannot be scanned for malware and need to be force downloaded.
- **`429`** — Too Many Requests: Too many requests have been sent in a given amount of time and the request has been rate limited. A Retry-After header should be present that specifies how many seconds you need to wait before a successful request can be made.
- **`500`** — Internal Server Error: Something went wrong on the server. If the issue persists, feel free to contact the [Webex Developer Support team](/explore/support).
- **`502`** — Bad Gateway: The server received an invalid response from an upstream server while processing the request. Try again later.
- **`503`** — Service Unavailable: Server is overloaded with requests. Try again later.
- **`504`** — Gateway Timeout: An upstream server failed to respond on time. If your query uses max parameter, please try to reduce it.

---

### 8.5 Room Tabs: Update a Room Tab

**Endpoint:** `PUT /room/tabs/{id}`

Updates the content URL of the specified Room Tab ID.

#### Parameters

| Name | In | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| `id` | `path` | `string` | Yes | The unique identifier for the Room Tab. |

#### Request Body Schema

```json
{
  "type": "object",
  "required": [
    "roomId",
    "contentUrl",
    "displayName"
  ],
  "properties": {
    "roomId": {
      "type": "string",
      "example": "Y2lzY29zcGFyazovL3VzL1JPT00vYmJjZWIxYWQtNDNmMS0zYjU4LTkxNDctZjE0YmIwYzRkMTU0",
      "description": "ID of the room that contains the room tab in question."
    },
    "contentUrl": {
      "type": "string",
      "example": "https://www.cisco.com",
      "description": "Content URL of the Room Tab. URL must use `https` protocol."
    },
    "displayName": {
      "type": "string",
      "example": "Cisco HomePage",
      "description": "User-friendly name for the room tab."
    }
  }
}
```

#### Responses

- **`200`** — OK
  ```json
  {
    "type": "object",
    "required": [
      "displayName"
    ],
    "properties": {
      "id": {
        "type": "string",
        "example": "Y2lzY29zcGFyazovL3VzL01FTUJFUlNISVAvMGQwYzkxYjYtY2U2MC00NzI1LWI2ZDAtMzQ1NWQ1ZDExZWYzOmNkZTFkZDQwLTJmMGQtMTFlNS1iYTljLTdiNjU1NmQyMjA3Yg",
        "description": "A unique identifier for the Room Tab."
      },
      "roomId": {
        "type": "string",
        "example": "Y2lzY29zcGFyazovL3VzL1JPT00vYmJjZWIxYWQtNDNmMS0zYjU4LTkxNDctZjE0YmIwYzRkMTU0",
        "description": "A unique identifier for the room containing the room tab."
      },
      "roomType": {
        "type": "string",
        "enum": [
          "direct",
          "group"
        ],
        "description": "The room type.\n * `direct` - 1:1 room\n * `group` - group room\n"
      },
      "displayName": {
        "type": "string",
        "example": "Cisco HomePage",
        "description": "User-friendly name for the room tab."
      },
      "contentUrl": {
        "type": "string",
        "example": "https://www.cisco.com",
        "description": "Room Tab's content URL."
      },
      "creatorId": {
        "type": "string",
        "example": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS9mNWIzNjE4Ny1jOGRkLTQ3MjctOGIyZi1mOWM0NDdmMjkwNDY",
        "description": "The person ID of the person who created this Room Tab."
      },
      "created": {
        "type": "string",
        "example": "2015-10-18T14:26:16.203Z",
        "description": "The date and time when the Room Tab was created."
      }
    },
    "$$ref": "#/components/schemas/RoomTab"
  }
  ```
- **`400`** — Bad Request: The request was invalid or cannot be otherwise served. An accompanying error message will explain further.
- **`401`** — Unauthorized: Authentication credentials were missing or incorrect.
- **`403`** — Forbidden: The request is understood, but it has been refused or access is not allowed.
- **`404`** — Not Found: The URI requested is invalid or the resource requested, such as a user, does not exist. Also returned when the requested format is not supported by the requested method.
- **`405`** — Method Not Allowed: The request was made to a resource using an HTTP request method that is not supported.
- **`409`** — Conflict: The request could not be processed because it conflicts with some established rule of the system. For example, a person may not be added to a room more than once.
- **`410`** — Gone: The requested resource is no longer available.
- **`415`** — Unsupported Media Type: The request was made to a resource without specifying a media type or used a media type that is not supported.
- **`423`** — Locked: The requested resource is temporarily unavailable. A Retry-After header may be present that specifies how many seconds you need to wait before attempting the request again.
- **`428`** — Precondition Required: File(s) cannot be scanned for malware and need to be force downloaded.
- **`429`** — Too Many Requests: Too many requests have been sent in a given amount of time and the request has been rate limited. A Retry-After header should be present that specifies how many seconds you need to wait before a successful request can be made.
- **`500`** — Internal Server Error: Something went wrong on the server. If the issue persists, feel free to contact the [Webex Developer Support team](/explore/support).
- **`502`** — Bad Gateway: The server received an invalid response from an upstream server while processing the request. Try again later.
- **`503`** — Service Unavailable: Server is overloaded with requests. Try again later.
- **`504`** — Gateway Timeout: An upstream server failed to respond on time. If your query uses max parameter, please try to reduce it.

---

## 9. Rooms

### 9.1 Rooms: Create a Room

**Endpoint:** `POST /rooms`

Creates a room. The authenticated user is automatically added as a member of the room. See the [Memberships API](/docs/api/v1/memberships) to learn how to add more people to the room.

To create a 1:1 room, use the [Create Messages](/docs/api/v1/messages/create-a-message) endpoint to send a message directly to another person by using the `toPersonId` or `toPersonEmail` parameters.

Bots are not able to create and simultaneously classify a room. A bot may update a space classification after a person of the same owning organization joined the space as the first human user.
A space can only be put into announcement mode when it is locked.

#### Request Body Schema

```json
{
  "type": "object",
  "required": [
    "title"
  ],
  "properties": {
    "title": {
      "type": "string",
      "example": "Project Unicorn - Sprint 0",
      "description": "A user-friendly name for the room."
    },
    "teamId": {
      "type": "string",
      "example": "Y2lzY29zcGFyazovL3VzL1JPT00vNjRlNDVhZTAtYzQ2Yi0xMWU1LTlkZjktMGQ0MWUzNDIxOTcz",
      "description": "The ID for the team with which this room is associated."
    },
    "classificationId": {
      "type": "string",
      "example": "Y2lzY29zcGFyazovL3VzL0NMQVNTSUZJQ0FUSU9OL2YyMDUyZTgyLTU0ZjgtMTFlYS1hMmUzLTJlNzI4Y2U4ODEyNQ",
      "description": "The `classificationId` for the room."
    },
    "isLocked": {
      "type": "boolean",
      "description": "Set the space as locked/moderated and the creator becomes a moderator"
    },
    "isPublic": {
      "type": "boolean",
      "description": "The room is public and therefore discoverable within the org. Anyone can find and join that room. When `true` the `description` must be filled in."
    },
    "description": {
      "type": "string",
      "example": "Company Announcements",
      "description": "The description of the space."
    },
    "isAnnouncementOnly": {
      "type": "boolean",
      "description": "Sets the space into announcement Mode."
    }
  }
}
```

#### Responses

- **`200`** — OK
  ```json
  {
    "type": "object",
    "properties": {
      "id": {
        "type": "string",
        "example": "Y2lzY29zcGFyazovL3VzL1JPT00vYmJjZWIxYWQtNDNmMS0zYjU4LTkxNDctZjE0YmIwYzRkMTU0",
        "description": "A unique identifier for the room."
      },
      "title": {
        "type": "string",
        "example": "Project Unicorn - Sprint 0",
        "description": "A user-friendly name for the room."
      },
      "type": {
        "type": "string",
        "enum": [
          "direct",
          "group"
        ],
        "description": "The room type.\n * `direct` - 1:1 room.\n * `group` - Group room.\n"
      },
      "isLocked": {
        "type": "boolean",
        "example": true,
        "description": "Whether the room is moderated (locked) or not."
      },
      "teamId": {
        "type": "string",
        "example": "Y2lzY29zcGFyazovL3VzL1JPT00vNjRlNDVhZTAtYzQ2Yi0xMWU1LTlkZjktMGQ0MWUzNDIxOTcz",
        "description": "The ID for the team with which this room is associated."
      },
      "lastActivity": {
        "type": "string",
        "example": "2016-04-21T19:12:48.920Z",
        "description": "The date and time of the room's last activity."
      },
      "creatorId": {
        "type": "string",
        "example": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS9mNWIzNjE4Ny1jOGRkLTQ3MjctOGIyZi1mOWM0NDdmMjkwNDY",
        "description": "The ID of the person who created this room."
      },
      "created": {
        "type": "string",
        "example": "2016-04-21T19:01:55.966Z",
        "description": "The date and time the room was created."
      },
      "ownerId": {
        "type": "string",
        "example": "Y2lzY29zcGFyazovL3VzL09SR0FOSVpBVElPTi85NmFiYzJhYS0zZGNjLTExZTUtYTE1Mi1mZTM0ODE5Y2RjOWE",
        "description": "The ID of the organization which owns this room. See [Webex Data](/docs/api/guides/compliance#webex-teams-data) in the [Compliance Guide](/docs/api/guides/compliance) for more information."
      },
      "classificationId": {
        "type": "string",
        "example": "Y2lzY29zcGFyazovL3VzL0NMQVNTSUZJQ0FUSU9OL2YyMDUyZTgyLTU0ZjgtMTFlYS1hMmUzLTJlNzI4Y2U4ODEyNQ",
        "description": "Space classification ID represents the space's current classification.  It can be attached during space creation time, and can be modified at the request of an authorized user."
      },
      "isAnnouncementOnly": {
        "type": "boolean",
        "description": "Indicates when a space is in Announcement Mode where only moderators can post messages"
      },
      "isReadOnly": {
        "type": "boolean",
        "description": "A compliance officer can set a direct room as read-only, which will disallow any new information exchanges in this space, while maintaing historical data."
      },
      "isPublic": {
        "type": "boolean",
        "example": true,
        "description": "The room is public and therefore discoverable within the org. Anyone can find and join that room."
      },
      "madePublic": {
        "type": "string",
        "example": "2022-10-10T17:24:19.388Z",
        "description": "Date and time when the room was made public."
      },
      "description": {
        "type": "string",
        "example": "Company Announcements",
        "description": "The description of the space."
      }
    },
    "$$ref": "#/components/schemas/Room"
  }
  ```
- **`400`** — Bad Request: The request was invalid or cannot be otherwise served. An accompanying error message will explain further.
- **`401`** — Unauthorized: Authentication credentials were missing or incorrect.
- **`403`** — Forbidden: The request is understood, but it has been refused or access is not allowed.
- **`404`** — Not Found: The URI requested is invalid or the resource requested, such as a user, does not exist. Also returned when the requested format is not supported by the requested method.
- **`405`** — Method Not Allowed: The request was made to a resource using an HTTP request method that is not supported.
- **`409`** — Conflict: The request could not be processed because it conflicts with some established rule of the system. For example, a person may not be added to a room more than once.
- **`410`** — Gone: The requested resource is no longer available.
- **`415`** — Unsupported Media Type: The request was made to a resource without specifying a media type or used a media type that is not supported.
- **`423`** — Locked: The requested resource is temporarily unavailable. A Retry-After header may be present that specifies how many seconds you need to wait before attempting the request again.
- **`428`** — Precondition Required: File(s) cannot be scanned for malware and need to be force downloaded.
- **`429`** — Too Many Requests: Too many requests have been sent in a given amount of time and the request has been rate limited. A Retry-After header should be present that specifies how many seconds you need to wait before a successful request can be made.
- **`500`** — Internal Server Error: Something went wrong on the server. If the issue persists, feel free to contact the [Webex Developer Support team](/explore/support).
- **`502`** — Bad Gateway: The server received an invalid response from an upstream server while processing the request. Try again later.
- **`503`** — Service Unavailable: Server is overloaded with requests. Try again later.
- **`504`** — Gateway Timeout: An upstream server failed to respond on time. If your query uses max parameter, please try to reduce it.

---

### 9.2 Rooms: Delete a Room

**Endpoint:** `DELETE /rooms/{roomId}`

Deletes a room, by ID. Deleted rooms cannot be recovered.
As a security measure to prevent accidental deletion, when a non moderator deletes the room they are removed from the room instead.

Deleting a room that is part of a team will archive the room instead.

A Compliance Officer has no special privileges, i.e. they cannot delete rooms they are not part of.

Specify the room ID in the `roomId` parameter in the URI.

#### Parameters

| Name | In | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| `roomId` | `path` | `string` | Yes | The unique identifier for the room. |

#### Responses

- **`204`** — No Content
- **`400`** — Bad Request: The request was invalid or cannot be otherwise served. An accompanying error message will explain further.
- **`401`** — Unauthorized: Authentication credentials were missing or incorrect.
- **`403`** — Forbidden: The request is understood, but it has been refused or access is not allowed.
- **`404`** — Not Found: The URI requested is invalid or the resource requested, such as a user, does not exist. Also returned when the requested format is not supported by the requested method.
- **`405`** — Method Not Allowed: The request was made to a resource using an HTTP request method that is not supported.
- **`409`** — Conflict: The request could not be processed because it conflicts with some established rule of the system. For example, a person may not be added to a room more than once.
- **`410`** — Gone: The requested resource is no longer available.
- **`415`** — Unsupported Media Type: The request was made to a resource without specifying a media type or used a media type that is not supported.
- **`423`** — Locked: The requested resource is temporarily unavailable. A Retry-After header may be present that specifies how many seconds you need to wait before attempting the request again.
- **`428`** — Precondition Required: File(s) cannot be scanned for malware and need to be force downloaded.
- **`429`** — Too Many Requests: Too many requests have been sent in a given amount of time and the request has been rate limited. A Retry-After header should be present that specifies how many seconds you need to wait before a successful request can be made.
- **`500`** — Internal Server Error: Something went wrong on the server. If the issue persists, feel free to contact the [Webex Developer Support team](/explore/support).
- **`502`** — Bad Gateway: The server received an invalid response from an upstream server while processing the request. Try again later.
- **`503`** — Service Unavailable: Server is overloaded with requests. Try again later.
- **`504`** — Gateway Timeout: An upstream server failed to respond on time. If your query uses max parameter, please try to reduce it.

---

### 9.3 Rooms: Get Room Details

**Endpoint:** `GET /rooms/{roomId}`

Shows details for a room, by ID.

The `title` of the room for 1:1 rooms will be the display name of the other person. When a Compliance Officer lists 1:1 rooms, the "other" person cannot be determined. This means that the room's title may not be filled in and instead shows "Empty Title". Please use the [memberships API](https://developer.webex.com/docs/api/v1/memberships) to list the other person in the space.

Specify the room ID in the `roomId` parameter in the URI.

#### Parameters

| Name | In | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| `roomId` | `path` | `string` | Yes | The unique identifier for the room. |

#### Responses

- **`200`** — OK
  ```json
  {
    "type": "object",
    "properties": {
      "id": {
        "type": "string",
        "example": "Y2lzY29zcGFyazovL3VzL1JPT00vYmJjZWIxYWQtNDNmMS0zYjU4LTkxNDctZjE0YmIwYzRkMTU0",
        "description": "A unique identifier for the room."
      },
      "title": {
        "type": "string",
        "example": "Project Unicorn - Sprint 0",
        "description": "A user-friendly name for the room."
      },
      "type": {
        "type": "string",
        "enum": [
          "direct",
          "group"
        ],
        "description": "The room type.\n * `direct` - 1:1 room.\n * `group` - Group room.\n"
      },
      "isLocked": {
        "type": "boolean",
        "example": true,
        "description": "Whether the room is moderated (locked) or not."
      },
      "teamId": {
        "type": "string",
        "example": "Y2lzY29zcGFyazovL3VzL1JPT00vNjRlNDVhZTAtYzQ2Yi0xMWU1LTlkZjktMGQ0MWUzNDIxOTcz",
        "description": "The ID for the team with which this room is associated."
      },
      "lastActivity": {
        "type": "string",
        "example": "2016-04-21T19:12:48.920Z",
        "description": "The date and time of the room's last activity."
      },
      "creatorId": {
        "type": "string",
        "example": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS9mNWIzNjE4Ny1jOGRkLTQ3MjctOGIyZi1mOWM0NDdmMjkwNDY",
        "description": "The ID of the person who created this room."
      },
      "created": {
        "type": "string",
        "example": "2016-04-21T19:01:55.966Z",
        "description": "The date and time the room was created."
      },
      "ownerId": {
        "type": "string",
        "example": "Y2lzY29zcGFyazovL3VzL09SR0FOSVpBVElPTi85NmFiYzJhYS0zZGNjLTExZTUtYTE1Mi1mZTM0ODE5Y2RjOWE",
        "description": "The ID of the organization which owns this room. See [Webex Data](/docs/api/guides/compliance#webex-teams-data) in the [Compliance Guide](/docs/api/guides/compliance) for more information."
      },
      "classificationId": {
        "type": "string",
        "example": "Y2lzY29zcGFyazovL3VzL0NMQVNTSUZJQ0FUSU9OL2YyMDUyZTgyLTU0ZjgtMTFlYS1hMmUzLTJlNzI4Y2U4ODEyNQ",
        "description": "Space classification ID represents the space's current classification.  It can be attached during space creation time, and can be modified at the request of an authorized user."
      },
      "isAnnouncementOnly": {
        "type": "boolean",
        "description": "Indicates when a space is in Announcement Mode where only moderators can post messages"
      },
      "isReadOnly": {
        "type": "boolean",
        "description": "A compliance officer can set a direct room as read-only, which will disallow any new information exchanges in this space, while maintaing historical data."
      },
      "isPublic": {
        "type": "boolean",
        "example": true,
        "description": "The room is public and therefore discoverable within the org. Anyone can find and join that room."
      },
      "madePublic": {
        "type": "string",
        "example": "2022-10-10T17:24:19.388Z",
        "description": "Date and time when the room was made public."
      },
      "description": {
        "type": "string",
        "example": "Company Announcements",
        "description": "The description of the space."
      }
    },
    "$$ref": "#/components/schemas/Room"
  }
  ```
- **`400`** — Bad Request: The request was invalid or cannot be otherwise served. An accompanying error message will explain further.
- **`401`** — Unauthorized: Authentication credentials were missing or incorrect.
- **`403`** — Forbidden: The request is understood, but it has been refused or access is not allowed.
- **`404`** — Not Found: The URI requested is invalid or the resource requested, such as a user, does not exist. Also returned when the requested format is not supported by the requested method.
- **`405`** — Method Not Allowed: The request was made to a resource using an HTTP request method that is not supported.
- **`409`** — Conflict: The request could not be processed because it conflicts with some established rule of the system. For example, a person may not be added to a room more than once.
- **`410`** — Gone: The requested resource is no longer available.
- **`415`** — Unsupported Media Type: The request was made to a resource without specifying a media type or used a media type that is not supported.
- **`423`** — Locked: The requested resource is temporarily unavailable. A Retry-After header may be present that specifies how many seconds you need to wait before attempting the request again.
- **`428`** — Precondition Required: File(s) cannot be scanned for malware and need to be force downloaded.
- **`429`** — Too Many Requests: Too many requests have been sent in a given amount of time and the request has been rate limited. A Retry-After header should be present that specifies how many seconds you need to wait before a successful request can be made.
- **`500`** — Internal Server Error: Something went wrong on the server. If the issue persists, feel free to contact the [Webex Developer Support team](/explore/support).
- **`502`** — Bad Gateway: The server received an invalid response from an upstream server while processing the request. Try again later.
- **`503`** — Service Unavailable: Server is overloaded with requests. Try again later.
- **`504`** — Gateway Timeout: An upstream server failed to respond on time. If your query uses max parameter, please try to reduce it.

---

### 9.4 Rooms: Get Room Meeting Details

**Endpoint:** `GET /rooms/{roomId}/meetingInfo`

<div>
<callout type="warning">
The meetingInfo API is deprecated and will be EOL on Jan 31, 2025. Meetings in the WSMP must be scheduled and licensed via the meetings backend.
The [Create a Meeting](/docs/api/v1/meetings/create-a-meeting) endpoint will provide the SIP address for the meeting to call.
</callout>
</div>

Shows Webex meeting details for a room such as the SIP address, meeting URL, toll-free and toll dial-in numbers.

Specify the room ID in the `roomId` parameter in the URI.

#### Parameters

| Name | In | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| `roomId` | `path` | `string` | Yes | The unique identifier for the room. |

#### Responses

- **`200`** — OK
  ```json
  {
    "type": "object",
    "properties": {
      "roomId": {
        "type": "string",
        "example": "Y2lzY29zcGFyazovL3VzL1JPT00vYmJjZWIxYWQtNDNmMS0zYjU4LTkxNDctZjE0YmIwYzRkMTU0",
        "description": "A unique identifier for the room."
      },
      "meetingLink": {
        "type": "string",
        "example": "https://cisco.webex.com/m/37a7d3a8-6563-487f-9577-cd029101c087",
        "description": "The Webex meeting URL for the room."
      },
      "sipAddress": {
        "type": "string",
        "example": "201632887@cisco.webex.com",
        "description": "The SIP address for the room."
      },
      "meetingNumber": {
        "type": "string",
        "example": "201632887",
        "description": "The Webex meeting number for the room."
      },
      "meetingId": {
        "type": "string",
        "example": "c1c30b52501b4d34aa75a57bdb867853",
        "description": "The Webex meeting ID for the room."
      },
      "callInTollFreeNumber": {
        "type": "string",
        "example": "+1-866-432-9903",
        "description": "The toll-free PSTN number for the room."
      },
      "callInTollNumber": {
        "type": "string",
        "example": "+1-408-525-6800",
        "description": "The toll (local) PSTN number for the room."
      }
    },
    "$$ref": "#/components/schemas/RoomMeetingDetails"
  }
  ```
- **`400`** — Bad Request: The request was invalid or cannot be otherwise served. An accompanying error message will explain further.
- **`401`** — Unauthorized: Authentication credentials were missing or incorrect.
- **`403`** — Forbidden: The request is understood, but it has been refused or access is not allowed.
- **`404`** — Not Found: The URI requested is invalid or the resource requested, such as a user, does not exist. Also returned when the requested format is not supported by the requested method.
- **`405`** — Method Not Allowed: The request was made to a resource using an HTTP request method that is not supported.
- **`409`** — Conflict: The request could not be processed because it conflicts with some established rule of the system. For example, a person may not be added to a room more than once.
- **`410`** — Gone: The requested resource is no longer available.
- **`415`** — Unsupported Media Type: The request was made to a resource without specifying a media type or used a media type that is not supported.
- **`423`** — Locked: The requested resource is temporarily unavailable. A Retry-After header may be present that specifies how many seconds you need to wait before attempting the request again.
- **`428`** — Precondition Required: File(s) cannot be scanned for malware and need to be force downloaded.
- **`429`** — Too Many Requests: Too many requests have been sent in a given amount of time and the request has been rate limited. A Retry-After header should be present that specifies how many seconds you need to wait before a successful request can be made.
- **`500`** — Internal Server Error: Something went wrong on the server. If the issue persists, feel free to contact the [Webex Developer Support team](/explore/support).
- **`502`** — Bad Gateway: The server received an invalid response from an upstream server while processing the request. Try again later.
- **`503`** — Service Unavailable: Server is overloaded with requests. Try again later.
- **`504`** — Gateway Timeout: An upstream server failed to respond on time. If your query uses max parameter, please try to reduce it.

---

### 9.5 Rooms: List Rooms

**Endpoint:** `GET /rooms`

List rooms to which the authenticated user belongs to.

The `title` of the room for 1:1 rooms will be the display name of the other person. Please use the [memberships API](https://developer.webex.com/docs/api/v1/memberships) to list the people in the space.

Long result sets will be split into [pages](/docs/basics#pagination).

Known Limitations:
The underlying database does not support natural sorting by `lastactivity` and will only sort on limited set of results, which are pulled from the database in order of `roomId`. For users or bots in more than 3000 spaces this can result in anomalies such as spaces that have had recent activity not being returned in the results when sorting by `lastacivity`.

#### Parameters

| Name | In | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| `teamId` | `query` | `string` | No | List rooms associated with a team, by ID. Cannot be set in combination with `orgPublicSpaces`. |
| `type` | `query` | `string` | No | List rooms by type. Cannot be set in combination with `orgPublicSpaces`. |
| `orgPublicSpaces` | `query` | `boolean` | No | Shows the org's public spaces joined and unjoined. When set the result list is sorted by the `madePublic` timestamp. |
| `from` | `query` | `string` | No | Filters rooms, that were made public after this time. See `madePublic` timestamp |
| `to` | `query` | `string` | No | Filters rooms, that were made public before this time. See `maePublic` timestamp |
| `sortBy` | `query` | `string` | No | Sort results. Cannot be set in combination with `orgPublicSpaces`. |
| `max` | `query` | `number` | No | Limit the maximum number of rooms in the response. Value must be between 1 and 1000, inclusive. |

#### Responses

- **`200`** — OK
  ```json
  {
    "type": "object",
    "properties": {
      "items": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "id": {
              "type": "string",
              "example": "Y2lzY29zcGFyazovL3VzL1JPT00vYmJjZWIxYWQtNDNmMS0zYjU4LTkxNDctZjE0YmIwYzRkMTU0",
              "description": "A unique identifier for the room."
            },
            "title": {
              "type": "string",
              "example": "Project Unicorn - Sprint 0",
              "description": "A user-friendly name for the room."
            },
            "type": {
              "type": "string",
              "enum": [
                "direct",
                "group"
              ],
              "description": "The room type.\n * `direct` - 1:1 room.\n * `group` - Group room.\n"
            },
            "isLocked": {
              "type": "boolean",
              "example": true,
              "description": "Whether the room is moderated (locked) or not."
            },
            "teamId": {
              "type": "string",
              "example": "Y2lzY29zcGFyazovL3VzL1JPT00vNjRlNDVhZTAtYzQ2Yi0xMWU1LTlkZjktMGQ0MWUzNDIxOTcz",
              "description": "The ID for the team with which this room is associated."
            },
            "lastActivity": {
              "type": "string",
              "example": "2016-04-21T19:12:48.920Z",
              "description": "The date and time of the room's last activity."
            },
            "creatorId": {
              "type": "string",
              "example": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS9mNWIzNjE4Ny1jOGRkLTQ3MjctOGIyZi1mOWM0NDdmMjkwNDY",
              "description": "The ID of the person who created this room."
            },
            "created": {
              "type": "string",
              "example": "2016-04-21T19:01:55.966Z",
              "description": "The date and time the room was created."
            },
            "ownerId": {
              "type": "string",
              "example": "Y2lzY29zcGFyazovL3VzL09SR0FOSVpBVElPTi85NmFiYzJhYS0zZGNjLTExZTUtYTE1Mi1mZTM0ODE5Y2RjOWE",
              "description": "The ID of the organization which owns this room. See [Webex Data](/docs/api/guides/compliance#webex-teams-data) in the [Compliance Guide](/docs/api/guides/compliance) for more information."
            },
            "classificationId": {
              "type": "string",
              "example": "Y2lzY29zcGFyazovL3VzL0NMQVNTSUZJQ0FUSU9OL2YyMDUyZTgyLTU0ZjgtMTFlYS1hMmUzLTJlNzI4Y2U4ODEyNQ",
              "description": "Space classification ID represents the space's current classification.  It can be attached during space creation time, and can be modified at the request of an authorized user."
            },
            "isAnnouncementOnly": {
              "type": "boolean",
              "description": "Indicates when a space is in Announcement Mode where only moderators can post messages"
            },
            "isReadOnly": {
              "type": "boolean",
              "description": "A compliance officer can set a direct room as read-only, which will disallow any new information exchanges in this space, while maintaing historical data."
            },
            "isPublic": {
              "type": "boolean",
              "example": true,
              "description": "The room is public and therefore discoverable within the org. Anyone can find and join that room."
            },
            "madePublic": {
              "type": "string",
              "example": "2022-10-10T17:24:19.388Z",
              "description": "Date and time when the room was made public."
            },
            "description": {
              "type": "string",
              "example": "Company Announcements",
              "description": "The description of the space."
            }
          },
          "$$ref": "#/components/schemas/Room"
        }
      }
    },
    "$$ref": "#/components/schemas/RoomCollectionResponse"
  }
  ```
- **`400`** — Bad Request: The request was invalid or cannot be otherwise served. An accompanying error message will explain further.
- **`401`** — Unauthorized: Authentication credentials were missing or incorrect.
- **`403`** — Forbidden: The request is understood, but it has been refused or access is not allowed.
- **`404`** — Not Found: The URI requested is invalid or the resource requested, such as a user, does not exist. Also returned when the requested format is not supported by the requested method.
- **`405`** — Method Not Allowed: The request was made to a resource using an HTTP request method that is not supported.
- **`409`** — Conflict: The request could not be processed because it conflicts with some established rule of the system. For example, a person may not be added to a room more than once.
- **`410`** — Gone: The requested resource is no longer available.
- **`415`** — Unsupported Media Type: The request was made to a resource without specifying a media type or used a media type that is not supported.
- **`423`** — Locked: The requested resource is temporarily unavailable. A Retry-After header may be present that specifies how many seconds you need to wait before attempting the request again.
- **`428`** — Precondition Required: File(s) cannot be scanned for malware and need to be force downloaded.
- **`429`** — Too Many Requests: Too many requests have been sent in a given amount of time and the request has been rate limited. A Retry-After header should be present that specifies how many seconds you need to wait before a successful request can be made.
- **`500`** — Internal Server Error: Something went wrong on the server. If the issue persists, feel free to contact the [Webex Developer Support team](/explore/support).
- **`502`** — Bad Gateway: The server received an invalid response from an upstream server while processing the request. Try again later.
- **`503`** — Service Unavailable: Server is overloaded with requests. Try again later.
- **`504`** — Gateway Timeout: An upstream server failed to respond on time. If your query uses max parameter, please try to reduce it.

---

### 9.6 Rooms: Update a Room

**Endpoint:** `PUT /rooms/{roomId}`

Updates details for a room, by ID.

Specify the room ID in the `roomId` parameter in the URI.
A space can only be put into announcement mode when it is locked.
Any space participant or compliance officer can convert a space from public to private. Only a compliance officer can convert a space from private to public and only if the space is classified with the lowest category (usually `public`), and the space has a description.
To remove a `description` please use a space character ` ` by itself.

<div><Callout type="info">When using this method for moving a space under a team, ensure that all moderators in the space are also team members. If a moderator is not part of the team, demote or remove them as a moderator. Alternatively, add the non-team moderators to the team. This ensures compliance with the requirement that all space moderators must be team members for successful operation execution.
</Callout></div>

<div><Callout type="info">A Compliance Officer who is not a member of a space can only update the `classificationId`, `isAnnouncementOnly`, `description`, and `isPublic` fields.
</Callout></div>

#### Parameters

| Name | In | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| `roomId` | `path` | `string` | Yes | The unique identifier for the room. |

#### Request Body Schema

```json
{
  "type": "object",
  "required": [
    "title"
  ],
  "properties": {
    "title": {
      "type": "string",
      "example": "Project Unicorn - Sprint 0",
      "description": "A user-friendly name for the room."
    },
    "classificationId": {
      "type": "string",
      "example": "Y2lzY29zcGFyazovL3VzL0NMQVNTSUZJQ0FUSU9OL2YyMDUyZTgyLTU0ZjgtMTFlYS1hMmUzLTJlNzI4Y2U4ODEyNQ",
      "description": "The classificationId for the room."
    },
    "teamId": {
      "type": "string",
      "example": "Y2lzY29zcGFyazovL3VzL1RFQU0vZWUwMWIxMzAtMjJlYi0xMWVjLTg5MTktMGY0NjdjMGNlZmFk",
      "description": "The teamId to which this space should be assigned. Only unowned spaces can be assigned to a team. Assignment between teams is unsupported."
    },
    "isLocked": {
      "type": "boolean",
      "description": "Set the space as locked/moderated and the creator becomes a moderator"
    },
    "isPublic": {
      "type": "boolean",
      "description": "The room is public and therefore discoverable within the org. Anyone can find and join that room. When `true` the `description` must be filled in."
    },
    "description": {
      "type": "string",
      "example": "Company Announcements",
      "description": "The description of the space."
    },
    "isAnnouncementOnly": {
      "type": "boolean",
      "description": "Sets the space into Announcement Mode or clears the Anouncement Mode (`false`)"
    },
    "isReadOnly": {
      "type": "boolean",
      "description": "A compliance officer can set a direct room as read-only, which will disallow any new information exchanges in this space, while maintaing historical data."
    }
  }
}
```

#### Responses

- **`200`** — OK
  ```json
  {
    "type": "object",
    "properties": {
      "id": {
        "type": "string",
        "example": "Y2lzY29zcGFyazovL3VzL1JPT00vYmJjZWIxYWQtNDNmMS0zYjU4LTkxNDctZjE0YmIwYzRkMTU0",
        "description": "A unique identifier for the room."
      },
      "title": {
        "type": "string",
        "example": "Project Unicorn - Sprint 0",
        "description": "A user-friendly name for the room."
      },
      "type": {
        "type": "string",
        "enum": [
          "direct",
          "group"
        ],
        "description": "The room type.\n * `direct` - 1:1 room.\n * `group` - Group room.\n"
      },
      "isLocked": {
        "type": "boolean",
        "example": true,
        "description": "Whether the room is moderated (locked) or not."
      },
      "teamId": {
        "type": "string",
        "example": "Y2lzY29zcGFyazovL3VzL1JPT00vNjRlNDVhZTAtYzQ2Yi0xMWU1LTlkZjktMGQ0MWUzNDIxOTcz",
        "description": "The ID for the team with which this room is associated."
      },
      "lastActivity": {
        "type": "string",
        "example": "2016-04-21T19:12:48.920Z",
        "description": "The date and time of the room's last activity."
      },
      "creatorId": {
        "type": "string",
        "example": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS9mNWIzNjE4Ny1jOGRkLTQ3MjctOGIyZi1mOWM0NDdmMjkwNDY",
        "description": "The ID of the person who created this room."
      },
      "created": {
        "type": "string",
        "example": "2016-04-21T19:01:55.966Z",
        "description": "The date and time the room was created."
      },
      "ownerId": {
        "type": "string",
        "example": "Y2lzY29zcGFyazovL3VzL09SR0FOSVpBVElPTi85NmFiYzJhYS0zZGNjLTExZTUtYTE1Mi1mZTM0ODE5Y2RjOWE",
        "description": "The ID of the organization which owns this room. See [Webex Data](/docs/api/guides/compliance#webex-teams-data) in the [Compliance Guide](/docs/api/guides/compliance) for more information."
      },
      "classificationId": {
        "type": "string",
        "example": "Y2lzY29zcGFyazovL3VzL0NMQVNTSUZJQ0FUSU9OL2YyMDUyZTgyLTU0ZjgtMTFlYS1hMmUzLTJlNzI4Y2U4ODEyNQ",
        "description": "Space classification ID represents the space's current classification.  It can be attached during space creation time, and can be modified at the request of an authorized user."
      },
      "isAnnouncementOnly": {
        "type": "boolean",
        "description": "Indicates when a space is in Announcement Mode where only moderators can post messages"
      },
      "isReadOnly": {
        "type": "boolean",
        "description": "A compliance officer can set a direct room as read-only, which will disallow any new information exchanges in this space, while maintaing historical data."
      },
      "isPublic": {
        "type": "boolean",
        "example": true,
        "description": "The room is public and therefore discoverable within the org. Anyone can find and join that room."
      },
      "madePublic": {
        "type": "string",
        "example": "2022-10-10T17:24:19.388Z",
        "description": "Date and time when the room was made public."
      },
      "description": {
        "type": "string",
        "example": "Company Announcements",
        "description": "The description of the space."
      }
    },
    "$$ref": "#/components/schemas/Room"
  }
  ```
- **`400`** — Bad Request: The request was invalid or cannot be otherwise served. An accompanying error message will explain further.
- **`401`** — Unauthorized: Authentication credentials were missing or incorrect.
- **`403`** — Forbidden: The request is understood, but it has been refused or access is not allowed.
- **`404`** — Not Found: The URI requested is invalid or the resource requested, such as a user, does not exist. Also returned when the requested format is not supported by the requested method.
- **`405`** — Method Not Allowed: The request was made to a resource using an HTTP request method that is not supported.
- **`409`** — Conflict: The request could not be processed because it conflicts with some established rule of the system. For example, a person may not be added to a room more than once.
- **`410`** — Gone: The requested resource is no longer available.
- **`415`** — Unsupported Media Type: The request was made to a resource without specifying a media type or used a media type that is not supported.
- **`423`** — Locked: The requested resource is temporarily unavailable. A Retry-After header may be present that specifies how many seconds you need to wait before attempting the request again.
- **`428`** — Precondition Required: File(s) cannot be scanned for malware and need to be force downloaded.
- **`429`** — Too Many Requests: Too many requests have been sent in a given amount of time and the request has been rate limited. A Retry-After header should be present that specifies how many seconds you need to wait before a successful request can be made.
- **`500`** — Internal Server Error: Something went wrong on the server. If the issue persists, feel free to contact the [Webex Developer Support team](/explore/support).
- **`502`** — Bad Gateway: The server received an invalid response from an upstream server while processing the request. Try again later.
- **`503`** — Service Unavailable: Server is overloaded with requests. Try again later.
- **`504`** — Gateway Timeout: An upstream server failed to respond on time. If your query uses max parameter, please try to reduce it.

---

## 10. Team Memberships

### 10.1 Team Memberships: Create a Team Membership

**Endpoint:** `POST /team/memberships`

Add someone to a team by Person ID or email address, optionally making them a moderator.

#### Request Body Schema

```json
{
  "type": "object",
  "required": [
    "teamId"
  ],
  "properties": {
    "teamId": {
      "type": "string",
      "example": "Y2lzY29zcGFyazovL3VzL1RFQU0vMTNlMThmNDAtNDJmYy0xMWU2LWE5ZDgtMjExYTBkYzc5NzY5",
      "description": "The team ID."
    },
    "personId": {
      "type": "string",
      "example": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS9mNWIzNjE4Ny1jOGRkLTQ3MjctOGIyZi1mOWM0NDdmMjkwNDY",
      "description": "The person ID."
    },
    "personEmail": {
      "type": "string",
      "example": "john.andersen@example.com",
      "description": "The email address of the person."
    },
    "isModerator": {
      "type": "boolean",
      "example": true,
      "description": "Whether or not the participant is a team moderator."
    }
  }
}
```

#### Responses

- **`200`** — OK
  ```json
  {
    "type": "object",
    "properties": {
      "id": {
        "type": "string",
        "example": "Y2lzY29zcGFyazovL3VzL1RFQU1fTUVNQkVSU0hJUC8wZmNmYTJiOC1hZGNjLTQ1ZWEtYTc4Mi1lNDYwNTkyZjgxZWY6MTNlMThmNDAtNDJmYy0xMWU2LWE5ZDgtMjExYTBkYzc5NzY5",
        "description": "A unique identifier for the team membership."
      },
      "teamId": {
        "type": "string",
        "example": "Y2lzY29zcGFyazovL3VzL1RFQU0vMTNlMThmNDAtNDJmYy0xMWU2LWE5ZDgtMjExYTBkYzc5NzY5",
        "description": "The team ID."
      },
      "personId": {
        "type": "string",
        "example": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS9mNWIzNjE4Ny1jOGRkLTQ3MjctOGIyZi1mOWM0NDdmMjkwNDY",
        "description": "The person ID."
      },
      "personEmail": {
        "type": "string",
        "example": "john.andersen@example.com",
        "description": "The email address of the person."
      },
      "personDisplayName": {
        "type": "string",
        "example": "John Andersen",
        "description": "The display name of the person."
      },
      "personOrgId": {
        "type": "string",
        "example": "Y2lzY29zcGFyazovL3VzL09SR0FOSVpBVElPTi85NmFiYzJhYS0zZGNjLTExZTUtYTE1Mi1mZTM0ODE5Y2RjOWE",
        "description": "The organization ID of the person."
      },
      "isModerator": {
        "type": "boolean",
        "example": true,
        "description": "Whether or not the participant is a team moderator."
      },
      "created": {
        "type": "string",
        "example": "2015-10-18T14:26:16.203Z",
        "description": "The date and time when the team membership was created."
      }
    },
    "$$ref": "#/components/schemas/TeamMembership"
  }
  ```
- **`400`** — Bad Request: The request was invalid or cannot be otherwise served. An accompanying error message will explain further.
- **`401`** — Unauthorized: Authentication credentials were missing or incorrect.
- **`403`** — Forbidden: The request is understood, but it has been refused or access is not allowed.
- **`404`** — Not Found: The URI requested is invalid or the resource requested, such as a user, does not exist. Also returned when the requested format is not supported by the requested method.
- **`405`** — Method Not Allowed: The request was made to a resource using an HTTP request method that is not supported.
- **`409`** — Conflict: The request could not be processed because it conflicts with some established rule of the system. For example, a person may not be added to a room more than once.
- **`410`** — Gone: The requested resource is no longer available.
- **`415`** — Unsupported Media Type: The request was made to a resource without specifying a media type or used a media type that is not supported.
- **`423`** — Locked: The requested resource is temporarily unavailable. A Retry-After header may be present that specifies how many seconds you need to wait before attempting the request again.
- **`428`** — Precondition Required: File(s) cannot be scanned for malware and need to be force downloaded.
- **`429`** — Too Many Requests: Too many requests have been sent in a given amount of time and the request has been rate limited. A Retry-After header should be present that specifies how many seconds you need to wait before a successful request can be made.
- **`500`** — Internal Server Error: Something went wrong on the server. If the issue persists, feel free to contact the [Webex Developer Support team](/explore/support).
- **`502`** — Bad Gateway: The server received an invalid response from an upstream server while processing the request. Try again later.
- **`503`** — Service Unavailable: Server is overloaded with requests. Try again later.
- **`504`** — Gateway Timeout: An upstream server failed to respond on time. If your query uses max parameter, please try to reduce it.

---

### 10.2 Team Memberships: Delete a Team Membership

**Endpoint:** `DELETE /team/memberships/{membershipId}`

Deletes a team membership, by ID.

Specify the team membership ID in the `membershipId` URI parameter.

The team membership for the last moderator of a team may not be deleted; [promote another user](/docs/api/v1/team-memberships/update-a-team-membership) to team moderator first.

#### Parameters

| Name | In | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| `membershipId` | `path` | `string` | Yes | The unique identifier for the team membership. |

#### Responses

- **`204`** — No Content
- **`400`** — Bad Request: The request was invalid or cannot be otherwise served. An accompanying error message will explain further.
- **`401`** — Unauthorized: Authentication credentials were missing or incorrect.
- **`403`** — Forbidden: The request is understood, but it has been refused or access is not allowed.
- **`404`** — Not Found: The URI requested is invalid or the resource requested, such as a user, does not exist. Also returned when the requested format is not supported by the requested method.
- **`405`** — Method Not Allowed: The request was made to a resource using an HTTP request method that is not supported.
- **`409`** — Conflict: The request could not be processed because it conflicts with some established rule of the system. For example, a person may not be added to a room more than once.
- **`410`** — Gone: The requested resource is no longer available.
- **`415`** — Unsupported Media Type: The request was made to a resource without specifying a media type or used a media type that is not supported.
- **`423`** — Locked: The requested resource is temporarily unavailable. A Retry-After header may be present that specifies how many seconds you need to wait before attempting the request again.
- **`428`** — Precondition Required: File(s) cannot be scanned for malware and need to be force downloaded.
- **`429`** — Too Many Requests: Too many requests have been sent in a given amount of time and the request has been rate limited. A Retry-After header should be present that specifies how many seconds you need to wait before a successful request can be made.
- **`500`** — Internal Server Error: Something went wrong on the server. If the issue persists, feel free to contact the [Webex Developer Support team](/explore/support).
- **`502`** — Bad Gateway: The server received an invalid response from an upstream server while processing the request. Try again later.
- **`503`** — Service Unavailable: Server is overloaded with requests. Try again later.
- **`504`** — Gateway Timeout: An upstream server failed to respond on time. If your query uses max parameter, please try to reduce it.

---

### 10.3 Team Memberships: Get Team Membership Details

**Endpoint:** `GET /team/memberships/{membershipId}`

Shows details for a team membership, by ID.

Specify the team membership ID in the `membershipId` URI parameter.

#### Parameters

| Name | In | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| `membershipId` | `path` | `string` | Yes | The unique identifier for the team membership. |

#### Responses

- **`200`** — OK
  ```json
  {
    "type": "object",
    "properties": {
      "id": {
        "type": "string",
        "example": "Y2lzY29zcGFyazovL3VzL1RFQU1fTUVNQkVSU0hJUC8wZmNmYTJiOC1hZGNjLTQ1ZWEtYTc4Mi1lNDYwNTkyZjgxZWY6MTNlMThmNDAtNDJmYy0xMWU2LWE5ZDgtMjExYTBkYzc5NzY5",
        "description": "A unique identifier for the team membership."
      },
      "teamId": {
        "type": "string",
        "example": "Y2lzY29zcGFyazovL3VzL1RFQU0vMTNlMThmNDAtNDJmYy0xMWU2LWE5ZDgtMjExYTBkYzc5NzY5",
        "description": "The team ID."
      },
      "personId": {
        "type": "string",
        "example": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS9mNWIzNjE4Ny1jOGRkLTQ3MjctOGIyZi1mOWM0NDdmMjkwNDY",
        "description": "The person ID."
      },
      "personEmail": {
        "type": "string",
        "example": "john.andersen@example.com",
        "description": "The email address of the person."
      },
      "personDisplayName": {
        "type": "string",
        "example": "John Andersen",
        "description": "The display name of the person."
      },
      "personOrgId": {
        "type": "string",
        "example": "Y2lzY29zcGFyazovL3VzL09SR0FOSVpBVElPTi85NmFiYzJhYS0zZGNjLTExZTUtYTE1Mi1mZTM0ODE5Y2RjOWE",
        "description": "The organization ID of the person."
      },
      "isModerator": {
        "type": "boolean",
        "example": true,
        "description": "Whether or not the participant is a team moderator."
      },
      "created": {
        "type": "string",
        "example": "2015-10-18T14:26:16.203Z",
        "description": "The date and time when the team membership was created."
      }
    },
    "$$ref": "#/components/schemas/TeamMembership"
  }
  ```
- **`400`** — Bad Request: The request was invalid or cannot be otherwise served. An accompanying error message will explain further.
- **`401`** — Unauthorized: Authentication credentials were missing or incorrect.
- **`403`** — Forbidden: The request is understood, but it has been refused or access is not allowed.
- **`404`** — Not Found: The URI requested is invalid or the resource requested, such as a user, does not exist. Also returned when the requested format is not supported by the requested method.
- **`405`** — Method Not Allowed: The request was made to a resource using an HTTP request method that is not supported.
- **`409`** — Conflict: The request could not be processed because it conflicts with some established rule of the system. For example, a person may not be added to a room more than once.
- **`410`** — Gone: The requested resource is no longer available.
- **`415`** — Unsupported Media Type: The request was made to a resource without specifying a media type or used a media type that is not supported.
- **`423`** — Locked: The requested resource is temporarily unavailable. A Retry-After header may be present that specifies how many seconds you need to wait before attempting the request again.
- **`428`** — Precondition Required: File(s) cannot be scanned for malware and need to be force downloaded.
- **`429`** — Too Many Requests: Too many requests have been sent in a given amount of time and the request has been rate limited. A Retry-After header should be present that specifies how many seconds you need to wait before a successful request can be made.
- **`500`** — Internal Server Error: Something went wrong on the server. If the issue persists, feel free to contact the [Webex Developer Support team](/explore/support).
- **`502`** — Bad Gateway: The server received an invalid response from an upstream server while processing the request. Try again later.
- **`503`** — Service Unavailable: Server is overloaded with requests. Try again later.
- **`504`** — Gateway Timeout: An upstream server failed to respond on time. If your query uses max parameter, please try to reduce it.

---

### 10.4 Team Memberships: List Team Memberships

**Endpoint:** `GET /team/memberships`

Lists all team memberships for a given team, specified by the `teamId` query parameter.

Use query parameters to filter the response.

#### Parameters

| Name | In | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| `teamId` | `query` | `string` | Yes | List memberships for a team, by ID. |
| `max` | `query` | `number` | No | Limit the maximum number of team memberships in the response. |

#### Responses

- **`200`** — OK
  ```json
  {
    "type": "object",
    "properties": {
      "items": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "id": {
              "type": "string",
              "example": "Y2lzY29zcGFyazovL3VzL1RFQU1fTUVNQkVSU0hJUC8wZmNmYTJiOC1hZGNjLTQ1ZWEtYTc4Mi1lNDYwNTkyZjgxZWY6MTNlMThmNDAtNDJmYy0xMWU2LWE5ZDgtMjExYTBkYzc5NzY5",
              "description": "A unique identifier for the team membership."
            },
            "teamId": {
              "type": "string",
              "example": "Y2lzY29zcGFyazovL3VzL1RFQU0vMTNlMThmNDAtNDJmYy0xMWU2LWE5ZDgtMjExYTBkYzc5NzY5",
              "description": "The team ID."
            },
            "personId": {
              "type": "string",
              "example": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS9mNWIzNjE4Ny1jOGRkLTQ3MjctOGIyZi1mOWM0NDdmMjkwNDY",
              "description": "The person ID."
            },
            "personEmail": {
              "type": "string",
              "example": "john.andersen@example.com",
              "description": "The email address of the person."
            },
            "personDisplayName": {
              "type": "string",
              "example": "John Andersen",
              "description": "The display name of the person."
            },
            "personOrgId": {
              "type": "string",
              "example": "Y2lzY29zcGFyazovL3VzL09SR0FOSVpBVElPTi85NmFiYzJhYS0zZGNjLTExZTUtYTE1Mi1mZTM0ODE5Y2RjOWE",
              "description": "The organization ID of the person."
            },
            "isModerator": {
              "type": "boolean",
              "example": true,
              "description": "Whether or not the participant is a team moderator."
            },
            "created": {
              "type": "string",
              "example": "2015-10-18T14:26:16.203Z",
              "description": "The date and time when the team membership was created."
            }
          },
          "$$ref": "#/components/schemas/TeamMembership"
        }
      }
    },
    "$$ref": "#/components/schemas/TeamMembershipCollectionResponse"
  }
  ```
- **`400`** — Bad Request: The request was invalid or cannot be otherwise served. An accompanying error message will explain further.
- **`401`** — Unauthorized: Authentication credentials were missing or incorrect.
- **`403`** — Forbidden: The request is understood, but it has been refused or access is not allowed.
- **`404`** — Not Found: The URI requested is invalid or the resource requested, such as a user, does not exist. Also returned when the requested format is not supported by the requested method.
- **`405`** — Method Not Allowed: The request was made to a resource using an HTTP request method that is not supported.
- **`409`** — Conflict: The request could not be processed because it conflicts with some established rule of the system. For example, a person may not be added to a room more than once.
- **`410`** — Gone: The requested resource is no longer available.
- **`415`** — Unsupported Media Type: The request was made to a resource without specifying a media type or used a media type that is not supported.
- **`423`** — Locked: The requested resource is temporarily unavailable. A Retry-After header may be present that specifies how many seconds you need to wait before attempting the request again.
- **`428`** — Precondition Required: File(s) cannot be scanned for malware and need to be force downloaded.
- **`429`** — Too Many Requests: Too many requests have been sent in a given amount of time and the request has been rate limited. A Retry-After header should be present that specifies how many seconds you need to wait before a successful request can be made.
- **`500`** — Internal Server Error: Something went wrong on the server. If the issue persists, feel free to contact the [Webex Developer Support team](/explore/support).
- **`502`** — Bad Gateway: The server received an invalid response from an upstream server while processing the request. Try again later.
- **`503`** — Service Unavailable: Server is overloaded with requests. Try again later.
- **`504`** — Gateway Timeout: An upstream server failed to respond on time. If your query uses max parameter, please try to reduce it.

---

### 10.5 Team Memberships: Update a Team Membership

**Endpoint:** `PUT /team/memberships/{membershipId}`

Updates a team membership, by ID.

Specify the team membership ID in the `membershipId` URI parameter.

#### Parameters

| Name | In | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| `membershipId` | `path` | `string` | Yes | The unique identifier for the team membership. |

#### Request Body Schema

```json
{
  "type": "object",
  "required": [
    "isModerator"
  ],
  "properties": {
    "isModerator": {
      "type": "boolean",
      "example": true,
      "description": "Whether or not the participant is a team moderator."
    }
  }
}
```

#### Responses

- **`200`** — OK
  ```json
  {
    "type": "object",
    "properties": {
      "id": {
        "type": "string",
        "example": "Y2lzY29zcGFyazovL3VzL1RFQU1fTUVNQkVSU0hJUC8wZmNmYTJiOC1hZGNjLTQ1ZWEtYTc4Mi1lNDYwNTkyZjgxZWY6MTNlMThmNDAtNDJmYy0xMWU2LWE5ZDgtMjExYTBkYzc5NzY5",
        "description": "A unique identifier for the team membership."
      },
      "teamId": {
        "type": "string",
        "example": "Y2lzY29zcGFyazovL3VzL1RFQU0vMTNlMThmNDAtNDJmYy0xMWU2LWE5ZDgtMjExYTBkYzc5NzY5",
        "description": "The team ID."
      },
      "personId": {
        "type": "string",
        "example": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS9mNWIzNjE4Ny1jOGRkLTQ3MjctOGIyZi1mOWM0NDdmMjkwNDY",
        "description": "The person ID."
      },
      "personEmail": {
        "type": "string",
        "example": "john.andersen@example.com",
        "description": "The email address of the person."
      },
      "personDisplayName": {
        "type": "string",
        "example": "John Andersen",
        "description": "The display name of the person."
      },
      "personOrgId": {
        "type": "string",
        "example": "Y2lzY29zcGFyazovL3VzL09SR0FOSVpBVElPTi85NmFiYzJhYS0zZGNjLTExZTUtYTE1Mi1mZTM0ODE5Y2RjOWE",
        "description": "The organization ID of the person."
      },
      "isModerator": {
        "type": "boolean",
        "example": true,
        "description": "Whether or not the participant is a team moderator."
      },
      "created": {
        "type": "string",
        "example": "2015-10-18T14:26:16.203Z",
        "description": "The date and time when the team membership was created."
      }
    },
    "$$ref": "#/components/schemas/TeamMembership"
  }
  ```
- **`400`** — Bad Request: The request was invalid or cannot be otherwise served. An accompanying error message will explain further.
- **`401`** — Unauthorized: Authentication credentials were missing or incorrect.
- **`403`** — Forbidden: The request is understood, but it has been refused or access is not allowed.
- **`404`** — Not Found: The URI requested is invalid or the resource requested, such as a user, does not exist. Also returned when the requested format is not supported by the requested method.
- **`405`** — Method Not Allowed: The request was made to a resource using an HTTP request method that is not supported.
- **`409`** — Conflict: The request could not be processed because it conflicts with some established rule of the system. For example, a person may not be added to a room more than once.
- **`410`** — Gone: The requested resource is no longer available.
- **`415`** — Unsupported Media Type: The request was made to a resource without specifying a media type or used a media type that is not supported.
- **`423`** — Locked: The requested resource is temporarily unavailable. A Retry-After header may be present that specifies how many seconds you need to wait before attempting the request again.
- **`428`** — Precondition Required: File(s) cannot be scanned for malware and need to be force downloaded.
- **`429`** — Too Many Requests: Too many requests have been sent in a given amount of time and the request has been rate limited. A Retry-After header should be present that specifies how many seconds you need to wait before a successful request can be made.
- **`500`** — Internal Server Error: Something went wrong on the server. If the issue persists, feel free to contact the [Webex Developer Support team](/explore/support).
- **`502`** — Bad Gateway: The server received an invalid response from an upstream server while processing the request. Try again later.
- **`503`** — Service Unavailable: Server is overloaded with requests. Try again later.
- **`504`** — Gateway Timeout: An upstream server failed to respond on time. If your query uses max parameter, please try to reduce it.

---

## 11. Teams

### 11.1 Teams: Create a Team

**Endpoint:** `POST /teams`

Creates a team.

The authenticated user is automatically added as a member of the team. See the [Team Memberships API](/docs/api/v1/team-memberships) to learn how to add more people to the team.

#### Request Body Schema

```json
{
  "type": "object",
  "required": [
    "name"
  ],
  "properties": {
    "name": {
      "type": "string",
      "example": "Build Squad",
      "description": "A user-friendly name for the team."
    },
    "description": {
      "type": "string",
      "example": "The A team",
      "description": "The teams description."
    }
  }
}
```

#### Responses

- **`200`** — OK
  ```json
  {
    "type": "object",
    "properties": {
      "id": {
        "type": "string",
        "example": "Y2lzY29zcGFyazovL3VzL1RFQU0vMTNlMThmNDAtNDJmYy0xMWU2LWE5ZDgtMjExYTBkYzc5NzY5",
        "description": "A unique identifier for the team."
      },
      "name": {
        "type": "string",
        "example": "Build Squad",
        "description": "A user-friendly name for the team."
      },
      "description": {
        "type": "string",
        "example": "The A Team",
        "description": "The teams description."
      },
      "created": {
        "type": "string",
        "example": "2015-10-18T14:26:16.000Z",
        "description": "The date and time the team was created."
      }
    },
    "$$ref": "#/components/schemas/Team"
  }
  ```
- **`400`** — Bad Request: The request was invalid or cannot be otherwise served. An accompanying error message will explain further.
- **`401`** — Unauthorized: Authentication credentials were missing or incorrect.
- **`403`** — Forbidden: The request is understood, but it has been refused or access is not allowed.
- **`404`** — Not Found: The URI requested is invalid or the resource requested, such as a user, does not exist. Also returned when the requested format is not supported by the requested method.
- **`405`** — Method Not Allowed: The request was made to a resource using an HTTP request method that is not supported.
- **`409`** — Conflict: The request could not be processed because it conflicts with some established rule of the system. For example, a person may not be added to a room more than once.
- **`410`** — Gone: The requested resource is no longer available.
- **`415`** — Unsupported Media Type: The request was made to a resource without specifying a media type or used a media type that is not supported.
- **`423`** — Locked: The requested resource is temporarily unavailable. A Retry-After header may be present that specifies how many seconds you need to wait before attempting the request again.
- **`428`** — Precondition Required: File(s) cannot be scanned for malware and need to be force downloaded.
- **`429`** — Too Many Requests: Too many requests have been sent in a given amount of time and the request has been rate limited. A Retry-After header should be present that specifies how many seconds you need to wait before a successful request can be made.
- **`500`** — Internal Server Error: Something went wrong on the server. If the issue persists, feel free to contact the [Webex Developer Support team](/explore/support).
- **`502`** — Bad Gateway: The server received an invalid response from an upstream server while processing the request. Try again later.
- **`503`** — Service Unavailable: Server is overloaded with requests. Try again later.
- **`504`** — Gateway Timeout: An upstream server failed to respond on time. If your query uses max parameter, please try to reduce it.

---

### 11.2 Teams: Delete a Team

**Endpoint:** `DELETE /teams/{teamId}`

Deletes a team, by ID.

Specify the team ID in the `teamId` parameter in the URI.

#### Parameters

| Name | In | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| `teamId` | `path` | `string` | Yes | The unique identifier for the team. |

#### Responses

- **`204`** — No Content
- **`400`** — Bad Request: The request was invalid or cannot be otherwise served. An accompanying error message will explain further.
- **`401`** — Unauthorized: Authentication credentials were missing or incorrect.
- **`403`** — Forbidden: The request is understood, but it has been refused or access is not allowed.
- **`404`** — Not Found: The URI requested is invalid or the resource requested, such as a user, does not exist. Also returned when the requested format is not supported by the requested method.
- **`405`** — Method Not Allowed: The request was made to a resource using an HTTP request method that is not supported.
- **`409`** — Conflict: The request could not be processed because it conflicts with some established rule of the system. For example, a person may not be added to a room more than once.
- **`410`** — Gone: The requested resource is no longer available.
- **`415`** — Unsupported Media Type: The request was made to a resource without specifying a media type or used a media type that is not supported.
- **`423`** — Locked: The requested resource is temporarily unavailable. A Retry-After header may be present that specifies how many seconds you need to wait before attempting the request again.
- **`428`** — Precondition Required: File(s) cannot be scanned for malware and need to be force downloaded.
- **`429`** — Too Many Requests: Too many requests have been sent in a given amount of time and the request has been rate limited. A Retry-After header should be present that specifies how many seconds you need to wait before a successful request can be made.
- **`500`** — Internal Server Error: Something went wrong on the server. If the issue persists, feel free to contact the [Webex Developer Support team](/explore/support).
- **`502`** — Bad Gateway: The server received an invalid response from an upstream server while processing the request. Try again later.
- **`503`** — Service Unavailable: Server is overloaded with requests. Try again later.
- **`504`** — Gateway Timeout: An upstream server failed to respond on time. If your query uses max parameter, please try to reduce it.

---

### 11.3 Teams: Get Team Details

**Endpoint:** `GET /teams/{teamId}`

Shows details for a team, by ID.

Specify the team ID in the `teamId` parameter in the URI.

#### Parameters

| Name | In | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| `teamId` | `path` | `string` | Yes | The unique identifier for the team. |
| `description` | `query` | `string` | No | The teams description. |

#### Responses

- **`200`** — OK
  ```json
  {
    "type": "object",
    "properties": {
      "id": {
        "type": "string",
        "example": "Y2lzY29zcGFyazovL3VzL1RFQU0vMTNlMThmNDAtNDJmYy0xMWU2LWE5ZDgtMjExYTBkYzc5NzY5",
        "description": "A unique identifier for the team."
      },
      "name": {
        "type": "string",
        "example": "Build Squad",
        "description": "A user-friendly name for the team."
      },
      "description": {
        "type": "string",
        "example": "The A Team",
        "description": "The teams description."
      },
      "created": {
        "type": "string",
        "example": "2015-10-18T14:26:16.000Z",
        "description": "The date and time the team was created."
      }
    },
    "$$ref": "#/components/schemas/Team"
  }
  ```
- **`400`** — Bad Request: The request was invalid or cannot be otherwise served. An accompanying error message will explain further.
- **`401`** — Unauthorized: Authentication credentials were missing or incorrect.
- **`403`** — Forbidden: The request is understood, but it has been refused or access is not allowed.
- **`404`** — Not Found: The URI requested is invalid or the resource requested, such as a user, does not exist. Also returned when the requested format is not supported by the requested method.
- **`405`** — Method Not Allowed: The request was made to a resource using an HTTP request method that is not supported.
- **`409`** — Conflict: The request could not be processed because it conflicts with some established rule of the system. For example, a person may not be added to a room more than once.
- **`410`** — Gone: The requested resource is no longer available.
- **`415`** — Unsupported Media Type: The request was made to a resource without specifying a media type or used a media type that is not supported.
- **`423`** — Locked: The requested resource is temporarily unavailable. A Retry-After header may be present that specifies how many seconds you need to wait before attempting the request again.
- **`428`** — Precondition Required: File(s) cannot be scanned for malware and need to be force downloaded.
- **`429`** — Too Many Requests: Too many requests have been sent in a given amount of time and the request has been rate limited. A Retry-After header should be present that specifies how many seconds you need to wait before a successful request can be made.
- **`500`** — Internal Server Error: Something went wrong on the server. If the issue persists, feel free to contact the [Webex Developer Support team](/explore/support).
- **`502`** — Bad Gateway: The server received an invalid response from an upstream server while processing the request. Try again later.
- **`503`** — Service Unavailable: Server is overloaded with requests. Try again later.
- **`504`** — Gateway Timeout: An upstream server failed to respond on time. If your query uses max parameter, please try to reduce it.

---

### 11.4 Teams: List Teams

**Endpoint:** `GET /teams`

Lists teams to which the authenticated user belongs.

#### Parameters

| Name | In | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| `max` | `query` | `number` | No | Limit the maximum number of teams in the response. |

#### Responses

- **`200`** — OK
  ```json
  {
    "type": "object",
    "properties": {
      "items": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "id": {
              "type": "string",
              "example": "Y2lzY29zcGFyazovL3VzL1RFQU0vMTNlMThmNDAtNDJmYy0xMWU2LWE5ZDgtMjExYTBkYzc5NzY5",
              "description": "A unique identifier for the team."
            },
            "name": {
              "type": "string",
              "example": "Build Squad",
              "description": "A user-friendly name for the team."
            },
            "description": {
              "type": "string",
              "example": "The A Team",
              "description": "The teams description."
            },
            "created": {
              "type": "string",
              "example": "2015-10-18T14:26:16.000Z",
              "description": "The date and time the team was created."
            }
          },
          "$$ref": "#/components/schemas/Team"
        }
      }
    },
    "$$ref": "#/components/schemas/TeamCollectionResponse"
  }
  ```
- **`400`** — Bad Request: The request was invalid or cannot be otherwise served. An accompanying error message will explain further.
- **`401`** — Unauthorized: Authentication credentials were missing or incorrect.
- **`403`** — Forbidden: The request is understood, but it has been refused or access is not allowed.
- **`404`** — Not Found: The URI requested is invalid or the resource requested, such as a user, does not exist. Also returned when the requested format is not supported by the requested method.
- **`405`** — Method Not Allowed: The request was made to a resource using an HTTP request method that is not supported.
- **`409`** — Conflict: The request could not be processed because it conflicts with some established rule of the system. For example, a person may not be added to a room more than once.
- **`410`** — Gone: The requested resource is no longer available.
- **`415`** — Unsupported Media Type: The request was made to a resource without specifying a media type or used a media type that is not supported.
- **`423`** — Locked: The requested resource is temporarily unavailable. A Retry-After header may be present that specifies how many seconds you need to wait before attempting the request again.
- **`428`** — Precondition Required: File(s) cannot be scanned for malware and need to be force downloaded.
- **`429`** — Too Many Requests: Too many requests have been sent in a given amount of time and the request has been rate limited. A Retry-After header should be present that specifies how many seconds you need to wait before a successful request can be made.
- **`500`** — Internal Server Error: Something went wrong on the server. If the issue persists, feel free to contact the [Webex Developer Support team](/explore/support).
- **`502`** — Bad Gateway: The server received an invalid response from an upstream server while processing the request. Try again later.
- **`503`** — Service Unavailable: Server is overloaded with requests. Try again later.
- **`504`** — Gateway Timeout: An upstream server failed to respond on time. If your query uses max parameter, please try to reduce it.

---

### 11.5 Teams: Update a Team

**Endpoint:** `PUT /teams/{teamId}`

Updates details for a team, by ID.

Specify the team ID in the `teamId` parameter in the URI.

#### Parameters

| Name | In | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| `teamId` | `path` | `string` | Yes | The unique identifier for the team. |

#### Request Body Schema

```json
{
  "type": "object",
  "required": [
    "name"
  ],
  "properties": {
    "name": {
      "type": "string",
      "example": "Build Squad",
      "description": "A user-friendly name for the team."
    },
    "description": {
      "type": "string",
      "example": "The A team",
      "description": "The teams description."
    }
  }
}
```

#### Responses

- **`200`** — OK
  ```json
  {
    "type": "object",
    "properties": {
      "id": {
        "type": "string",
        "example": "Y2lzY29zcGFyazovL3VzL1RFQU0vMTNlMThmNDAtNDJmYy0xMWU2LWE5ZDgtMjExYTBkYzc5NzY5",
        "description": "A unique identifier for the team."
      },
      "name": {
        "type": "string",
        "example": "Build Squad",
        "description": "A user-friendly name for the team."
      },
      "description": {
        "type": "string",
        "example": "The A Team",
        "description": "The teams description."
      },
      "created": {
        "type": "string",
        "example": "2015-10-18T14:26:16.000Z",
        "description": "The date and time the team was created."
      }
    },
    "$$ref": "#/components/schemas/Team"
  }
  ```
- **`400`** — Bad Request: The request was invalid or cannot be otherwise served. An accompanying error message will explain further.
- **`401`** — Unauthorized: Authentication credentials were missing or incorrect.
- **`403`** — Forbidden: The request is understood, but it has been refused or access is not allowed.
- **`404`** — Not Found: The URI requested is invalid or the resource requested, such as a user, does not exist. Also returned when the requested format is not supported by the requested method.
- **`405`** — Method Not Allowed: The request was made to a resource using an HTTP request method that is not supported.
- **`409`** — Conflict: The request could not be processed because it conflicts with some established rule of the system. For example, a person may not be added to a room more than once.
- **`410`** — Gone: The requested resource is no longer available.
- **`415`** — Unsupported Media Type: The request was made to a resource without specifying a media type or used a media type that is not supported.
- **`423`** — Locked: The requested resource is temporarily unavailable. A Retry-After header may be present that specifies how many seconds you need to wait before attempting the request again.
- **`428`** — Precondition Required: File(s) cannot be scanned for malware and need to be force downloaded.
- **`429`** — Too Many Requests: Too many requests have been sent in a given amount of time and the request has been rate limited. A Retry-After header should be present that specifies how many seconds you need to wait before a successful request can be made.
- **`500`** — Internal Server Error: Something went wrong on the server. If the issue persists, feel free to contact the [Webex Developer Support team](/explore/support).
- **`502`** — Bad Gateway: The server received an invalid response from an upstream server while processing the request. Try again later.
- **`503`** — Service Unavailable: Server is overloaded with requests. Try again later.
- **`504`** — Gateway Timeout: An upstream server failed to respond on time. If your query uses max parameter, please try to reduce it.

---

## 12. Webhooks

### 12.1 Webhooks: Create a Webhook

**Endpoint:** `POST /webhooks`

Creates a webhook.

To learn more about how to create and use webhooks, see The [Webhooks Guide](/docs/api/guides/webhooks).

#### Request Body Schema

```json
{
  "type": "object",
  "required": [
    "name",
    "targetUrl",
    "resource",
    "event"
  ],
  "properties": {
    "name": {
      "type": "string",
      "example": "My Awesome Webhook",
      "description": "A user-friendly name for the webhook."
    },
    "targetUrl": {
      "type": "string",
      "example": "https://example.com/mywebhook",
      "description": "URL that receives POST requests for each event."
    },
    "resource": {
      "type": "string",
      "enum": [
        "attachmentActions",
        "dataSources",
        "memberships",
        "messages",
        "rooms",
        "meetings",
        "recordings",
        "convergedRecordings",
        "meetingParticipants",
        "meetingTranscripts",
        "telephony_calls",
        "telephony_conference",
        "telephony_mwi",
        "uc_counters",
        "serviceApp",
        "adminBatchJobs"
      ],
      "description": "Resource type for the webhook. Creating a webhook requires 'read' scope on the resource the webhook is for.\n * `attachmentActions` - [Attachment Actions](/docs/api/v1/attachment-actions) resource.\n * `dataSources` - [data sources](/docs/api/v1/data-sources) resource.\n * `memberships` - [Memberships](/docs/api/v1/memberships) resource.\n * `messages` - [Messages](/docs/api/v1/messages) resource.\n * `rooms` - [Rooms](/docs/api/v1/rooms) resource.\n * `meetings` - [Meetings](/docs/api/v1/meetings) resource.\n * `recordings` - [Recordings](/docs/api/v1/recordings) resource.\n * `convergedRecordings` - [CallRecordings](/docs/api/v1/converged-recordings) resource.\n * `meetingParticipants` - [Meeting Participants](/docs/api/v1/meeting-participants) resource.\n * `meetingTranscripts` - [Meeting Transcripts](/docs/api/v1/meeting-transcripts) resource.\n * `telephony_calls` - [Webex Calling](/docs/webex-calling-overview) call resources.\n * `telephony_conference` - [Webex Calling](/docs/webex-calling-overview) conference controls resource.\n * `telephony_mwi` - [Webex Calling](/docs/webex-calling-overview) voicemail message waiting indicator resource.\n * `uc_counters` - Performance counter for a dedicated instance.\n * `serviceApp` - Service App authorization notification.\n * `adminBatchJobs` - Admin Batch Jobs notification.\n"
    },
    "event": {
      "type": "string",
      "enum": [
        "created",
        "updated",
        "deleted",
        "started",
        "ended",
        "joined",
        "left",
        "migrated",
        "authorized",
        "deauthorized",
        "statusChanged"
      ],
      "description": "Event type for the webhook.\n * `created` - An object is created.\n * `updated` - An object is updated.\n * `deleted` - An object is deleted.\n * `started` - A meeting is started.\n * `ended` - A meeting is ended.\n * `joined` - A participant joined.\n * `left` - A participant left.\n * `migrated` - A room was migrated to a different geography. The roomId has changed.\n * `authorized` - A Service App was authorized.\n * `deauthorized` - A Service App was deauthorized.\n * `statusChanged` - Status of admin batch job was changed.\n"
    },
    "filter": {
      "type": "string",
      "example": "roomId=Y2lzY29zcGFyazovL3VzL1JPT00vYmJjZWIxYWQtNDNmMS0zYjU4LTkxNDctZjE0YmIwYzRkMTU0",
      "description": "Filter that defines the webhook scope. See [Filtering Webhooks](/docs/api/guides/webhooks#filtering-webhooks) for more information. Please note that if a filter of `hostEmail`, `hostUserId`, `ownerEmail` or `ownerId` is specified, `ownedBy` must be set to `org`."
    },
    "secret": {
      "type": "string",
      "example": "86dacc007724d8ea666f88fc77d918dad9537a15",
      "description": "Secret used to generate payload signature."
    },
    "ownedBy": {
      "type": "string",
      "example": "org",
      "description": "Specify `org` when creating an org/admin level webhook. Supported for `meetings`, `recordings`, `convergedRecordings`,`meetingParticipants`, `meetingTranscripts`, `videoMeshAlerts`, `controlHubAlerts`, `rooms`, `messaging` and `adminBatchJobs` (for Compliance Officers and messages with file attachments only - see [inline file DLP](/docs/api/guides/webex-real-time-file-dlp-basics)) resources."
    }
  }
}
```

#### Responses

- **`200`** — OK
  ```json
  {
    "type": "object",
    "properties": {
      "id": {
        "type": "string",
        "example": "Y2lzY29zcGFyazovL3VzL1dFQkhPT0svOTZhYmMyYWEtM2RjYy0xMWU1LWExNTItZmUzNDgxOWNkYzlh",
        "description": "A unique identifier for the webhook."
      },
      "name": {
        "type": "string",
        "example": "My Awesome Webhook",
        "description": "A user-friendly name for the webhook."
      },
      "targetUrl": {
        "type": "string",
        "example": "https://example.com/mywebhook",
        "description": "URL that receives POST requests for each event."
      },
      "resource": {
        "type": "string",
        "enum": [
          "attachmentActions",
          "dataSources",
          "memberships",
          "messages",
          "rooms",
          "meetings",
          "recordings",
          "convergedRecordings",
          "meetingParticipants",
          "meetingTranscripts",
          "telephony_calls",
          "telephony_conference",
          "telephony_mwi",
          "uc_counters",
          "serviceApp",
          "adminBatchJobs"
        ],
        "description": "Resource type for the webhook. Creating a webhook requires 'read' scope on the resource the webhook is for.\n * `attachmentActions` - [Attachment Actions](/docs/api/v1/attachment-actions) resource.\n * `dataSources` - [data sources](/docs/api/v1/data-sources) resource.\n * `memberships` - [Memberships](/docs/api/v1/memberships) resource.\n * `messages` - [Messages](/docs/api/v1/messages) resource.\n * `rooms` - [Rooms](/docs/api/v1/rooms) resource.\n * `meetings` - [Meetings](/docs/api/v1/meetings) resource.\n * `recordings` - [Recordings](/docs/api/v1/recordings) resource.\n * `convergedRecordings` - [CallRecordings](/docs/api/v1/converged-recordings) resource.\n * `meetingParticipants` - [Meeting Participants](/docs/api/v1/meeting-participants) resource.\n * `meetingTranscripts` - [Meeting Transcripts](/docs/api/v1/meeting-transcripts) resource.\n * `telephony_calls` - [Webex Calling](/docs/webex-calling-overview) call resources.\n * `telephony_conference` - [Webex Calling](/docs/webex-calling-overview) conference controls resource.\n * `telephony_mwi` - [Webex Calling](/docs/webex-calling-overview) voicemail message waiting indicator resource.\n * `uc_counters` - Performance counter for a dedicated instance.\n * `serviceApp` - Service App authorization notification.\n * `adminBatchJobs` - Admin Batch Jobs notification.\n"
      },
      "event": {
        "type": "string",
        "enum": [
          "created",
          "updated",
          "deleted",
          "started",
          "ended",
          "joined",
          "left",
          "migrated",
          "authorized",
          "deauthorized",
          "statusChanged"
        ],
        "description": "Event type for the webhook.\n * `created` - An object was created.\n * `updated` - An object was updated.\n * `deleted` - An object was deleted.\n * `started` - A meeting was started.\n * `ended` - A meeting was ended.\n * `joined` - A participant joined.\n * `left` - A participant left.\n * `migrated` - A room was migrated to a different geography. The roomId has changed.\n * `authorized` - A Service App was authorized.\n * `deauthorized` - A Service App was deauthorized.\n * `statusChanged` - Status of admin batch job was changed.\n"
      },
      "filter": {
        "type": "string",
        "example": "roomId=Y2lzY29zcGFyazovL3VzL1JPT00vYmJjZWIxYWQtNDNmMS0zYjU4LTkxNDctZjE0YmIwYzRkMTU0",
        "description": "Filter that defines the webhook scope."
      },
      "secret": {
        "type": "string",
        "example": "86dacc007724d8ea666f88fc77d918dad9537a15",
        "description": "Secret used to generate payload signature."
      },
      "status": {
        "type": "string",
        "enum": [
          "active",
          "inactive"
        ],
        "description": "Status of the webhook. Use `active` to reactivate a disabled webhook.\n * `active` - Webhook is active.\n * `inactive` - Webhook is inactive.\n"
      },
      "created": {
        "type": "string",
        "example": "2015-10-18T14:26:16+00:00",
        "description": "Date and time the webhook was created."
      },
      "ownedBy": {
        "type": "string",
        "example": "org",
        "description": "Specify `org` when creating an org/admin level webhook. Supported for `meetings`, `recordings`, `convergedRecordings`, `meetingParticipants`, `meetingTranscripts`, `videoMeshAlerts`, `controlHubAlerts`, `rooms`, `messaging` and `adminBatchJobs`  (for Compliance Officers and messages with file attachments only - see [inline file DLP](/docs/api/guides/webex-real-time-file-dlp-basics)) resources."
      }
    },
    "$$ref": "#/components/schemas/Webhook"
  }
  ```
- **`400`** — Bad Request: The request was invalid or cannot be otherwise served. An accompanying error message will explain further.
- **`401`** — Unauthorized: Authentication credentials were missing or incorrect.
- **`403`** — Forbidden: The request is understood, but it has been refused or access is not allowed.
- **`404`** — Not Found: The URI requested is invalid or the resource requested, such as a user, does not exist. Also returned when the requested format is not supported by the requested method.
- **`405`** — Method Not Allowed: The request was made to a resource using an HTTP request method that is not supported.
- **`409`** — Conflict: The request could not be processed because it conflicts with some established rule of the system. For example, a person may not be added to a room more than once.
- **`410`** — Gone: The requested resource is no longer available.
- **`415`** — Unsupported Media Type: The request was made to a resource without specifying a media type or used a media type that is not supported.
- **`423`** — Locked: The requested resource is temporarily unavailable. A Retry-After header may be present that specifies how many seconds you need to wait before attempting the request again.
- **`428`** — Precondition Required: File(s) cannot be scanned for malware and need to be force downloaded.
- **`429`** — Too Many Requests: Too many requests have been sent in a given amount of time and the request has been rate limited. A Retry-After header should be present that specifies how many seconds you need to wait before a successful request can be made.
- **`500`** — Internal Server Error: Something went wrong on the server. If the issue persists, feel free to contact the [Webex Developer Support team](/explore/support).
- **`502`** — Bad Gateway: The server received an invalid response from an upstream server while processing the request. Try again later.
- **`503`** — Service Unavailable: Server is overloaded with requests. Try again later.
- **`504`** — Gateway Timeout: An upstream server failed to respond on time. If your query uses max parameter, please try to reduce it.

---

### 12.2 Webhooks: Delete a Webhook

**Endpoint:** `DELETE /webhooks/{webhookId}`

Deletes a webhook, by ID.

Specify the webhook ID in the `webhookId` parameter in the URI.

#### Parameters

| Name | In | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| `webhookId` | `path` | `string` | Yes | The unique identifier for the webhook. |

#### Responses

- **`204`** — No Content
- **`400`** — Bad Request: The request was invalid or cannot be otherwise served. An accompanying error message will explain further.
- **`401`** — Unauthorized: Authentication credentials were missing or incorrect.
- **`403`** — Forbidden: The request is understood, but it has been refused or access is not allowed.
- **`404`** — Not Found: The URI requested is invalid or the resource requested, such as a user, does not exist. Also returned when the requested format is not supported by the requested method.
- **`405`** — Method Not Allowed: The request was made to a resource using an HTTP request method that is not supported.
- **`409`** — Conflict: The request could not be processed because it conflicts with some established rule of the system. For example, a person may not be added to a room more than once.
- **`410`** — Gone: The requested resource is no longer available.
- **`415`** — Unsupported Media Type: The request was made to a resource without specifying a media type or used a media type that is not supported.
- **`423`** — Locked: The requested resource is temporarily unavailable. A Retry-After header may be present that specifies how many seconds you need to wait before attempting the request again.
- **`428`** — Precondition Required: File(s) cannot be scanned for malware and need to be force downloaded.
- **`429`** — Too Many Requests: Too many requests have been sent in a given amount of time and the request has been rate limited. A Retry-After header should be present that specifies how many seconds you need to wait before a successful request can be made.
- **`500`** — Internal Server Error: Something went wrong on the server. If the issue persists, feel free to contact the [Webex Developer Support team](/explore/support).
- **`502`** — Bad Gateway: The server received an invalid response from an upstream server while processing the request. Try again later.
- **`503`** — Service Unavailable: Server is overloaded with requests. Try again later.
- **`504`** — Gateway Timeout: An upstream server failed to respond on time. If your query uses max parameter, please try to reduce it.

---

### 12.3 Webhooks: Get Webhook Details

**Endpoint:** `GET /webhooks/{webhookId}`

Shows details for a webhook, by ID.

Specify the webhook ID in the `webhookId` parameter in the URI.

#### Parameters

| Name | In | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| `webhookId` | `path` | `string` | Yes | The unique identifier for the webhook. |

#### Responses

- **`200`** — OK
  ```json
  {
    "type": "object",
    "properties": {
      "id": {
        "type": "string",
        "example": "Y2lzY29zcGFyazovL3VzL1dFQkhPT0svOTZhYmMyYWEtM2RjYy0xMWU1LWExNTItZmUzNDgxOWNkYzlh",
        "description": "A unique identifier for the webhook."
      },
      "name": {
        "type": "string",
        "example": "My Awesome Webhook",
        "description": "A user-friendly name for the webhook."
      },
      "targetUrl": {
        "type": "string",
        "example": "https://example.com/mywebhook",
        "description": "URL that receives POST requests for each event."
      },
      "resource": {
        "type": "string",
        "enum": [
          "attachmentActions",
          "dataSources",
          "memberships",
          "messages",
          "rooms",
          "meetings",
          "recordings",
          "convergedRecordings",
          "meetingParticipants",
          "meetingTranscripts",
          "telephony_calls",
          "telephony_conference",
          "telephony_mwi",
          "uc_counters",
          "serviceApp",
          "adminBatchJobs"
        ],
        "description": "Resource type for the webhook. Creating a webhook requires 'read' scope on the resource the webhook is for.\n * `attachmentActions` - [Attachment Actions](/docs/api/v1/attachment-actions) resource.\n * `dataSources` - [data sources](/docs/api/v1/data-sources) resource.\n * `memberships` - [Memberships](/docs/api/v1/memberships) resource.\n * `messages` - [Messages](/docs/api/v1/messages) resource.\n * `rooms` - [Rooms](/docs/api/v1/rooms) resource.\n * `meetings` - [Meetings](/docs/api/v1/meetings) resource.\n * `recordings` - [Recordings](/docs/api/v1/recordings) resource.\n * `convergedRecordings` - [CallRecordings](/docs/api/v1/converged-recordings) resource.\n * `meetingParticipants` - [Meeting Participants](/docs/api/v1/meeting-participants) resource.\n * `meetingTranscripts` - [Meeting Transcripts](/docs/api/v1/meeting-transcripts) resource.\n * `telephony_calls` - [Webex Calling](/docs/webex-calling-overview) call resources.\n * `telephony_conference` - [Webex Calling](/docs/webex-calling-overview) conference controls resource.\n * `telephony_mwi` - [Webex Calling](/docs/webex-calling-overview) voicemail message waiting indicator resource.\n * `uc_counters` - Performance counter for a dedicated instance.\n * `serviceApp` - Service App authorization notification.\n * `adminBatchJobs` - Admin Batch Jobs notification.\n"
      },
      "event": {
        "type": "string",
        "enum": [
          "created",
          "updated",
          "deleted",
          "started",
          "ended",
          "joined",
          "left",
          "migrated",
          "authorized",
          "deauthorized",
          "statusChanged"
        ],
        "description": "Event type for the webhook.\n * `created` - An object was created.\n * `updated` - An object was updated.\n * `deleted` - An object was deleted.\n * `started` - A meeting was started.\n * `ended` - A meeting was ended.\n * `joined` - A participant joined.\n * `left` - A participant left.\n * `migrated` - A room was migrated to a different geography. The roomId has changed.\n * `authorized` - A Service App was authorized.\n * `deauthorized` - A Service App was deauthorized.\n * `statusChanged` - Status of admin batch job was changed.\n"
      },
      "filter": {
        "type": "string",
        "example": "roomId=Y2lzY29zcGFyazovL3VzL1JPT00vYmJjZWIxYWQtNDNmMS0zYjU4LTkxNDctZjE0YmIwYzRkMTU0",
        "description": "Filter that defines the webhook scope."
      },
      "secret": {
        "type": "string",
        "example": "86dacc007724d8ea666f88fc77d918dad9537a15",
        "description": "Secret used to generate payload signature."
      },
      "status": {
        "type": "string",
        "enum": [
          "active",
          "inactive"
        ],
        "description": "Status of the webhook. Use `active` to reactivate a disabled webhook.\n * `active` - Webhook is active.\n * `inactive` - Webhook is inactive.\n"
      },
      "created": {
        "type": "string",
        "example": "2015-10-18T14:26:16+00:00",
        "description": "Date and time the webhook was created."
      },
      "ownedBy": {
        "type": "string",
        "example": "org",
        "description": "Specify `org` when creating an org/admin level webhook. Supported for `meetings`, `recordings`, `convergedRecordings`, `meetingParticipants`, `meetingTranscripts`, `videoMeshAlerts`, `controlHubAlerts`, `rooms`, `messaging` and `adminBatchJobs`  (for Compliance Officers and messages with file attachments only - see [inline file DLP](/docs/api/guides/webex-real-time-file-dlp-basics)) resources."
      }
    },
    "$$ref": "#/components/schemas/Webhook"
  }
  ```
- **`400`** — Bad Request: The request was invalid or cannot be otherwise served. An accompanying error message will explain further.
- **`401`** — Unauthorized: Authentication credentials were missing or incorrect.
- **`403`** — Forbidden: The request is understood, but it has been refused or access is not allowed.
- **`404`** — Not Found: The URI requested is invalid or the resource requested, such as a user, does not exist. Also returned when the requested format is not supported by the requested method.
- **`405`** — Method Not Allowed: The request was made to a resource using an HTTP request method that is not supported.
- **`409`** — Conflict: The request could not be processed because it conflicts with some established rule of the system. For example, a person may not be added to a room more than once.
- **`410`** — Gone: The requested resource is no longer available.
- **`415`** — Unsupported Media Type: The request was made to a resource without specifying a media type or used a media type that is not supported.
- **`423`** — Locked: The requested resource is temporarily unavailable. A Retry-After header may be present that specifies how many seconds you need to wait before attempting the request again.
- **`428`** — Precondition Required: File(s) cannot be scanned for malware and need to be force downloaded.
- **`429`** — Too Many Requests: Too many requests have been sent in a given amount of time and the request has been rate limited. A Retry-After header should be present that specifies how many seconds you need to wait before a successful request can be made.
- **`500`** — Internal Server Error: Something went wrong on the server. If the issue persists, feel free to contact the [Webex Developer Support team](/explore/support).
- **`502`** — Bad Gateway: The server received an invalid response from an upstream server while processing the request. Try again later.
- **`503`** — Service Unavailable: Server is overloaded with requests. Try again later.
- **`504`** — Gateway Timeout: An upstream server failed to respond on time. If your query uses max parameter, please try to reduce it.

---

### 12.4 Webhooks: List Webhooks

**Endpoint:** `GET /webhooks`

List all of your webhooks.

#### Parameters

| Name | In | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| `max` | `query` | `number` | No | Limit the maximum number of webhooks in the response. |
| `ownedBy` | `query` | `string` | No | Limit the result list to org wide webhooks. Only allowed value is `org`. |

#### Responses

- **`200`** — OK
  ```json
  {
    "type": "object",
    "properties": {
      "items": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "id": {
              "type": "string",
              "example": "Y2lzY29zcGFyazovL3VzL1dFQkhPT0svOTZhYmMyYWEtM2RjYy0xMWU1LWExNTItZmUzNDgxOWNkYzlh",
              "description": "A unique identifier for the webhook."
            },
            "name": {
              "type": "string",
              "example": "My Awesome Webhook",
              "description": "A user-friendly name for the webhook."
            },
            "targetUrl": {
              "type": "string",
              "example": "https://example.com/mywebhook",
              "description": "URL that receives POST requests for each event."
            },
            "resource": {
              "type": "string",
              "enum": [
                "attachmentActions",
                "dataSources",
                "memberships",
                "messages",
                "rooms",
                "meetings",
                "recordings",
                "convergedRecordings",
                "meetingParticipants",
                "meetingTranscripts",
                "telephony_calls",
                "telephony_conference",
                "telephony_mwi",
                "uc_counters",
                "serviceApp",
                "adminBatchJobs"
              ],
              "description": "Resource type for the webhook. Creating a webhook requires 'read' scope on the resource the webhook is for.\n * `attachmentActions` - [Attachment Actions](/docs/api/v1/attachment-actions) resource.\n * `dataSources` - [data sources](/docs/api/v1/data-sources) resource.\n * `memberships` - [Memberships](/docs/api/v1/memberships) resource.\n * `messages` - [Messages](/docs/api/v1/messages) resource.\n * `rooms` - [Rooms](/docs/api/v1/rooms) resource.\n * `meetings` - [Meetings](/docs/api/v1/meetings) resource.\n * `recordings` - [Recordings](/docs/api/v1/recordings) resource.\n * `convergedRecordings` - [CallRecordings](/docs/api/v1/converged-recordings) resource.\n * `meetingParticipants` - [Meeting Participants](/docs/api/v1/meeting-participants) resource.\n * `meetingTranscripts` - [Meeting Transcripts](/docs/api/v1/meeting-transcripts) resource.\n * `telephony_calls` - [Webex Calling](/docs/webex-calling-overview) call resources.\n * `telephony_conference` - [Webex Calling](/docs/webex-calling-overview) conference controls resource.\n * `telephony_mwi` - [Webex Calling](/docs/webex-calling-overview) voicemail message waiting indicator resource.\n * `uc_counters` - Performance counter for a dedicated instance.\n * `serviceApp` - Service App authorization notification.\n * `adminBatchJobs` - Admin Batch Jobs notification.\n"
            },
            "event": {
              "type": "string",
              "enum": [
                "created",
                "updated",
                "deleted",
                "started",
                "ended",
                "joined",
                "left",
                "migrated",
                "authorized",
                "deauthorized",
                "statusChanged"
              ],
              "description": "Event type for the webhook.\n * `created` - An object was created.\n * `updated` - An object was updated.\n * `deleted` - An object was deleted.\n * `started` - A meeting was started.\n * `ended` - A meeting was ended.\n * `joined` - A participant joined.\n * `left` - A participant left.\n * `migrated` - A room was migrated to a different geography. The roomId has changed.\n * `authorized` - A Service App was authorized.\n * `deauthorized` - A Service App was deauthorized.\n * `statusChanged` - Status of admin batch job was changed.\n"
            },
            "filter": {
              "type": "string",
              "example": "roomId=Y2lzY29zcGFyazovL3VzL1JPT00vYmJjZWIxYWQtNDNmMS0zYjU4LTkxNDctZjE0YmIwYzRkMTU0",
              "description": "Filter that defines the webhook scope."
            },
            "secret": {
              "type": "string",
              "example": "86dacc007724d8ea666f88fc77d918dad9537a15",
              "description": "Secret used to generate payload signature."
            },
            "status": {
              "type": "string",
              "enum": [
                "active",
                "inactive"
              ],
              "description": "Status of the webhook. Use `active` to reactivate a disabled webhook.\n * `active` - Webhook is active.\n * `inactive` - Webhook is inactive.\n"
            },
            "created": {
              "type": "string",
              "example": "2015-10-18T14:26:16+00:00",
              "description": "Date and time the webhook was created."
            },
            "ownedBy": {
              "type": "string",
              "example": "org",
              "description": "Specify `org` when creating an org/admin level webhook. Supported for `meetings`, `recordings`, `convergedRecordings`, `meetingParticipants`, `meetingTranscripts`, `videoMeshAlerts`, `controlHubAlerts`, `rooms`, `messaging` and `adminBatchJobs`  (for Compliance Officers and messages with file attachments only - see [inline file DLP](/docs/api/guides/webex-real-time-file-dlp-basics)) resources."
            }
          },
          "$$ref": "#/components/schemas/Webhook"
        }
      }
    },
    "$$ref": "#/components/schemas/WebhookCollectionResponse"
  }
  ```
- **`400`** — Bad Request: The request was invalid or cannot be otherwise served. An accompanying error message will explain further.
- **`401`** — Unauthorized: Authentication credentials were missing or incorrect.
- **`403`** — Forbidden: The request is understood, but it has been refused or access is not allowed.
- **`404`** — Not Found: The URI requested is invalid or the resource requested, such as a user, does not exist. Also returned when the requested format is not supported by the requested method.
- **`405`** — Method Not Allowed: The request was made to a resource using an HTTP request method that is not supported.
- **`409`** — Conflict: The request could not be processed because it conflicts with some established rule of the system. For example, a person may not be added to a room more than once.
- **`410`** — Gone: The requested resource is no longer available.
- **`415`** — Unsupported Media Type: The request was made to a resource without specifying a media type or used a media type that is not supported.
- **`423`** — Locked: The requested resource is temporarily unavailable. A Retry-After header may be present that specifies how many seconds you need to wait before attempting the request again.
- **`428`** — Precondition Required: File(s) cannot be scanned for malware and need to be force downloaded.
- **`429`** — Too Many Requests: Too many requests have been sent in a given amount of time and the request has been rate limited. A Retry-After header should be present that specifies how many seconds you need to wait before a successful request can be made.
- **`500`** — Internal Server Error: Something went wrong on the server. If the issue persists, feel free to contact the [Webex Developer Support team](/explore/support).
- **`502`** — Bad Gateway: The server received an invalid response from an upstream server while processing the request. Try again later.
- **`503`** — Service Unavailable: Server is overloaded with requests. Try again later.
- **`504`** — Gateway Timeout: An upstream server failed to respond on time. If your query uses max parameter, please try to reduce it.

---

### 12.5 Webhooks: Update a Webhook

**Endpoint:** `PUT /webhooks/{webhookId}`

Updates a webhook, by ID. You cannot use this call to deactivate a webhook, only to activate a webhook that was auto deactivated.
The fields that can be updated are `name`, `targetURL`, `secret` and `status`. All other fields, if supplied, are ignored.

Specify the webhook ID in the `webhookId` parameter in the URI.

#### Parameters

| Name | In | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| `webhookId` | `path` | `string` | Yes | The unique identifier for the webhook. |

#### Request Body Schema

```json
{
  "type": "object",
  "required": [
    "name",
    "targetUrl"
  ],
  "properties": {
    "name": {
      "type": "string",
      "example": "My Awesome Webhook",
      "description": "A user-friendly name for the webhook."
    },
    "targetUrl": {
      "type": "string",
      "example": "https://example.com/mywebhook",
      "description": "URL that receives POST requests for each event."
    },
    "secret": {
      "type": "string",
      "example": "86dacc007724d8ea666f88fc77d918dad9537a15",
      "description": "Secret used to generate payload signature."
    },
    "ownedBy": {
      "type": "string",
      "example": "org",
      "description": "Specify `org` when creating an org/admin level webhook. Supported for `meetings`, `recordings`, `convergedRecordings`, `meetingParticipants`, `meetingTranscripts`, `videoMeshAlerts`, `controlHubAlerts`, `rooms`, `messaging` and `adminBatchJobs`  (for Compliance Officers and messages with file attachments only - see [inline file DLP](/docs/api/guides/webex-real-time-file-dlp-basics)) resources."
    },
    "status": {
      "type": "string",
      "enum": [
        "active"
      ],
      "description": "Status of the webhook. Use \"active\" to reactivate a disabled webhook."
    }
  }
}
```

#### Responses

- **`200`** — OK
  ```json
  {
    "type": "object",
    "properties": {
      "id": {
        "type": "string",
        "example": "Y2lzY29zcGFyazovL3VzL1dFQkhPT0svOTZhYmMyYWEtM2RjYy0xMWU1LWExNTItZmUzNDgxOWNkYzlh",
        "description": "A unique identifier for the webhook."
      },
      "name": {
        "type": "string",
        "example": "My Awesome Webhook",
        "description": "A user-friendly name for the webhook."
      },
      "targetUrl": {
        "type": "string",
        "example": "https://example.com/mywebhook",
        "description": "URL that receives POST requests for each event."
      },
      "resource": {
        "type": "string",
        "enum": [
          "attachmentActions",
          "dataSources",
          "memberships",
          "messages",
          "rooms",
          "meetings",
          "recordings",
          "convergedRecordings",
          "meetingParticipants",
          "meetingTranscripts",
          "telephony_calls",
          "telephony_conference",
          "telephony_mwi",
          "uc_counters",
          "serviceApp",
          "adminBatchJobs"
        ],
        "description": "Resource type for the webhook. Creating a webhook requires 'read' scope on the resource the webhook is for.\n * `attachmentActions` - [Attachment Actions](/docs/api/v1/attachment-actions) resource.\n * `dataSources` - [data sources](/docs/api/v1/data-sources) resource.\n * `memberships` - [Memberships](/docs/api/v1/memberships) resource.\n * `messages` - [Messages](/docs/api/v1/messages) resource.\n * `rooms` - [Rooms](/docs/api/v1/rooms) resource.\n * `meetings` - [Meetings](/docs/api/v1/meetings) resource.\n * `recordings` - [Recordings](/docs/api/v1/recordings) resource.\n * `convergedRecordings` - [CallRecordings](/docs/api/v1/converged-recordings) resource.\n * `meetingParticipants` - [Meeting Participants](/docs/api/v1/meeting-participants) resource.\n * `meetingTranscripts` - [Meeting Transcripts](/docs/api/v1/meeting-transcripts) resource.\n * `telephony_calls` - [Webex Calling](/docs/webex-calling-overview) call resources.\n * `telephony_conference` - [Webex Calling](/docs/webex-calling-overview) conference controls resource.\n * `telephony_mwi` - [Webex Calling](/docs/webex-calling-overview) voicemail message waiting indicator resource.\n * `uc_counters` - Performance counter for a dedicated instance.\n * `serviceApp` - Service App authorization notification.\n * `adminBatchJobs` - Admin Batch Jobs notification.\n"
      },
      "event": {
        "type": "string",
        "enum": [
          "created",
          "updated",
          "deleted",
          "started",
          "ended",
          "joined",
          "left",
          "migrated",
          "authorized",
          "deauthorized",
          "statusChanged"
        ],
        "description": "Event type for the webhook.\n * `created` - An object was created.\n * `updated` - An object was updated.\n * `deleted` - An object was deleted.\n * `started` - A meeting was started.\n * `ended` - A meeting was ended.\n * `joined` - A participant joined.\n * `left` - A participant left.\n * `migrated` - A room was migrated to a different geography. The roomId has changed.\n * `authorized` - A Service App was authorized.\n * `deauthorized` - A Service App was deauthorized.\n * `statusChanged` - Status of admin batch job was changed.\n"
      },
      "filter": {
        "type": "string",
        "example": "roomId=Y2lzY29zcGFyazovL3VzL1JPT00vYmJjZWIxYWQtNDNmMS0zYjU4LTkxNDctZjE0YmIwYzRkMTU0",
        "description": "Filter that defines the webhook scope."
      },
      "secret": {
        "type": "string",
        "example": "86dacc007724d8ea666f88fc77d918dad9537a15",
        "description": "Secret used to generate payload signature."
      },
      "status": {
        "type": "string",
        "enum": [
          "active",
          "inactive"
        ],
        "description": "Status of the webhook. Use `active` to reactivate a disabled webhook.\n * `active` - Webhook is active.\n * `inactive` - Webhook is inactive.\n"
      },
      "created": {
        "type": "string",
        "example": "2015-10-18T14:26:16+00:00",
        "description": "Date and time the webhook was created."
      },
      "ownedBy": {
        "type": "string",
        "example": "org",
        "description": "Specify `org` when creating an org/admin level webhook. Supported for `meetings`, `recordings`, `convergedRecordings`, `meetingParticipants`, `meetingTranscripts`, `videoMeshAlerts`, `controlHubAlerts`, `rooms`, `messaging` and `adminBatchJobs`  (for Compliance Officers and messages with file attachments only - see [inline file DLP](/docs/api/guides/webex-real-time-file-dlp-basics)) resources."
      }
    },
    "$$ref": "#/components/schemas/Webhook"
  }
  ```
- **`400`** — Bad Request: The request was invalid or cannot be otherwise served. An accompanying error message will explain further.
- **`401`** — Unauthorized: Authentication credentials were missing or incorrect.
- **`403`** — Forbidden: The request is understood, but it has been refused or access is not allowed.
- **`404`** — Not Found: The URI requested is invalid or the resource requested, such as a user, does not exist. Also returned when the requested format is not supported by the requested method.
- **`405`** — Method Not Allowed: The request was made to a resource using an HTTP request method that is not supported.
- **`409`** — Conflict: The request could not be processed because it conflicts with some established rule of the system. For example, a person may not be added to a room more than once.
- **`410`** — Gone: The requested resource is no longer available.
- **`415`** — Unsupported Media Type: The request was made to a resource without specifying a media type or used a media type that is not supported.
- **`423`** — Locked: The requested resource is temporarily unavailable. A Retry-After header may be present that specifies how many seconds you need to wait before attempting the request again.
- **`428`** — Precondition Required: File(s) cannot be scanned for malware and need to be force downloaded.
- **`429`** — Too Many Requests: Too many requests have been sent in a given amount of time and the request has been rate limited. A Retry-After header should be present that specifies how many seconds you need to wait before a successful request can be made.
- **`500`** — Internal Server Error: Something went wrong on the server. If the issue persists, feel free to contact the [Webex Developer Support team](/explore/support).
- **`502`** — Bad Gateway: The server received an invalid response from an upstream server while processing the request. Try again later.
- **`503`** — Service Unavailable: Server is overloaded with requests. Try again later.
- **`504`** — Gateway Timeout: An upstream server failed to respond on time. If your query uses max parameter, please try to reduce it.

---
