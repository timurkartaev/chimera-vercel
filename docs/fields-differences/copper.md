# Differences between fields in CopperCRM

## Opportunities

| Entity Schema Fields | Entity Schema Types | Find By ID Object Fields | Find By ID Types |
|----------------------|---------------------|--------------------------|------------------|
| assignee_id          | number              | assignee_id              | int              |
| close_date           | string              | close_date               | str              |
| company_id           | number              | company_id               | int              |
| company_name         | string              | company_name             | str              |
| custom_104810        | string              | custom_104810            | str              |
| custom_107587        | string              | custom_107587            | str              |
| custom_107887        | string              | custom_107887            | null             |
| custom_107890        | string              | custom_107890            | null             |
| custom_111060        | string              | custom_111060            | null             |
| custom_113843        | string              | custom_113843            | str              |
| custom_114310        | boolean             | custom_114310            | bool             |
| custom_182699        | string              | custom_182699            | str              |
| custom_226946        | number              | custom_226946            | null             |
| custom_248275        | string              | custom_248275            | null             |
| custom_248282        | string              | custom_248282            | null             |
| custom_257541        | string              | custom_257541            | null             |
| custom_257554        | string              | custom_257554            | str              |
| custom_285046        | number              | custom_285046            | int              |
| custom_288717        | boolean             | custom_288717            | bool             |
| custom_288719        | boolean             | custom_288719            | bool             |
| custom_288721        | integer             | custom_288721            | null             |
| custom_288722        | string              | custom_288722            | int              |
| custom_288724        | string              | custom_288724            | int              |
| custom_288725        | string              | custom_288725            | int              |
| custom_288727        | string              | custom_288727            | int              |
| custom_288766        | string              | custom_288766            | str              |
| custom_295917        | number              | custom_295917            | int              |
| custom_305253        | number              | custom_305253            | int              |
| custom_330338        | number              | custom_330338            | int              |
| custom_330339        | string              | custom_330339            | str              |
| custom_330343        | string              | custom_330343            | int              |
| custom_330344        | string              | custom_330344            | str              |
| custom_330345        | string              | custom_330345            | int              |
| custom_330352        | string              | custom_330352            | str              |
| custom_330356        | string              | custom_330356            | int              |
| custom_330357        | string              | custom_330357            | int              |
| custom_330358        | number              | custom_330358            | int              |
| custom_330359        | number              | custom_330359            | int              |
| custom_330360        | string              | custom_330360            | int              |
| custom_344230        | boolean             | custom_344230            | bool             |
| custom_344231        | string              | custom_344231            | null             |
| custom_344363        | string              | custom_344363            | null             |
| custom_344372[]      | integer             | custom_344372[]          | array            |
| custom_344373        | string              | custom_344373            | null             |
| custom_344374        | string              | custom_344374            | null             |
| custom_349962[]      | integer             | custom_349962[]          | array            |
| custom_365440        | string              | custom_365440            | null             |
| custom_367051        | string              | custom_367051            | null             |
| custom_379268        | string              | custom_379268            | str              |
| custom_391555        | string              | custom_391555            | str              |
| custom_418074        | boolean             | custom_418074            | bool             |
| custom_418077        | string              | custom_418077            | str              |
| custom_418650        | boolean             | custom_418650            | bool             |
| custom_418651        | string              | custom_418651            | null             |
| custom_418656[]      | integer             | custom_418656[]          | array            |
| custom_418657        | string              | custom_418657            | null             |
| custom_435367        | string              | custom_435367            | null             |
| custom_484800        | boolean             | custom_484800            | bool             |
| custom_542838        | number              | custom_542838            | int              |
| custom_554918        | string              | custom_554918            | null             |
| custom_646696        | string              | custom_646696            | str              |
| custom_671286        | string              | custom_671286            | null             |
| custom_73630         | string              | custom_73630             | null             |
| custom_84682         | string              | custom_84682             | str              |
| customer_source_id   | number              | customer_source_id       | null             |
| date_created         | integer             | date_created             | int              |
| date_modified        | integer             | date_modified            | int              |
| details              | string              | details                  | null             |
| id                   | integer             | id                       | int              |
| interaction_count    | number              | interaction_count        | int              |
| loss_reason_id       | number              | loss_reason_id           | null             |
| monetary_unit        | string              | monetary_unit            | str              |
| monetary_value       | number              | monetary_value           | int              |
| name                 | string              | name                     | str              |
| pipeline_id          | number              | pipeline_id              | int              |
| pipeline_stage_id    | number              | pipeline_stage_id        | int              |
| primary_contact_id   | number              | primary_contact_id       | int              |
| priority             | string              | priority                 | str              |
| status               | string              | status                   | str              |
| tags[]               | string              | tags[]                   | array            |
| win_probability      | number              | win_probability          | int              |
| custom_346502        | string              |                          |                  |
| custom_346506        | string              |                          |                  |
| custom_346508        | string              |                          |                  |
| custom_346509        | string              |                          |                  |
| custom_346510        | string              |                          |                  |
|                      |                     | converted_unit           | str              |
|                      |                     | converted_value          | int              |
|                      |                     | custom_346502[]          | array            |
|                      |                     | custom_346506[]          | array            |
|                      |                     | custom_346508[]          | array            |
|                      |                     | custom_346509[]          | array            |
|                      |                     | custom_346510[]          | array            |
|                      |                     | date_last_contacted      | null             |
|                      |                     | date_lead_created        | null             |
|                      |                     | date_stage_changed       | int              |
|                      |                     | leads_converted_from[]   | array            |
|                      |                     | pipeline_is_revenue      | bool             |
|                      |                     | pipeline_type            | str              |

## Companies

| Entity Schema Fields      | Entity Schema Types | Find By ID Object Fields | Find By ID Types |
|---------------------------|---------------------|--------------------------|------------------|
| address.city              | string              | address.city             | str              |
| address.country           | string              | address.country          | null             |
| address.postal_code       | string              | address.postal_code      | str              |
| address.state             | string              | address.state            | str              |
| address.street            | string              | address.street           | str              |
| assignee_id               | integer             | assignee_id              | int              |
| date_created              | integer             | date_created             | int              |
| date_modified             | integer             | date_modified            | int              |
| details                   | string              | details                  | null             |
| email_domain              | string              | email_domain             | null             |
| email_domains             | string              | email_domains            | null             |
| name                      | string              | name                     | str              |
| phone_numbers[]           | object              | phone_numbers[]          | array            |
| phone_numbers[].category  | string              | phone_numbers[].category | object           |
| phone_numbers[].number    | string              | phone_numbers[].number   | object           |
| socials[]                 | object              | socials[]                | array            |
| tags[]                    | string              | tags[]                   | array            |
| websites[]                | object              | websites[]               | array            |
| age                       | number              |                          |                  |
| custom_18443              | string              |                          |                  |
| custom_257554             | string              |                          |                  |
| custom_295265             | string              |                          |                  |
| custom_346507             | string              |                          |                  |
| custom_365439             | string              |                          |                  |
| custom_391554             | string              |                          |                  |
| custom_671286             | string              |                          |                  |
| followed                  | integer             |                          |                  |
| id                        | integer             |                          |                  |
| maximum_created_date      | integer             |                          |                  |
| maximum_interaction_count | number              |                          |                  |
| maximum_interaction_date  | integer             |                          |                  |
| minimum_created_date      | integer             |                          |                  |
| minimum_interaction_count | number              |                          |                  |
| minimum_interaction_date  | integer             |                          |                  |
| phone_number              | string              |                          |                  |
| socials[].category        | string              |                          |                  |
| socials[].url             | string              |                          |                  |
| websites[].category       | string              |                          |                  |
| websites[].url            | string              |                          |                  |

## Leads

| Entity Schema Fields     | Entity Schema Types | Find By ID Object Fields | Find By ID Types |
|--------------------------|---------------------|--------------------------|------------------|
| address.city             | string              | address.city             | str              |
| address.country          | string              | address.country          | null             |
| address.postal_code      | string              | address.postal_code      | str              |
| address.state            | string              | address.state            | str              |
| address.street           | string              | address.street           | str              |
| assignee_id              | integer             | assignee_id              | int              |
| company_name             | string              | company_name             | null             |
| custom_248282            | string              | custom_248282            | null             |
| custom_288717            | boolean             | custom_288717            | bool             |
| custom_288719            | boolean             | custom_288719            | bool             |
| custom_330352            | string              | custom_330352            | null             |
| custom_554917            | string              | custom_554917            | null             |
| custom_671286            | string              | custom_671286            | null             |
| customer_source_id       | integer             | customer_source_id       | null             |
| date_created             | integer             | date_created             | int              |
| date_last_contacted      | integer             | date_last_contacted      | null             |
| date_modified            | integer             | date_modified            | int              |
| details                  | string              | details                  | null             |
| first_name               | string              | first_name               | str              |
| id                       | integer             | id                       | int              |
| last_name                | string              | last_name                | str              |
| monetary_unit            | string              | monetary_unit            | null             |
| monetary_value           | number              | monetary_value           | null             |
| name                     | string              | name                     | str              |
| phone_numbers[]          | object              | phone_numbers[]          | array            |
| socials[]                | object              | socials[]                | array            |
| status_id                | number              | status_id                | int              |
| tags[]                   | string              | tags[]                   | array            |
| title                    | string              | title                    | null             |
| websites[]               | object              | websites[]               | array            |
| custom_346511            | string              |                          |                  |
| email.category           | string              |                          |                  |
| email.email              | string              |                          |                  |
| emails                   | string              |                          |                  |
| phone_numbers[].category | string              |                          |                  |
| phone_numbers[].number   | string              |                          |                  |
| socials[].category       | string              |                          |                  |
| socials[].url            | string              |                          |                  |
| websites[].category      | string              |                          |                  |
| websites[].url           | string              |                          |                  |
|                          |                     | converted_at             | null             |
|                          |                     | converted_contact_id     | null             |
|                          |                     | converted_opportunity_id | null             |
|                          |                     | converted_unit           | str              |
|                          |                     | converted_value          | null             |
|                          |                     | custom_346511[]          | array            |
|                          |                     | email                    | null             |
|                          |                     | interaction_count        | int              |
|                          |                     | middle_name              | null             |
|                          |                     | prefix                   | null             |
|                          |                     | status                   | str              |
|                          |                     | suffix                   | null             |