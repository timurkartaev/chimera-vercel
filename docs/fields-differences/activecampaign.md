# Differences between fields in ActiveCampaign.io


## Deals

| Entity Schema Title | Entity Schema Fields | Entity Schema Types | Readonly | Possible Values | Reference Collection | Find By ID Object Fields | Find By ID Types |
|---------------------|----------------------|---------------------|----------|-----------------|----------------------|--------------------------|------------------|
|  | account | string |  |  | accounts | account | null |
|  | activitycount | string |  |  |  | activitycount | str |
|  | cdate | string |  |  |  | cdate | str |
|  | contact | string |  |  | contacts | contact | str |
|  | currency | string |  |  |  | currency | str |
|  | customerAccount | string |  |  | accounts | customerAccount | null |
|  | description | string |  |  |  | description | str |
|  | edate | string |  |  |  | edate | str |
|  | group | string |  |  |  | group | str |
|  | id | string | true |  |  | id | str |
|  | isDisabled | boolean |  |  |  | isDisabled | bool |
|  | links | object |  |  |  | links | object |
|  | links.account | string |  |  |  | links.account | str |
|  | links.contact | string |  |  |  | links.contact | str |
|  | links.contactDeals | string |  |  |  | links.contactDeals | str |
|  | links.customerAccount | string |  |  |  | links.customerAccount | str |
|  | links.dealActivities | string |  |  |  | links.dealActivities | str |
|  | links.dealCustomFieldData | string |  |  |  | links.dealCustomFieldData | str |
|  | links.group | string |  |  |  | links.group | str |
|  | links.nextTask | string |  |  |  | links.nextTask | str |
|  | links.notes | string |  |  |  | links.notes | str |
|  | links.organization | string |  |  |  | links.organization | str |
|  | links.owner | string |  |  |  | links.owner | str |
|  | links.scoreValues | string |  |  |  | links.scoreValues | str |
|  | links.stage | string |  |  |  | links.stage | str |
|  | links.tasks | string |  |  |  | links.tasks | str |
|  | mdate | string |  |  |  | mdate | str |
|  | nextdate | string |  |  |  | nextdate | null |
|  | nextdealid | string |  |  | deals | nextdealid | str |
|  | nexttaskid | string |  |  | deal-tasks | nexttaskid | str |
|  | organization | string |  |  | accounts | organization | null |
|  | owner | string |  |  | users | owner | str |
|  | percent | string |  |  |  | percent | str |
|  | stage | string |  |  | deal-stages | stage | str |
|  | status | string |  | `Open`, `Won`, `Lost` |  | status | str |
|  | title | string |  |  |  | title | str |
|  | value | string |  |  |  | value | str |
|  | winProbability | integer |  |  |  | winProbability | null |
|  | winProbabilityMdate | string |  |  |  | winProbabilityMdate | str |
|  |  |  |  |  |  | hash | str |
|  |  |  |  |  |  | nextTask | null |

## Contacts

| Entity Schema Title | Entity Schema Fields | Entity Schema Types | Readonly | Possible Values | Reference Collection | Find By ID Object Fields | Find By ID Types |
|---------------------|----------------------|---------------------|----------|-----------------|----------------------|--------------------------|------------------|
|  | accountContacts | array |  |  |  | accountContacts | array |
|  | accountContacts[] | string |  |  |  | accountContacts[] | array |
|  | adate | string |  |  |  | adate | str |
|  | anonymized | string |  |  |  | anonymized | str |
|  | bounced_date | string |  |  |  | bounced_date | null |
|  | bounced_hard | string |  |  |  | bounced_hard | str |
|  | bounced_soft | string |  |  |  | bounced_soft | str |
|  | cdate | string |  |  |  | cdate | str |
|  | contactAutomations | array |  |  |  | contactAutomations | array |
|  | contactAutomations[] | string |  |  |  | contactAutomations[] | array |
|  | contactLists | array |  |  |  | contactLists | array |
|  | created_by | string |  |  |  | created_by | str |
|  | created_timestamp | string |  |  |  | created_timestamp | str |
|  | created_utc_timestamp | string |  |  |  | created_utc_timestamp | str |
|  | deals | array |  |  |  | deals | array |
|  | deals[] | string |  |  |  | deals[] | array |
|  | deleted | string |  |  |  | deleted | str |
|  | deleted_at | string |  |  |  | deleted_at | null |
|  | edate | string |  |  |  | edate | str |
|  | email | string |  |  |  | email | str |
|  | email_domain | string |  |  |  | email_domain | str |
|  | email_local | string |  |  |  | email_local | str |
|  | fieldValues | array |  |  |  | fieldValues | array |
|  | firstName | string |  |  |  | firstName | str |
|  | geoIps | array |  |  |  | geoIps | array |
|  | gravatar | string |  |  |  | gravatar | str |
|  | hash | string |  |  |  | hash | str |
|  | id | string | true |  |  | id | str |
|  | ip | string |  |  |  | ip | str |
|  | lastName | string |  |  |  | lastName | str |
|  | mpp_tracking | string |  |  |  | mpp_tracking | str |
|  | orgid | string |  |  | accounts | orgid | str |
|  | orgname | string |  |  |  | orgname | str |
|  | phone | string |  |  |  | phone | str |
|  | rating_tstamp | string |  |  |  | rating_tstamp | null |
|  | segmentio_id | string |  |  |  | segmentio_id | str |
|  | sentcnt | string |  |  |  | sentcnt | str |
|  | socialdata_lastcheck | string |  |  |  | socialdata_lastcheck | null |
|  | ua | string |  |  |  | ua | str |
|  | udate | string |  |  |  | udate | str |
|  | updated_by | string |  |  |  | updated_by | str |
|  | updated_timestamp | string |  |  |  | updated_timestamp | str |
|  | updated_utc_timestamp | string |  |  |  | updated_utc_timestamp | str |
|  | <span style='color:red'>***email_empty***</span> | boolean |  |  |  |  |  |
|  | <span style='color:red'>***jobTitle***</span> | string |  |  |  |  |  |
|  |  |  |  |  |  | best_send_hour | str |
|  |  |  |  |  |  | contactLists[] | array |
|  |  |  |  |  |  | fieldValues[] | array |
|  |  |  |  |  |  | geoIps[] | array |
|  |  |  |  |  |  | last_click_date | null |
|  |  |  |  |  |  | last_mpp_open_date | null |
|  |  |  |  |  |  | last_open_date | null |
|  |  |  |  |  |  | links | object |
|  |  |  |  |  |  | links.accountContacts | str |
|  |  |  |  |  |  | links.automationEntryCounts | str |
|  |  |  |  |  |  | links.bounceLogs | str |
|  |  |  |  |  |  | links.contactAutomations | str |
|  |  |  |  |  |  | links.contactData | str |
|  |  |  |  |  |  | links.contactDeals | str |
|  |  |  |  |  |  | links.contactGoals | str |
|  |  |  |  |  |  | links.contactLists | str |
|  |  |  |  |  |  | links.contactLogs | str |
|  |  |  |  |  |  | links.contactTags | str |
|  |  |  |  |  |  | links.deals | str |
|  |  |  |  |  |  | links.fieldValues | str |
|  |  |  |  |  |  | links.geoIps | str |
|  |  |  |  |  |  | links.notes | str |
|  |  |  |  |  |  | links.organization | str |
|  |  |  |  |  |  | links.plusAppend | str |
|  |  |  |  |  |  | links.scoreValues | str |
|  |  |  |  |  |  | links.trackingLogs | str |
|  |  |  |  |  |  | organization | null |

## Accounts

| Entity Schema Title | Entity Schema Fields | Entity Schema Types | Readonly | Possible Values | Reference Collection | Find By ID Object Fields | Find By ID Types |
|---------------------|----------------------|---------------------|----------|-----------------|----------------------|--------------------------|------------------|
|  | accountUrl | string |  |  |  | accountUrl | null |
|  | createdTimestamp | string |  |  |  | createdTimestamp | str |
|  | id | string | true |  |  | id | str |
|  | name | string |  |  |  | name | str |
|  | owner | string |  |  | users | owner | str |
|  | updatedTimestamp | string |  |  |  | updatedTimestamp | str |
|  | <span style='color:red'>***contactCount***</span> | string |  |  |  |  |  |
|  | <span style='color:red'>***dealCount***</span> | string |  |  |  |  |  |
|  |  |  |  |  |  | links | object |
|  |  |  |  |  |  | links.accountContacts | str |
|  |  |  |  |  |  | links.accountCustomFieldData | str |
|  |  |  |  |  |  | links.contactEmails | str |
|  |  |  |  |  |  | links.emailActivities | str |
|  |  |  |  |  |  | links.notes | str |
|  |  |  |  |  |  | links.owner | str |