# Differences between fields in NetSuite


## Accounts

| Diff | Entity Schema Title | Schema Field ID | Entity Schema Types | Readonly | Possible Values | Reference Collection | FindByID Field ID | Find By ID Types | Value |
|------|---------------------|-----------------|---------------------|----------|-----------------|----------------------|-------------------|------------------|-------|
|  |  | accountContextSearch | object | false |  |  | accountContextSearch | object | {"links": [{"rel": "self", "href": "https://td2999479.suitetalk.api.netsuite.com/services/rest/record/v1/account/284/accountContextSearch"}], "items": [], "totalResults": 0} |
|  |  | accountContextSearch.items |  | false |  |  | accountContextSearch.items | array | [] |
|  | Links | accountContextSearch.links | array | true |  |  | accountContextSearch.links | array | [{"rel": "self", "href": "https://td2999479.suitetalk.api.netsuite.com/services/rest/record/v1/account/284/accountContextSearch"}] |
|  |  | accountContextSearch.links[] | object | false |  |  | accountContextSearch.links[] | object | {"rel": "self", "href": "https://td2999479.suitetalk.api.netsuite.com/services/rest/record/v1/account/284/accountContextSearch"} |
|  | Total Results | accountContextSearch.totalResults | integer | true |  |  | accountContextSearch.totalResults | integer | 0 |
|  | Name | acctName | string | false |  |  | acctName | string | Accumulated Depreciation |
|  |  | acctType | object | false |  |  | acctType | object | {"id": "DeferExpense", "refName": "Deferred Expense"} |
|  | Internal identifier | acctType.id | string | false |  |  | acctType.id | string | DeferExpense |
|  | Reference Name | acctType.refName | string | true |  |  | acctType.refName | string | Deferred Expense |
|  |  | cashFlowRate | object | false |  |  | cashFlowRate | object | {"id": "AVERAGE", "refName": "Average"} |
|  | Internal identifier | cashFlowRate.id | string | false |  |  | cashFlowRate.id | string | AVERAGE |
|  | Reference Name | cashFlowRate.refName | string | true |  |  | cashFlowRate.refName | string | Average |
|  | Eliminate Intercompany Transactions | eliminate | boolean | false |  |  | eliminate | boolean | False |
|  |  | generalRate | object | false |  |  | generalRate | object | {"id": "CURRENT", "refName": "Current"} |
|  | Internal identifier | generalRate.id | string | false |  |  | generalRate.id | string | CURRENT |
|  | Reference Name | generalRate.refName | string | true |  |  | generalRate.refName | string | Current |
|  | Internal ID | id | string | false |  |  | id | string | 284 |
|  | Include Children | includeChildren | boolean | false |  |  | includeChildren | boolean | True |
|  | Inventory | inventory | boolean | false |  |  | inventory | boolean | False |
|  | Inactive | isInactive | boolean | false |  |  | isInactive | boolean | False |
|  | Summary | isSummary | boolean | false |  |  | isSummary | boolean | False |
|  | Last Modified Date | lastModifiedDate | string | false |  |  | lastModifiedDate | string | 2025-06-17T21:53:00Z |
|  | Links | links | array | true |  |  | links | array | [{"rel": "self", "href": "https://td2999479.suitetalk.api.netsuite.com/services/rest/record/v1/account/284?expandSubResources=true"}] |
|  |  | links[] | object | false |  |  | links[] | object | {"rel": "self", "href": "https://td2999479.suitetalk.api.netsuite.com/services/rest/record/v1/account/284?expandSubResources=true"} |
|  |  | localizations | object | false |  |  | localizations | object | {"links": [{"rel": "self", "href": "https://td2999479.suitetalk.api.netsuite.com/services/rest/record/v1/account/284/localizations"}], "items": [], "totalResults": 0} |
|  |  | localizations.items |  | false |  |  | localizations.items | array | [] |
|  | Links | localizations.links | array | true |  |  | localizations.links | array | [{"rel": "self", "href": "https://td2999479.suitetalk.api.netsuite.com/services/rest/record/v1/account/284/localizations"}] |
|  |  | localizations.links[] | object | false |  |  | localizations.links[] | object | {"rel": "self", "href": "https://td2999479.suitetalk.api.netsuite.com/services/rest/record/v1/account/284/localizations"} |
|  | Total Results | localizations.totalResults | integer | true |  |  | localizations.totalResults | integer | 0 |
|  | Revalue Open Balance for Foreign Currency Transactions | revalue | boolean | false |  |  | revalue | boolean | False |
|  |  | sSpecAcct | object | false |  |  | sSpecAcct | object | {"id": "AccumDeprec", "refName": "AccumDeprec"} |
|  | Internal identifier | sSpecAcct.id | string | false |  |  | sSpecAcct.id | string | AccumDeprec |
|  | Reference Name | sSpecAcct.refName | string | true |  |  | sSpecAcct.refName | string | AccumDeprec |
|  |  | subsidiary | object | false |  |  | subsidiary | object | {"links": [{"rel": "self", "href": "https://td2999479.suitetalk.api.netsuite.com/services/rest/record/v1/account/284/subsidiary"}], "count": 1, "hasMore": false, "items": [{"links": [{"rel": "self", "href": "https://td2999479.suitetalk.api.netsuite.com/services/rest/record/v1/subsidiary/1"}], "id": "1", "refName": "Headquarters"}], "offset": 0, "totalResults": 1} |
|  | Count | subsidiary.count | integer | true |  |  | subsidiary.count | integer | 1 |
|  | Has More Results | subsidiary.hasMore | boolean | true |  |  | subsidiary.hasMore | boolean | False |
|  |  | subsidiary.items |  | false |  |  | subsidiary.items | array | [{"links": [{"rel": "self", "href": "https://td2999479.suitetalk.api.netsuite.com/services/rest/record/v1/subsidiary/1"}], "id": "1", "refName": "Headquarters"}] |
|  |  | subsidiary.items[] |  | false |  |  | subsidiary.items[] | object | {"links": [{"rel": "self", "href": "https://td2999479.suitetalk.api.netsuite.com/services/rest/record/v1/subsidiary/1"}], "id": "1", "refName": "Headquarters"} |
|  | Links | subsidiary.links | array | true |  |  | subsidiary.links | array | [{"rel": "self", "href": "https://td2999479.suitetalk.api.netsuite.com/services/rest/record/v1/account/284/subsidiary"}] |
|  |  | subsidiary.links[] | object | false |  |  | subsidiary.links[] | object | {"rel": "self", "href": "https://td2999479.suitetalk.api.netsuite.com/services/rest/record/v1/account/284/subsidiary"} |
|  | Query Offset | subsidiary.offset | integer | true |  |  | subsidiary.offset | integer | 0 |
|  | Total Results | subsidiary.totalResults | integer | true |  |  | subsidiary.totalResults | integer | 1 |
| Schema | Count | <span style='color:red'>***accountContextSearch.count***</span> | integer | true |  |  |  |  |  |
| Schema | Has More Results | <span style='color:red'>***accountContextSearch.hasMore***</span> | boolean | true |  |  |  |  |  |
| Schema | Query Offset | <span style='color:red'>***accountContextSearch.offset***</span> | integer | true |  |  |  |  |  |
| Schema | Display Name | <span style='color:red'>***accountSearchDisplayName***</span> | string | false |  |  |  |  |  |
| Schema | Name | <span style='color:red'>***accountSearchDisplayNameCopy***</span> | string | false |  |  |  |  |  |
| Schema | Number | <span style='color:red'>***acctNumber***</span> | string | false |  |  |  |  |  |
| Schema | Balance | <span style='color:red'>***balance***</span> | number | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***billableExpensesAcct***</span> | object | false |  |  |  |  |  |
| Schema | External identifier | <span style='color:red'>***billableExpensesAcct.externalId***</span> | string | false |  |  |  |  |  |
| Schema | Internal identifier | <span style='color:red'>***billableExpensesAcct.id***</span> | string | false |  |  |  |  |  |
| Schema | Links | <span style='color:red'>***billableExpensesAcct.links***</span> | array | true |  |  |  |  |  |
| Schema | Reference Name | <span style='color:red'>***billableExpensesAcct.refName***</span> | string | true |  |  |  |  |  |
| Schema |  | <span style='color:red'>***category1099Misc***</span> | object | false |  |  |  |  |  |
| Schema | External identifier | <span style='color:red'>***category1099Misc.externalId***</span> | string | false |  |  |  |  |  |
| Schema | Internal identifier | <span style='color:red'>***category1099Misc.id***</span> | string | false |  |  |  |  |  |
| Schema | Links | <span style='color:red'>***category1099Misc.links***</span> | array | true |  |  |  |  |  |
| Schema | Reference Name | <span style='color:red'>***category1099Misc.refName***</span> | string | true |  |  |  |  |  |
| Schema |  | <span style='color:red'>***class***</span> | object | false |  |  |  |  |  |
| Schema | External identifier | <span style='color:red'>***class.externalId***</span> | string | false |  |  |  |  |  |
| Schema | Internal identifier | <span style='color:red'>***class.id***</span> | string | false |  |  |  |  |  |
| Schema | Links | <span style='color:red'>***class.links***</span> | array | true |  |  |  |  |  |
| Schema | Reference Name | <span style='color:red'>***class.refName***</span> | string | true |  |  |  |  |  |
| Schema | Next Check Number | <span style='color:red'>***curDocNum***</span> | integer | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***currency***</span> | object | false |  |  |  |  |  |
| Schema | External identifier | <span style='color:red'>***currency.externalId***</span> | string | false |  |  |  |  |  |
| Schema | Internal identifier | <span style='color:red'>***currency.id***</span> | string | false |  |  |  |  |  |
| Schema | Links | <span style='color:red'>***currency.links***</span> | array | true |  |  |  |  |  |
| Schema | Reference Name | <span style='color:red'>***currency.refName***</span> | string | true |  |  |  |  |  |
| Schema |  | <span style='color:red'>***deferralAcct***</span> | object | false |  |  |  |  |  |
| Schema | External identifier | <span style='color:red'>***deferralAcct.externalId***</span> | string | false |  |  |  |  |  |
| Schema | Internal identifier | <span style='color:red'>***deferralAcct.id***</span> | string | false |  |  |  |  |  |
| Schema | Links | <span style='color:red'>***deferralAcct.links***</span> | array | true |  |  |  |  |  |
| Schema | Reference Name | <span style='color:red'>***deferralAcct.refName***</span> | string | true |  |  |  |  |  |
| Schema |  | <span style='color:red'>***department***</span> | object | false |  |  |  |  |  |
| Schema | External identifier | <span style='color:red'>***department.externalId***</span> | string | false |  |  |  |  |  |
| Schema | Internal identifier | <span style='color:red'>***department.id***</span> | string | false |  |  |  |  |  |
| Schema | Links | <span style='color:red'>***department.links***</span> | array | true |  |  |  |  |  |
| Schema | Reference Name | <span style='color:red'>***department.refName***</span> | string | true |  |  |  |  |  |
| Schema | Description | <span style='color:red'>***description***</span> | string | false |  |  |  |  |  |
| Schema | Display Name (with hierarchy) | <span style='color:red'>***displayNameWithHierarchy***</span> | string | false |  |  |  |  |  |
| Schema | External ID | <span style='color:red'>***externalId***</span> | string | false |  |  |  |  |  |
| Schema | Full Name | <span style='color:red'>***fullName***</span> | string | false |  |  |  |  |  |
| Schema | Count | <span style='color:red'>***localizations.count***</span> | integer | true |  |  |  |  |  |
| Schema | Has More Results | <span style='color:red'>***localizations.hasMore***</span> | boolean | true |  |  |  |  |  |
| Schema | Query Offset | <span style='color:red'>***localizations.offset***</span> | integer | true |  |  |  |  |  |
| Schema |  | <span style='color:red'>***location***</span> | object | false |  |  |  |  |  |
| Schema | External identifier | <span style='color:red'>***location.externalId***</span> | string | false |  |  |  |  |  |
| Schema | Internal identifier | <span style='color:red'>***location.id***</span> | string | false |  |  |  |  |  |
| Schema | Links | <span style='color:red'>***location.links***</span> | array | true |  |  |  |  |  |
| Schema | Reference Name | <span style='color:red'>***location.refName***</span> | string | true |  |  |  |  |  |
| Schema | Opening Balance | <span style='color:red'>***openingBalance***</span> | number | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***parent***</span> | object | false |  |  |  |  |  |
| Schema | External identifier | <span style='color:red'>***parent.externalId***</span> | string | false |  |  |  |  |  |
| Schema | Internal identifier | <span style='color:red'>***parent.id***</span> | string | false |  |  |  |  |  |
| Schema | Links | <span style='color:red'>***parent.links***</span> | array | true |  |  |  |  |  |
| Schema | Reference Name | <span style='color:red'>***parent.refName***</span> | string | true |  |  |  |  |  |
| Schema | Use Match Bank Data and Reconcile Account Statement Pages | <span style='color:red'>***reconcileWithMatching***</span> | boolean | false |  |  |  |  |  |
| Schema | Reference Name | <span style='color:red'>***refName***</span> | string | true |  |  |  |  |  |
| Schema | Bank Account Number | <span style='color:red'>***sBankCompanyId***</span> | string | false |  |  |  |  |  |
| Schema | Bank Name | <span style='color:red'>***sBankName***</span> | string | false |  |  |  |  |  |
| Schema | Bank Routing Number | <span style='color:red'>***sBankRoutingNumber***</span> | string | false |  |  |  |  |  |
| Schema | Date | <span style='color:red'>***tranDate***</span> | string | false |  |  |  |  |  |
| Schema | Default Unit | <span style='color:red'>***unit***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***unitsType***</span> | object | false |  |  |  |  |  |
| Schema | External identifier | <span style='color:red'>***unitsType.externalId***</span> | string | false |  |  |  |  |  |
| Schema | Internal identifier | <span style='color:red'>***unitsType.id***</span> | string | false |  |  |  |  |  |
| Schema | Links | <span style='color:red'>***unitsType.links***</span> | array | true |  |  |  |  |  |
| Schema | Reference Name | <span style='color:red'>***unitsType.refName***</span> | string | true |  |  |  |  |  |
| FindByID |  |  |  |  |  |  | accountContextSearch.links[].href | string | https://td2999479.suitetalk.api.netsuite.com/services/rest/record/v1/account/284/accountContextSearch |
| FindByID |  |  |  |  |  |  | accountContextSearch.links[].rel | string | self |
| FindByID |  |  |  |  |  |  | links[].href | string | https://td2999479.suitetalk.api.netsuite.com/services/rest/record/v1/account/284?expandSubResources=true |
| FindByID |  |  |  |  |  |  | links[].rel | string | self |
| FindByID |  |  |  |  |  |  | localizations.links[].href | string | https://td2999479.suitetalk.api.netsuite.com/services/rest/record/v1/account/284/localizations |
| FindByID |  |  |  |  |  |  | localizations.links[].rel | string | self |
| FindByID |  |  |  |  |  |  | subsidiary.items[].id | string | 1 |
| FindByID |  |  |  |  |  |  | subsidiary.items[].links | array | [{"rel": "self", "href": "https://td2999479.suitetalk.api.netsuite.com/services/rest/record/v1/subsidiary/1"}] |
| FindByID |  |  |  |  |  |  | subsidiary.items[].links[] | object | {"rel": "self", "href": "https://td2999479.suitetalk.api.netsuite.com/services/rest/record/v1/subsidiary/1"} |
| FindByID |  |  |  |  |  |  | subsidiary.items[].links[].href | string | https://td2999479.suitetalk.api.netsuite.com/services/rest/record/v1/subsidiary/1 |
| FindByID |  |  |  |  |  |  | subsidiary.items[].links[].rel | string | self |
| FindByID |  |  |  |  |  |  | subsidiary.items[].refName | string | Headquarters |
| FindByID |  |  |  |  |  |  | subsidiary.links[].href | string | https://td2999479.suitetalk.api.netsuite.com/services/rest/record/v1/account/284/subsidiary |
| FindByID |  |  |  |  |  |  | subsidiary.links[].rel | string | self |

## Contacts

| Diff | Entity Schema Title | Schema Field ID | Entity Schema Types | Readonly | Possible Values | Reference Collection | FindByID Field ID | Find By ID Types | Value |
|------|---------------------|-----------------|---------------------|----------|-----------------|----------------------|-------------------|------------------|-------|
|  |  | category | object | false |  |  | category | object | {"links": [{"rel": "self", "href": "https://td2999479.suitetalk.api.netsuite.com/services/rest/record/v1/contact/9392/category"}], "count": 0, "hasMore": false, "items": [], "offset": 0, "totalResults": 0} |
|  | Count | category.count | integer | true |  |  | category.count | integer | 0 |
|  | Has More Results | category.hasMore | boolean | true |  |  | category.hasMore | boolean | False |
|  |  | category.items |  | false |  |  | category.items | array | [] |
|  | Links | category.links | array | true |  |  | category.links | array | [{"rel": "self", "href": "https://td2999479.suitetalk.api.netsuite.com/services/rest/record/v1/contact/9392/category"}] |
|  |  | category.links[] | object | false |  |  | category.links[] | object | {"rel": "self", "href": "https://td2999479.suitetalk.api.netsuite.com/services/rest/record/v1/contact/9392/category"} |
|  | Query Offset | category.offset | integer | true |  |  | category.offset | integer | 0 |
|  | Total Results | category.totalResults | integer | true |  |  | category.totalResults | integer | 0 |
|  | Last Modified Date | custentity_esc_last_modified_date | string | false |  |  | custentity_esc_last_modified_date | string | 2025-06-17 |
|  |  | customForm | object | false |  |  | customForm | object | {"id": "-40", "refName": "Standard Contact Form"} |
|  | Internal identifier | customForm.id | string | false |  |  | customForm.id | string | -40 |
|  | Reference Name | customForm.refName | string | true |  |  | customForm.refName | string | Standard Contact Form |
|  | Date Created | dateCreated | string | false |  |  | dateCreated | string | 2025-06-17T14:51:00Z |
|  | Email | email | string | false |  |  | email | string | 78s1wf3i@example.com |
|  | Entity ID | entityId | string | false |  |  | entityId | string | 8EfDwj FwBUDB21 |
|  | First Name | firstName | string | false |  |  | firstName | string | 8EfDwj |
|  |  | globalSubscriptionStatus | object | false |  |  | globalSubscriptionStatus | object | {"id": "2", "refName": "Soft Opt-Out"} |
|  | Internal identifier | globalSubscriptionStatus.id | string | false |  |  | globalSubscriptionStatus.id | string | 2 |
|  | Reference Name | globalSubscriptionStatus.refName | string | true |  |  | globalSubscriptionStatus.refName | string | Soft Opt-Out |
|  | Internal ID | id | string | false |  |  | id | string | 9392 |
|  | Contact is Inactive | isInactive | boolean | false |  |  | isInactive | boolean | False |
|  | Private | isPrivate | boolean | false |  |  | isPrivate | boolean | False |
|  | Last Modified Date | lastModifiedDate | string | false |  |  | lastModifiedDate | string | 2025-06-17T14:51:00Z |
|  | Last Name | lastName | string | false |  |  | lastName | string | FwBUDB21 |
|  | Links | links | array | true |  |  | links | array | [{"rel": "self", "href": "https://td2999479.suitetalk.api.netsuite.com/services/rest/record/v1/contact/9392?expandSubResources=true"}] |
|  |  | links[] | object | false |  |  | links[] | object | {"rel": "self", "href": "https://td2999479.suitetalk.api.netsuite.com/services/rest/record/v1/contact/9392?expandSubResources=true"} |
|  |  | owner | integer | false |  |  | owner | integer | -5 |
|  |  | subsidiary | object | false |  |  | subsidiary | object | {"links": [{"rel": "self", "href": "https://td2999479.suitetalk.api.netsuite.com/services/rest/record/v1/subsidiary/1"}], "id": "1", "refName": "Headquarters"} |
|  | Internal identifier | subsidiary.id | string | false |  |  | subsidiary.id | string | 1 |
|  | Links | subsidiary.links | array | true |  |  | subsidiary.links | array | [{"rel": "self", "href": "https://td2999479.suitetalk.api.netsuite.com/services/rest/record/v1/subsidiary/1"}] |
|  |  | subsidiary.links[] | object | false |  |  | subsidiary.links[] | object | {"rel": "self", "href": "https://td2999479.suitetalk.api.netsuite.com/services/rest/record/v1/subsidiary/1"} |
|  | Reference Name | subsidiary.refName | string | true |  |  | subsidiary.refName | string | Headquarters |
|  | Unsubscribe from Campaigns | unsubscribe | boolean | false |  |  | unsubscribe | boolean | True |
| Schema | Alt. Email | <span style='color:red'>***altEmail***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***assistant***</span> | object | false |  |  |  |  |  |
| Schema | External identifier | <span style='color:red'>***assistant.externalId***</span> | string | false |  |  |  |  |  |
| Schema | Internal identifier | <span style='color:red'>***assistant.id***</span> | string | false |  |  |  |  |  |
| Schema | Links | <span style='color:red'>***assistant.links***</span> | array | true |  |  |  |  |  |
| Schema | Reference Name | <span style='color:red'>***assistant.refName***</span> | string | true |  |  |  |  |  |
| Schema | Assist. Phone | <span style='color:red'>***assistantPhone***</span> | string | false |  |  |  |  |  |
| Schema | Comments | <span style='color:red'>***comments***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***company***</span> | object | false |  |  |  |  |  |
| Schema | External identifier | <span style='color:red'>***company.externalId***</span> | string | false |  |  |  |  |  |
| Schema | Internal identifier | <span style='color:red'>***company.id***</span> | string | false |  |  |  |  |  |
| Schema | Links | <span style='color:red'>***company.links***</span> | array | true |  |  |  |  |  |
| Schema | Reference Name | <span style='color:red'>***company.refName***</span> | string | true |  |  |  |  |  |
| Schema |  | <span style='color:red'>***contactCampaignEvent***</span> | object | false |  |  |  |  |  |
| Schema | External identifier | <span style='color:red'>***contactCampaignEvent.externalId***</span> | string | false |  |  |  |  |  |
| Schema | Internal identifier | <span style='color:red'>***contactCampaignEvent.id***</span> | string | false |  |  |  |  |  |
| Schema | Links | <span style='color:red'>***contactCampaignEvent.links***</span> | array | true |  |  |  |  |  |
| Schema | Reference Name | <span style='color:red'>***contactCampaignEvent.refName***</span> | string | true |  |  |  |  |  |
| Schema |  | <span style='color:red'>***contactSource***</span> | object | false |  |  |  |  |  |
| Schema | External identifier | <span style='color:red'>***contactSource.externalId***</span> | string | false |  |  |  |  |  |
| Schema | Internal identifier | <span style='color:red'>***contactSource.id***</span> | string | false |  |  |  |  |  |
| Schema | Links | <span style='color:red'>***contactSource.links***</span> | array | true |  |  |  |  |  |
| Schema | Reference Name | <span style='color:red'>***contactSource.refName***</span> | string | true |  |  |  |  |  |
| Schema |  | <span style='color:red'>***contactSourceCampaignCategory***</span> | object | false |  |  |  |  |  |
| Schema | External identifier | <span style='color:red'>***contactSourceCampaignCategory.externalId***</span> | string | false |  |  |  |  |  |
| Schema | Internal identifier | <span style='color:red'>***contactSourceCampaignCategory.id***</span> | string | false |  |  |  |  |  |
| Schema | Links | <span style='color:red'>***contactSourceCampaignCategory.links***</span> | array | true |  |  |  |  |  |
| Schema | Reference Name | <span style='color:red'>***contactSourceCampaignCategory.refName***</span> | string | true |  |  |  |  |  |
| Schema | Last Sales Activity | <span style='color:red'>***custentity_date_lsa***</span> | string | false |  |  |  |  |  |
| Schema | LSA Link | <span style='color:red'>***custentity_link_lsa***</span> | string | false |  |  |  |  |  |
| Schema | LSA Link Name | <span style='color:red'>***custentity_link_name_lsa***</span> | string | false |  |  |  |  |  |
| Schema | CUSTOM FREEFORM TEXT | <span style='color:red'>***custentitycustom_freeform_text***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***emailPreference***</span> | object | false |  |  |  |  |  |
| Schema | Internal identifier | <span style='color:red'>***emailPreference.id***</span> | string | false |  |  |  |  |  |
| Schema | Reference Name | <span style='color:red'>***emailPreference.refName***</span> | string | true |  |  |  |  |  |
| Schema | External ID | <span style='color:red'>***externalId***</span> | string | false |  |  |  |  |  |
| Schema | Fax | <span style='color:red'>***fax***</span> | string | false |  |  |  |  |  |
| Schema | Home Phone | <span style='color:red'>***homePhone***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***image***</span> | object | false |  |  |  |  |  |
| Schema | External identifier | <span style='color:red'>***image.externalId***</span> | string | false |  |  |  |  |  |
| Schema | Internal identifier | <span style='color:red'>***image.id***</span> | string | false |  |  |  |  |  |
| Schema | Links | <span style='color:red'>***image.links***</span> | array | true |  |  |  |  |  |
| Schema | Reference Name | <span style='color:red'>***image.refName***</span> | string | true |  |  |  |  |  |
| Schema | Middle Name | <span style='color:red'>***middleName***</span> | string | false |  |  |  |  |  |
| Schema | Mobile Phone | <span style='color:red'>***mobilePhone***</span> | string | false |  |  |  |  |  |
| Schema | Office Phone | <span style='color:red'>***officePhone***</span> | string | false |  |  |  |  |  |
| Schema | Main Phone | <span style='color:red'>***phone***</span> | string | false |  |  |  |  |  |
| Schema | Reference Name | <span style='color:red'>***refName***</span> | string | true |  |  |  |  |  |
| Schema | Mr./Ms... | <span style='color:red'>***salutation***</span> | string | false |  |  |  |  |  |
| Schema | External identifier | <span style='color:red'>***subsidiary.externalId***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***supervisor***</span> | object | false |  |  |  |  |  |
| Schema | External identifier | <span style='color:red'>***supervisor.externalId***</span> | string | false |  |  |  |  |  |
| Schema | Internal identifier | <span style='color:red'>***supervisor.id***</span> | string | false |  |  |  |  |  |
| Schema | Links | <span style='color:red'>***supervisor.links***</span> | array | true |  |  |  |  |  |
| Schema | Reference Name | <span style='color:red'>***supervisor.refName***</span> | string | true |  |  |  |  |  |
| Schema | Sup. Phone | <span style='color:red'>***supervisorPhone***</span> | string | false |  |  |  |  |  |
| Schema | Job Title | <span style='color:red'>***title***</span> | string | false |  |  |  |  |  |
| FindByID |  |  |  |  |  |  | category.links[].href | string | https://td2999479.suitetalk.api.netsuite.com/services/rest/record/v1/contact/9392/category |
| FindByID |  |  |  |  |  |  | category.links[].rel | string | self |
| FindByID |  |  |  |  |  |  | links[].href | string | https://td2999479.suitetalk.api.netsuite.com/services/rest/record/v1/contact/9392?expandSubResources=true |
| FindByID |  |  |  |  |  |  | links[].rel | string | self |
| FindByID |  |  |  |  |  |  | subsidiary.links[].href | string | https://td2999479.suitetalk.api.netsuite.com/services/rest/record/v1/subsidiary/1 |
| FindByID |  |  |  |  |  |  | subsidiary.links[].rel | string | self |