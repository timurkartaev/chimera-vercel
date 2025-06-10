# Differences between fields in Close.io

## Opportunity

| Entity Schema Fields      | Find By ID Object Fields  |
|---------------------------|---------------------------|
| annualized_expected_value | annualized_expected_value |
| annualized_value          | annualized_value          |
| confidence                | confidence                |
| contact_id                | contact_id                |
| created_by                | created_by                |
| date_created              | date_created              |
| date_updated              | date_updated              |
| date_won                  | date_won                  |
| expected_value            | expected_value            |
| id                        | id                        |
| lead_id                   | lead_id                   |
| lead_name                 | lead_name                 |
| note                      | note                      |
| organization_id           | organization_id           |
| status_id                 | status_id                 |
| status_label              | status_label              |
| status_type               | status_type               |
| updated_by                | updated_by                |
| user_id                   | user_id                   |
| user_name                 | user_name                 |
| value                     | value                     |
| value_currency            | value_currency            |
| value_formatted           | value_formatted           |
| value_period              | value_period              |
|                           | attachments[]             |
|                           | contact_name              |
|                           | created_by_name           |
|                           | date_lost                 |
|                           | integration_links[]       |
|                           | integration_links[].name  |
|                           | integration_links[].url   |
|                           | pipeline_id               |
|                           | pipeline_name             |
|                           | status_display_name       |
|                           | updated_by_name           |

## Lead

| Entity Schema Fields                            | Find By ID Object Fields                  |
|-------------------------------------------------|-------------------------------------------|
| addresses[]                                     | addresses[]                               |
| created_by                                      | created_by                                |
| date_created                                    | date_created                              |
| date_updated                                    | date_updated                              |
| description                                     | description                               |
| html_url                                        | html_url                                  |
| id                                              | id                                        |
| name                                            | name                                      |
| status_id                                       | status_id                                 |
| updated_by                                      | updated_by                                |
| url                                             | url                                       |
| addresses[].address_1                           |                                           |
| addresses[].address_2                           |                                           |
| addresses[].city                                |                                           |
| addresses[].country                             |                                           |
| addresses[].label                               |                                           |
| addresses[].state                               |                                           |
| addresses[].zipcode                             |                                           |
| lcf_7yX9TSz3qifWiNmca3yX5Y1zSPnil7rGRdiUUDssDnV |                                           |
|                                                 | contacts[]                                |
|                                                 | contacts[].created_by                     |
|                                                 | contacts[].date_created                   |
|                                                 | contacts[].date_updated                   |
|                                                 | contacts[].display_name                   |
|                                                 | contacts[].emails[]                       |
|                                                 | contacts[].id                             |
|                                                 | contacts[].integration_links[]            |
|                                                 | contacts[].integration_links[].name       |
|                                                 | contacts[].integration_links[].url        |
|                                                 | contacts[].lead_id                        |
|                                                 | contacts[].name                           |
|                                                 | contacts[].organization_id                |
|                                                 | contacts[].phones[]                       |
|                                                 | contacts[].title                          |
|                                                 | contacts[].updated_by                     |
|                                                 | contacts[].urls[]                         |
|                                                 | created_by_name                           |
|                                                 | display_name                              |
|                                                 | integration_links[]                       |
|                                                 | opportunities[]                           |
|                                                 | opportunities[].annualized_expected_value |
|                                                 | opportunities[].annualized_value          |
|                                                 | opportunities[].attachments[]             |
|                                                 | opportunities[].confidence                |
|                                                 | opportunities[].contact_id                |
|                                                 | opportunities[].contact_name              |
|                                                 | opportunities[].created_by                |
|                                                 | opportunities[].created_by_name           |
|                                                 | opportunities[].date_created              |
|                                                 | opportunities[].date_lost                 |
|                                                 | opportunities[].date_updated              |
|                                                 | opportunities[].date_won                  |
|                                                 | opportunities[].expected_value            |
|                                                 | opportunities[].id                        |
|                                                 | opportunities[].integration_links[]       |
|                                                 | opportunities[].integration_links[].name  |
|                                                 | opportunities[].integration_links[].url   |
|                                                 | opportunities[].lead_id                   |
|                                                 | opportunities[].lead_name                 |
|                                                 | opportunities[].note                      |
|                                                 | opportunities[].organization_id           |
|                                                 | opportunities[].pipeline_id               |
|                                                 | opportunities[].pipeline_name             |
|                                                 | opportunities[].status_display_name       |
|                                                 | opportunities[].status_id                 |
|                                                 | opportunities[].status_label              |
|                                                 | opportunities[].status_type               |
|                                                 | opportunities[].updated_by                |
|                                                 | opportunities[].updated_by_name           |
|                                                 | opportunities[].user_id                   |
|                                                 | opportunities[].user_name                 |
|                                                 | opportunities[].value                     |
|                                                 | opportunities[].value_currency            |
|                                                 | opportunities[].value_formatted           |
|                                                 | opportunities[].value_period              |
|                                                 | organization_id                           |
|                                                 | status_label                              |
|                                                 | tasks[]                                   |
|                                                 | updated_by_name                           |

## Contact

| Entity Schema Fields | Find By ID Object Fields |
|----------------------|--------------------------|
| created_by           | created_by               |
| date_created         | date_created             |
| date_updated         | date_updated             |
| id                   | id                       |
| lead_id              | lead_id                  |
| name                 | name                     |
| organization_id      | organization_id          |
| phones[]             | phones[]                 |
| title                | title                    |
| updated_by           | updated_by               |
| urls[]               | urls[]                   |
| email                |                          |
| emails[]             | emails[]                 |
| emails[].email       |                          |
| emails[].type        |                          |
| phones[].phone       |                          |
| phones[].type        |                          |
| urls[].type          |                          |
| urls[].url           |                          |
|                      | display_name             |
|                      | integration_links[]      |
|                      | integration_links[].name |
|                      | integration_links[].url  |

