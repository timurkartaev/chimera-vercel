# Differences between fields in Salesforce

## Opportunities

| Entity Schema Fields          | Find By ID Object Fields      |
|-------------------------------|-------------------------------|
| AccountId                     | AccountId                     |
| Amount                        | Amount                        |
| CampaignId                    | CampaignId                    |
| CloseDate                     | CloseDate                     |
| ContactId                     | ContactId                     |
| CreatedById                   | CreatedById                   |
| CreatedDate                   | CreatedDate                   |
| CurrentGenerators__c          | CurrentGenerators__c          |
| DeliveryInstallationStatus__c | DeliveryInstallationStatus__c |
| Description                   | Description                   |
| ExpectedRevenue               | ExpectedRevenue               |
| Fiscal                        | Fiscal                        |
| FiscalQuarter                 | FiscalQuarter                 |
| FiscalYear                    | FiscalYear                    |
| ForecastCategory              | ForecastCategory              |
| ForecastCategoryName          | ForecastCategoryName          |
| HasOpenActivity               | HasOpenActivity               |
| HasOpportunityLineItem        | HasOpportunityLineItem        |
| HasOverdueTask                | HasOverdueTask                |
| Id                            | Id                            |
| IsClosed                      | IsClosed                      |
| IsDeleted                     | IsDeleted                     |
| IsPrivate                     | IsPrivate                     |
| IsWon                         | IsWon                         |
| LastActivityDate              | LastActivityDate              |
| LastAmountChangedHistoryId    | LastAmountChangedHistoryId    |
| LastCloseDateChangedHistoryId | LastCloseDateChangedHistoryId |
| LastModifiedById              | LastModifiedById              |
| LastModifiedDate              | LastModifiedDate              |
| LastReferencedDate            | LastReferencedDate            |
| LastStageChangeDate           | LastStageChangeDate           |
| LastViewedDate                | LastViewedDate                |
| LeadSource                    | LeadSource                    |
| MainCompetitors__c            | MainCompetitors__c            |
| Name                          | Name                          |
| NextStep                      | NextStep                      |
| OrderNumber__c                | OrderNumber__c                |
| OwnerId                       | OwnerId                       |
| Pricebook2Id                  | Pricebook2Id                  |
| Probability                   | Probability                   |
| PushCount                     | PushCount                     |
| StageId                       | StageId                       |
| StageName                     | StageName                     |
| SystemModstamp                | SystemModstamp                |
| TotalOpportunityQuantity      | TotalOpportunityQuantity      |
| TrackingNumber__c             | TrackingNumber__c             |
| Type                          | Type                          |

## Leads

| Entity Schema Fields   | Find By ID Object Fields |
|------------------------|--------------------------|
| AnnualRevenue          | AnnualRevenue            |
| City                   | City                     |
| CleanStatus            | CleanStatus              |
| Company                | Company                  |
| CompanyDunsNumber      | CompanyDunsNumber        |
| ConvertedAccountId     | ConvertedAccountId       |
| ConvertedContactId     | ConvertedContactId       |
| ConvertedDate          | ConvertedDate            |
| ConvertedOpportunityId | ConvertedOpportunityId   |
| Country                | Country                  |
| CountryCode            | CountryCode              |
| CreatedById            | CreatedById              |
| CreatedDate            | CreatedDate              |
| CurrentGenerators__c   | CurrentGenerators__c     |
| DandbCompanyId         | DandbCompanyId           |
| Description            | Description              |
| Email                  | Email                    |
| EmailBouncedDate       | EmailBouncedDate         |
| EmailBouncedReason     | EmailBouncedReason       |
| Fax                    | Fax                      |
| FirstName              | FirstName                |
| GeocodeAccuracy        | GeocodeAccuracy          |
| Id                     | Id                       |
| IndividualId           | IndividualId             |
| Industry               | Industry                 |
| IsConverted            | IsConverted              |
| IsDeleted              | IsDeleted                |
| IsPriorityRecord       | IsPriorityRecord         |
| IsUnreadByOwner        | IsUnreadByOwner          |
| Jigsaw                 | Jigsaw                   |
| JigsawContactId        | JigsawContactId          |
| LastActivityDate       | LastActivityDate         |
| LastModifiedById       | LastModifiedById         |
| LastModifiedDate       | LastModifiedDate         |
| LastName               | LastName                 |
| LastReferencedDate     | LastReferencedDate       |
| LastViewedDate         | LastViewedDate           |
| Latitude               | Latitude                 |
| LeadSource             | LeadSource               |
| Longitude              | Longitude                |
| MasterRecordId         | MasterRecordId           |
| MobilePhone            | MobilePhone              |
| Name                   | Name                     |
| NumberOfEmployees      | NumberOfEmployees        |
| NumberofLocations__c   | NumberofLocations__c     |
| OwnerId                | OwnerId                  |
| Phone                  | Phone                    |
| PhotoUrl               | PhotoUrl                 |
| PostalCode             | PostalCode               |
| Primary__c             | Primary__c               |
| ProductInterest__c     | ProductInterest__c       |
| Rating                 | Rating                   |
| SICCode__c             | SICCode__c               |
| Salutation             | Salutation               |
| State                  | State                    |
| StateCode              | StateCode                |
| Status                 | Status                   |
| Street                 | Street                   |
| SystemModstamp         | SystemModstamp           |
| Title                  | Title                    |
| Website                | Website                  |
|                        | Address                  |

## Accounts

| Entity Schema Fields    | Find By ID Object Fields        |
|-------------------------|---------------------------------|
| AccountNumber           | AccountNumber                   |
| AccountSource           | AccountSource                   |
| Active__c               | Active__c                       |
| AnnualRevenue           | AnnualRevenue                   |
| BillingCity             | BillingCity                     |
| BillingCountry          | BillingCountry                  |
| BillingCountryCode      | BillingCountryCode              |
| BillingGeocodeAccuracy  | BillingGeocodeAccuracy          |
| BillingLatitude         | BillingLatitude                 |
| BillingLongitude        | BillingLongitude                |
| BillingPostalCode       | BillingPostalCode               |
| BillingState            | BillingState                    |
| BillingStateCode        | BillingStateCode                |
| BillingStreet           | BillingStreet                   |
| CleanStatus             | CleanStatus                     |
| CreatedById             | CreatedById                     |
| CreatedDate             | CreatedDate                     |
| CustomerPriority__c     | CustomerPriority__c             |
| DandbCompanyId          | DandbCompanyId                  |
| Description             | Description                     |
| DunsNumber              | DunsNumber                      |
| Fax                     | Fax                             |
| Id                      | Id                              |
| Industry                | Industry                        |
| IsDeleted               | IsDeleted                       |
| Jigsaw                  | Jigsaw                          |
| JigsawCompanyId         | JigsawCompanyId                 |
| LastActivityDate        | LastActivityDate                |
| LastModifiedById        | LastModifiedById                |
| LastModifiedDate        | LastModifiedDate                |
| LastReferencedDate      | LastReferencedDate              |
| LastViewedDate          | LastViewedDate                  |
| MasterRecordId          | MasterRecordId                  |
| NaicsCode               | NaicsCode                       |
| NaicsDesc               | NaicsDesc                       |
| Name                    | Name                            |
| NumberOfEmployees       | NumberOfEmployees               |
| NumberofLocations__c    | NumberofLocations__c            |
| OperatingHoursId        | OperatingHoursId                |
| OwnerId                 | OwnerId                         |
| Ownership               | Ownership                       |
| ParentId                | ParentId                        |
| Phone                   | Phone                           |
| PhotoUrl                | PhotoUrl                        |
| Rating                  | Rating                          |
| SLAExpirationDate__c    | SLAExpirationDate__c            |
| SLASerialNumber__c      | SLASerialNumber__c              |
| SLA__c                  | SLA__c                          |
| ShippingCity            | ShippingCity                    |
| ShippingCountry         | ShippingCountry                 |
| ShippingCountryCode     | ShippingCountryCode             |
| ShippingGeocodeAccuracy | ShippingGeocodeAccuracy         |
| ShippingLatitude        | ShippingLatitude                |
| ShippingLongitude       | ShippingLongitude               |
| ShippingPostalCode      | ShippingPostalCode              |
| ShippingState           | ShippingState                   |
| ShippingStateCode       | ShippingStateCode               |
| ShippingStreet          | ShippingStreet                  |
| Sic                     | Sic                             |
| SicDesc                 | SicDesc                         |
| Site                    | Site                            |
| SystemModstamp          | SystemModstamp                  |
| TickerSymbol            | TickerSymbol                    |
| Tradestyle              | Tradestyle                      |
| Type                    | Type                            |
| UpsellOpportunity__c    | UpsellOpportunity__c            |
| Website                 | Website                         |
| YearStarted             | YearStarted                     |
| ChannelProgramLevelName |                                 |
| ChannelProgramName      |                                 |
| IsCustomerPortal        |                                 |
| IsPartner               |                                 |
|                         | BillingAddress.city             |
|                         | BillingAddress.country          |
|                         | BillingAddress.countryCode      |
|                         | BillingAddress.geocodeAccuracy  |
|                         | BillingAddress.latitude         |
|                         | BillingAddress.longitude        |
|                         | BillingAddress.postalCode       |
|                         | BillingAddress.state            |
|                         | BillingAddress.stateCode        |
|                         | BillingAddress.street           |
|                         | ShippingAddress.city            |
|                         | ShippingAddress.country         |
|                         | ShippingAddress.countryCode     |
|                         | ShippingAddress.geocodeAccuracy |
|                         | ShippingAddress.latitude        |
|                         | ShippingAddress.longitude       |
|                         | ShippingAddress.postalCode      |
|                         | ShippingAddress.state           |
|                         | ShippingAddress.stateCode       |
|                         | ShippingAddress.street          |