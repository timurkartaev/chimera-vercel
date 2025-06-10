# Differences between fields in Close.io

## Opportunity

| Entity Schema Fields      | Entity Schema Types | Find By ID Object Fields  | Find By ID Types |
|---------------------------|---------------------|---------------------------|------------------|
| annualized_expected_value | integer             | annualized_expected_value | int              |
| annualized_value          | integer             | annualized_value          | int              |
| confidence                | integer             | confidence                | int              |
| contact_id                | string              | contact_id                | str              |
| created_by                | string              | created_by                | str              |
| date_created              | string              | date_created              | str              |
| date_updated              | string              | date_updated              | str              |
| date_won                  | string              | date_won                  | str              |
| expected_value            | integer             | expected_value            | int              |
| id                        | string              | id                        | str              |
| lead_id                   | string              | lead_id                   | str              |
| lead_name                 | string              | lead_name                 | str              |
| note                      | string              | note                      | str              |
| organization_id           | string              | organization_id           | str              |
| status_id                 | string              | status_id                 | str              |
| status_label              | string              | status_label              | str              |
| status_type               | string              | status_type               | str              |
| updated_by                | string              | updated_by                | str              |
| user_id                   | string              | user_id                   | str              |
| user_name                 | string              | user_name                 | str              |
| value                     | integer             | value                     | int              |
| value_currency            | string              | value_currency            | str              |
| value_formatted           | string              | value_formatted           | str              |
| value_period              | string              | value_period              | str              |
|                           |                     | attachments[]             | array            |
|                           |                     | contact_name              | str              |
|                           |                     | created_by_name           | str              |
|                           |                     | date_lost                 | null             |
|                           |                     | integration_links[]       | array            |
|                           |                     | integration_links[].name  | object           |
|                           |                     | integration_links[].url   | object           |
|                           |                     | pipeline_id               | str              |
|                           |                     | pipeline_name             | str              |
|                           |                     | status_display_name       | str              |
|                           |                     | updated_by_name           | str              |

## Lead

| Entity Schema Fields                            | Entity Schema Types | Find By ID Object Fields                  | Find By ID Types |
|-------------------------------------------------|---------------------|-------------------------------------------|------------------|
| addresses[]                                     | object              | addresses[]                               | array            |
| created_by                                      | string              | created_by                                | str              |
| date_created                                    | string              | date_created                              | str              |
| date_updated                                    | string              | date_updated                              | str              |
| description                                     | string              | description                               | str              |
| html_url                                        | string              | html_url                                  | str              |
| id                                              | string              | id                                        | str              |
| name                                            | string              | name                                      | str              |
| status_id                                       | string              | status_id                                 | str              |
| updated_by                                      | string              | updated_by                                | str              |
| url                                             | string              | url                                       | null             |
| addresses[].address_1                           | string              |                                           |                  |
| addresses[].address_2                           | string              |                                           |                  |
| addresses[].city                                | string              |                                           |                  |
| addresses[].country                             | string              |                                           |                  |
| addresses[].label                               | string              |                                           |                  |
| addresses[].state                               | string              |                                           |                  |
| addresses[].zipcode                             | string              |                                           |                  |
| lcf_7yX9TSz3qifWiNmca3yX5Y1zSPnil7rGRdiUUDssDnV | string              |                                           |                  |
|                                                 |                     | contacts[]                                | array            |
|                                                 |                     | contacts[].created_by                     | object           |
|                                                 |                     | contacts[].date_created                   | object           |
|                                                 |                     | contacts[].date_updated                   | object           |
|                                                 |                     | contacts[].display_name                   | object           |
|                                                 |                     | contacts[].emails[]                       | object           |
|                                                 |                     | contacts[].id                             | object           |
|                                                 |                     | contacts[].integration_links[]            | object           |
|                                                 |                     | contacts[].integration_links[].name       | str              |
|                                                 |                     | contacts[].integration_links[].url        |                  |
|                                                 |                     | contacts[].lead_id                        | object           |
|                                                 |                     | contacts[].name                           | object           |
|                                                 |                     | contacts[].organization_id                | object           |
|                                                 |                     | contacts[].phones[]                       | object           |
|                                                 |                     | contacts[].title                          | object           |
|                                                 |                     | contacts[].updated_by                     | object           |
|                                                 |                     | contacts[].urls[]                         | object           |
|                                                 |                     | created_by_name                           | str              |
|                                                 |                     | display_name                              | str              |
|                                                 |                     | integration_links[]                       | array            |
|                                                 |                     | opportunities[]                           | array            |
|                                                 |                     | opportunities[].annualized_expected_value | object           |
|                                                 |                     | opportunities[].annualized_value          | object           |
|                                                 |                     | opportunities[].attachments[]             | object           |
|                                                 |                     | opportunities[].confidence                | object           |
|                                                 |                     | opportunities[].contact_id                | object           |
|                                                 |                     | opportunities[].contact_name              | object           |
|                                                 |                     | opportunities[].created_by                | object           |
|                                                 |                     | opportunities[].created_by_name           | object           |
|                                                 |                     | opportunities[].date_created              | object           |
|                                                 |                     | opportunities[].date_lost                 | object           |
|                                                 |                     | opportunities[].date_updated              | object           |
|                                                 |                     | opportunities[].date_won                  | object           |
|                                                 |                     | opportunities[].expected_value            | object           |
|                                                 |                     | opportunities[].id                        | object           |
|                                                 |                     | opportunities[].integration_links[]       | object           |
|                                                 |                     | opportunities[].integration_links[].name  |                  |
|                                                 |                     | opportunities[].integration_links[].url   |                  |
|                                                 |                     | opportunities[].lead_id                   | object           |
|                                                 |                     | opportunities[].lead_name                 | object           |
|                                                 |                     | opportunities[].note                      | object           |
|                                                 |                     | opportunities[].organization_id           | object           |
|                                                 |                     | opportunities[].pipeline_id               | object           |
|                                                 |                     | opportunities[].pipeline_name             | object           |
|                                                 |                     | opportunities[].status_display_name       | object           |
|                                                 |                     | opportunities[].status_id                 | object           |
|                                                 |                     | opportunities[].status_label              | object           |
|                                                 |                     | opportunities[].status_type               | object           |
|                                                 |                     | opportunities[].updated_by                | object           |
|                                                 |                     | opportunities[].updated_by_name           | object           |
|                                                 |                     | opportunities[].user_id                   | object           |
|                                                 |                     | opportunities[].user_name                 | object           |
|                                                 |                     | opportunities[].value                     | object           |
|                                                 |                     | opportunities[].value_currency            | object           |
|                                                 |                     | opportunities[].value_formatted           | object           |
|                                                 |                     | opportunities[].value_period              | object           |
|                                                 |                     | organization_id                           | str              |
|                                                 |                     | status_label                              | str              |
|                                                 |                     | tasks[]                                   | array            |
|                                                 |                     | updated_by_name                           | str              |

## Contact

| Entity Schema Fields | Entity Schema Types | Find By ID Object Fields | Find By ID Types |
|----------------------|---------------------|--------------------------|------------------|
| created_by           | string              | created_by               | str              |
| date_created         | string              | date_created             | str              |
| date_updated         | string              | date_updated             | str              |
| emails[]             | object              | emails[]                 | array            |
| id                   | string              | id                       | str              |
| lead_id              | string              | lead_id                  | str              |
| name                 | string              | name                     | str              |
| organization_id      | string              | organization_id          | str              |
| phones[]             | object              | phones[]                 | array            |
| title                | string              | title                    | null             |
| updated_by           | string              | updated_by               | str              |
| urls[]               | object              | urls[]                   | array            |
| email                | string              |                          |                  |
| emails[].email       | string              |                          |                  |
| emails[].type        | string              |                          |                  |
| phones[].phone       | string              |                          |                  |
| phones[].type        | string              |                          |                  |
| urls[].type          | string              |                          |                  |
| urls[].url           | string              |                          |                  |
|                      |                     | display_name             | str              |
|                      |                     | integration_links[]      | array            |
|                      |                     | integration_links[].name | object           |
|                      |                     | integration_links[].url  | object           |
