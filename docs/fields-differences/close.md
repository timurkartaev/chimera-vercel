# Differences between fields in Close.io


## Opportunity

| Entity Schema Title | Entity Schema Fields | Entity Schema Types | Readonly | Possible Values | Reference Collection | Find By ID Object Fields | Find By ID Types | Value |
|---------------------|----------------------|---------------------|----------|-----------------|----------------------|--------------------------|------------------|-------|
|  | annualized_expected_value | integer | false |  |  | annualized_expected_value | integer | 5000000 |
|  | annualized_value | integer | false |  |  | annualized_value | integer | 10000000 |
|  | confidence | integer | false |  |  | confidence | integer | 50 |
| Contact | contact_id | string | false |  | contact | contact_id | string | cont_Ga5TgqZ8RIEuhxrhIn0lnULpfpjzWoqoi5R8YG6JVR4 |
|  | created_by | string | false |  | user | created_by | string | user_GKlMqFGtoWUGwXEowlvV0N8emnTcgV2PHDnqKg4ks8c |
|  | date_created | string | false |  |  | date_created | string | 2025-06-09T13:06:32.277000+00:00 |
|  | date_updated | string | false |  |  | date_updated | string | 2025-06-09T13:06:32.277000+00:00 |
|  | date_won | string | false |  |  | date_won | string | 2025-09-18 |
|  | expected_value | integer | false |  |  | expected_value | integer | 5000000 |
|  | id | string | true |  |  | id | string | oppo_nbV15NALNPtNFPTLOp8gXG5BFT7f8xUE4NeuQ4xoz2l |
| Lead | *lead_id | string | false |  | lead | lead_id | string | lead_HcmG4cyICfAIu1J0sRziNKe63cbNaifOxZZ0PppgksW |
|  | lead_name | string | false |  |  | lead_name | string | Test Lead |
|  | note | string | false |  |  | note | string | Test |
|  | organization_id | string | false |  |  | organization_id | string | orga_gNFL1woApqkIrs9v9nZzZRALJMdvnlXmUuPi7VVxYZP |
|  | status_id | string | false |  | opportunity-status | status_id | string | stat_2ALoqfMtw2P6OHAWOen0zEpaZk01I7Y1attZZIoCmWH |
|  | status_label | string | false |  |  | status_label | string | Active |
|  | status_type | string | false |  |  | status_type | string | active |
|  | updated_by | string | false |  | user | updated_by | string | user_GKlMqFGtoWUGwXEowlvV0N8emnTcgV2PHDnqKg4ks8c |
| User | user_id | string | false |  | user | user_id | string | user_GKlMqFGtoWUGwXEowlvV0N8emnTcgV2PHDnqKg4ks8c |
|  | user_name | string | false |  |  | user_name | string | PandaDoc Development |
|  | value | integer | false |  |  | value | integer | 10000000 |
|  | value_currency | string | false |  |  | value_currency | string | USD |
|  | value_formatted | string | false |  |  | value_formatted | string | $100,000 |
|  | value_period | string | false |  |  | value_period | string | one_time |
|  |  |  |  |  |  | attachments | array | [] |
|  |  |  |  |  |  | contact_name | string | Doniyor Rufatov |
|  |  |  |  |  |  | created_by_name | string | PandaDoc Development |
|  |  |  |  |  |  | date_lost | null | None |
|  |  |  |  |  |  | integration_links | array | [{"name": "Send Document via PandaDoc", "url": "http://localhost:8001/integrations/closeio/new?opportunity=oppo_nbV15NALNPtNFPTLOp8gXG5BFT7f8xUE4NeuQ4xoz2l"}, {"name": "Send Document via PandaDoc", "url": "https://app.stg-int.sealdocs.com/integrations/closeio/new?opportunity=oppo_nbV15NALNPtNFPTLOp8gXG5BFT7f8xUE4NeuQ4xoz2l"}, {"name": "Send Document via PandaDoc", "url": "https://app.pandadoc.com/integrations/closeio/new?opportunity=oppo_nbV15NALNPtNFPTLOp8gXG5BFT7f8xUE4NeuQ4xoz2l"}] |
|  |  |  |  |  |  | integration_links[] | object |  |
|  |  |  |  |  |  | integration_links[].name | string |  |
|  |  |  |  |  |  | integration_links[].url | string |  |
|  |  |  |  |  |  | pipeline_id | string | pipe_0g9Z9TvZV5VkJyRbsZ6jjI |
|  |  |  |  |  |  | pipeline_name | string | Sales |
|  |  |  |  |  |  | status_display_name | string | Active |
|  |  |  |  |  |  | updated_by_name | string | PandaDoc Development |

## Lead

| Entity Schema Title | Entity Schema Fields | Entity Schema Types | Readonly | Possible Values | Reference Collection | Find By ID Object Fields | Find By ID Types | Value |
|---------------------|----------------------|---------------------|----------|-----------------|----------------------|--------------------------|------------------|-------|
|  | addresses | array | false |  |  | addresses | array | [] |
|  | addresses[] | object | false |  |  | addresses[] | object |  |
|  | addresses[].address_1 | string | false |  |  | addresses[].address_1 | string |  |
|  | addresses[].address_2 | string | false |  |  | addresses[].address_2 | string |  |
|  | addresses[].city | string | false |  |  | addresses[].city | string |  |
|  | addresses[].country | string | false |  |  | addresses[].country | string |  |
|  | addresses[].label | string | false |  |  | addresses[].label | string |  |
|  | addresses[].state | string | false |  |  | addresses[].state | string |  |
|  | addresses[].zipcode | string | false |  |  | addresses[].zipcode | string |  |
|  | created_by | string | false |  | user | created_by | string | user_GKlMqFGtoWUGwXEowlvV0N8emnTcgV2PHDnqKg4ks8c |
|  | date_created | string | false |  |  | date_created | string | 2025-06-09T13:05:47.220000+00:00 |
|  | date_updated | string | false |  |  | date_updated | string | 2025-06-09T13:05:47.242000+00:00 |
|  | description | string | false |  |  | description | string |  |
|  | html_url | string | false |  |  | html_url | string | https://app.close.com/lead/lead_HcmG4cyICfAIu1J0sRziNKe63cbNaifOxZZ0PppgksW/ |
|  | id | string | true |  |  | id | string | lead_HcmG4cyICfAIu1J0sRziNKe63cbNaifOxZZ0PppgksW |
|  | name | string | false |  |  | name | string | Test Lead |
|  | status_id | string | false |  | lead-status | status_id | string | stat_b31EZ3X2aBjJbmIAc2rdYLjxU81368l2qkLsb1hSILf |
|  | updated_by | string | false |  | user | updated_by | string | user_GKlMqFGtoWUGwXEowlvV0N8emnTcgV2PHDnqKg4ks8c |
|  | url | string | false |  |  | url | null | None |
| CustomFieldCloseIO | <span style='color:red'>***lcf_7yX9TSz3qifWiNmca3yX5Y1zSPnil7rGRdiUUDssDnV***</span> | string | false |  |  |  |  |  |
|  |  |  |  |  |  | contacts | array | [{"created_by": "user_GKlMqFGtoWUGwXEowlvV0N8emnTcgV2PHDnqKg4ks8c", "date_created": "2025-06-09T13:05:47.235000+00:00", "date_updated": "2025-06-09T13:05:47.235000+00:00", "display_name": "Doniyor Rufatov", "emails": [], "id": "cont_Ga5TgqZ8RIEuhxrhIn0lnULpfpjzWoqoi5R8YG6JVR4", "integration_links": [{"name": "Send Document via PandaDoc", "url": "http://localhost:8001/integrations/closeio/new?contact=cont_Ga5TgqZ8RIEuhxrhIn0lnULpfpjzWoqoi5R8YG6JVR4"}, {"name": "Send Document via PandaDoc", "url": "https://app.stg-int.sealdocs.com/integrations/closeio/new?contact=cont_Ga5TgqZ8RIEuhxrhIn0lnULpfpjzWoqoi5R8YG6JVR4"}, {"name": "Send Document via PandaDoc", "url": "https://app.pandadoc.com/integrations/closeio/new?contact=cont_Ga5TgqZ8RIEuhxrhIn0lnULpfpjzWoqoi5R8YG6JVR4"}], "lead_id": "lead_HcmG4cyICfAIu1J0sRziNKe63cbNaifOxZZ0PppgksW", "name": "Doniyor Rufatov", "organization_id": "orga_gNFL1woApqkIrs9v9nZzZRALJMdvnlXmUuPi7VVxYZP", "phones": [], "title": null, "updated_by": "user_GKlMqFGtoWUGwXEowlvV0N8emnTcgV2PHDnqKg4ks8c", "urls": []}] |
|  |  |  |  |  |  | contacts[] | object |  |
|  |  |  |  |  |  | contacts[].created_by | string |  |
|  |  |  |  |  |  | contacts[].date_created | string |  |
|  |  |  |  |  |  | contacts[].date_updated | string |  |
|  |  |  |  |  |  | contacts[].display_name | string |  |
|  |  |  |  |  |  | contacts[].emails | array |  |
|  |  |  |  |  |  | contacts[].id | string |  |
|  |  |  |  |  |  | contacts[].integration_links | array |  |
|  |  |  |  |  |  | contacts[].integration_links[] | object |  |
|  |  |  |  |  |  | contacts[].integration_links[].name | string |  |
|  |  |  |  |  |  | contacts[].integration_links[].url | string |  |
|  |  |  |  |  |  | contacts[].lead_id | string |  |
|  |  |  |  |  |  | contacts[].name | string |  |
|  |  |  |  |  |  | contacts[].organization_id | string |  |
|  |  |  |  |  |  | contacts[].phones | array |  |
|  |  |  |  |  |  | contacts[].title | null |  |
|  |  |  |  |  |  | contacts[].updated_by | string |  |
|  |  |  |  |  |  | contacts[].urls | array |  |
|  |  |  |  |  |  | created_by_name | string | PandaDoc Development |
|  |  |  |  |  |  | custom | object | {} |
|  |  |  |  |  |  | display_name | string | Test Lead |
|  |  |  |  |  |  | integration_links | array | [] |
|  |  |  |  |  |  | opportunities | array | [{"annualized_expected_value": 5000000, "annualized_value": 10000000, "attachments": [], "confidence": 50, "contact_id": "cont_Ga5TgqZ8RIEuhxrhIn0lnULpfpjzWoqoi5R8YG6JVR4", "contact_name": "Doniyor Rufatov", "created_by": "user_GKlMqFGtoWUGwXEowlvV0N8emnTcgV2PHDnqKg4ks8c", "created_by_name": "PandaDoc Development", "date_created": "2025-06-09T13:06:32.277000+00:00", "date_lost": null, "date_updated": "2025-06-09T13:06:32.277000+00:00", "date_won": "2025-09-18", "expected_value": 5000000, "id": "oppo_nbV15NALNPtNFPTLOp8gXG5BFT7f8xUE4NeuQ4xoz2l", "integration_links": [{"name": "Send Document via PandaDoc", "url": "http://localhost:8001/integrations/closeio/new?opportunity=oppo_nbV15NALNPtNFPTLOp8gXG5BFT7f8xUE4NeuQ4xoz2l"}, {"name": "Send Document via PandaDoc", "url": "https://app.stg-int.sealdocs.com/integrations/closeio/new?opportunity=oppo_nbV15NALNPtNFPTLOp8gXG5BFT7f8xUE4NeuQ4xoz2l"}, {"name": "Send Document via PandaDoc", "url": "https://app.pandadoc.com/integrations/closeio/new?opportunity=oppo_nbV15NALNPtNFPTLOp8gXG5BFT7f8xUE4NeuQ4xoz2l"}], "lead_id": "lead_HcmG4cyICfAIu1J0sRziNKe63cbNaifOxZZ0PppgksW", "lead_name": "Test Lead", "note": "Test", "organization_id": "orga_gNFL1woApqkIrs9v9nZzZRALJMdvnlXmUuPi7VVxYZP", "pipeline_id": "pipe_0g9Z9TvZV5VkJyRbsZ6jjI", "pipeline_name": "Sales", "status_display_name": "Active", "status_id": "stat_2ALoqfMtw2P6OHAWOen0zEpaZk01I7Y1attZZIoCmWH", "status_label": "Active", "status_type": "active", "updated_by": "user_GKlMqFGtoWUGwXEowlvV0N8emnTcgV2PHDnqKg4ks8c", "updated_by_name": "PandaDoc Development", "user_id": "user_GKlMqFGtoWUGwXEowlvV0N8emnTcgV2PHDnqKg4ks8c", "user_name": "PandaDoc Development", "value": 10000000, "value_currency": "USD", "value_formatted": "$100,000", "value_period": "one_time"}] |
|  |  |  |  |  |  | opportunities[] | object |  |
|  |  |  |  |  |  | opportunities[].annualized_expected_value | integer |  |
|  |  |  |  |  |  | opportunities[].annualized_value | integer |  |
|  |  |  |  |  |  | opportunities[].attachments | array |  |
|  |  |  |  |  |  | opportunities[].confidence | integer |  |
|  |  |  |  |  |  | opportunities[].contact_id | string |  |
|  |  |  |  |  |  | opportunities[].contact_name | string |  |
|  |  |  |  |  |  | opportunities[].created_by | string |  |
|  |  |  |  |  |  | opportunities[].created_by_name | string |  |
|  |  |  |  |  |  | opportunities[].date_created | string |  |
|  |  |  |  |  |  | opportunities[].date_lost | null |  |
|  |  |  |  |  |  | opportunities[].date_updated | string |  |
|  |  |  |  |  |  | opportunities[].date_won | string |  |
|  |  |  |  |  |  | opportunities[].expected_value | integer |  |
|  |  |  |  |  |  | opportunities[].id | string |  |
|  |  |  |  |  |  | opportunities[].integration_links | array |  |
|  |  |  |  |  |  | opportunities[].integration_links[] | object |  |
|  |  |  |  |  |  | opportunities[].integration_links[].name | string |  |
|  |  |  |  |  |  | opportunities[].integration_links[].url | string |  |
|  |  |  |  |  |  | opportunities[].lead_id | string |  |
|  |  |  |  |  |  | opportunities[].lead_name | string |  |
|  |  |  |  |  |  | opportunities[].note | string |  |
|  |  |  |  |  |  | opportunities[].organization_id | string |  |
|  |  |  |  |  |  | opportunities[].pipeline_id | string |  |
|  |  |  |  |  |  | opportunities[].pipeline_name | string |  |
|  |  |  |  |  |  | opportunities[].status_display_name | string |  |
|  |  |  |  |  |  | opportunities[].status_id | string |  |
|  |  |  |  |  |  | opportunities[].status_label | string |  |
|  |  |  |  |  |  | opportunities[].status_type | string |  |
|  |  |  |  |  |  | opportunities[].updated_by | string |  |
|  |  |  |  |  |  | opportunities[].updated_by_name | string |  |
|  |  |  |  |  |  | opportunities[].user_id | string |  |
|  |  |  |  |  |  | opportunities[].user_name | string |  |
|  |  |  |  |  |  | opportunities[].value | integer |  |
|  |  |  |  |  |  | opportunities[].value_currency | string |  |
|  |  |  |  |  |  | opportunities[].value_formatted | string |  |
|  |  |  |  |  |  | opportunities[].value_period | string |  |
|  |  |  |  |  |  | organization_id | string | orga_gNFL1woApqkIrs9v9nZzZRALJMdvnlXmUuPi7VVxYZP |
|  |  |  |  |  |  | status_label | string | Potential |
|  |  |  |  |  |  | tasks | array | [] |
|  |  |  |  |  |  | updated_by_name | string | PandaDoc Development |

## Contact

| Entity Schema Title | Entity Schema Fields | Entity Schema Types | Readonly | Possible Values | Reference Collection | Find By ID Object Fields | Find By ID Types | Value |
|---------------------|----------------------|---------------------|----------|-----------------|----------------------|--------------------------|------------------|-------|
|  | created_by | string | false |  | user | created_by | string | user_GKlMqFGtoWUGwXEowlvV0N8emnTcgV2PHDnqKg4ks8c |
|  | date_created | string | false |  |  | date_created | string | 2025-06-09T13:05:47.235000+00:00 |
|  | date_updated | string | false |  |  | date_updated | string | 2025-06-09T13:05:47.235000+00:00 |
|  | emails | array | false |  |  | emails | array | [] |
|  | emails[] | object | false |  |  | emails[] | object |  |
|  | emails[].email | string | false |  |  | emails[].email | string |  |
|  | emails[].type | string | false |  |  | emails[].type | string |  |
|  | id | string | true |  |  | id | string | cont_Ga5TgqZ8RIEuhxrhIn0lnULpfpjzWoqoi5R8YG6JVR4 |
| Lead | lead_id | string | false |  | lead | lead_id | string | lead_HcmG4cyICfAIu1J0sRziNKe63cbNaifOxZZ0PppgksW |
|  | name | string | false |  |  | name | string | Doniyor Rufatov |
|  | organization_id | string | false |  |  | organization_id | string | orga_gNFL1woApqkIrs9v9nZzZRALJMdvnlXmUuPi7VVxYZP |
|  | phones | array | false |  |  | phones | array | [] |
|  | phones[] | object | false |  |  | phones[] | object |  |
|  | phones[].phone | string | false |  |  | phones[].phone | string |  |
|  | phones[].type | string | false |  |  | phones[].type | string |  |
|  | title | string | false |  |  | title | null | None |
|  | updated_by | string | false |  | user | updated_by | string | user_GKlMqFGtoWUGwXEowlvV0N8emnTcgV2PHDnqKg4ks8c |
|  | urls | array | false |  |  | urls | array | [] |
|  | urls[] | object | false |  |  | urls[] | object |  |
|  | urls[].type | string | false |  |  | urls[].type | string |  |
|  | urls[].url | string | false |  |  | urls[].url | string |  |
|  | <span style='color:red'>***email***</span> | string | false |  |  |  |  |  |
|  |  |  |  |  |  | display_name | string | Doniyor Rufatov |
|  |  |  |  |  |  | integration_links | array | [{"name": "Send Document via PandaDoc", "url": "http://localhost:8001/integrations/closeio/new?contact=cont_Ga5TgqZ8RIEuhxrhIn0lnULpfpjzWoqoi5R8YG6JVR4"}, {"name": "Send Document via PandaDoc", "url": "https://app.stg-int.sealdocs.com/integrations/closeio/new?contact=cont_Ga5TgqZ8RIEuhxrhIn0lnULpfpjzWoqoi5R8YG6JVR4"}, {"name": "Send Document via PandaDoc", "url": "https://app.pandadoc.com/integrations/closeio/new?contact=cont_Ga5TgqZ8RIEuhxrhIn0lnULpfpjzWoqoi5R8YG6JVR4"}] |
|  |  |  |  |  |  | integration_links[] | object |  |
|  |  |  |  |  |  | integration_links[].name | string |  |
|  |  |  |  |  |  | integration_links[].url | string |  |