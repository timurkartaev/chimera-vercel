# Differences between fields in Salesforce.io

## Opportunities

| Entity Schema Title          | Entity Schema Fields          | Entity Schema Types | Find By ID Object Fields      | Find By ID Types |
|------------------------------|-------------------------------|---------------------|-------------------------------|------------------|
| Account ID                   | AccountId                     | string              | AccountId                     | str              |
| Amount                       | Amount                        | number              | Amount                        | int              |
| Campaign ID                  | CampaignId                    | string              | CampaignId                    | null             |
| Close Date                   | CloseDate                     | string              | CloseDate                     | str              |
| Contact ID                   | ContactId                     | string              | ContactId                     | null             |
| Created By ID                | CreatedById                   | string              | CreatedById                   | str              |
| Created Date                 | CreatedDate                   | string              | CreatedDate                   | str              |
| Current Generator(s)         | CurrentGenerators__c          | string              | CurrentGenerators__c          | null             |
| Delivery/Installation Status | DeliveryInstallationStatus__c | string              | DeliveryInstallationStatus__c | null             |
| Description                  | Description                   | string              | Description                   | null             |
| Expected Amount              | ExpectedRevenue               | number              | ExpectedRevenue               | int              |
| Fiscal Period                | Fiscal                        | string              | Fiscal                        | str              |
| Fiscal Quarter               | FiscalQuarter                 | number              | FiscalQuarter                 | int              |
| Fiscal Year                  | FiscalYear                    | number              | FiscalYear                    | int              |
| Forecast Category            | ForecastCategory              | string              | ForecastCategory              | str              |
| Forecast Category            | ForecastCategoryName          | string              | ForecastCategoryName          | str              |
| Has Open Activity            | HasOpenActivity               | boolean             | HasOpenActivity               | bool             |
| Has Line Item                | HasOpportunityLineItem        | boolean             | HasOpportunityLineItem        | bool             |
| Has Overdue Task             | HasOverdueTask                | boolean             | HasOverdueTask                | bool             |
| Opportunity ID               | Id                            | string              | Id                            | str              |
| Closed                       | IsClosed                      | boolean             | IsClosed                      | bool             |
| Deleted                      | IsDeleted                     | boolean             | IsDeleted                     | bool             |
| Private                      | IsPrivate                     | boolean             | IsPrivate                     | bool             |
| Won                          | IsWon                         | boolean             | IsWon                         | bool             |
| Last Activity                | LastActivityDate              | string              | LastActivityDate              | null             |
| Opportunity History ID       | LastAmountChangedHistoryId    | string              | LastAmountChangedHistoryId    | null             |
| Opportunity History ID       | LastCloseDateChangedHistoryId | string              | LastCloseDateChangedHistoryId | null             |
| Last Modified By ID          | LastModifiedById              | string              | LastModifiedById              | str              |
| Last Modified Date           | LastModifiedDate              | string              | LastModifiedDate              | str              |
| Last Referenced Date         | LastReferencedDate            | string              | LastReferencedDate            | str              |
| Last Stage Change Date       | LastStageChangeDate           | string              | LastStageChangeDate           | null             |
| Last Viewed Date             | LastViewedDate                | string              | LastViewedDate                | str              |
| Lead Source                  | LeadSource                    | string              | LeadSource                    | str              |
| Main Competitor(s)           | MainCompetitors__c            | string              | MainCompetitors__c            | str              |
| Name                         | Name                          | string              | Name                          | str              |
| Next Step                    | NextStep                      | string              | NextStep                      | null             |
| Order Number                 | OrderNumber__c                | string              | OrderNumber__c                | null             |
| Owner ID                     | OwnerId                       | string              | OwnerId                       | str              |
| Price Book ID                | Pricebook2Id                  | string              | Pricebook2Id                  | str              |
| Probability (%)              | Probability                   | number              | Probability                   | int              |
| Push Count                   | PushCount                     | number              | PushCount                     | int              |
| Stage ID                     | StageId                       | string              | StageId                       | str              |
| Stage                        | StageName                     | string              | StageName                     | str              |
| System Modstamp              | SystemModstamp                | string              | SystemModstamp                | str              |
| Quantity                     | TotalOpportunityQuantity      | number              | TotalOpportunityQuantity      | int              |
| Tracking Number              | TrackingNumber__c             | string              | TrackingNumber__c             | null             |
| Opportunity Type             | Type                          | string              | Type                          | str              |

## Leads

| Entity Schema Title      | Entity Schema Fields   | Entity Schema Types | Find By ID Object Fields | Find By ID Types |
|--------------------------|------------------------|---------------------|--------------------------|------------------|
| Annual Revenue           | AnnualRevenue          | number              | AnnualRevenue            | null             |
| City                     | City                   | string              | City                     | null             |
| Clean Status             | CleanStatus            | string              | CleanStatus              | str              |
| Company                  | Company                | string              | Company                  | str              |
| Company D-U-N-S Number   | CompanyDunsNumber      | string              | CompanyDunsNumber        | null             |
| Converted Account ID     | ConvertedAccountId     | string              | ConvertedAccountId       | null             |
| Converted Contact ID     | ConvertedContactId     | string              | ConvertedContactId       | null             |
| Converted Date           | ConvertedDate          | string              | ConvertedDate            | null             |
| Converted Opportunity ID | ConvertedOpportunityId | string              | ConvertedOpportunityId   | null             |
| Country                  | Country                | string              | Country                  | null             |
| Country Code             | CountryCode            | string              | CountryCode              | null             |
| Created By ID            | CreatedById            | string              | CreatedById              | str              |
| Created Date             | CreatedDate            | string              | CreatedDate              | str              |
| Current Generator(s)     | CurrentGenerators__c   | string              | CurrentGenerators__c     | null             |
| D&B Company ID           | DandbCompanyId         | string              | DandbCompanyId           | null             |
| Description              | Description            | string              | Description              | null             |
| Email                    | Email                  | string              | Email                    | null             |
| Email Bounced Date       | EmailBouncedDate       | string              | EmailBouncedDate         | null             |
| Email Bounced Reason     | EmailBouncedReason     | string              | EmailBouncedReason       | null             |
| Fax                      | Fax                    | string              | Fax                      | null             |
| First Name               | FirstName              | string              | FirstName                | null             |
| Geocode Accuracy         | GeocodeAccuracy        | string              | GeocodeAccuracy          | null             |
| Lead ID                  | Id                     | string              | Id                       | str              |
| Individual ID            | IndividualId           | string              | IndividualId             | null             |
| Industry                 | Industry               | string              | Industry                 | null             |
| Converted                | IsConverted            | boolean             | IsConverted              | bool             |
| Deleted                  | IsDeleted              | boolean             | IsDeleted                | bool             |
| Important                | IsPriorityRecord       | boolean             | IsPriorityRecord         | bool             |
| Unread By Owner          | IsUnreadByOwner        | boolean             | IsUnreadByOwner          | bool             |
| Data.com Key             | Jigsaw                 | string              | Jigsaw                   | null             |
| Jigsaw Contact ID        | JigsawContactId        | string              | JigsawContactId          | null             |
| Last Activity            | LastActivityDate       | string              | LastActivityDate         | null             |
| Last Modified By ID      | LastModifiedById       | string              | LastModifiedById         | str              |
| Last Modified Date       | LastModifiedDate       | string              | LastModifiedDate         | str              |
| Last Name                | LastName               | string              | LastName                 | str              |
| Last Referenced Date     | LastReferencedDate     | string              | LastReferencedDate       | str              |
| Last Viewed Date         | LastViewedDate         | string              | LastViewedDate           | str              |
| Latitude                 | Latitude               | number              | Latitude                 | null             |
| Lead Source              | LeadSource             | string              | LeadSource               | null             |
| Longitude                | Longitude              | number              | Longitude                | null             |
| Master Record ID         | MasterRecordId         | string              | MasterRecordId           | null             |
| Mobile Phone             | MobilePhone            | string              | MobilePhone              | null             |
| Full Name                | Name                   | string              | Name                     | str              |
| Employees                | NumberOfEmployees      | number              | NumberOfEmployees        | null             |
| Number of Locations      | NumberofLocations__c   | number              | NumberofLocations__c     | null             |
| Owner ID                 | OwnerId                | string              | OwnerId                  | str              |
| Phone                    | Phone                  | string              | Phone                    | null             |
| Photo URL                | PhotoUrl               | string              | PhotoUrl                 | str              |
| Zip/Postal Code          | PostalCode             | string              | PostalCode               | null             |
| Primary                  | Primary__c             | string              | Primary__c               | null             |
| Product Interest         | ProductInterest__c     | string              | ProductInterest__c       | null             |
| Rating                   | Rating                 | string              | Rating                   | null             |
| SIC Code                 | SICCode__c             | string              | SICCode__c               | null             |
| Salutation               | Salutation             | string              | Salutation               | str              |
| State/Province           | State                  | string              | State                    | null             |
| State/Province Code      | StateCode              | string              | StateCode                | null             |
| Status                   | Status                 | string              | Status                   | str              |
| Street                   | Street                 | string              | Street                   | null             |
| System Modstamp          | SystemModstamp         | string              | SystemModstamp           | str              |
| Title                    | Title                  | string              | Title                    | null             |
| Website                  | Website                | string              | Website                  | null             |
|                          |                        |                     | Address                  | null             |

## Accounts

| Entity Schema Title          | Entity Schema Fields                                         | Entity Schema Types | Find By ID Object Fields        | Find By ID Types |
|------------------------------|--------------------------------------------------------------|---------------------|---------------------------------|------------------|
| Account Number               | AccountNumber                                                | string              | AccountNumber                   | str              |
| Account Source               | AccountSource                                                | string              | AccountSource                   | null             |
| Active                       | Active__c                                                    | string              | Active__c                       | str              |
| Annual Revenue               | AnnualRevenue                                                | number              | AnnualRevenue                   | int              |
| Billing City                 | BillingCity                                                  | string              | BillingCity                     | str              |
| Billing Country              | BillingCountry                                               | string              | BillingCountry                  | str              |
| Billing Country Code         | BillingCountryCode                                           | string              | BillingCountryCode              | str              |
| Billing Geocode Accuracy     | BillingGeocodeAccuracy                                       | string              | BillingGeocodeAccuracy          | null             |
| Billing Latitude             | BillingLatitude                                              | number              | BillingLatitude                 | null             |
| Billing Longitude            | BillingLongitude                                             | number              | BillingLongitude                | null             |
| Billing Zip/Postal Code      | BillingPostalCode                                            | string              | BillingPostalCode               | str              |
| Billing State/Province       | BillingState                                                 | string              | BillingState                    | str              |
| Billing State/Province Code  | BillingStateCode                                             | string              | BillingStateCode                | str              |
| Billing Street               | BillingStreet                                                | string              | BillingStreet                   | str              |
| Clean Status                 | CleanStatus                                                  | string              | CleanStatus                     | str              |
| Created By ID                | CreatedById                                                  | string              | CreatedById                     | str              |
| Created Date                 | CreatedDate                                                  | string              | CreatedDate                     | str              |
| Customer Priority            | CustomerPriority__c                                          | string              | CustomerPriority__c             | str              |
| D&B Company ID               | DandbCompanyId                                               | string              | DandbCompanyId                  | null             |
| Account Description          | Description                                                  | string              | Description                     | null             |
| D-U-N-S Number               | DunsNumber                                                   | string              | DunsNumber                      | null             |
| Account Fax                  | Fax                                                          | string              | Fax                             | str              |
| Account ID                   | Id                                                           | string              | Id                              | str              |
| Industry                     | Industry                                                     | string              | Industry                        | str              |
| Deleted                      | IsDeleted                                                    | boolean             | IsDeleted                       | bool             |
| Data.com Key                 | Jigsaw                                                       | string              | Jigsaw                          | null             |
| Jigsaw Company ID            | JigsawCompanyId                                              | string              | JigsawCompanyId                 | null             |
| Last Activity                | LastActivityDate                                             | string              | LastActivityDate                | null             |
| Last Modified By ID          | LastModifiedById                                             | string              | LastModifiedById                | str              |
| Last Modified Date           | LastModifiedDate                                             | string              | LastModifiedDate                | str              |
| Last Referenced Date         | LastReferencedDate                                           | string              | LastReferencedDate              | str              |
| Last Viewed Date             | LastViewedDate                                               | string              | LastViewedDate                  | str              |
| Master Record ID             | MasterRecordId                                               | string              | MasterRecordId                  | null             |
| NAICS Code                   | NaicsCode                                                    | string              | NaicsCode                       | null             |
| NAICS Description            | NaicsDesc                                                    | string              | NaicsDesc                       | null             |
| Account Name                 | Name                                                         | string              | Name                            | str              |
| Employees                    | NumberOfEmployees                                            | number              | NumberOfEmployees               | int              |
| Number of Locations          | NumberofLocations__c                                         | number              | NumberofLocations__c            | int              |
| Operating Hour ID            | OperatingHoursId                                             | string              | OperatingHoursId                | null             |
| Owner ID                     | OwnerId                                                      | string              | OwnerId                         | str              |
| Ownership                    | Ownership                                                    | string              | Ownership                       | str              |
| Parent Account ID            | ParentId                                                     | string              | ParentId                        | null             |
| Account Phone                | Phone                                                        | string              | Phone                           | str              |
| Photo URL                    | PhotoUrl                                                     | string              | PhotoUrl                        | str              |
| Account Rating               | Rating                                                       | string              | Rating                          | null             |
| SLA Expiration Date          | SLAExpirationDate__c                                         | string              | SLAExpirationDate__c            | str              |
| SLA Serial Number            | SLASerialNumber__c                                           | string              | SLASerialNumber__c              | str              |
| SLA                          | SLA__c                                                       | string              | SLA__c                          | str              |
| Shipping City                | ShippingCity                                                 | string              | ShippingCity                    | str              |
| Shipping Country             | ShippingCountry                                              | string              | ShippingCountry                 | str              |
| Shipping Country Code        | ShippingCountryCode                                          | string              | ShippingCountryCode             | str              |
| Shipping Geocode Accuracy    | ShippingGeocodeAccuracy                                      | string              | ShippingGeocodeAccuracy         | null             |
| Shipping Latitude            | ShippingLatitude                                             | number              | ShippingLatitude                | null             |
| Shipping Longitude           | ShippingLongitude                                            | number              | ShippingLongitude               | null             |
| Shipping Zip/Postal Code     | ShippingPostalCode                                           | string              | ShippingPostalCode              | str              |
| Shipping State/Province      | ShippingState                                                | string              | ShippingState                   | str              |
| Shipping State/Province Code | ShippingStateCode                                            | string              | ShippingStateCode               | str              |
| Shipping Street              | ShippingStreet                                               | string              | ShippingStreet                  | str              |
| SIC Code                     | Sic                                                          | string              | Sic                             | str              |
| SIC Description              | SicDesc                                                      | string              | SicDesc                         | null             |
| Account Site                 | Site                                                         | string              | Site                            | null             |
| System Modstamp              | SystemModstamp                                               | string              | SystemModstamp                  | str              |
| Ticker Symbol                | TickerSymbol                                                 | string              | TickerSymbol                    | null             |
| Tradestyle                   | Tradestyle                                                   | string              | Tradestyle                      | null             |
| Account Type                 | Type                                                         | string              | Type                            | str              |
| Upsell Opportunity           | UpsellOpportunity__c                                         | string              | UpsellOpportunity__c            | str              |
| Website                      | Website                                                      | string              | Website                         | str              |
| Year Started                 | YearStarted                                                  | string              | YearStarted                     | null             |
| Channel Program Level Name   | <span style='color:red'>***ChannelProgramLevelName***</span> | string              |                                 |                  |
| Channel Program Name         | <span style='color:red'>***ChannelProgramName***</span>      | string              |                                 |                  |
| Customer Portal Account      | <span style='color:red'>***IsCustomerPortal***</span>        | boolean             |                                 |                  |
| Partner Account              | <span style='color:red'>***IsPartner***</span>               | boolean             |                                 |                  |
|                              |                                                              |                     | BillingAddress.city             | str              |
|                              |                                                              |                     | BillingAddress.country          | str              |
|                              |                                                              |                     | BillingAddress.countryCode      | str              |
|                              |                                                              |                     | BillingAddress.geocodeAccuracy  | null             |
|                              |                                                              |                     | BillingAddress.latitude         | null             |
|                              |                                                              |                     | BillingAddress.longitude        | null             |
|                              |                                                              |                     | BillingAddress.postalCode       | str              |
|                              |                                                              |                     | BillingAddress.state            | str              |
|                              |                                                              |                     | BillingAddress.stateCode        | str              |
|                              |                                                              |                     | BillingAddress.street           | str              |
|                              |                                                              |                     | ShippingAddress.city            | str              |
|                              |                                                              |                     | ShippingAddress.country         | str              |
|                              |                                                              |                     | ShippingAddress.countryCode     | str              |
|                              |                                                              |                     | ShippingAddress.geocodeAccuracy | null             |
|                              |                                                              |                     | ShippingAddress.latitude        | null             |
|                              |                                                              |                     | ShippingAddress.longitude       | null             |
|                              |                                                              |                     | ShippingAddress.postalCode      | str              |
|                              |                                                              |                     | ShippingAddress.state           | str              |
|                              |                                                              |                     | ShippingAddress.stateCode       | str              |
|                              |                                                              |                     | ShippingAddress.street          | str              |