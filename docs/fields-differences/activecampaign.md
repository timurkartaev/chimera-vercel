# Differences between fields in ActiveCampaign.io


## Deals

| Entity Schema Title | Entity Schema Fields | Entity Schema Types | Readonly | Possible Values | Reference Collection | Find By ID Object Fields | Find By ID Types | Value |
|---------------------|----------------------|---------------------|----------|-----------------|----------------------|--------------------------|------------------|-------|
|  | account | string | false |  | accounts | account | null | None |
|  | activitycount | string | false |  |  | activitycount | str | 2 |
|  | cdate | string | false |  |  | cdate | str | 2025-06-09T08:10:34-05:00 |
|  | contact | string | false |  | contacts | contact | str | 2 |
|  | *currency | string | false |  |  | currency | str | usd |
|  | customerAccount | string | false |  | accounts | customerAccount | null | None |
|  | description | string | false |  |  | description | str | test |
|  | edate | string | false |  |  | edate | str | 2025-06-12 03:18:02 |
|  | group | string | false |  |  | group | str | 1 |
|  | id | string | true |  |  | id | str | 1 |
|  | isDisabled | boolean | false |  |  | isDisabled | bool | False |
|  | links | object | false |  |  | links | object | {"dealActivities": "https://pandadoc72354.activehosted.com/api/3/deals/1/dealActivities", "contact": "https://pandadoc72354.activehosted.com/api/3/deals/1/contact", "contactDeals": "https://pandadoc72354.activehosted.com/api/3/deals/1/contactDeals", "group": "https://pandadoc72354.activehosted.com/api/3/deals/1/group", "nextTask": "https://pandadoc72354.activehosted.com/api/3/deals/1/nextTask", "notes": "https://pandadoc72354.activehosted.com/api/3/deals/1/notes", "account": "https://pandadoc72354.activehosted.com/api/3/deals/1/account", "customerAccount": "https://pandadoc72354.activehosted.com/api/3/deals/1/customerAccount", "organization": "https://pandadoc72354.activehosted.com/api/3/deals/1/organization", "owner": "https://pandadoc72354.activehosted.com/api/3/deals/1/owner", "scoreValues": "https://pandadoc72354.activehosted.com/api/3/deals/1/scoreValues", "stage": "https://pandadoc72354.activehosted.com/api/3/deals/1/stage", "tasks": "https://pandadoc72354.activehosted.com/api/3/deals/1/tasks", "dealCustomFieldData": "https://pandadoc72354.activehosted.com/api/3/deals/1/dealCustomFieldData"} |
|  | links.account | string | false |  |  | links.account | str |  |
|  | links.contact | string | false |  |  | links.contact | str |  |
|  | links.contactDeals | string | false |  |  | links.contactDeals | str |  |
|  | links.customerAccount | string | false |  |  | links.customerAccount | str |  |
|  | links.dealActivities | string | false |  |  | links.dealActivities | str |  |
|  | links.dealCustomFieldData | string | false |  |  | links.dealCustomFieldData | str |  |
|  | links.group | string | false |  |  | links.group | str |  |
|  | links.nextTask | string | false |  |  | links.nextTask | str |  |
|  | links.notes | string | false |  |  | links.notes | str |  |
|  | links.organization | string | false |  |  | links.organization | str |  |
|  | links.owner | string | false |  |  | links.owner | str |  |
|  | links.scoreValues | string | false |  |  | links.scoreValues | str |  |
|  | links.stage | string | false |  |  | links.stage | str |  |
|  | links.tasks | string | false |  |  | links.tasks | str |  |
|  | mdate | string | false |  |  | mdate | str | 2025-06-09T08:10:35-05:00 |
|  | nextdate | string | false |  |  | nextdate | null | None |
|  | nextdealid | string | false |  | deals | nextdealid | str | 1 |
|  | nexttaskid | string | false |  | deal-tasks | nexttaskid | str | 0 |
|  | organization | string | false |  | accounts | organization | null | None |
|  | *owner | string | false |  | users | owner | str | 1 |
|  | percent | string | false |  |  | percent | str | 0 |
|  | stage | string | false |  | deal-stages | stage | str | 1 |
|  | status | string | false | `Open`, `Won`, `Lost` |  | status | str | 0 |
|  | title | string | false |  |  | title | str | Doniyor Test Deal |
|  | *value | string | false |  |  | value | str | 10000 |
|  | winProbability | integer | false |  |  | winProbability | null | None |
|  | winProbabilityMdate | string | false |  |  | winProbabilityMdate | str | 2025-06-09T08:10:34-05:00 |
|  |  |  |  |  |  | hash | str | ae1d8ba8 |
|  |  |  |  |  |  | nextTask | null | None |

## Contacts

| Entity Schema Title | Entity Schema Fields | Entity Schema Types | Readonly | Possible Values | Reference Collection | Find By ID Object Fields | Find By ID Types | Value |
|---------------------|----------------------|---------------------|----------|-----------------|----------------------|--------------------------|------------------|-------|
|  | accountContacts | array | false |  |  | accountContacts | array | [] |
|  | adate | string | false |  |  | adate | str | 2025-06-10T02:28:00-05:00 |
|  | anonymized | string | false |  |  | anonymized | str | 0 |
|  | bounced_date | string | false |  |  | bounced_date | null | None |
|  | bounced_hard | string | false |  |  | bounced_hard | str | 0 |
|  | bounced_soft | string | false |  |  | bounced_soft | str | 0 |
|  | cdate | string | false |  |  | cdate | str | 2025-06-09T08:10:33-05:00 |
|  | contactAutomations | array | false |  |  | contactAutomations | array | [] |
|  | contactLists | array | false |  |  | contactLists | array | [] |
|  | created_by | string | false |  |  | created_by | str | 0 |
|  | created_timestamp | string | false |  |  | created_timestamp | str | 2025-06-09 08:10:33 |
|  | created_utc_timestamp | string | false |  |  | created_utc_timestamp | str | 2025-06-09 08:10:33 |
|  | deals | array | false |  |  | deals | array | ["1"] |
|  | deleted | string | false |  |  | deleted | str | 0 |
|  | deleted_at | string | false |  |  | deleted_at | null | None |
|  | edate | string | false |  |  | edate | str | 2025-06-12T03:18:02-05:00 |
|  | *email | string | false |  |  | email | str | contr.doniyor.rufatov@pandadoc.com |
|  | email_domain | string | false |  |  | email_domain | str | pandadoc.com |
|  | email_local | string | false |  |  | email_local | str |  |
|  | fieldValues | array | false |  |  | fieldValues | array | [] |
|  | firstName | string | false |  |  | firstName | str | Doniyor |
|  | geoIps | array | false |  |  | geoIps | array | [] |
|  | gravatar | string | false |  |  | gravatar | str | 0 |
|  | hash | string | false |  |  | hash | str | 07d5ff89c9eac11c743ce9ea44192b4d |
|  | id | string | true |  |  | id | str | 2 |
|  | ip | string | false |  |  | ip | str | 0 |
|  | lastName | string | false |  |  | lastName | str |  |
|  | mpp_tracking | string | false |  |  | mpp_tracking | str | 0 |
|  | orgid | string | false |  | accounts | orgid | str | 0 |
|  | orgname | string | false |  |  | orgname | str |  |
|  | phone | string | false |  |  | phone | str |  |
|  | rating_tstamp | string | false |  |  | rating_tstamp | null | None |
|  | segmentio_id | string | false |  |  | segmentio_id | str |  |
|  | sentcnt | string | false |  |  | sentcnt | str | 0 |
|  | socialdata_lastcheck | string | false |  |  | socialdata_lastcheck | null | None |
|  | ua | string | false |  |  | ua | str |  |
|  | udate | string | false |  |  | udate | str | 2025-06-09T08:10:33-05:00 |
|  | updated_by | string | false |  |  | updated_by | str | 0 |
|  | updated_timestamp | string | false |  |  | updated_timestamp | str | 2025-06-12 03:18:02 |
|  | updated_utc_timestamp | string | false |  |  | updated_utc_timestamp | str | 2025-06-12 03:18:02 |
|  |  |  |  |  |  | best_send_hour | str | 0 |
|  |  |  |  |  |  | last_click_date | null | None |
|  |  |  |  |  |  | last_mpp_open_date | null | None |
|  |  |  |  |  |  | last_open_date | null | None |
|  |  |  |  |  |  | links | object | {"bounceLogs": "https://pandadoc72354.activehosted.com/api/3/contacts/2/bounceLogs", "contactAutomations": "https://pandadoc72354.activehosted.com/api/3/contacts/2/contactAutomations?limit=2500&orders%5Blastdate%5D=DESC", "contactData": "https://pandadoc72354.activehosted.com/api/3/contacts/2/contactData", "contactGoals": "https://pandadoc72354.activehosted.com/api/3/contacts/2/contactGoals", "contactLists": "https://pandadoc72354.activehosted.com/api/3/contacts/2/contactLists", "contactLogs": "https://pandadoc72354.activehosted.com/api/3/contacts/2/contactLogs", "contactTags": "https://pandadoc72354.activehosted.com/api/3/contacts/2/contactTags", "contactDeals": "https://pandadoc72354.activehosted.com/api/3/contacts/2/contactDeals", "deals": "https://pandadoc72354.activehosted.com/api/3/contacts/2/deals", "fieldValues": "https://pandadoc72354.activehosted.com/api/3/contacts/2/fieldValues", "geoIps": "https://pandadoc72354.activehosted.com/api/3/contacts/2/geoIps", "notes": "https://pandadoc72354.activehosted.com/api/3/contacts/2/notes", "organization": "https://pandadoc72354.activehosted.com/api/3/contacts/2/organization", "plusAppend": "https://pandadoc72354.activehosted.com/api/3/contacts/2/plusAppend", "trackingLogs": "https://pandadoc72354.activehosted.com/api/3/contacts/2/trackingLogs", "scoreValues": "https://pandadoc72354.activehosted.com/api/3/contacts/2/scoreValues", "accountContacts": "https://pandadoc72354.activehosted.com/api/3/contacts/2/accountContacts", "automationEntryCounts": "https://pandadoc72354.activehosted.com/api/3/contacts/2/automationEntryCounts"} |
|  |  |  |  |  |  | links.accountContacts | str |  |
|  |  |  |  |  |  | links.automationEntryCounts | str |  |
|  |  |  |  |  |  | links.bounceLogs | str |  |
|  |  |  |  |  |  | links.contactAutomations | str |  |
|  |  |  |  |  |  | links.contactData | str |  |
|  |  |  |  |  |  | links.contactDeals | str |  |
|  |  |  |  |  |  | links.contactGoals | str |  |
|  |  |  |  |  |  | links.contactLists | str |  |
|  |  |  |  |  |  | links.contactLogs | str |  |
|  |  |  |  |  |  | links.contactTags | str |  |
|  |  |  |  |  |  | links.deals | str |  |
|  |  |  |  |  |  | links.fieldValues | str |  |
|  |  |  |  |  |  | links.geoIps | str |  |
|  |  |  |  |  |  | links.notes | str |  |
|  |  |  |  |  |  | links.organization | str |  |
|  |  |  |  |  |  | links.plusAppend | str |  |
|  |  |  |  |  |  | links.scoreValues | str |  |
|  |  |  |  |  |  | links.trackingLogs | str |  |
|  |  |  |  |  |  | organization | null | None |

## Accounts

| Entity Schema Title | Entity Schema Fields | Entity Schema Types | Readonly | Possible Values | Reference Collection | Find By ID Object Fields | Find By ID Types | Value |
|---------------------|----------------------|---------------------|----------|-----------------|----------------------|--------------------------|------------------|-------|
|  | accountUrl | string | false |  |  | accountUrl | null | None |
|  | createdTimestamp | string | false |  |  | createdTimestamp | str | 2025-06-10T02:28:15-05:00 |
|  | id | string | true |  |  | id | str | 1 |
|  | *name | string | false |  |  | name | str | Test Account |
|  | owner | string | false |  | users | owner | str | 1 |
|  | updatedTimestamp | string | false |  |  | updatedTimestamp | str | 2025-06-10T02:28:15-05:00 |
|  |  |  |  |  |  | links | object | {"notes": "https://pandadoc72354.activehosted.com/api/3/accounts/1/notes", "accountCustomFieldData": "https://pandadoc72354.activehosted.com/api/3/accounts/1/accountCustomFieldData", "accountContacts": "https://pandadoc72354.activehosted.com/api/3/accounts/1/accountContacts", "emailActivities": "https://pandadoc72354.activehosted.com/api/3/accounts/1/emailActivities", "contactEmails": "https://pandadoc72354.activehosted.com/api/3/accounts/1/contactEmails", "owner": "https://pandadoc72354.activehosted.com/api/3/accounts/1/owner"} |
|  |  |  |  |  |  | links.accountContacts | str |  |
|  |  |  |  |  |  | links.accountCustomFieldData | str |  |
|  |  |  |  |  |  | links.contactEmails | str |  |
|  |  |  |  |  |  | links.emailActivities | str |  |
|  |  |  |  |  |  | links.notes | str |  |
|  |  |  |  |  |  | links.owner | str |  |