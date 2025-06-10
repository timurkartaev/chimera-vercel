# Differences between fields in Salesforce

## Opportunities

| Entity Schema Fields          | Entity Schema Types | Find By ID Object Fields      | Find By ID Types |
|-------------------------------|---------------------|-------------------------------|------------------|
| AccountId                     | string              | AccountId                     | str              |
| Amount                        | number              | Amount                        | int              |
| CampaignId                    | string              | CampaignId                    | null             |
| CloseDate                     | string              | CloseDate                     | str              |
| ContactId                     | string              | ContactId                     | null             |
| CreatedById                   | string              | CreatedById                   | str              |
| CreatedDate                   | string              | CreatedDate                   | str              |
| CurrentGenerators__c          | string              | CurrentGenerators__c          | null             |
| DeliveryInstallationStatus__c | string              | DeliveryInstallationStatus__c | null             |
| Description                   | string              | Description                   | null             |
| ExpectedRevenue               | number              | ExpectedRevenue               | int              |
| Fiscal                        | string              | Fiscal                        | str              |
| FiscalQuarter                 | number              | FiscalQuarter                 | int              |
| FiscalYear                    | number              | FiscalYear                    | int              |
| ForecastCategory              | string              | ForecastCategory              | str              |
| ForecastCategoryName          | string              | ForecastCategoryName          | str              |
| HasOpenActivity               | boolean             | HasOpenActivity               | bool             |
| HasOpportunityLineItem        | boolean             | HasOpportunityLineItem        | bool             |
| HasOverdueTask                | boolean             | HasOverdueTask                | bool             |
| Id                            | string              | Id                            | str              |
| IsClosed                      | boolean             | IsClosed                      | bool             |
| IsDeleted                     | boolean             | IsDeleted                     | bool             |
| IsPrivate                     | boolean             | IsPrivate                     | bool             |
| IsWon                         | boolean             | IsWon                         | bool             |
| LastActivityDate              | string              | LastActivityDate              | null             |
| LastAmountChangedHistoryId    | string              | LastAmountChangedHistoryId    | null             |
| LastCloseDateChangedHistoryId | string              | LastCloseDateChangedHistoryId | null             |
| LastModifiedById              | string              | LastModifiedById              | str              |
| LastModifiedDate              | string              | LastModifiedDate              | str              |
| LastReferencedDate            | string              | LastReferencedDate            | str              |
| LastStageChangeDate           | string              | LastStageChangeDate           | null             |
| LastViewedDate                | string              | LastViewedDate                | str              |
| LeadSource                    | string              | LeadSource                    | str              |
| MainCompetitors__c            | string              | MainCompetitors__c            | str              |
| Name                          | string              | Name                          | str              |
| NextStep                      | string              | NextStep                      | null             |
| OrderNumber__c                | string              | OrderNumber__c                | null             |
| OwnerId                       | string              | OwnerId                       | str              |
| Pricebook2Id                  | string              | Pricebook2Id                  | str              |
| Probability                   | number              | Probability                   | int              |
| PushCount                     | number              | PushCount                     | int              |
| StageId                       | string              | StageId                       | str              |
| StageName                     | string              | StageName                     | str              |
| SystemModstamp                | string              | SystemModstamp                | str              |
| TotalOpportunityQuantity      | number              | TotalOpportunityQuantity      | int              |
| TrackingNumber__c             | string              | TrackingNumber__c             | null             |
| Type                          | string              | Type                          | str              |

## Leads

| Entity Schema Fields   | Entity Schema Types | Find By ID Object Fields | Find By ID Types |
|------------------------|---------------------|--------------------------|------------------|
| AnnualRevenue          | number              | AnnualRevenue            | null             |
| City                   | string              | City                     | null             |
| CleanStatus            | string              | CleanStatus              | str              |
| Company                | string              | Company                  | str              |
| CompanyDunsNumber      | string              | CompanyDunsNumber        | null             |
| ConvertedAccountId     | string              | ConvertedAccountId       | null             |
| ConvertedContactId     | string              | ConvertedContactId       | null             |
| ConvertedDate          | string              | ConvertedDate            | null             |
| ConvertedOpportunityId | string              | ConvertedOpportunityId   | null             |
| Country                | string              | Country                  | null             |
| CountryCode            | string              | CountryCode              | null             |
| CreatedById            | string              | CreatedById              | str              |
| CreatedDate            | string              | CreatedDate              | str              |
| CurrentGenerators__c   | string              | CurrentGenerators__c     | null             |
| DandbCompanyId         | string              | DandbCompanyId           | null             |
| Description            | string              | Description              | null             |
| Email                  | string              | Email                    | null             |
| EmailBouncedDate       | string              | EmailBouncedDate         | null             |
| EmailBouncedReason     | string              | EmailBouncedReason       | null             |
| Fax                    | string              | Fax                      | null             |
| FirstName              | string              | FirstName                | null             |
| GeocodeAccuracy        | string              | GeocodeAccuracy          | null             |
| Id                     | string              | Id                       | str              |
| IndividualId           | string              | IndividualId             | null             |
| Industry               | string              | Industry                 | null             |
| IsConverted            | boolean             | IsConverted              | bool             |
| IsDeleted              | boolean             | IsDeleted                | bool             |
| IsPriorityRecord       | boolean             | IsPriorityRecord         | bool             |
| IsUnreadByOwner        | boolean             | IsUnreadByOwner          | bool             |
| Jigsaw                 | string              | Jigsaw                   | null             |
| JigsawContactId        | string              | JigsawContactId          | null             |
| LastActivityDate       | string              | LastActivityDate         | null             |
| LastModifiedById       | string              | LastModifiedById         | str              |
| LastModifiedDate       | string              | LastModifiedDate         | str              |
| LastName               | string              | LastName                 | str              |
| LastReferencedDate     | string              | LastReferencedDate       | str              |
| LastViewedDate         | string              | LastViewedDate           | str              |
| Latitude               | number              | Latitude                 | null             |
| LeadSource             | string              | LeadSource               | null             |
| Longitude              | number              | Longitude                | null             |
| MasterRecordId         | string              | MasterRecordId           | null             |
| MobilePhone            | string              | MobilePhone              | null             |
| Name                   | string              | Name                     | str              |
| NumberOfEmployees      | number              | NumberOfEmployees        | null             |
| NumberofLocations__c   | number              | NumberofLocations__c     | null             |
| OwnerId                | string              | OwnerId                  | str              |
| Phone                  | string              | Phone                    | null             |
| PhotoUrl               | string              | PhotoUrl                 | str              |
| PostalCode             | string              | PostalCode               | null             |
| Primary__c             | string              | Primary__c               | null             |
| ProductInterest__c     | string              | ProductInterest__c       | null             |
| Rating                 | string              | Rating                   | null             |
| SICCode__c             | string              | SICCode__c               | null             |
| Salutation             | string              | Salutation               | str              |
| State                  | string              | State                    | null             |
| StateCode              | string              | StateCode                | null             |
| Status                 | string              | Status                   | str              |
| Street                 | string              | Street                   | null             |
| SystemModstamp         | string              | SystemModstamp           | str              |
| Title                  | string              | Title                    | null             |
| Website                | string              | Website                  | null             |
|                        |                     | Address                  | null             |

## Accounts

| Entity Schema Fields    | Entity Schema Types | Find By ID Object Fields        | Find By ID Types |
|-------------------------|---------------------|---------------------------------|------------------|
| AccountNumber           | string              | AccountNumber                   | str              |
| AccountSource           | string              | AccountSource                   | null             |
| Active__c               | string              | Active__c                       | str              |
| AnnualRevenue           | number              | AnnualRevenue                   | int              |
| BillingCity             | string              | BillingCity                     | str              |
| BillingCountry          | string              | BillingCountry                  | str              |
| BillingCountryCode      | string              | BillingCountryCode              | str              |
| BillingGeocodeAccuracy  | string              | BillingGeocodeAccuracy          | null             |
| BillingLatitude         | number              | BillingLatitude                 | null             |
| BillingLongitude        | number              | BillingLongitude                | null             |
| BillingPostalCode       | string              | BillingPostalCode               | str              |
| BillingState            | string              | BillingState                    | str              |
| BillingStateCode        | string              | BillingStateCode                | str              |
| BillingStreet           | string              | BillingStreet                   | str              |
| CleanStatus             | string              | CleanStatus                     | str              |
| CreatedById             | string              | CreatedById                     | str              |
| CreatedDate             | string              | CreatedDate                     | str              |
| CustomerPriority__c     | string              | CustomerPriority__c             | str              |
| DandbCompanyId          | string              | DandbCompanyId                  | null             |
| Description             | string              | Description                     | null             |
| DunsNumber              | string              | DunsNumber                      | null             |
| Fax                     | string              | Fax                             | str              |
| Id                      | string              | Id                              | str              |
| Industry                | string              | Industry                        | str              |
| IsDeleted               | boolean             | IsDeleted                       | bool             |
| Jigsaw                  | string              | Jigsaw                          | null             |
| JigsawCompanyId         | string              | JigsawCompanyId                 | null             |
| LastActivityDate        | string              | LastActivityDate                | null             |
| LastModifiedById        | string              | LastModifiedById                | str              |
| LastModifiedDate        | string              | LastModifiedDate                | str              |
| LastReferencedDate      | string              | LastReferencedDate              | str              |
| LastViewedDate          | string              | LastViewedDate                  | str              |
| MasterRecordId          | string              | MasterRecordId                  | null             |
| NaicsCode               | string              | NaicsCode                       | null             |
| NaicsDesc               | string              | NaicsDesc                       | null             |
| Name                    | string              | Name                            | str              |
| NumberOfEmployees       | number              | NumberOfEmployees               | int              |
| NumberofLocations__c    | number              | NumberofLocations__c            | int              |
| OperatingHoursId        | string              | OperatingHoursId                | null             |
| OwnerId                 | string              | OwnerId                         | str              |
| Ownership               | string              | Ownership                       | str              |
| ParentId                | string              | ParentId                        | null             |
| Phone                   | string              | Phone                           | str              |
| PhotoUrl                | string              | PhotoUrl                        | str              |
| Rating                  | string              | Rating                          | null             |
| SLAExpirationDate__c    | string              | SLAExpirationDate__c            | str              |
| SLASerialNumber__c      | string              | SLASerialNumber__c              | str              |
| SLA__c                  | string              | SLA__c                          | str              |
| ShippingCity            | string              | ShippingCity                    | str              |
| ShippingCountry         | string              | ShippingCountry                 | str              |
| ShippingCountryCode     | string              | ShippingCountryCode             | str              |
| ShippingGeocodeAccuracy | string              | ShippingGeocodeAccuracy         | null             |
| ShippingLatitude        | number              | ShippingLatitude                | null             |
| ShippingLongitude       | number              | ShippingLongitude               | null             |
| ShippingPostalCode      | string              | ShippingPostalCode              | str              |
| ShippingState           | string              | ShippingState                   | str              |
| ShippingStateCode       | string              | ShippingStateCode               | str              |
| ShippingStreet          | string              | ShippingStreet                  | str              |
| Sic                     | string              | Sic                             | str              |
| SicDesc                 | string              | SicDesc                         | null             |
| Site                    | string              | Site                            | null             |
| SystemModstamp          | string              | SystemModstamp                  | str              |
| TickerSymbol            | string              | TickerSymbol                    | null             |
| Tradestyle              | string              | Tradestyle                      | null             |
| Type                    | string              | Type                            | str              |
| UpsellOpportunity__c    | string              | UpsellOpportunity__c            | str              |
| Website                 | string              | Website                         | str              |
| YearStarted             | string              | YearStarted                     | null             |
| ChannelProgramLevelName | string              |                                 |                  |
| ChannelProgramName      | string              |                                 |                  |
| IsCustomerPortal        | boolean             |                                 |                  |
| IsPartner               | boolean             |                                 |                  |
|                         |                     | BillingAddress.city             | str              |
|                         |                     | BillingAddress.country          | str              |
|                         |                     | BillingAddress.countryCode      | str              |
|                         |                     | BillingAddress.geocodeAccuracy  | null             |
|                         |                     | BillingAddress.latitude         | null             |
|                         |                     | BillingAddress.longitude        | null             |
|                         |                     | BillingAddress.postalCode       | str              |
|                         |                     | BillingAddress.state            | str              |
|                         |                     | BillingAddress.stateCode        | str              |
|                         |                     | BillingAddress.street           | str              |
|                         |                     | ShippingAddress.city            | str              |
|                         |                     | ShippingAddress.country         | str              |
|                         |                     | ShippingAddress.countryCode     | str              |
|                         |                     | ShippingAddress.geocodeAccuracy | null             |
|                         |                     | ShippingAddress.latitude        | null             |
|                         |                     | ShippingAddress.longitude       | null             |
|                         |                     | ShippingAddress.postalCode      | str              |
|                         |                     | ShippingAddress.state           | str              |
|                         |                     | ShippingAddress.stateCode       | str              |
|                         |                     | ShippingAddress.street          | str              |