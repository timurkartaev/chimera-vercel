# Differences between fields in ActiveCampaign


## Deals

| Diff | Entity Schema Title | Schema Field ID | Entity Schema Types | Readonly | Possible Values | Reference Collection | FindByID Field ID | Find By ID Types | Value |
|------|---------------------|-----------------|---------------------|----------|-----------------|----------------------|-------------------|------------------|-------|
|  |  | account | string | false |  | accounts | account | null | None |
|  |  | activitycount | string | false |  |  | activitycount | string | 2 |
|  |  | cdate | string | false |  |  | cdate | string | 2025-06-17T06:27:38-05:00 |
|  |  | contact | string | false |  | contacts | contact | string | 862 |
|  |  | *currency | string | false |  |  | currency | string | usd |
|  |  | customerAccount | string | false |  | accounts | customerAccount | null | None |
|  |  | description | string | false |  |  | description | string | Test Deal to test iPaaS |
|  |  | edate | string | false |  |  | edate | string | 2025-06-17 06:27:44 |
|  |  | group | string | false |  |  | group | string | 1 |
|  |  | id | string | true |  |  | id | string | 42 |
|  |  | isDisabled | boolean | false |  |  | isDisabled | boolean | False |
|  |  | links | object | false |  |  | links | object | {"dealActivities": "https://pandadoc1634815026.activehosted.com/api/3/deals/42/dealActivities", "contact": "https://pandadoc1634815026.activehosted.com/api/3/deals/42/contact", "contactDeals": "https://pandadoc1634815026.activehosted.com/api/3/deals/42/contactDeals", "group": "https://pandadoc1634815026.activehosted.com/api/3/deals/42/group", "nextTask": "https://pandadoc1634815026.activehosted.com/api/3/deals/42/nextTask", "notes": "https://pandadoc1634815026.activehosted.com/api/3/deals/42/notes", "account": "https://pandadoc1634815026.activehosted.com/api/3/deals/42/account", "customerAccount": "https://pandadoc1634815026.activehosted.com/api/3/deals/42/customerAccount", "organization": "https://pandadoc1634815026.activehosted.com/api/3/deals/42/organization", "owner": "https://pandadoc1634815026.activehosted.com/api/3/deals/42/owner", "scoreValues": "https://pandadoc1634815026.activehosted.com/api/3/deals/42/scoreValues", "stage": "https://pandadoc1634815026.activehosted.com/api/3/deals/42/stage", "tasks": "https://pandadoc1634815026.activehosted.com/api/3/deals/42/tasks", "dealCustomFieldData": "https://pandadoc1634815026.activehosted.com/api/3/deals/42/dealCustomFieldData"} |
|  |  | links.account | string | false |  |  | links.account | string | https://pandadoc1634815026.activehosted.com/api/3/deals/42/account |
|  |  | links.contact | string | false |  |  | links.contact | string | https://pandadoc1634815026.activehosted.com/api/3/deals/42/contact |
|  |  | links.contactDeals | string | false |  |  | links.contactDeals | string | https://pandadoc1634815026.activehosted.com/api/3/deals/42/contactDeals |
|  |  | links.customerAccount | string | false |  |  | links.customerAccount | string | https://pandadoc1634815026.activehosted.com/api/3/deals/42/customerAccount |
|  |  | links.dealActivities | string | false |  |  | links.dealActivities | string | https://pandadoc1634815026.activehosted.com/api/3/deals/42/dealActivities |
|  |  | links.dealCustomFieldData | string | false |  |  | links.dealCustomFieldData | string | https://pandadoc1634815026.activehosted.com/api/3/deals/42/dealCustomFieldData |
|  |  | links.group | string | false |  |  | links.group | string | https://pandadoc1634815026.activehosted.com/api/3/deals/42/group |
|  |  | links.nextTask | string | false |  |  | links.nextTask | string | https://pandadoc1634815026.activehosted.com/api/3/deals/42/nextTask |
|  |  | links.notes | string | false |  |  | links.notes | string | https://pandadoc1634815026.activehosted.com/api/3/deals/42/notes |
|  |  | links.organization | string | false |  |  | links.organization | string | https://pandadoc1634815026.activehosted.com/api/3/deals/42/organization |
|  |  | links.owner | string | false |  |  | links.owner | string | https://pandadoc1634815026.activehosted.com/api/3/deals/42/owner |
|  |  | links.scoreValues | string | false |  |  | links.scoreValues | string | https://pandadoc1634815026.activehosted.com/api/3/deals/42/scoreValues |
|  |  | links.stage | string | false |  |  | links.stage | string | https://pandadoc1634815026.activehosted.com/api/3/deals/42/stage |
|  |  | links.tasks | string | false |  |  | links.tasks | string | https://pandadoc1634815026.activehosted.com/api/3/deals/42/tasks |
|  |  | mdate | string | false |  |  | mdate | string | 2025-06-17T06:27:38-05:00 |
|  |  | nextdate | string | false |  |  | nextdate | null | None |
|  |  | nextdealid | string | false |  | deals | nextdealid | string | 42 |
|  |  | nexttaskid | string | false |  | deal-tasks | nexttaskid | null | None |
|  |  | organization | string | false |  | accounts | organization | null | None |
|  |  | *owner | string | false |  | users | owner | string | 1 |
|  |  | percent | string | false |  |  | percent | string | 0 |
|  |  | stage | string | false |  | deal-stages | stage | string | 1 |
|  |  | status | string | false | `Open`, `Won`, `Lost` |  | status | string | 0 |
|  |  | title | string | false |  |  | title | string | Doniyor Test deal |
|  |  | *value | string | false |  |  | value | string | 10000 |
|  |  | winProbability | integer | false |  |  | winProbability | null | None |
|  |  | winProbabilityMdate | string | false |  |  | winProbabilityMdate | string | 2025-06-17T06:27:38-05:00 |
| FindByID |  |  |  |  |  |  | hash | string | 6a99868c |

## Contacts

| Diff | Entity Schema Title | Schema Field ID | Entity Schema Types | Readonly | Possible Values | Reference Collection | FindByID Field ID | Find By ID Types | Value |
|------|---------------------|-----------------|---------------------|----------|-----------------|----------------------|-------------------|------------------|-------|
|  |  | accountContacts | array | false |  |  | accountContacts | array | [] |
|  |  | accountContacts[] | string | false |  |  | accountContacts[] | string |  |
|  |  | adate | string | false |  |  | adate | string | 2025-06-17T06:31:00-05:00 |
|  |  | anonymized | string | false |  |  | anonymized | string | 0 |
|  |  | bounced_date | string | false |  |  | bounced_date | null | None |
|  |  | bounced_hard | string | false |  |  | bounced_hard | string | 0 |
|  |  | bounced_soft | string | false |  |  | bounced_soft | string | 0 |
|  |  | cdate | string | false |  |  | cdate | string | 2025-06-17T06:27:37-05:00 |
|  |  | contactAutomations | array | false |  |  | contactAutomations | array | [] |
|  |  | contactAutomations[] | string | false |  |  | contactAutomations[] | string |  |
|  |  | contactLists | array | false |  |  | contactLists | array | [] |
|  |  | created_by | string | false |  |  | created_by | string | 0 |
|  |  | created_timestamp | string | false |  |  | created_timestamp | string | 2025-06-17 06:27:37 |
|  |  | created_utc_timestamp | string | false |  |  | created_utc_timestamp | string | 2025-06-17 06:27:37 |
|  |  | deals | array | false |  |  | deals | array | ["42"] |
|  |  | deals[] | string | false |  |  | deals[] | string | 42 |
|  |  | deleted | string | false |  |  | deleted | string | 0 |
|  |  | deleted_at | string | false |  |  | deleted_at | null | None |
|  |  | edate | string | false |  |  | edate | string | 2025-06-17T06:27:56-05:00 |
|  |  | *email | string | false |  |  | email | string | contr.doniyor.rufatov@pandadoc.com |
|  |  | email_domain | string | false |  |  | email_domain | string | pandadoc.com |
|  |  | email_local | string | false |  |  | email_local | string |  |
|  |  | fieldValues | array | false |  |  | fieldValues | array | [] |
|  |  | firstName | string | false |  |  | firstName | string | Doniyor |
|  |  | geoIps | array | false |  |  | geoIps | array | [] |
|  |  | gravatar | string | false |  |  | gravatar | string | 0 |
|  |  | hash | string | false |  |  | hash | string | ca6448dfc018f27a964708b9dae31fc1 |
|  |  | id | string | true |  |  | id | string | 862 |
|  |  | ip | string | false |  |  | ip | string | 0 |
|  |  | lastName | string | false |  |  | lastName | string | Rufatov |
|  |  | mpp_tracking | string | false |  |  | mpp_tracking | string | 0 |
|  |  | orgid | string | false |  | accounts | orgid | string | 0 |
|  |  | orgname | string | false |  |  | orgname | string |  |
|  |  | phone | string | false |  |  | phone | string |  |
|  |  | rating_tstamp | string | false |  |  | rating_tstamp | null | None |
|  |  | segmentio_id | string | false |  |  | segmentio_id | string |  |
|  |  | sentcnt | string | false |  |  | sentcnt | string | 0 |
|  |  | socialdata_lastcheck | string | false |  |  | socialdata_lastcheck | null | None |
|  |  | ua | string | false |  |  | ua | string |  |
|  |  | udate | string | false |  |  | udate | string | 2025-06-17T06:27:37-05:00 |
|  |  | updated_by | string | false |  |  | updated_by | string | 0 |
|  |  | updated_timestamp | string | false |  |  | updated_timestamp | string | 2025-06-17 06:27:56 |
|  |  | updated_utc_timestamp | string | false |  |  | updated_utc_timestamp | string | 2025-06-17 06:27:56 |
| Schema |  | <span style='color:red'>***email_empty***</span> | boolean | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***jobTitle***</span> | string | false |  |  |  |  |  |
| FindByID |  |  |  |  |  |  | best_send_hour | string | 0 |
| FindByID |  |  |  |  |  |  | last_click_date | null | None |
| FindByID |  |  |  |  |  |  | last_mpp_open_date | null | None |
| FindByID |  |  |  |  |  |  | last_open_date | null | None |
| FindByID |  |  |  |  |  |  | links | object | {"bounceLogs": "https://pandadoc1634815026.activehosted.com/api/3/contacts/862/bounceLogs", "contactAutomations": "https://pandadoc1634815026.activehosted.com/api/3/contacts/862/contactAutomations?limit=2500&orders%5Blastdate%5D=DESC", "contactData": "https://pandadoc1634815026.activehosted.com/api/3/contacts/862/contactData", "contactGoals": "https://pandadoc1634815026.activehosted.com/api/3/contacts/862/contactGoals", "contactLists": "https://pandadoc1634815026.activehosted.com/api/3/contacts/862/contactLists", "contactLogs": "https://pandadoc1634815026.activehosted.com/api/3/contacts/862/contactLogs", "contactTags": "https://pandadoc1634815026.activehosted.com/api/3/contacts/862/contactTags", "contactDeals": "https://pandadoc1634815026.activehosted.com/api/3/contacts/862/contactDeals", "deals": "https://pandadoc1634815026.activehosted.com/api/3/contacts/862/deals", "fieldValues": "https://pandadoc1634815026.activehosted.com/api/3/contacts/862/fieldValues", "geoIps": "https://pandadoc1634815026.activehosted.com/api/3/contacts/862/geoIps", "notes": "https://pandadoc1634815026.activehosted.com/api/3/contacts/862/notes", "organization": "https://pandadoc1634815026.activehosted.com/api/3/contacts/862/organization", "plusAppend": "https://pandadoc1634815026.activehosted.com/api/3/contacts/862/plusAppend", "trackingLogs": "https://pandadoc1634815026.activehosted.com/api/3/contacts/862/trackingLogs", "scoreValues": "https://pandadoc1634815026.activehosted.com/api/3/contacts/862/scoreValues", "accountContacts": "https://pandadoc1634815026.activehosted.com/api/3/contacts/862/accountContacts", "automationEntryCounts": "https://pandadoc1634815026.activehosted.com/api/3/contacts/862/automationEntryCounts"} |
| FindByID |  |  |  |  |  |  | links.accountContacts | string | https://pandadoc1634815026.activehosted.com/api/3/contacts/862/accountContacts |
| FindByID |  |  |  |  |  |  | links.automationEntryCounts | string | https://pandadoc1634815026.activehosted.com/api/3/contacts/862/automationEntryCounts |
| FindByID |  |  |  |  |  |  | links.bounceLogs | string | https://pandadoc1634815026.activehosted.com/api/3/contacts/862/bounceLogs |
| FindByID |  |  |  |  |  |  | links.contactAutomations | string | https://pandadoc1634815026.activehosted.com/api/3/contacts/862/contactAutomations?limit=2500&orders%5Blastdate%5D=DESC |
| FindByID |  |  |  |  |  |  | links.contactData | string | https://pandadoc1634815026.activehosted.com/api/3/contacts/862/contactData |
| FindByID |  |  |  |  |  |  | links.contactDeals | string | https://pandadoc1634815026.activehosted.com/api/3/contacts/862/contactDeals |
| FindByID |  |  |  |  |  |  | links.contactGoals | string | https://pandadoc1634815026.activehosted.com/api/3/contacts/862/contactGoals |
| FindByID |  |  |  |  |  |  | links.contactLists | string | https://pandadoc1634815026.activehosted.com/api/3/contacts/862/contactLists |
| FindByID |  |  |  |  |  |  | links.contactLogs | string | https://pandadoc1634815026.activehosted.com/api/3/contacts/862/contactLogs |
| FindByID |  |  |  |  |  |  | links.contactTags | string | https://pandadoc1634815026.activehosted.com/api/3/contacts/862/contactTags |
| FindByID |  |  |  |  |  |  | links.deals | string | https://pandadoc1634815026.activehosted.com/api/3/contacts/862/deals |
| FindByID |  |  |  |  |  |  | links.fieldValues | string | https://pandadoc1634815026.activehosted.com/api/3/contacts/862/fieldValues |
| FindByID |  |  |  |  |  |  | links.geoIps | string | https://pandadoc1634815026.activehosted.com/api/3/contacts/862/geoIps |
| FindByID |  |  |  |  |  |  | links.notes | string | https://pandadoc1634815026.activehosted.com/api/3/contacts/862/notes |
| FindByID |  |  |  |  |  |  | links.organization | string | https://pandadoc1634815026.activehosted.com/api/3/contacts/862/organization |
| FindByID |  |  |  |  |  |  | links.plusAppend | string | https://pandadoc1634815026.activehosted.com/api/3/contacts/862/plusAppend |
| FindByID |  |  |  |  |  |  | links.scoreValues | string | https://pandadoc1634815026.activehosted.com/api/3/contacts/862/scoreValues |
| FindByID |  |  |  |  |  |  | links.trackingLogs | string | https://pandadoc1634815026.activehosted.com/api/3/contacts/862/trackingLogs |
| FindByID |  |  |  |  |  |  | organization | null | None |

## Accounts

| Diff | Entity Schema Title | Schema Field ID | Entity Schema Types | Readonly | Possible Values | Reference Collection | FindByID Field ID | Find By ID Types | Value |
|------|---------------------|-----------------|---------------------|----------|-----------------|----------------------|-------------------|------------------|-------|
|  |  | accountUrl | string | false |  |  | accountUrl | string |  |
|  |  | createdTimestamp | string | false |  |  | createdTimestamp | string | 2021-10-21T07:02:59-05:00 |
|  |  | id | string | true |  |  | id | string | 1 |
|  |  | *name | string | false |  |  | name | string | PandaDoc, Inc. |
|  |  | owner | string | false |  | users | owner | string | 1 |
|  |  | updatedTimestamp | string | false |  |  | updatedTimestamp | string | 2024-03-12T06:27:00-05:00 |
| Schema |  | <span style='color:red'>***contactCount***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***dealCount***</span> | string | false |  |  |  |  |  |
| FindByID |  |  |  |  |  |  | links | object | {"notes": "https://pandadoc1634815026.activehosted.com/api/3/accounts/1/notes", "accountCustomFieldData": "https://pandadoc1634815026.activehosted.com/api/3/accounts/1/accountCustomFieldData", "accountContacts": "https://pandadoc1634815026.activehosted.com/api/3/accounts/1/accountContacts", "emailActivities": "https://pandadoc1634815026.activehosted.com/api/3/accounts/1/emailActivities", "contactEmails": "https://pandadoc1634815026.activehosted.com/api/3/accounts/1/contactEmails", "owner": "https://pandadoc1634815026.activehosted.com/api/3/accounts/1/owner"} |
| FindByID |  |  |  |  |  |  | links.accountContacts | string | https://pandadoc1634815026.activehosted.com/api/3/accounts/1/accountContacts |
| FindByID |  |  |  |  |  |  | links.accountCustomFieldData | string | https://pandadoc1634815026.activehosted.com/api/3/accounts/1/accountCustomFieldData |
| FindByID |  |  |  |  |  |  | links.contactEmails | string | https://pandadoc1634815026.activehosted.com/api/3/accounts/1/contactEmails |
| FindByID |  |  |  |  |  |  | links.emailActivities | string | https://pandadoc1634815026.activehosted.com/api/3/accounts/1/emailActivities |
| FindByID |  |  |  |  |  |  | links.notes | string | https://pandadoc1634815026.activehosted.com/api/3/accounts/1/notes |
| FindByID |  |  |  |  |  |  | links.owner | string | https://pandadoc1634815026.activehosted.com/api/3/accounts/1/owner |