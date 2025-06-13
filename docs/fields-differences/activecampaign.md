# Differences between fields in ActiveCampaign.io


## Deals

| Entity Schema Title | Entity Schema Fields | Entity Schema Types | Readonly | Possible Values | Reference Collection | Find By ID Object Fields | Find By ID Types | Value |
|---------------------|----------------------|---------------------|----------|-----------------|----------------------|--------------------------|------------------|-------|
|  | account | string | false |  | accounts | account | null | None |
|  | activitycount | string | false |  |  | activitycount | string | 2 |
|  | cdate | string | false |  |  | cdate | string | 2025-06-09T08:10:34-05:00 |
|  | contact | string | false |  | contacts | contact | string | 2 |
|  | *currency | string | false |  |  | currency | string | usd |
|  | customerAccount | string | false |  | accounts | customerAccount | null | None |
|  | description | string | false |  |  | description | string | test |
|  | edate | string | false |  |  | edate | string | 2025-06-12 03:18:02 |
|  | group | string | false |  |  | group | string | 1 |
|  | id | string | true |  |  | id | string | 1 |
|  | isDisabled | boolean | false |  |  | isDisabled | boolean | False |
|  | links | object | false |  |  | links | object | {"dealActivities": "https://pandadoc72354.activehosted.com/api/3/deals/1/dealActivities", "contact": "https://pandadoc72354.activehosted.com/api/3/deals/1/contact", "contactDeals": "https://pandadoc72354.activehosted.com/api/3/deals/1/contactDeals", "group": "https://pandadoc72354.activehosted.com/api/3/deals/1/group", "nextTask": "https://pandadoc72354.activehosted.com/api/3/deals/1/nextTask", "notes": "https://pandadoc72354.activehosted.com/api/3/deals/1/notes", "account": "https://pandadoc72354.activehosted.com/api/3/deals/1/account", "customerAccount": "https://pandadoc72354.activehosted.com/api/3/deals/1/customerAccount", "organization": "https://pandadoc72354.activehosted.com/api/3/deals/1/organization", "owner": "https://pandadoc72354.activehosted.com/api/3/deals/1/owner", "scoreValues": "https://pandadoc72354.activehosted.com/api/3/deals/1/scoreValues", "stage": "https://pandadoc72354.activehosted.com/api/3/deals/1/stage", "tasks": "https://pandadoc72354.activehosted.com/api/3/deals/1/tasks", "dealCustomFieldData": "https://pandadoc72354.activehosted.com/api/3/deals/1/dealCustomFieldData"} |
|  | links.account | string | false |  |  | links.account | string |  |
|  | links.contact | string | false |  |  | links.contact | string |  |
|  | links.contactDeals | string | false |  |  | links.contactDeals | string |  |
|  | links.customerAccount | string | false |  |  | links.customerAccount | string |  |
|  | links.dealActivities | string | false |  |  | links.dealActivities | string |  |
|  | links.dealCustomFieldData | string | false |  |  | links.dealCustomFieldData | string |  |
|  | links.group | string | false |  |  | links.group | string |  |
|  | links.nextTask | string | false |  |  | links.nextTask | string |  |
|  | links.notes | string | false |  |  | links.notes | string |  |
|  | links.organization | string | false |  |  | links.organization | string |  |
|  | links.owner | string | false |  |  | links.owner | string |  |
|  | links.scoreValues | string | false |  |  | links.scoreValues | string |  |
|  | links.stage | string | false |  |  | links.stage | string |  |
|  | links.tasks | string | false |  |  | links.tasks | string |  |
|  | mdate | string | false |  |  | mdate | string | 2025-06-09T08:10:35-05:00 |
|  | nextdate | string | false |  |  | nextdate | null | None |
|  | nextdealid | string | false |  | deals | nextdealid | string | 1 |
|  | nexttaskid | string | false |  | deal-tasks | nexttaskid | string | 0 |
|  | organization | string | false |  | accounts | organization | null | None |
|  | *owner | string | false |  | users | owner | string | 1 |
|  | percent | string | false |  |  | percent | string | 0 |
|  | stage | string | false |  | deal-stages | stage | string | 1 |
|  | status | string | false | `Open`, `Won`, `Lost` |  | status | string | 0 |
|  | title | string | false |  |  | title | string | Doniyor Test Deal |
|  | *value | string | false |  |  | value | string | 10000 |
|  | winProbability | integer | false |  |  | winProbability | null | None |
|  | winProbabilityMdate | string | false |  |  | winProbabilityMdate | string | 2025-06-09T08:10:34-05:00 |
|  |  |  |  |  |  | hash | string | ae1d8ba8 |
|  |  |  |  |  |  | nextTask | null | None |

## Contacts

| Entity Schema Title | Entity Schema Fields | Entity Schema Types | Readonly | Possible Values | Reference Collection | Find By ID Object Fields | Find By ID Types | Value |
|---------------------|----------------------|---------------------|----------|-----------------|----------------------|--------------------------|------------------|-------|
|  | accountContacts | array | false |  |  | accountContacts | array | [] |
|  | accountContacts[] | string | false |  |  | accountContacts[] | string |  |
|  | adate | string | false |  |  | adate | string | 2025-06-10T02:28:00-05:00 |
|  | anonymized | string | false |  |  | anonymized | string | 0 |
|  | bounced_date | string | false |  |  | bounced_date | null | None |
|  | bounced_hard | string | false |  |  | bounced_hard | string | 0 |
|  | bounced_soft | string | false |  |  | bounced_soft | string | 0 |
|  | cdate | string | false |  |  | cdate | string | 2025-06-09T08:10:33-05:00 |
|  | contactAutomations | array | false |  |  | contactAutomations | array | [] |
|  | contactAutomations[] | string | false |  |  | contactAutomations[] | string |  |
|  | contactLists | array | false |  |  | contactLists | array | [] |
|  | created_by | string | false |  |  | created_by | string | 0 |
|  | created_timestamp | string | false |  |  | created_timestamp | string | 2025-06-09 08:10:33 |
|  | created_utc_timestamp | string | false |  |  | created_utc_timestamp | string | 2025-06-09 08:10:33 |
|  | deals | array | false |  |  | deals | array | ["1"] |
|  | deals[] | string | false |  |  | deals[] | string |  |
|  | deleted | string | false |  |  | deleted | string | 0 |
|  | deleted_at | string | false |  |  | deleted_at | null | None |
|  | edate | string | false |  |  | edate | string | 2025-06-12T03:18:02-05:00 |
|  | *email | string | false |  |  | email | string | contr.doniyor.rufatov@pandadoc.com |
|  | email_domain | string | false |  |  | email_domain | string | pandadoc.com |
|  | email_local | string | false |  |  | email_local | string |  |
|  | fieldValues | array | false |  |  | fieldValues | array | [] |
|  | firstName | string | false |  |  | firstName | string | Doniyor |
|  | geoIps | array | false |  |  | geoIps | array | [] |
|  | gravatar | string | false |  |  | gravatar | string | 0 |
|  | hash | string | false |  |  | hash | string | 07d5ff89c9eac11c743ce9ea44192b4d |
|  | id | string | true |  |  | id | string | 2 |
|  | ip | string | false |  |  | ip | string | 0 |
|  | lastName | string | false |  |  | lastName | string |  |
|  | mpp_tracking | string | false |  |  | mpp_tracking | string | 0 |
|  | orgid | string | false |  | accounts | orgid | string | 0 |
|  | orgname | string | false |  |  | orgname | string |  |
|  | phone | string | false |  |  | phone | string |  |
|  | rating_tstamp | string | false |  |  | rating_tstamp | null | None |
|  | segmentio_id | string | false |  |  | segmentio_id | string |  |
|  | sentcnt | string | false |  |  | sentcnt | string | 0 |
|  | socialdata_lastcheck | string | false |  |  | socialdata_lastcheck | null | None |
|  | ua | string | false |  |  | ua | string |  |
|  | udate | string | false |  |  | udate | string | 2025-06-09T08:10:33-05:00 |
|  | updated_by | string | false |  |  | updated_by | string | 0 |
|  | updated_timestamp | string | false |  |  | updated_timestamp | string | 2025-06-12 03:18:02 |
|  | updated_utc_timestamp | string | false |  |  | updated_utc_timestamp | string | 2025-06-12 03:18:02 |
|  | <span style='color:red'>***email_empty***</span> | boolean | false |  |  |  |  |  |
|  | <span style='color:red'>***jobTitle***</span> | string | false |  |  |  |  |  |
|  |  |  |  |  |  | best_send_hour | string | 0 |
|  |  |  |  |  |  | last_click_date | null | None |
|  |  |  |  |  |  | last_mpp_open_date | null | None |
|  |  |  |  |  |  | last_open_date | null | None |
|  |  |  |  |  |  | links | object | {"bounceLogs": "https://pandadoc72354.activehosted.com/api/3/contacts/2/bounceLogs", "contactAutomations": "https://pandadoc72354.activehosted.com/api/3/contacts/2/contactAutomations?limit=2500&orders%5Blastdate%5D=DESC", "contactData": "https://pandadoc72354.activehosted.com/api/3/contacts/2/contactData", "contactGoals": "https://pandadoc72354.activehosted.com/api/3/contacts/2/contactGoals", "contactLists": "https://pandadoc72354.activehosted.com/api/3/contacts/2/contactLists", "contactLogs": "https://pandadoc72354.activehosted.com/api/3/contacts/2/contactLogs", "contactTags": "https://pandadoc72354.activehosted.com/api/3/contacts/2/contactTags", "contactDeals": "https://pandadoc72354.activehosted.com/api/3/contacts/2/contactDeals", "deals": "https://pandadoc72354.activehosted.com/api/3/contacts/2/deals", "fieldValues": "https://pandadoc72354.activehosted.com/api/3/contacts/2/fieldValues", "geoIps": "https://pandadoc72354.activehosted.com/api/3/contacts/2/geoIps", "notes": "https://pandadoc72354.activehosted.com/api/3/contacts/2/notes", "organization": "https://pandadoc72354.activehosted.com/api/3/contacts/2/organization", "plusAppend": "https://pandadoc72354.activehosted.com/api/3/contacts/2/plusAppend", "trackingLogs": "https://pandadoc72354.activehosted.com/api/3/contacts/2/trackingLogs", "scoreValues": "https://pandadoc72354.activehosted.com/api/3/contacts/2/scoreValues", "accountContacts": "https://pandadoc72354.activehosted.com/api/3/contacts/2/accountContacts", "automationEntryCounts": "https://pandadoc72354.activehosted.com/api/3/contacts/2/automationEntryCounts"} |
|  |  |  |  |  |  | links.accountContacts | string |  |
|  |  |  |  |  |  | links.automationEntryCounts | string |  |
|  |  |  |  |  |  | links.bounceLogs | string |  |
|  |  |  |  |  |  | links.contactAutomations | string |  |
|  |  |  |  |  |  | links.contactData | string |  |
|  |  |  |  |  |  | links.contactDeals | string |  |
|  |  |  |  |  |  | links.contactGoals | string |  |
|  |  |  |  |  |  | links.contactLists | string |  |
|  |  |  |  |  |  | links.contactLogs | string |  |
|  |  |  |  |  |  | links.contactTags | string |  |
|  |  |  |  |  |  | links.deals | string |  |
|  |  |  |  |  |  | links.fieldValues | string |  |
|  |  |  |  |  |  | links.geoIps | string |  |
|  |  |  |  |  |  | links.notes | string |  |
|  |  |  |  |  |  | links.organization | string |  |
|  |  |  |  |  |  | links.plusAppend | string |  |
|  |  |  |  |  |  | links.scoreValues | string |  |
|  |  |  |  |  |  | links.trackingLogs | string |  |
|  |  |  |  |  |  | organization | null | None |

## Accounts

| Entity Schema Title | Entity Schema Fields | Entity Schema Types | Readonly | Possible Values | Reference Collection | Find By ID Object Fields | Find By ID Types | Value |
|---------------------|----------------------|---------------------|----------|-----------------|----------------------|--------------------------|------------------|-------|
|  | accountUrl | string | false |  |  | accountUrl | null | None |
|  | createdTimestamp | string | false |  |  | createdTimestamp | string | 2025-06-10T02:28:15-05:00 |
|  | id | string | true |  |  | id | string | 1 |
|  | *name | string | false |  |  | name | string | Test Account |
|  | owner | string | false |  | users | owner | string | 1 |
|  | updatedTimestamp | string | false |  |  | updatedTimestamp | string | 2025-06-10T02:28:15-05:00 |
|  | <span style='color:red'>***contactCount***</span> | string | false |  |  |  |  |  |
|  | <span style='color:red'>***dealCount***</span> | string | false |  |  |  |  |  |
|  |  |  |  |  |  | links | object | {"notes": "https://pandadoc72354.activehosted.com/api/3/accounts/1/notes", "accountCustomFieldData": "https://pandadoc72354.activehosted.com/api/3/accounts/1/accountCustomFieldData", "accountContacts": "https://pandadoc72354.activehosted.com/api/3/accounts/1/accountContacts", "emailActivities": "https://pandadoc72354.activehosted.com/api/3/accounts/1/emailActivities", "contactEmails": "https://pandadoc72354.activehosted.com/api/3/accounts/1/contactEmails", "owner": "https://pandadoc72354.activehosted.com/api/3/accounts/1/owner"} |
|  |  |  |  |  |  | links.accountContacts | string |  |
|  |  |  |  |  |  | links.accountCustomFieldData | string |  |
|  |  |  |  |  |  | links.contactEmails | string |  |
|  |  |  |  |  |  | links.emailActivities | string |  |
|  |  |  |  |  |  | links.notes | string |  |
|  |  |  |  |  |  | links.owner | string |  |