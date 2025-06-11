# Differences between fields in Close.io


## Opportunity

| Entity Schema Title | Entity Schema Fields | Entity Schema Types | Readonly | Possible Values | Reference Collection | Find By ID Object Fields | Find By ID Types |
|---------------------|----------------------|---------------------|----------|-----------------|----------------------|--------------------------|------------------|
|  | annualized_expected_value | integer |  |  |  | annualized_expected_value | int |
|  | annualized_value | integer |  |  |  | annualized_value | int |
|  | confidence | integer |  |  |  | confidence | int |
| Contact | contact_id | string |  |  | contact | contact_id | str |
|  | created_by | string |  |  | user | created_by | str |
|  | date_created | string |  |  |  | date_created | str |
|  | date_updated | string |  |  |  | date_updated | str |
|  | date_won | string |  |  |  | date_won | str |
|  | expected_value | integer |  |  |  | expected_value | int |
|  | id | string | true |  |  | id | str |
| Lead | *lead_id | string |  |  | lead | lead_id | str |
|  | lead_name | string |  |  |  | lead_name | str |
|  | note | string |  |  |  | note | str |
|  | organization_id | string |  |  |  | organization_id | str |
|  | status_id | string |  |  | opportunity-status | status_id | str |
|  | status_label | string |  |  |  | status_label | str |
|  | status_type | string |  |  |  | status_type | str |
|  | updated_by | string |  |  | user | updated_by | str |
| User | user_id | string |  |  | user | user_id | str |
|  | user_name | string |  |  |  | user_name | str |
|  | value | integer |  |  |  | value | int |
|  | value_currency | string |  |  |  | value_currency | str |
|  | value_formatted | string |  |  |  | value_formatted | str |
|  | value_period | string |  |  |  | value_period | str |
|  |  |  |  |  |  | attachments | array |
|  |  |  |  |  |  | attachments[] | array |
|  |  |  |  |  |  | contact_name | str |
|  |  |  |  |  |  | created_by_name | str |
|  |  |  |  |  |  | date_lost | null |
|  |  |  |  |  |  | integration_links | array |
|  |  |  |  |  |  | integration_links[] | array |
|  |  |  |  |  |  | integration_links[].name | object |
|  |  |  |  |  |  | integration_links[].url | object |
|  |  |  |  |  |  | pipeline_id | str |
|  |  |  |  |  |  | pipeline_name | str |
|  |  |  |  |  |  | status_display_name | str |
|  |  |  |  |  |  | updated_by_name | str |

## Lead

| Entity Schema Title | Entity Schema Fields | Entity Schema Types | Readonly | Possible Values | Reference Collection | Find By ID Object Fields | Find By ID Types |
|---------------------|----------------------|---------------------|----------|-----------------|----------------------|--------------------------|------------------|
|  | addresses | array |  |  |  | addresses | array |
|  | addresses[] | object |  |  |  | addresses[] | array |
|  | created_by | string |  |  | user | created_by | str |
|  | date_created | string |  |  |  | date_created | str |
|  | date_updated | string |  |  |  | date_updated | str |
|  | description | string |  |  |  | description | str |
|  | html_url | string |  |  |  | html_url | str |
|  | id | string | true |  |  | id | str |
|  | name | string |  |  |  | name | str |
|  | status_id | string |  |  | lead-status | status_id | str |
|  | updated_by | string |  |  | user | updated_by | str |
|  | url | string |  |  |  | url | null |
|  | <span style='color:red'>***addresses[].address_1***</span> | string |  |  |  |  |  |
|  | <span style='color:red'>***addresses[].address_2***</span> | string |  |  |  |  |  |
|  | <span style='color:red'>***addresses[].city***</span> | string |  |  |  |  |  |
|  | <span style='color:red'>***addresses[].country***</span> | string |  |  |  |  |  |
|  | <span style='color:red'>***addresses[].label***</span> | string |  |  |  |  |  |
|  | <span style='color:red'>***addresses[].state***</span> | string |  |  |  |  |  |
|  | <span style='color:red'>***addresses[].zipcode***</span> | string |  |  |  |  |  |
| CustomFieldCloseIO | <span style='color:red'>***lcf_7yX9TSz3qifWiNmca3yX5Y1zSPnil7rGRdiUUDssDnV***</span> | string |  |  |  |  |  |
|  |  |  |  |  |  | contacts | array |
|  |  |  |  |  |  | contacts[] | array |
|  |  |  |  |  |  | contacts[].created_by | object |
|  |  |  |  |  |  | contacts[].date_created | object |
|  |  |  |  |  |  | contacts[].date_updated | object |
|  |  |  |  |  |  | contacts[].display_name | object |
|  |  |  |  |  |  | contacts[].emails | object |
|  |  |  |  |  |  | contacts[].emails[] | object |
|  |  |  |  |  |  | contacts[].id | object |
|  |  |  |  |  |  | contacts[].integration_links | object |
|  |  |  |  |  |  | contacts[].integration_links[] | object |
|  |  |  |  |  |  | contacts[].integration_links[].name | str |
|  |  |  |  |  |  | contacts[].integration_links[].url |  |
|  |  |  |  |  |  | contacts[].lead_id | object |
|  |  |  |  |  |  | contacts[].name | object |
|  |  |  |  |  |  | contacts[].organization_id | object |
|  |  |  |  |  |  | contacts[].phones | object |
|  |  |  |  |  |  | contacts[].phones[] | object |
|  |  |  |  |  |  | contacts[].title | object |
|  |  |  |  |  |  | contacts[].updated_by | object |
|  |  |  |  |  |  | contacts[].urls | object |
|  |  |  |  |  |  | contacts[].urls[] | object |
|  |  |  |  |  |  | created_by_name | str |
|  |  |  |  |  |  | custom | object |
|  |  |  |  |  |  | display_name | str |
|  |  |  |  |  |  | integration_links | array |
|  |  |  |  |  |  | integration_links[] | array |
|  |  |  |  |  |  | opportunities | array |
|  |  |  |  |  |  | opportunities[] | array |
|  |  |  |  |  |  | opportunities[].annualized_expected_value | object |
|  |  |  |  |  |  | opportunities[].annualized_value | object |
|  |  |  |  |  |  | opportunities[].attachments | object |
|  |  |  |  |  |  | opportunities[].attachments[] | object |
|  |  |  |  |  |  | opportunities[].confidence | object |
|  |  |  |  |  |  | opportunities[].contact_id | object |
|  |  |  |  |  |  | opportunities[].contact_name | object |
|  |  |  |  |  |  | opportunities[].created_by | object |
|  |  |  |  |  |  | opportunities[].created_by_name | object |
|  |  |  |  |  |  | opportunities[].date_created | object |
|  |  |  |  |  |  | opportunities[].date_lost | object |
|  |  |  |  |  |  | opportunities[].date_updated | object |
|  |  |  |  |  |  | opportunities[].date_won | object |
|  |  |  |  |  |  | opportunities[].expected_value | object |
|  |  |  |  |  |  | opportunities[].id | object |
|  |  |  |  |  |  | opportunities[].integration_links | object |
|  |  |  |  |  |  | opportunities[].integration_links[] | object |
|  |  |  |  |  |  | opportunities[].integration_links[].name |  |
|  |  |  |  |  |  | opportunities[].integration_links[].url |  |
|  |  |  |  |  |  | opportunities[].lead_id | object |
|  |  |  |  |  |  | opportunities[].lead_name | object |
|  |  |  |  |  |  | opportunities[].note | object |
|  |  |  |  |  |  | opportunities[].organization_id | object |
|  |  |  |  |  |  | opportunities[].pipeline_id | object |
|  |  |  |  |  |  | opportunities[].pipeline_name | object |
|  |  |  |  |  |  | opportunities[].status_display_name | object |
|  |  |  |  |  |  | opportunities[].status_id | object |
|  |  |  |  |  |  | opportunities[].status_label | object |
|  |  |  |  |  |  | opportunities[].status_type | object |
|  |  |  |  |  |  | opportunities[].updated_by | object |
|  |  |  |  |  |  | opportunities[].updated_by_name | object |
|  |  |  |  |  |  | opportunities[].user_id | object |
|  |  |  |  |  |  | opportunities[].user_name | object |
|  |  |  |  |  |  | opportunities[].value | object |
|  |  |  |  |  |  | opportunities[].value_currency | object |
|  |  |  |  |  |  | opportunities[].value_formatted | object |
|  |  |  |  |  |  | opportunities[].value_period | object |
|  |  |  |  |  |  | organization_id | str |
|  |  |  |  |  |  | status_label | str |
|  |  |  |  |  |  | tasks | array |
|  |  |  |  |  |  | tasks[] | array |
|  |  |  |  |  |  | updated_by_name | str |

## Contact

| Entity Schema Title | Entity Schema Fields | Entity Schema Types | Readonly | Possible Values | Reference Collection | Find By ID Object Fields | Find By ID Types |
|---------------------|----------------------|---------------------|----------|-----------------|----------------------|--------------------------|------------------|
|  | created_by | string |  |  | user | created_by | str |
|  | date_created | string |  |  |  | date_created | str |
|  | date_updated | string |  |  |  | date_updated | str |
|  | emails | array |  |  |  | emails | array |
|  | emails[] | object |  |  |  | emails[] | array |
|  | id | string | true |  |  | id | str |
| Lead | lead_id | string |  |  | lead | lead_id | str |
|  | name | string |  |  |  | name | str |
|  | organization_id | string |  |  |  | organization_id | str |
|  | phones | array |  |  |  | phones | array |
|  | phones[] | object |  |  |  | phones[] | array |
|  | title | string |  |  |  | title | null |
|  | updated_by | string |  |  | user | updated_by | str |
|  | urls | array |  |  |  | urls | array |
|  | urls[] | object |  |  |  | urls[] | array |
|  | <span style='color:red'>***email***</span> | string |  |  |  |  |  |
|  | <span style='color:red'>***emails[].email***</span> | string |  |  |  |  |  |
|  | <span style='color:red'>***emails[].type***</span> | string |  |  |  |  |  |
|  | <span style='color:red'>***phones[].phone***</span> | string |  |  |  |  |  |
|  | <span style='color:red'>***phones[].type***</span> | string |  |  |  |  |  |
|  | <span style='color:red'>***urls[].type***</span> | string |  |  |  |  |  |
|  | <span style='color:red'>***urls[].url***</span> | string |  |  |  |  |  |
|  |  |  |  |  |  | display_name | str |
|  |  |  |  |  |  | integration_links | array |
|  |  |  |  |  |  | integration_links[] | array |
|  |  |  |  |  |  | integration_links[].name | object |
|  |  |  |  |  |  | integration_links[].url | object |