# Differences between fields in Brevo


## Deals

| Diff | Entity Schema Title | Schema Field ID | Entity Schema Types | Readonly | Possible Values | Reference Collection | FindByID Field ID | Find By ID Types | Value |
|------|---------------------|-----------------|---------------------|----------|-----------------|----------------------|-------------------|------------------|-------|
|  |  | attributes | object | false |  |  | attributes | object | {"amount": 1000, "created_at": "2025-07-16T06:20:34Z", "deal_name": "I\u2019m a Deal example, this is my name.", "deal_owner": "68762ec05fb5e5f4de0e6806", "deal_stage": "95f3915b-f6cd-43da-b32f-3838ebce956b", "last_activity_date": "2025-07-16T06:20:34.349Z", "last_updated_date": "2025-07-16T06:20:34Z", "number_of_activities": 1, "number_of_contacts": 1, "pipeline": "68762ec1047717b48eab7e73", "stage_updated_at": "2025-07-16T06:20:34Z"} |
|  |  | attributes.amount | integer | false |  |  | attributes.amount | integer | 1000 |
|  |  | attributes.created_at | string | false |  |  | attributes.created_at | string | 2025-07-16T06:20:34Z |
|  |  | attributes.deal_name | string | false |  |  | attributes.deal_name | string | I’m a Deal example, this is my name. |
|  |  | attributes.deal_owner | string | false |  |  | attributes.deal_owner | string | 68762ec05fb5e5f4de0e6806 |
|  |  | attributes.deal_stage | string | false |  | pipeline-stages | attributes.deal_stage | string | 95f3915b-f6cd-43da-b32f-3838ebce956b |
|  |  | attributes.last_activity_date | string | false |  |  | attributes.last_activity_date | string | 2025-07-16T06:20:34.349Z |
|  |  | attributes.last_updated_date | string | false |  |  | attributes.last_updated_date | string | 2025-07-16T06:20:34Z |
|  |  | attributes.number_of_activities | integer | false |  |  | attributes.number_of_activities | integer | 1 |
|  |  | attributes.number_of_contacts | integer | false |  |  | attributes.number_of_contacts | integer | 1 |
|  |  | attributes.pipeline | string | false |  | pipelines | attributes.pipeline | string | 68762ec1047717b48eab7e73 |
|  |  | attributes.stage_updated_at | string | false |  |  | attributes.stage_updated_at | string | 2025-07-16T06:20:34Z |
|  |  | id | string | false |  |  | id | string | 687744b25f3b04912d4dd668 |
|  |  | linkedCompaniesIds | array | false |  |  | linkedCompaniesIds | array | ["687744eec7d66a05b7a65304"] |
|  |  | linkedCompaniesIds[] | string | false |  |  | linkedCompaniesIds[] | string | 687744eec7d66a05b7a65304 |
|  |  | linkedContactsIds | array | false |  |  | linkedContactsIds | array | [1] |
|  |  | linkedContactsIds[] | integer | false |  |  | linkedContactsIds[] | integer | 1 |
| Schema |  | <span style='color:red'>***attributes.next_activity_date***</span> | string | false |  |  |  |  |  |
| FindByID |  |  |  |  |  |  | companyTimelineEnabledFrom | null | None |
| FindByID |  |  |  |  |  |  | createdBy | string | 68762ec05fb5e5f4de0e6806 |
| FindByID |  |  |  |  |  |  | refs | object | {} |

## Companies

| Diff | Entity Schema Title | Schema Field ID | Entity Schema Types | Readonly | Possible Values | Reference Collection | FindByID Field ID | Find By ID Types | Value |
|------|---------------------|-----------------|---------------------|----------|-----------------|----------------------|-------------------|------------------|-------|
|  |  | attributes | object | false |  |  | attributes | object | {"created_at": "2025-07-16T06:21:34.184Z", "domain": "pandadoc.com", "industry": "crm", "last_updated_at": "2025-07-16T06:21:34.184Z", "name": "PandaDoc", "number_of_contacts": 0, "owner": "68762ec05fb5e5f4de0e6806", "owner_assign_date": "2025-07-16T06:21:34.184Z", "phone_number": "998901880534"} |
|  |  | attributes.created_at | string | false |  |  | attributes.created_at | string | 2025-07-16T06:21:34.184Z |
|  |  | attributes.domain | string | false |  |  | attributes.domain | string | pandadoc.com |
|  |  | attributes.last_updated_at | string | false |  |  | attributes.last_updated_at | string | 2025-07-16T06:21:34.184Z |
|  |  | attributes.name | string | true |  |  | attributes.name | string | PandaDoc |
|  |  | id | string | true |  |  | id | string | 687744eec7d66a05b7a65304 |
|  |  | linkedContactsIds | array | false |  |  | linkedContactsIds | array | [] |
|  |  | linkedContactsIds[] | integer | false |  |  | linkedContactsIds[] | integer |  |
|  |  | linkedDealsIds | array | false |  |  | linkedDealsIds | array | ["687744b25f3b04912d4dd668"] |
|  |  | linkedDealsIds[] | string | false |  | deals | linkedDealsIds[] | string | 687744b25f3b04912d4dd668 |
| Schema |  | <span style='color:red'>***name***</span> | string | false |  |  |  |  |  |
| FindByID |  |  |  |  |  |  | attributes.industry | string | crm |
| FindByID |  |  |  |  |  |  | attributes.number_of_contacts | integer | 0 |
| FindByID |  |  |  |  |  |  | attributes.owner | string | 68762ec05fb5e5f4de0e6806 |
| FindByID |  |  |  |  |  |  | attributes.owner_assign_date | string | 2025-07-16T06:21:34.184Z |
| FindByID |  |  |  |  |  |  | attributes.phone_number | string | 998901880534 |
| FindByID |  |  |  |  |  |  | createdBy | string | 68762ec05fb5e5f4de0e6806 |
| FindByID |  |  |  |  |  |  | refs | object | {"linkedContacts": null} |
| FindByID |  |  |  |  |  |  | refs.linkedContacts | null | None |

## Contacts

| Diff | Entity Schema Title | Schema Field ID | Entity Schema Types | Readonly | Possible Values | Reference Collection | FindByID Field ID | Find By ID Types | Value |
|------|---------------------|-----------------|---------------------|----------|-----------------|----------------------|-------------------|------------------|-------|
|  |  | attributes | object | false |  |  | attributes | object | {} |
|  |  | createdAt | string | false |  |  | createdAt | string | 2025-07-15T12:34:42.345+02:00 |
|  |  | email | string | false |  |  | email | string | contr.doniyor.rufatov@pandadoc.com |
|  |  | emailBlacklisted | boolean | false |  |  | emailBlacklisted | boolean | False |
|  |  | id | integer | false |  |  | id | integer | 1 |
|  |  | listIds | array | false |  |  | listIds | array | [2] |
|  |  | listIds[] | integer | false |  |  | listIds[] | integer | 2 |
|  |  | modifiedAt | string | false |  |  | modifiedAt | string | 2025-07-15T12:34:42.345+02:00 |
|  |  | smsBlacklisted | boolean | false |  |  | smsBlacklisted | boolean | False |
|  |  | statistics | object | false |  |  | statistics | object | {} |
| Schema |  | <span style='color:red'>***attributes.ADDRESS***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***attributes.AREA***</span> | string | false |  |  |  |  |  |
| Schema | BLACKLIST | <span style='color:red'>***attributes.BLACKLIST***</span> | number | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***attributes.CITY***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***attributes.CIV***</span> | string | false |  |  |  |  |  |
| Schema | CLICKERS | <span style='color:red'>***attributes.CLICKERS***</span> | number | false |  |  |  |  |  |
| Schema | CONTACT_TIMEZONE | <span style='color:red'>***attributes.CONTACT_TIMEZONE***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***attributes.DOB***</span> | string | false |  |  |  |  |  |
| Schema | EXT_ID | <span style='color:red'>***attributes.EXT_ID***</span> | string | false |  |  |  |  |  |
| Schema | FIRSTNAME | <span style='color:red'>***attributes.FIRSTNAME***</span> | string | false |  |  |  |  |  |
| Schema | JOB_TITLE | <span style='color:red'>***attributes.JOB_TITLE***</span> | string | false |  |  |  |  |  |
| Schema | LANDLINE_NUMBER | <span style='color:red'>***attributes.LANDLINE_NUMBER***</span> | string | false |  |  |  |  |  |
| Schema | LASTNAME | <span style='color:red'>***attributes.LASTNAME***</span> | string | false |  |  |  |  |  |
| Schema | LINKEDIN | <span style='color:red'>***attributes.LINKEDIN***</span> | string | false |  |  |  |  |  |
| Schema | READERS | <span style='color:red'>***attributes.READERS***</span> | number | false |  |  |  |  |  |
| Schema | SMS | <span style='color:red'>***attributes.SMS***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***attributes.ZIP_CODE***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***listUnsubscribed***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***statistics.clicked***</span> | array | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***statistics.delivered***</span> | array | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***statistics.messagesSent***</span> | array | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***statistics.opened***</span> | array | false |  |  |  |  |  |