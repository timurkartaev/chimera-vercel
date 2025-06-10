# Differences between fields in ActiveCampaign

## Deals

| Entity Schema Fields      | Find By ID Object Fields  |
|---------------------------|---------------------------|
| account                   | account                   |
| activitycount             | activitycount             |
| cdate                     | cdate                     |
| contact                   | contact                   |
| currency                  | currency                  |
| customerAccount           | customerAccount           |
| description               | description               |
| edate                     | edate                     |
| group                     | group                     |
| id                        | id                        |
| isDisabled                | isDisabled                |
| links.account             | links.account             |
| links.contact             | links.contact             |
| links.contactDeals        | links.contactDeals        |
| links.customerAccount     | links.customerAccount     |
| links.dealActivities      | links.dealActivities      |
| links.dealCustomFieldData | links.dealCustomFieldData |
| links.group               | links.group               |
| links.nextTask            | links.nextTask            |
| links.notes               | links.notes               |
| links.organization        | links.organization        |
| links.owner               | links.owner               |
| links.scoreValues         | links.scoreValues         |
| links.stage               | links.stage               |
| links.tasks               | links.tasks               |
| mdate                     | mdate                     |
| nextdate                  | nextdate                  |
| nextdealid                | nextdealid                |
| nexttaskid                | nexttaskid                |
| organization              | organization              |
| owner                     | owner                     |
| percent                   | percent                   |
| stage                     | stage                     |
| status                    | status                    |
| title                     | title                     |
| value                     | value                     |
| winProbability            | winProbability            |
| winProbabilityMdate       | winProbabilityMdate       |
|                           | hash                      |
|                           | nextTask                  |

## Contacts

| Entity Schema Fields  | Find By ID Object Fields    |
|-----------------------|-----------------------------|
| accountContacts[]     | accountContacts[]           |
| adate                 | adate                       |
| anonymized            | anonymized                  |
| bounced_date          | bounced_date                |
| bounced_hard          | bounced_hard                |
| bounced_soft          | bounced_soft                |
| cdate                 | cdate                       |
| contactAutomations[]  | contactAutomations[]        |
| created_by            | created_by                  |
| created_timestamp     | created_timestamp           |
| created_utc_timestamp | created_utc_timestamp       |
| deals[]               | deals[]                     |
| deleted               | deleted                     |
| deleted_at            | deleted_at                  |
| edate                 | edate                       |
| email                 | email                       |
| email_domain          | email_domain                |
| email_local           | email_local                 |
| firstName             | firstName                   |
| gravatar              | gravatar                    |
| hash                  | hash                        |
| id                    | id                          |
| ip                    | ip                          |
| lastName              | lastName                    |
| mpp_tracking          | mpp_tracking                |
| orgid                 | orgid                       |
| orgname               | orgname                     |
| phone                 | phone                       |
| rating_tstamp         | rating_tstamp               |
| segmentio_id          | segmentio_id                |
| sentcnt               | sentcnt                     |
| socialdata_lastcheck  | socialdata_lastcheck        |
| ua                    | ua                          |
| udate                 | udate                       |
| updated_by            | updated_by                  |
| updated_timestamp     | updated_timestamp           |
| updated_utc_timestamp | updated_utc_timestamp       |
| contactLists          |                             |
| email_empty           |                             |
| fieldValues           |                             |
| geoIps                |                             |
| jobTitle              |                             |
|                       | best_send_hour              |
|                       | contactLists[]              |
|                       | fieldValues[]               |
|                       | geoIps[]                    |
|                       | last_click_date             |
|                       | last_mpp_open_date          |
|                       | last_open_date              |
|                       | links.accountContacts       |
|                       | links.automationEntryCounts |
|                       | links.bounceLogs            |
|                       | links.contactAutomations    |
|                       | links.contactData           |
|                       | links.contactDeals          |
|                       | links.contactGoals          |
|                       | links.contactLists          |
|                       | links.contactLogs           |
|                       | links.contactTags           |
|                       | links.deals                 |
|                       | links.fieldValues           |
|                       | links.geoIps                |
|                       | links.notes                 |
|                       | links.organization          |
|                       | links.plusAppend            |
|                       | links.scoreValues           |
|                       | links.trackingLogs          |
|                       | organization                |

## Accounts

| Entity Schema Fields | Find By ID Object Fields     |
|----------------------|------------------------------|
| accountUrl           | accountUrl                   |
| createdTimestamp     | createdTimestamp             |
| id                   | id                           |
| name                 | name                         |
| owner                | owner                        |
| updatedTimestamp     | updatedTimestamp             |
| contactCount         |                              |
| dealCount            |                              |
|                      | links.accountContacts        |
|                      | links.accountCustomFieldData |
|                      | links.contactEmails          |
|                      | links.emailActivities        |
|                      | links.notes                  |
|                      | links.owner                  |