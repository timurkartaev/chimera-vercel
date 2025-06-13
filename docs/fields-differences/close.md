# Differences between fields in Close.io


## Opportunity

| Entity Schema Title | Entity Schema Fields | Entity Schema Types | Readonly | Possible Values | Reference Collection | Find By ID Object Fields | Find By ID Types | Value |
|---------------------|----------------------|---------------------|----------|-----------------|----------------------|--------------------------|------------------|-------|
|  | annualized_expected_value | integer | false |  |  | annualized_expected_value | int | 5000000 |
|  | annualized_value | integer | false |  |  | annualized_value | int | 10000000 |
|  | confidence | integer | false |  |  | confidence | int | 50 |
| Contact | contact_id | string | false |  | contact | contact_id | str | cont_Ga5TgqZ8RIEuhxrhIn0lnULpfpjzWoqoi5R8YG6JVR4 |
|  | created_by | string | false |  | user | created_by | str | user_GKlMqFGtoWUGwXEowlvV0N8emnTcgV2PHDnqKg4ks8c |
|  | date_created | string | false |  |  | date_created | str | 2025-06-09T13:06:32.277000+00:00 |
|  | date_updated | string | false |  |  | date_updated | str | 2025-06-09T13:06:32.277000+00:00 |
|  | date_won | string | false |  |  | date_won | str | 2025-09-18 |
|  | expected_value | integer | false |  |  | expected_value | int | 5000000 |
|  | id | string | true |  |  | id | str | oppo_nbV15NALNPtNFPTLOp8gXG5BFT7f8xUE4NeuQ4xoz2l |
| Lead | *lead_id | string | false |  | lead | lead_id | str | lead_HcmG4cyICfAIu1J0sRziNKe63cbNaifOxZZ0PppgksW |
|  | lead_name | string | false |  |  | lead_name | str | Test Lead |
|  | note | string | false |  |  | note | str | Test |
|  | organization_id | string | false |  |  | organization_id | str | orga_gNFL1woApqkIrs9v9nZzZRALJMdvnlXmUuPi7VVxYZP |
|  | status_id | string | false |  | opportunity-status | status_id | str | stat_2ALoqfMtw2P6OHAWOen0zEpaZk01I7Y1attZZIoCmWH |
|  | status_label | string | false |  |  | status_label | str | Active |
|  | status_type | string | false |  |  | status_type | str | active |
|  | updated_by | string | false |  | user | updated_by | str | user_GKlMqFGtoWUGwXEowlvV0N8emnTcgV2PHDnqKg4ks8c |
| User | user_id | string | false |  | user | user_id | str | user_GKlMqFGtoWUGwXEowlvV0N8emnTcgV2PHDnqKg4ks8c |
|  | user_name | string | false |  |  | user_name | str | PandaDoc Development |
|  | value | integer | false |  |  | value | int | 10000000 |
|  | value_currency | string | false |  |  | value_currency | str | USD |
|  | value_formatted | string | false |  |  | value_formatted | str | $100,000 |
|  | value_period | string | false |  |  | value_period | str | one_time |
|  |  |  |  |  |  | attachments | array | [] |
|  |  |  |  |  |  | attachments[] | array |  |
|  |  |  |  |  |  | contact_name | str | Doniyor Rufatov |
|  |  |  |  |  |  | created_by_name | str | PandaDoc Development |
|  |  |  |  |  |  | date_lost | null | None |
|  |  |  |  |  |  | integration_links | array | [{"name": "Send Document via PandaDoc", "url": "http://localhost:8001/integrations/closeio/new?opportunity=oppo_nbV15NALNPtNFPTLOp8gXG5BFT7f8xUE4NeuQ4xoz2l"}, {"name": "Send Document via PandaDoc", "url": "https://app.stg-int.sealdocs.com/integrations/closeio/new?opportunity=oppo_nbV15NALNPtNFPTLOp8gXG5BFT7f8xUE4NeuQ4xoz2l"}, {"name": "Send Document via PandaDoc", "url": "https://app.pandadoc.com/integrations/closeio/new?opportunity=oppo_nbV15NALNPtNFPTLOp8gXG5BFT7f8xUE4NeuQ4xoz2l"}] |
|  |  |  |  |  |  | integration_links[] | array |  |
|  |  |  |  |  |  | integration_links[].name | object |  |
|  |  |  |  |  |  | integration_links[].url | object |  |
|  |  |  |  |  |  | pipeline_id | str | pipe_0g9Z9TvZV5VkJyRbsZ6jjI |
|  |  |  |  |  |  | pipeline_name | str | Sales |
|  |  |  |  |  |  | status_display_name | str | Active |
|  |  |  |  |  |  | updated_by_name | str | PandaDoc Development |

## Lead

| Entity Schema Title | Entity Schema Fields | Entity Schema Types | Readonly | Possible Values | Reference Collection | Find By ID Object Fields | Find By ID Types | Value |
|---------------------|----------------------|---------------------|----------|-----------------|----------------------|--------------------------|------------------|-------|
|  | addresses | array | false |  |  | addresses | array | [] |
|  | addresses[] | object | false |  |  | addresses[] | array |  |
|  | created_by | string | false |  | user | created_by | str | user_GKlMqFGtoWUGwXEowlvV0N8emnTcgV2PHDnqKg4ks8c |
|  | date_created | string | false |  |  | date_created | str | 2025-06-09T13:05:47.220000+00:00 |
|  | date_updated | string | false |  |  | date_updated | str | 2025-06-09T13:05:47.242000+00:00 |
|  | description | string | false |  |  | description | str |  |
|  | html_url | string | false |  |  | html_url | str | https://app.close.com/lead/lead_HcmG4cyICfAIu1J0sRziNKe63cbNaifOxZZ0PppgksW/ |
|  | id | string | true |  |  | id | str | lead_HcmG4cyICfAIu1J0sRziNKe63cbNaifOxZZ0PppgksW |
|  | name | string | false |  |  | name | str | Test Lead |
|  | status_id | string | false |  | lead-status | status_id | str | stat_b31EZ3X2aBjJbmIAc2rdYLjxU81368l2qkLsb1hSILf |
|  | updated_by | string | false |  | user | updated_by | str | user_GKlMqFGtoWUGwXEowlvV0N8emnTcgV2PHDnqKg4ks8c |
|  | url | string | false |  |  | url | null | None |
|  | <span style='color:red'>***addresses[].address_1***</span> | string | false |  |  |  |  |  |
|  | <span style='color:red'>***addresses[].address_2***</span> | string | false |  |  |  |  |  |
|  | <span style='color:red'>***addresses[].city***</span> | string | false |  |  |  |  |  |
|  | <span style='color:red'>***addresses[].country***</span> | string | false |  |  |  |  |  |
|  | <span style='color:red'>***addresses[].label***</span> | string | false |  |  |  |  |  |
|  | <span style='color:red'>***addresses[].state***</span> | string | false |  |  |  |  |  |
|  | <span style='color:red'>***addresses[].zipcode***</span> | string | false |  |  |  |  |  |
| CustomFieldCloseIO | <span style='color:red'>***lcf_7yX9TSz3qifWiNmca3yX5Y1zSPnil7rGRdiUUDssDnV***</span> | string | false |  |  |  |  |  |
|  |  |  |  |  |  | contacts | array | [{"created_by": "user_GKlMqFGtoWUGwXEowlvV0N8emnTcgV2PHDnqKg4ks8c", "date_created": "2025-06-09T13:05:47.235000+00:00", "date_updated": "2025-06-09T13:05:47.235000+00:00", "display_name": "Doniyor Rufatov", "emails": [], "id": "cont_Ga5TgqZ8RIEuhxrhIn0lnULpfpjzWoqoi5R8YG6JVR4", "integration_links": [{"name": "Send Document via PandaDoc", "url": "http://localhost:8001/integrations/closeio/new?contact=cont_Ga5TgqZ8RIEuhxrhIn0lnULpfpjzWoqoi5R8YG6JVR4"}, {"name": "Send Document via PandaDoc", "url": "https://app.stg-int.sealdocs.com/integrations/closeio/new?contact=cont_Ga5TgqZ8RIEuhxrhIn0lnULpfpjzWoqoi5R8YG6JVR4"}, {"name": "Send Document via PandaDoc", "url": "https://app.pandadoc.com/integrations/closeio/new?contact=cont_Ga5TgqZ8RIEuhxrhIn0lnULpfpjzWoqoi5R8YG6JVR4"}], "lead_id": "lead_HcmG4cyICfAIu1J0sRziNKe63cbNaifOxZZ0PppgksW", "name": "Doniyor Rufatov", "organization_id": "orga_gNFL1woApqkIrs9v9nZzZRALJMdvnlXmUuPi7VVxYZP", "phones": [], "title": null, "updated_by": "user_GKlMqFGtoWUGwXEowlvV0N8emnTcgV2PHDnqKg4ks8c", "urls": []}] |
|  |  |  |  |  |  | contacts[] | array |  |
|  |  |  |  |  |  | contacts[].created_by | object |  |
|  |  |  |  |  |  | contacts[].date_created | object |  |
|  |  |  |  |  |  | contacts[].date_updated | object |  |
|  |  |  |  |  |  | contacts[].display_name | object |  |
|  |  |  |  |  |  | contacts[].emails | object |  |
|  |  |  |  |  |  | contacts[].emails[] | object |  |
|  |  |  |  |  |  | contacts[].id | object |  |
|  |  |  |  |  |  | contacts[].integration_links | object |  |
|  |  |  |  |  |  | contacts[].integration_links[] | object |  |
|  |  |  |  |  |  | contacts[].integration_links[].name | str |  |
|  |  |  |  |  |  | contacts[].integration_links[].url |  |  |
|  |  |  |  |  |  | contacts[].lead_id | object |  |
|  |  |  |  |  |  | contacts[].name | object |  |
|  |  |  |  |  |  | contacts[].organization_id | object |  |
|  |  |  |  |  |  | contacts[].phones | object |  |
|  |  |  |  |  |  | contacts[].phones[] | object |  |
|  |  |  |  |  |  | contacts[].title | object |  |
|  |  |  |  |  |  | contacts[].updated_by | object |  |
|  |  |  |  |  |  | contacts[].urls | object |  |
|  |  |  |  |  |  | contacts[].urls[] | object |  |
|  |  |  |  |  |  | created_by_name | str | PandaDoc Development |
|  |  |  |  |  |  | custom | object | {} |
|  |  |  |  |  |  | display_name | str | Test Lead |
|  |  |  |  |  |  | integration_links | array | [] |
|  |  |  |  |  |  | integration_links[] | array |  |
|  |  |  |  |  |  | opportunities | array | [{"annualized_expected_value": 5000000, "annualized_value": 10000000, "attachments": [], "confidence": 50, "contact_id": "cont_Ga5TgqZ8RIEuhxrhIn0lnULpfpjzWoqoi5R8YG6JVR4", "contact_name": "Doniyor Rufatov", "created_by": "user_GKlMqFGtoWUGwXEowlvV0N8emnTcgV2PHDnqKg4ks8c", "created_by_name": "PandaDoc Development", "date_created": "2025-06-09T13:06:32.277000+00:00", "date_lost": null, "date_updated": "2025-06-09T13:06:32.277000+00:00", "date_won": "2025-09-18", "expected_value": 5000000, "id": "oppo_nbV15NALNPtNFPTLOp8gXG5BFT7f8xUE4NeuQ4xoz2l", "integration_links": [{"name": "Send Document via PandaDoc", "url": "http://localhost:8001/integrations/closeio/new?opportunity=oppo_nbV15NALNPtNFPTLOp8gXG5BFT7f8xUE4NeuQ4xoz2l"}, {"name": "Send Document via PandaDoc", "url": "https://app.stg-int.sealdocs.com/integrations/closeio/new?opportunity=oppo_nbV15NALNPtNFPTLOp8gXG5BFT7f8xUE4NeuQ4xoz2l"}, {"name": "Send Document via PandaDoc", "url": "https://app.pandadoc.com/integrations/closeio/new?opportunity=oppo_nbV15NALNPtNFPTLOp8gXG5BFT7f8xUE4NeuQ4xoz2l"}], "lead_id": "lead_HcmG4cyICfAIu1J0sRziNKe63cbNaifOxZZ0PppgksW", "lead_name": "Test Lead", "note": "Test", "organization_id": "orga_gNFL1woApqkIrs9v9nZzZRALJMdvnlXmUuPi7VVxYZP", "pipeline_id": "pipe_0g9Z9TvZV5VkJyRbsZ6jjI", "pipeline_name": "Sales", "status_display_name": "Active", "status_id": "stat_2ALoqfMtw2P6OHAWOen0zEpaZk01I7Y1attZZIoCmWH", "status_label": "Active", "status_type": "active", "updated_by": "user_GKlMqFGtoWUGwXEowlvV0N8emnTcgV2PHDnqKg4ks8c", "updated_by_name": "PandaDoc Development", "user_id": "user_GKlMqFGtoWUGwXEowlvV0N8emnTcgV2PHDnqKg4ks8c", "user_name": "PandaDoc Development", "value": 10000000, "value_currency": "USD", "value_formatted": "$100,000", "value_period": "one_time"}] |
|  |  |  |  |  |  | opportunities[] | array |  |
|  |  |  |  |  |  | opportunities[].annualized_expected_value | object |  |
|  |  |  |  |  |  | opportunities[].annualized_value | object |  |
|  |  |  |  |  |  | opportunities[].attachments | object |  |
|  |  |  |  |  |  | opportunities[].attachments[] | object |  |
|  |  |  |  |  |  | opportunities[].confidence | object |  |
|  |  |  |  |  |  | opportunities[].contact_id | object |  |
|  |  |  |  |  |  | opportunities[].contact_name | object |  |
|  |  |  |  |  |  | opportunities[].created_by | object |  |
|  |  |  |  |  |  | opportunities[].created_by_name | object |  |
|  |  |  |  |  |  | opportunities[].date_created | object |  |
|  |  |  |  |  |  | opportunities[].date_lost | object |  |
|  |  |  |  |  |  | opportunities[].date_updated | object |  |
|  |  |  |  |  |  | opportunities[].date_won | object |  |
|  |  |  |  |  |  | opportunities[].expected_value | object |  |
|  |  |  |  |  |  | opportunities[].id | object |  |
|  |  |  |  |  |  | opportunities[].integration_links | object |  |
|  |  |  |  |  |  | opportunities[].integration_links[] | object |  |
|  |  |  |  |  |  | opportunities[].integration_links[].name |  |  |
|  |  |  |  |  |  | opportunities[].integration_links[].url |  |  |
|  |  |  |  |  |  | opportunities[].lead_id | object |  |
|  |  |  |  |  |  | opportunities[].lead_name | object |  |
|  |  |  |  |  |  | opportunities[].note | object |  |
|  |  |  |  |  |  | opportunities[].organization_id | object |  |
|  |  |  |  |  |  | opportunities[].pipeline_id | object |  |
|  |  |  |  |  |  | opportunities[].pipeline_name | object |  |
|  |  |  |  |  |  | opportunities[].status_display_name | object |  |
|  |  |  |  |  |  | opportunities[].status_id | object |  |
|  |  |  |  |  |  | opportunities[].status_label | object |  |
|  |  |  |  |  |  | opportunities[].status_type | object |  |
|  |  |  |  |  |  | opportunities[].updated_by | object |  |
|  |  |  |  |  |  | opportunities[].updated_by_name | object |  |
|  |  |  |  |  |  | opportunities[].user_id | object |  |
|  |  |  |  |  |  | opportunities[].user_name | object |  |
|  |  |  |  |  |  | opportunities[].value | object |  |
|  |  |  |  |  |  | opportunities[].value_currency | object |  |
|  |  |  |  |  |  | opportunities[].value_formatted | object |  |
|  |  |  |  |  |  | opportunities[].value_period | object |  |
|  |  |  |  |  |  | organization_id | str | orga_gNFL1woApqkIrs9v9nZzZRALJMdvnlXmUuPi7VVxYZP |
|  |  |  |  |  |  | status_label | str | Potential |
|  |  |  |  |  |  | tasks | array | [] |
|  |  |  |  |  |  | tasks[] | array |  |
|  |  |  |  |  |  | updated_by_name | str | PandaDoc Development |

## Contact

| Entity Schema Title | Entity Schema Fields | Entity Schema Types | Readonly | Possible Values | Reference Collection | Find By ID Object Fields | Find By ID Types | Value |
|---------------------|----------------------|---------------------|----------|-----------------|----------------------|--------------------------|------------------|-------|
|  | created_by | string | false |  | user | created_by | str | user_GKlMqFGtoWUGwXEowlvV0N8emnTcgV2PHDnqKg4ks8c |
|  | date_created | string | false |  |  | date_created | str | 2025-06-09T13:05:47.235000+00:00 |
|  | date_updated | string | false |  |  | date_updated | str | 2025-06-09T13:05:47.235000+00:00 |
|  | emails | array | false |  |  | emails | array | [] |
|  | emails[] | object | false |  |  | emails[] | array |  |
|  | id | string | true |  |  | id | str | cont_Ga5TgqZ8RIEuhxrhIn0lnULpfpjzWoqoi5R8YG6JVR4 |
| Lead | lead_id | string | false |  | lead | lead_id | str | lead_HcmG4cyICfAIu1J0sRziNKe63cbNaifOxZZ0PppgksW |
|  | name | string | false |  |  | name | str | Doniyor Rufatov |
|  | organization_id | string | false |  |  | organization_id | str | orga_gNFL1woApqkIrs9v9nZzZRALJMdvnlXmUuPi7VVxYZP |
|  | phones | array | false |  |  | phones | array | [] |
|  | phones[] | object | false |  |  | phones[] | array |  |
|  | title | string | false |  |  | title | null | None |
|  | updated_by | string | false |  | user | updated_by | str | user_GKlMqFGtoWUGwXEowlvV0N8emnTcgV2PHDnqKg4ks8c |
|  | urls | array | false |  |  | urls | array | [] |
|  | urls[] | object | false |  |  | urls[] | array |  |
|  | <span style='color:red'>***email***</span> | string | false |  |  |  |  |  |
|  | <span style='color:red'>***emails[].email***</span> | string | false |  |  |  |  |  |
|  | <span style='color:red'>***emails[].type***</span> | string | false |  |  |  |  |  |
|  | <span style='color:red'>***phones[].phone***</span> | string | false |  |  |  |  |  |
|  | <span style='color:red'>***phones[].type***</span> | string | false |  |  |  |  |  |
|  | <span style='color:red'>***urls[].type***</span> | string | false |  |  |  |  |  |
|  | <span style='color:red'>***urls[].url***</span> | string | false |  |  |  |  |  |
|  |  |  |  |  |  | display_name | str | Doniyor Rufatov |
|  |  |  |  |  |  | integration_links | array | [{"name": "Send Document via PandaDoc", "url": "http://localhost:8001/integrations/closeio/new?contact=cont_Ga5TgqZ8RIEuhxrhIn0lnULpfpjzWoqoi5R8YG6JVR4"}, {"name": "Send Document via PandaDoc", "url": "https://app.stg-int.sealdocs.com/integrations/closeio/new?contact=cont_Ga5TgqZ8RIEuhxrhIn0lnULpfpjzWoqoi5R8YG6JVR4"}, {"name": "Send Document via PandaDoc", "url": "https://app.pandadoc.com/integrations/closeio/new?contact=cont_Ga5TgqZ8RIEuhxrhIn0lnULpfpjzWoqoi5R8YG6JVR4"}] |
|  |  |  |  |  |  | integration_links[] | array |  |
|  |  |  |  |  |  | integration_links[].name | object |  |
|  |  |  |  |  |  | integration_links[].url | object |  |