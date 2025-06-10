# Differences between fields in ActiveCampaign

## Deals

| Entity Schema Fields      | Entity Schema Types | Find By ID Object Fields  | Find By ID Types |
|---------------------------|---------------------|---------------------------|------------------|
| account                   | string              | account                   | null             |
| activitycount             | string              | activitycount             | str              |
| cdate                     | string              | cdate                     | str              |
| contact                   | string              | contact                   | str              |
| currency                  | string              | currency                  | str              |
| customerAccount           | string              | customerAccount           | null             |
| description               | string              | description               | str              |
| edate                     | string              | edate                     | str              |
| group                     | string              | group                     | str              |
| id                        | string              | id                        | str              |
| isDisabled                | boolean             | isDisabled                | bool             |
| links.account             | string              | links.account             | str              |
| links.contact             | string              | links.contact             | str              |
| links.contactDeals        | string              | links.contactDeals        | str              |
| links.customerAccount     | string              | links.customerAccount     | str              |
| links.dealActivities      | string              | links.dealActivities      | str              |
| links.dealCustomFieldData | string              | links.dealCustomFieldData | str              |
| links.group               | string              | links.group               | str              |
| links.nextTask            | string              | links.nextTask            | str              |
| links.notes               | string              | links.notes               | str              |
| links.organization        | string              | links.organization        | str              |
| links.owner               | string              | links.owner               | str              |
| links.scoreValues         | string              | links.scoreValues         | str              |
| links.stage               | string              | links.stage               | str              |
| links.tasks               | string              | links.tasks               | str              |
| mdate                     | string              | mdate                     | str              |
| nextdate                  | string              | nextdate                  | null             |
| nextdealid                | string              | nextdealid                | str              |
| nexttaskid                | string              | nexttaskid                | str              |
| organization              | string              | organization              | null             |
| owner                     | string              | owner                     | str              |
| percent                   | string              | percent                   | str              |
| stage                     | string              | stage                     | str              |
| status                    | string              | status                    | str              |
| title                     | string              | title                     | str              |
| value                     | string              | value                     | str              |
| winProbability            | integer             | winProbability            | null             |
| winProbabilityMdate       | string              | winProbabilityMdate       | str              |
|                           |                     | hash                      | str              |
|                           |                     | nextTask                  | null             |

## Contacts

| Entity Schema Fields  | Entity Schema Types | Find By ID Object Fields    | Find By ID Types |
|-----------------------|---------------------|-----------------------------|------------------|
| accountContacts[]     | string              | accountContacts[]           | array            |
| adate                 | string              | adate                       | str              |
| anonymized            | string              | anonymized                  | str              |
| bounced_date          | string              | bounced_date                | null             |
| bounced_hard          | string              | bounced_hard                | str              |
| bounced_soft          | string              | bounced_soft                | str              |
| cdate                 | string              | cdate                       | str              |
| contactAutomations[]  | string              | contactAutomations[]        | array            |
| created_by            | string              | created_by                  | str              |
| created_timestamp     | string              | created_timestamp           | str              |
| created_utc_timestamp | string              | created_utc_timestamp       | str              |
| deals[]               | string              | deals[]                     | array            |
| deleted               | string              | deleted                     | str              |
| deleted_at            | string              | deleted_at                  | null             |
| edate                 | string              | edate                       | str              |
| email                 | string              | email                       | str              |
| email_domain          | string              | email_domain                | str              |
| email_local           | string              | email_local                 | str              |
| firstName             | string              | firstName                   | str              |
| gravatar              | string              | gravatar                    | str              |
| hash                  | string              | hash                        | str              |
| id                    | string              | id                          | str              |
| ip                    | string              | ip                          | str              |
| lastName              | string              | lastName                    | str              |
| mpp_tracking          | string              | mpp_tracking                | str              |
| orgid                 | string              | orgid                       | str              |
| orgname               | string              | orgname                     | str              |
| phone                 | string              | phone                       | str              |
| rating_tstamp         | string              | rating_tstamp               | null             |
| segmentio_id          | string              | segmentio_id                | str              |
| sentcnt               | string              | sentcnt                     | str              |
| socialdata_lastcheck  | string              | socialdata_lastcheck        | null             |
| ua                    | string              | ua                          | str              |
| udate                 | string              | udate                       | str              |
| updated_by            | string              | updated_by                  | str              |
| updated_timestamp     | string              | updated_timestamp           | str              |
| updated_utc_timestamp | string              | updated_utc_timestamp       | str              |
| contactLists          | array               |                             |                  |
| email_empty           | boolean             |                             |                  |
| fieldValues           | array               |                             |                  |
| geoIps                | array               |                             |                  |
| jobTitle              | string              |                             |                  |
|                       |                     | best_send_hour              | str              |
|                       |                     | contactLists[]              | array            |
|                       |                     | fieldValues[]               | array            |
|                       |                     | geoIps[]                    | array            |
|                       |                     | last_click_date             | null             |
|                       |                     | last_mpp_open_date          | null             |
|                       |                     | last_open_date              | null             |
|                       |                     | links.accountContacts       | str              |
|                       |                     | links.automationEntryCounts | str              |
|                       |                     | links.bounceLogs            | str              |
|                       |                     | links.contactAutomations    | str              |
|                       |                     | links.contactData           | str              |
|                       |                     | links.contactDeals          | str              |
|                       |                     | links.contactGoals          | str              |
|                       |                     | links.contactLists          | str              |
|                       |                     | links.contactLogs           | str              |
|                       |                     | links.contactTags           | str              |
|                       |                     | links.deals                 | str              |
|                       |                     | links.fieldValues           | str              |
|                       |                     | links.geoIps                | str              |
|                       |                     | links.notes                 | str              |
|                       |                     | links.organization          | str              |
|                       |                     | links.plusAppend            | str              |
|                       |                     | links.scoreValues           | str              |
|                       |                     | links.trackingLogs          | str              |
|                       |                     | organization                | null             |

## Accounts

| Entity Schema Fields | Entity Schema Types | Find By ID Object Fields     | Find By ID Types |
|----------------------|---------------------|------------------------------|------------------|
| accountUrl           | string              | accountUrl                   | null             |
| createdTimestamp     | string              | createdTimestamp             | str              |
| id                   | string              | id                           | str              |
| name                 | string              | name                         | str              |
| owner                | string              | owner                        | str              |
| updatedTimestamp     | string              | updatedTimestamp             | str              |
| contactCount         | string              |                              |                  |
| dealCount            | string              |                              |                  |
|                      |                     | links.accountContacts        | str              |
|                      |                     | links.accountCustomFieldData | str              |
|                      |                     | links.contactEmails          | str              |
|                      |                     | links.emailActivities        | str              |
|                      |                     | links.notes                  | str              |
|                      |                     | links.owner                  | str              |