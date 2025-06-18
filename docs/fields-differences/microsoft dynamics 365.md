# Differences between fields in Microsoft Dynamics 365


## Opportunities

| Diff | Entity Schema Title | Schema Field ID | Entity Schema Types | Readonly | Possible Values | Reference Collection | FindByID Field ID | Find By ID Types | Value |
|------|---------------------|-----------------|---------------------|----------|-----------------|----------------------|-------------------|------------------|-------|
|  | Actual Close Date | actualclosedate | string | false |  |  | actualclosedate | null | None |
|  | Actual Revenue | actualvalue | number | false |  |  | actualvalue | null | None |
|  | Actual Revenue (Base) | actualvalue_base | number | false |  |  | actualvalue_base | null | None |
|  | Budget amount | budgetamount | number | false |  |  | budgetamount | null | None |
|  | Budget Amount (Base) | budgetamount_base | number | false |  |  | budgetamount_base | null | None |
|  | Budget | budgetstatus | string | false | `No Committed Budget`, `May Buy`, `Can Buy`, `Will Buy` |  | budgetstatus | null | None |
|  | Source Campaign | campaignid | string | false |  | campaigns | campaignid | null | None |
|  | Proposal Feedback Captured | captureproposalfeedback | boolean | false |  |  | captureproposalfeedback | boolean | False |
|  | Probability | closeprobability | number | false |  |  | closeprobability | integer | 93 |
|  | Final Proposal Ready | completefinalproposal | boolean | false |  |  | completefinalproposal | boolean | False |
|  | Complete Internal Review | completeinternalreview | boolean | false |  |  | completeinternalreview | boolean | False |
|  | Confirm Interest | confirminterest | boolean | false |  |  | confirminterest | boolean | False |
|  | Created By | createdby | string | false |  | systemusers | createdby | string | 28e6efdc-0649-f011-877a-000d3a183b4b |
|  | Created On | createdon | string | false |  |  | createdon | string | 2025-06-15T06:56:58Z |
|  | Created By (Delegate) | createdonbehalfby | string | false |  | systemusers | createdonbehalfby | null | None |
|  | Current Situation | currentsituation | string | false |  |  | currentsituation | string | Not enough grinders to support machines. |
|  | Potential Customer | customerid | object | false |  |  | customerid | object | {"id": "b4cea450-cb0c-ea11-a813-000d3a1b1223", "type": "accounts"} |
|  |  | customerid.id | string | false |  | {'$var': 'customerid.type'} | customerid.id | string | b4cea450-cb0c-ea11-a813-000d3a1b1223 |
|  |  | customerid.type | string | false |  |  | customerid.type | string | accounts |
|  | Customer Need | customerneed | string | false |  |  | customerneed | string | Need a new grinder to support the new machines. |
|  | Customer Pain Points | customerpainpoints | string | false |  |  | customerpainpoints | null | None |
|  | Decision Maker? | decisionmaker | boolean | false |  |  | decisionmaker | boolean | True |
|  | Description | description | string | false |  |  | description | string | Supply coffee machines for their new Building |
|  | Develop Proposal | developproposal | boolean | false |  |  | developproposal | boolean | False |
|  | Opportunity Discount Amount | discountamount | number | false |  |  | discountamount | null | None |
|  | Opportunity Discount Amount (Base) | discountamount_base | number | false |  |  | discountamount_base | null | None |
|  | Opportunity Discount (%) | discountpercentage | number | false |  |  | discountpercentage | null | None |
|  | Email Address | emailaddress | string | false |  |  | emailaddress | string | heriberto@northwindtraders.com |
|  | Est. close date | estimatedclosedate | string | false |  |  | estimatedclosedate | string | 2025-06-20 |
|  | Est. revenue | estimatedvalue | number | false |  |  | estimatedvalue | integer | 24995 |
|  | Est. Revenue (Base) | estimatedvalue_base | number | false |  |  | estimatedvalue_base | integer | 24995 |
|  | Evaluate Fit | evaluatefit | boolean | false |  |  | evaluatefit | boolean | False |
|  | Exchange Rate | exchangerate | number | false |  |  | exchangerate | integer | 1 |
|  | File Debrief | filedebrief | boolean | false |  |  | filedebrief | boolean | False |
|  | Final Decision Date | finaldecisiondate | string | false |  |  | finaldecisiondate | null | None |
|  | Freight Amount | freightamount | number | false |  |  | freightamount | null | None |
|  | Freight Amount (Base) | freightamount_base | number | false |  |  | freightamount_base | null | None |
|  | Identify Competitors | identifycompetitors | boolean | false |  |  | identifycompetitors | boolean | True |
|  | Identify Customer Contacts | identifycustomercontacts | boolean | false |  |  | identifycustomercontacts | boolean | True |
|  | Identify Sales Team | identifypursuitteam | boolean | false |  |  | identifypursuitteam | boolean | False |
|  | Initial Communication | initialcommunication | string | false | `Contacted`, `Not Contacted` |  | initialcommunication | null | None |
|  | Revenue | isrevenuesystemcalculated | boolean | false |  |  | isrevenuesystemcalculated | boolean | True |
|  | Last On Hold Time | lastonholdtime | string | false |  |  | lastonholdtime | null | None |
|  | Modified By | modifiedby | string | false |  | systemusers | modifiedby | string | 28e6efdc-0649-f011-877a-000d3a183b4b |
|  | Modified On | modifiedon | string | false |  |  | modifiedon | string | 2025-06-15T06:59:52Z |
|  | Modified By (Delegate) | modifiedonbehalfby | string | false |  | systemusers | modifiedonbehalfby | null | None |
|  | Forecast category | msdyn_forecastcategory | string | false | `Pipeline`, `Best case`, `Committed`, `Omitted`, `Won`, `Lost` |  | msdyn_forecastcategory | integer | 100000001 |
|  | GDPR Optout | msdyn_gdproptout | boolean | false |  |  | msdyn_gdproptout | boolean | False |
|  | (Deprecated) Opportunity Grade | msdyn_opportunitygrade | string | false | `Grade A`, `Grade B`, `Grade C`, `Grade D` |  | msdyn_opportunitygrade | null | None |
|  | (Deprecated) Opportunity Score | msdyn_opportunityscore | number | false |  |  | msdyn_opportunityscore | null | None |
|  | (Deprecated) Opportunity Score Trend | msdyn_opportunityscoretrend | string | false | `Improving`, `Steady`, `Declining`, `Not enough info` |  | msdyn_opportunityscoretrend | null | None |
|  | (Deprecated) Score History | msdyn_scorehistory | string | false |  |  | msdyn_scorehistory | null | None |
|  | (Deprecated) Score Reasons | msdyn_scorereasons | string | false |  |  | msdyn_scorereasons | null | None |
|  | msdyn_similaropportunities | msdyn_similaropportunities | string | false |  |  | msdyn_similaropportunities | null | None |
|  | Topic | name | string | false |  |  | name | string | 5 Café BG-1 Pro Grinders for Northwind Traders |
|  | Need | need | string | false | `Must have`, `Should have`, `Good to have`, `No need` |  | need | null | None |
|  | On Hold Time (Minutes) | onholdtime | number | false |  |  | onholdtime | null | None |
|  | Opportunity Id | opportunityid | string | true |  |  | opportunityid | string | 3cbbd39d-d3f0-ea11-a815-000d3a33f3c3 |
|  | Rating | opportunityratingcode | string | false | `Hot`, `Warm`, `Cold` |  | opportunityratingcode | integer | 3 |
|  | Originating Lead | originatingleadid | string | false |  | leads | originatingleadid | null | None |
|  | Owner | ownerid | string | false |  | systemusers | ownerid | string | 28e6efdc-0649-f011-877a-000d3a183b4b |
|  | Account | parentaccountid | string | false |  | accounts | parentaccountid | string | b4cea450-cb0c-ea11-a813-000d3a1b1223 |
|  | Contact | parentcontactid | string | false |  | contacts | parentcontactid | string | cdcfa450-cb0c-ea11-a813-000d3a1b1223 |
|  | Present Final Proposal | presentfinalproposal | boolean | false |  |  | presentfinalproposal | boolean | False |
|  | Presented Proposal | presentproposal | boolean | false |  |  | presentproposal | boolean | False |
|  | Pricing Error  | pricingerrorcode | string | false | `None`, `Detail Error`, `Missing Price Level`, `Inactive Price Level`, `Missing Quantity`, `Missing Unit Price`, `Missing Product`, `Invalid Product`, `Missing Pricing Code`, `Invalid Pricing Code`, `Missing UOM`, `Product Not In Price Level`, `Missing Price Level Amount`, `Missing Price Level Percentage`, `Missing Price`, `Missing Current Cost`, `Missing Standard Cost`, `Invalid Price Level Amount`, `Invalid Price Level Percentage`, `Invalid Price`, `Invalid Current Cost`, `Invalid Standard Cost`, `Invalid Rounding Policy`, `Invalid Rounding Option`, `Invalid Rounding Amount`, `Price Calculation Error`, `Invalid Discount Type`, `Discount Type Invalid State`, `Invalid Discount`, `Invalid Quantity`, `Invalid Pricing Precision`, `Missing Product Default UOM`, `Missing Product UOM Schedule `, `Inactive Discount Type`, `Invalid Price Level Currency`, `Price Attribute Out Of Range`, `Base Currency Attribute Overflow`, `Base Currency Attribute Underflow`, `Transaction currency is not set for the product price list item` |  | pricingerrorcode | integer | 0 |
|  | Priority | prioritycode | string | false | `Default Value` |  | prioritycode | integer | 1 |
|  | Proposed Solution | proposedsolution | string | false |  |  | proposedsolution | string | 5 Café BG-1 Pro Grinders should meet the customers requirements. |
|  | Purchase Process | purchaseprocess | string | false | `Individual`, `Committee`, `Unknown` |  | purchaseprocess | integer | 2 |
|  | Purchase Timeframe | purchasetimeframe | string | false | `Immediate`, `This Quarter`, `Next Quarter`, `This Year`, `Unknown` |  | purchasetimeframe | integer | 4 |
|  | Decide Go/No-Go | pursuitdecision | boolean | false |  |  | pursuitdecision | boolean | False |
|  | Qualification Comments | qualificationcomments | string | false |  |  | qualificationcomments | null | None |
|  | Quote Comments | quotecomments | string | false |  |  | quotecomments | null | None |
|  | Feedback Resolved | resolvefeedback | boolean | false |  |  | resolvefeedback | boolean | False |
|  | Sales Stage | salesstage | string | false | `Qualify`, `Develop`, `Propose`, `Close` |  | salesstage | null | None |
|  | Process Code | salesstagecode | string | false | `Default Value` |  | salesstagecode | integer | 1 |
|  | Scheduled Follow up (Prospect) | schedulefollowup_prospect | string | false |  |  | schedulefollowup_prospect | null | None |
|  | Scheduled Follow up (Qualify) | schedulefollowup_qualify | string | false |  |  | schedulefollowup_qualify | null | None |
|  | Schedule Proposal Meeting | scheduleproposalmeeting | string | false |  |  | scheduleproposalmeeting | null | None |
|  | Send Thank You Note | sendthankyounote | boolean | false |  |  | sendthankyounote | boolean | False |
|  | Skip Price Calculation | skippricecalculation | string | false | `DoPriceCalcAlways`, `SkipPriceCalcOnRetrieve` |  | skippricecalculation | integer | 0 |
|  | Status Reason | statuscode | string | false | `In Progress`, `On Hold`, `Won`, `Canceled`, `Out-Sold` |  | statuscode | integer | 1 |
|  | Step | stepid | string | false |  |  | stepid | null | None |
|  | Pipeline Phase | stepname | string | false |  |  | stepname | string | 1-Qualify |
|  | Timeline | timeline | string | false | `Immediate`, `This Quarter`, `Next Quarter`, `This Year`, `Not known` |  | timeline | null | None |
|  | Total Amount | totalamount | number | false |  |  | totalamount | integer | 24995 |
|  | Total Amount (Base) | totalamount_base | number | false |  |  | totalamount_base | integer | 24995 |
|  | Total Pre-Freight Amount | totalamountlessfreight | number | false |  |  | totalamountlessfreight | integer | 24995 |
|  | Total Pre-Freight Amount (Base) | totalamountlessfreight_base | number | false |  |  | totalamountlessfreight_base | integer | 24995 |
|  | Total Discount Amount | totaldiscountamount | number | false |  |  | totaldiscountamount | integer | 0 |
|  | Total Discount Amount (Base) | totaldiscountamount_base | number | false |  |  | totaldiscountamount_base | integer | 0 |
|  | Total Detail Amount | totallineitemamount | number | false |  |  | totallineitemamount | integer | 24995 |
|  | Total Detail Amount (Base) | totallineitemamount_base | number | false |  |  | totallineitemamount_base | integer | 24995 |
|  | Total Line Item Discount Amount | totallineitemdiscountamount | number | false |  |  | totallineitemdiscountamount | integer | 0 |
|  | Total Line Item Discount Amount (Base) | totallineitemdiscountamount_base | number | false |  |  | totallineitemdiscountamount_base | integer | 0 |
|  | Total Tax | totaltax | number | false |  |  | totaltax | integer | 0 |
|  | Total Tax (Base) | totaltax_base | number | false |  |  | totaltax_base | integer | 0 |
| FindByID |  |  |  |  |  |  | @odata.context |  |  |
| FindByID |  |  |  |  |  |  | @odata.etag |  |  |
| FindByID |  |  |  |  |  |  | accountid | null | None |
| FindByID |  |  |  |  |  |  | captureproposalfeedback@OData.Community.Display.V1.FormattedValue |  |  |
| FindByID |  |  |  |  |  |  | closeprobability@OData.Community.Display.V1.FormattedValue |  |  |
| FindByID |  |  |  |  |  |  | completefinalproposal@OData.Community.Display.V1.FormattedValue |  |  |
| FindByID |  |  |  |  |  |  | completeinternalreview@OData.Community.Display.V1.FormattedValue |  |  |
| FindByID |  |  |  |  |  |  | confirminterest@OData.Community.Display.V1.FormattedValue |  |  |
| FindByID |  |  |  |  |  |  | contactid | null | None |
| FindByID |  |  |  |  |  |  | createdon@OData.Community.Display.V1.FormattedValue |  |  |
| FindByID |  |  |  |  |  |  | decisionmaker@OData.Community.Display.V1.FormattedValue |  |  |
| FindByID |  |  |  |  |  |  | developproposal@OData.Community.Display.V1.FormattedValue |  |  |
| FindByID |  |  |  |  |  |  | estimatedclosedate@OData.Community.Display.V1.FormattedValue |  |  |
| FindByID |  |  |  |  |  |  | estimatedvalue@OData.Community.Display.V1.FormattedValue |  |  |
| FindByID |  |  |  |  |  |  | estimatedvalue_base@OData.Community.Display.V1.FormattedValue |  |  |
| FindByID |  |  |  |  |  |  | evaluatefit@OData.Community.Display.V1.FormattedValue |  |  |
| FindByID |  |  |  |  |  |  | exchangerate@OData.Community.Display.V1.FormattedValue |  |  |
| FindByID |  |  |  |  |  |  | filedebrief@OData.Community.Display.V1.FormattedValue |  |  |
| FindByID |  |  |  |  |  |  | identifycompetitors@OData.Community.Display.V1.FormattedValue |  |  |
| FindByID |  |  |  |  |  |  | identifycustomercontacts@OData.Community.Display.V1.FormattedValue |  |  |
| FindByID |  |  |  |  |  |  | identifypursuitteam@OData.Community.Display.V1.FormattedValue |  |  |
| FindByID |  |  |  |  |  |  | importsequencenumber | null | None |
| FindByID |  |  |  |  |  |  | isrevenuesystemcalculated@OData.Community.Display.V1.FormattedValue |  |  |
| FindByID |  |  |  |  |  |  | modifiedon@OData.Community.Display.V1.FormattedValue |  |  |
| FindByID |  |  |  |  |  |  | msdyn | string | 022c6c4d-b649-f011-877a-000d3a183b4b |
| FindByID |  |  |  |  |  |  | msdyn_forecastcategory@OData.Community.Display.V1.FormattedValue |  |  |
| FindByID |  |  |  |  |  |  | msdyn_gdproptout@OData.Community.Display.V1.FormattedValue |  |  |
| FindByID |  |  |  |  |  |  | opportunityratingcode@OData.Community.Display.V1.FormattedValue |  |  |
| FindByID |  |  |  |  |  |  | overriddencreatedon | null | None |
| FindByID |  |  |  |  |  |  | owningbusinessunit | string | a585f7d6-0649-f011-877a-000d3a183b4b |
| FindByID |  |  |  |  |  |  | owningteam | null | None |
| FindByID |  |  |  |  |  |  | owninguser | string | 28e6efdc-0649-f011-877a-000d3a183b4b |
| FindByID |  |  |  |  |  |  | participatesinworkflow | boolean | False |
| FindByID |  |  |  |  |  |  | participatesinworkflow@OData.Community.Display.V1.FormattedValue |  |  |
| FindByID |  |  |  |  |  |  | presentfinalproposal@OData.Community.Display.V1.FormattedValue |  |  |
| FindByID |  |  |  |  |  |  | presentproposal@OData.Community.Display.V1.FormattedValue |  |  |
| FindByID |  |  |  |  |  |  | pricelevelid | string | 65029c08-f01f-eb11-a812-000d3a33e825 |
| FindByID |  |  |  |  |  |  | pricingerrorcode@OData.Community.Display.V1.FormattedValue |  |  |
| FindByID |  |  |  |  |  |  | prioritycode@OData.Community.Display.V1.FormattedValue |  |  |
| FindByID |  |  |  |  |  |  | processid | null | None |
| FindByID |  |  |  |  |  |  | purchaseprocess@OData.Community.Display.V1.FormattedValue |  |  |
| FindByID |  |  |  |  |  |  | purchasetimeframe@OData.Community.Display.V1.FormattedValue |  |  |
| FindByID |  |  |  |  |  |  | pursuitdecision@OData.Community.Display.V1.FormattedValue |  |  |
| FindByID |  |  |  |  |  |  | resolvefeedback@OData.Community.Display.V1.FormattedValue |  |  |
| FindByID |  |  |  |  |  |  | salesstagecode@OData.Community.Display.V1.FormattedValue |  |  |
| FindByID |  |  |  |  |  |  | sendthankyounote@OData.Community.Display.V1.FormattedValue |  |  |
| FindByID |  |  |  |  |  |  | skippricecalculation@OData.Community.Display.V1.FormattedValue |  |  |
| FindByID |  |  |  |  |  |  | slaid | null | None |
| FindByID |  |  |  |  |  |  | slainvokedid | null | None |
| FindByID |  |  |  |  |  |  | stageid | null | None |
| FindByID |  |  |  |  |  |  | statecode | integer | 0 |
| FindByID |  |  |  |  |  |  | statecode@OData.Community.Display.V1.FormattedValue |  |  |
| FindByID |  |  |  |  |  |  | statuscode@OData.Community.Display.V1.FormattedValue |  |  |
| FindByID |  |  |  |  |  |  | teamsfollowed | null | None |
| FindByID |  |  |  |  |  |  | timespentbymeonemailandmeetings | null | None |
| FindByID |  |  |  |  |  |  | timezoneruleversionnumber | integer | 4 |
| FindByID |  |  |  |  |  |  | timezoneruleversionnumber@OData.Community.Display.V1.FormattedValue |  |  |
| FindByID |  |  |  |  |  |  | totalamount@OData.Community.Display.V1.FormattedValue |  |  |
| FindByID |  |  |  |  |  |  | totalamount_base@OData.Community.Display.V1.FormattedValue |  |  |
| FindByID |  |  |  |  |  |  | totalamountlessfreight@OData.Community.Display.V1.FormattedValue |  |  |
| FindByID |  |  |  |  |  |  | totalamountlessfreight_base@OData.Community.Display.V1.FormattedValue |  |  |
| FindByID |  |  |  |  |  |  | totaldiscountamount@OData.Community.Display.V1.FormattedValue |  |  |
| FindByID |  |  |  |  |  |  | totaldiscountamount_base@OData.Community.Display.V1.FormattedValue |  |  |
| FindByID |  |  |  |  |  |  | totallineitemamount@OData.Community.Display.V1.FormattedValue |  |  |
| FindByID |  |  |  |  |  |  | totallineitemamount_base@OData.Community.Display.V1.FormattedValue |  |  |
| FindByID |  |  |  |  |  |  | totallineitemdiscountamount@OData.Community.Display.V1.FormattedValue |  |  |
| FindByID |  |  |  |  |  |  | totallineitemdiscountamount_base@OData.Community.Display.V1.FormattedValue |  |  |
| FindByID |  |  |  |  |  |  | totaltax@OData.Community.Display.V1.FormattedValue |  |  |
| FindByID |  |  |  |  |  |  | totaltax_base@OData.Community.Display.V1.FormattedValue |  |  |
| FindByID |  |  |  |  |  |  | transactioncurrencyid | string | a578dafc-aa49-f011-877a-000d3a183b4b |
| FindByID |  |  |  |  |  |  | traversedpath | null | None |
| FindByID |  |  |  |  |  |  | utcconversiontimezonecode | null | None |
| FindByID |  |  |  |  |  |  | versionnumber | integer | 4613694 |
| FindByID |  |  |  |  |  |  | versionnumber@OData.Community.Display.V1.FormattedValue |  |  |

## Accounts

| Diff | Entity Schema Title | Schema Field ID | Entity Schema Types | Readonly | Possible Values | Reference Collection | FindByID Field ID | Find By ID Types | Value |
|------|---------------------|-----------------|---------------------|----------|-----------------|----------------------|-------------------|------------------|-------|
|  | Category | accountcategorycode | string | false | `Preferred Customer`, `Standard` |  | accountcategorycode | null | None |
|  | Classification | accountclassificationcode | string | false | `Default Value` |  | accountclassificationcode | integer | 1 |
|  | Account ID | accountid | string | true |  |  | accountid | string | 83883308-7ad5-ea11-a813-000d3a33f3b4 |
|  | Account Number | accountnumber | string | false |  |  | accountnumber | null | None |
|  | Account Rating | accountratingcode | string | false | `Default Value` |  | accountratingcode | integer | 1 |
|  | Address 1: Address Type | address1_addresstypecode | string | false | `Bill To`, `Ship To`, `Primary`, `Other` |  | address1_addresstypecode | null | None |
|  | Address 1: City | address1_city | string | false |  |  | address1_city | string | Redmond |
|  | Address 1 | address1_composite | string | false |  |  | address1_composite | string | 2345 Birchwood Dr Redmond, Washington 98101 United States |
|  | Address 1: Country/Region | address1_country | string | false |  |  | address1_country | string | United States |
|  | Address 1: County | address1_county | string | false |  |  | address1_county | null | None |
|  | Address 1: Fax | address1_fax | string | false |  |  | address1_fax | null | None |
|  | Address 1: Freight Terms | address1_freighttermscode | string | false | `FOB`, `No Charge` |  | address1_freighttermscode | null | None |
|  | Address 1: Latitude | address1_latitude | number | false |  |  | address1_latitude | null | None |
|  | Address 1: Street 1 | address1_line1 | string | false |  |  | address1_line1 | string | 2345 Birchwood Dr |
|  | Address 1: Street 2 | address1_line2 | string | false |  |  | address1_line2 | null | None |
|  | Address 1: Street 3 | address1_line3 | string | false |  |  | address1_line3 | null | None |
|  | Address 1: Longitude | address1_longitude | number | false |  |  | address1_longitude | null | None |
|  | Address 1: Name | address1_name | string | false |  |  | address1_name | null | None |
|  | Address 1: ZIP/Postal Code | address1_postalcode | string | false |  |  | address1_postalcode | string | 98101 |
|  | Address 1: Post Office Box | address1_postofficebox | string | false |  |  | address1_postofficebox | null | None |
|  | Address 1: Primary Contact Name | address1_primarycontactname | string | false |  |  | address1_primarycontactname | null | None |
|  | Address 1: Shipping Method | address1_shippingmethodcode | string | false | `Airborne`, `DHL`, `FedEx`, `UPS`, `Postal Mail`, `Full Load`, `Will Call` |  | address1_shippingmethodcode | null | None |
|  | Address 1: State/Province | address1_stateorprovince | string | false |  |  | address1_stateorprovince | string | Washington |
|  | Address Phone | address1_telephone1 | string | false |  |  | address1_telephone1 | null | None |
|  | Address 1: Telephone 2 | address1_telephone2 | string | false |  |  | address1_telephone2 | null | None |
|  | Address 1: Telephone 3 | address1_telephone3 | string | false |  |  | address1_telephone3 | null | None |
|  | Address 1: UPS Zone | address1_upszone | string | false |  |  | address1_upszone | null | None |
|  | Address 1: UTC Offset | address1_utcoffset | number | false |  |  | address1_utcoffset | null | None |
|  | Address 2: Address Type | address2_addresstypecode | string | false | `Default Value` |  | address2_addresstypecode | integer | 1 |
|  | Address 2: City | address2_city | string | false |  |  | address2_city | null | None |
|  | Address 2 | address2_composite | string | false |  |  | address2_composite | null | None |
|  | Address 2: Country/Region | address2_country | string | false |  |  | address2_country | null | None |
|  | Address 2: County | address2_county | string | false |  |  | address2_county | null | None |
|  | Address 2: Fax | address2_fax | string | false |  |  | address2_fax | null | None |
|  | Address 2: Freight Terms | address2_freighttermscode | string | false | `Default Value` |  | address2_freighttermscode | integer | 1 |
|  | Address 2: Latitude | address2_latitude | number | false |  |  | address2_latitude | null | None |
|  | Address 2: Street 1 | address2_line1 | string | false |  |  | address2_line1 | null | None |
|  | Address 2: Street 2 | address2_line2 | string | false |  |  | address2_line2 | null | None |
|  | Address 2: Street 3 | address2_line3 | string | false |  |  | address2_line3 | null | None |
|  | Address 2: Longitude | address2_longitude | number | false |  |  | address2_longitude | null | None |
|  | Address 2: Name | address2_name | string | false |  |  | address2_name | null | None |
|  | Address 2: ZIP/Postal Code | address2_postalcode | string | false |  |  | address2_postalcode | null | None |
|  | Address 2: Post Office Box | address2_postofficebox | string | false |  |  | address2_postofficebox | null | None |
|  | Address 2: Primary Contact Name | address2_primarycontactname | string | false |  |  | address2_primarycontactname | null | None |
|  | Address 2: Shipping Method | address2_shippingmethodcode | string | false | `Default Value` |  | address2_shippingmethodcode | integer | 1 |
|  | Address 2: State/Province | address2_stateorprovince | string | false |  |  | address2_stateorprovince | null | None |
|  | Address 2: Telephone 1 | address2_telephone1 | string | false |  |  | address2_telephone1 | null | None |
|  | Address 2: Telephone 2 | address2_telephone2 | string | false |  |  | address2_telephone2 | null | None |
|  | Address 2: Telephone 3 | address2_telephone3 | string | false |  |  | address2_telephone3 | null | None |
|  | Address 2: UPS Zone | address2_upszone | string | false |  |  | address2_upszone | null | None |
|  | Address 2: UTC Offset | address2_utcoffset | number | false |  |  | address2_utcoffset | null | None |
|  | Created By (IP Address) | adx_createdbyipaddress | string | false |  |  | adx_createdbyipaddress | null | None |
|  | Created By (User Name) | adx_createdbyusername | string | false |  |  | adx_createdbyusername | null | None |
|  | Modified By (IP Address) | adx_modifiedbyipaddress | string | false |  |  | adx_modifiedbyipaddress | null | None |
|  | Modified By (User Name) | adx_modifiedbyusername | string | false |  |  | adx_modifiedbyusername | null | None |
|  | Aging 30 | aging30 | number | false |  |  | aging30 | null | None |
|  | Aging 30 (Base) | aging30_base | number | false |  |  | aging30_base | null | None |
|  | Aging 60 | aging60 | number | false |  |  | aging60 | null | None |
|  | Aging 60 (Base) | aging60_base | number | false |  |  | aging60_base | null | None |
|  | Aging 90 | aging90 | number | false |  |  | aging90 | null | None |
|  | Aging 90 (Base) | aging90_base | number | false |  |  | aging90_base | null | None |
|  | Business Type | businesstypecode | string | false | `Default Value` |  | businesstypecode | integer | 1 |
|  | Created By | createdby | string | false |  | systemusers | createdby | string | 28e6efdc-0649-f011-877a-000d3a183b4b |
|  | Created On | createdon | string | false |  |  | createdon | string | 2025-06-15T06:56:28Z |
|  | Created By (Delegate) | createdonbehalfby | string | false |  | systemusers | createdonbehalfby | null | None |
|  | Credit Limit | creditlimit | number | false |  |  | creditlimit | integer | 450000 |
|  | Credit Limit (Base) | creditlimit_base | number | false |  |  | creditlimit_base | integer | 450000 |
|  | Credit Hold | creditonhold | boolean | false |  |  | creditonhold | boolean | False |
|  | Customer Size | customersizecode | string | false | `Default Value` |  | customersizecode | integer | 1 |
|  | Relationship Type | customertypecode | string | false | `Competitor`, `Consultant`, `Customer`, `Investor`, `Partner`, `Influencer`, `Press`, `Prospect`, `Reseller`, `Supplier`, `Vendor`, `Other` |  | customertypecode | null | None |
|  | Description | description | string | false |  |  | description | string | A. Datum provides you with a wide selection of products both in our stores and online. |
|  | Do not allow Bulk Emails | donotbulkemail | boolean | false |  |  | donotbulkemail | boolean | False |
|  | Do not allow Bulk Mails | donotbulkpostalmail | boolean | false |  |  | donotbulkpostalmail | boolean | False |
|  | Do not allow Emails | donotemail | boolean | false |  |  | donotemail | boolean | False |
|  | Do not allow Faxes | donotfax | boolean | false |  |  | donotfax | boolean | False |
|  | Do not allow Phone Calls | donotphone | boolean | false |  |  | donotphone | boolean | False |
|  | Do not allow Mails | donotpostalmail | boolean | false |  |  | donotpostalmail | boolean | False |
|  | Send Marketing Materials | donotsendmm | boolean | false |  |  | donotsendmm | boolean | False |
|  | Email | emailaddress1 | string | false |  |  | emailaddress1 | null | None |
|  | Email Address 2 | emailaddress2 | string | false |  |  | emailaddress2 | null | None |
|  | Email Address 3 | emailaddress3 | string | false |  |  | emailaddress3 | null | None |
|  | Exchange Rate | exchangerate | number | false |  |  | exchangerate | integer | 1 |
|  | Fax | fax | string | false |  |  | fax | string | 425-555-0159 |
|  | Follow Email Activity | followemail | boolean | false |  |  | followemail | boolean | True |
|  | FTP Site | ftpsiteurl | string | false |  |  | ftpsiteurl | null | None |
|  | Industry | industrycode | string | false | `Accounting`, `Agriculture and Non-petrol Natural Resource Extraction`, `Broadcasting Printing and Publishing`, `Brokers`, `Building Supply Retail`, `Business Services`, `Consulting`, `Consumer Services`, `Design, Direction and Creative Management`, `Distributors, Dispatchers and Processors`, `Doctor's Offices and Clinics`, `Durable Manufacturing`, `Eating and Drinking Places`, `Entertainment Retail`, `Equipment Rental and Leasing`, `Financial`, `Food and Tobacco Processing`, `Inbound Capital Intensive Processing`, `Inbound Repair and Services`, `Insurance`, `Legal Services`, `Non-Durable Merchandise Retail`, `Outbound Consumer Service`, `Petrochemical Extraction and Distribution`, `Service Retail`, `SIG Affiliations`, `Social Services`, `Special Outbound Trade Contractors`, `Specialty Realty`, `Transportation`, `Utility Creation and Distribution`, `Vehicle Retail`, `Wholesale` |  | industrycode | null | None |
|  | Last On Hold Time | lastonholdtime | string | false |  |  | lastonholdtime | null | None |
|  | Last Date Included in Campaign | lastusedincampaign | string | false |  |  | lastusedincampaign | null | None |
|  | Market Capitalization | marketcap | number | false |  |  | marketcap | null | None |
|  | Market Capitalization (Base) | marketcap_base | number | false |  |  | marketcap_base | null | None |
|  | Marketing Only | marketingonly | boolean | false |  |  | marketingonly | boolean | False |
|  | Modified By | modifiedby | string | false |  | systemusers | modifiedby | string | 28e6efdc-0649-f011-877a-000d3a183b4b |
|  | Modified On | modifiedon | string | false |  |  | modifiedon | string | 2025-06-15T07:03:35Z |
|  | Modified By (Delegate) | modifiedonbehalfby | string | false |  | systemusers | modifiedonbehalfby | null | None |
|  | GDPR Optout | msdyn_gdproptout | boolean | false |  |  | msdyn_gdproptout | boolean | False |
|  | Primary Time Zone | msdyn_primarytimezone | number | false |  |  | msdyn_primarytimezone | null | None |
|  | Account Name | name | string | false |  |  | name | string | A. Datum Corporation |
|  | Number of Employees | numberofemployees | number | false |  |  | numberofemployees | integer | 2000 |
|  | On Hold Time (Minutes) | onholdtime | number | false |  |  | onholdtime | null | None |
|  | Open Deals | opendeals | number | false |  |  | opendeals | integer | 3 |
|  | Open Deals (Last Updated On) | opendeals_date | string | false |  |  | opendeals_date | string | 2025-06-18T17:20:17Z |
|  | Open Deals (State) | opendeals_state | number | false |  |  | opendeals_state | integer | 1 |
|  | Open Revenue | openrevenue | number | false |  |  | openrevenue | integer | 120491 |
|  | Open Revenue (Base) | openrevenue_base | number | false |  |  | openrevenue_base | integer | 120491 |
|  | Open Revenue (Last Updated On) | openrevenue_date | string | false |  |  | openrevenue_date | string | 2025-06-18T17:20:17Z |
|  | Open Revenue (State) | openrevenue_state | number | false |  |  | openrevenue_state | integer | 1 |
|  | Originating Lead | originatingleadid | string | false |  | leads | originatingleadid | null | None |
|  | Owner | ownerid | string | false |  | systemusers | ownerid | string | 28e6efdc-0649-f011-877a-000d3a183b4b |
|  | Ownership | ownershipcode | string | false | `Public`, `Private`, `Subsidiary`, `Other` |  | ownershipcode | integer | 1 |
|  | Parent Account | parentaccountid | string | false |  | accounts | parentaccountid | null | None |
|  | Payment Terms | paymenttermscode | string | false | `Net 30`, `2% 10, Net 30`, `Net 45`, `Net 60` |  | paymenttermscode | null | None |
|  | Preferred Day | preferredappointmentdaycode | string | false | `Sunday`, `Monday`, `Tuesday`, `Wednesday`, `Thursday`, `Friday`, `Saturday` |  | preferredappointmentdaycode | null | None |
|  | Preferred Time | preferredappointmenttimecode | string | false | `Morning`, `Afternoon`, `Evening` |  | preferredappointmenttimecode | null | None |
|  | Preferred Method of Contact | preferredcontactmethodcode | string | false | `Any`, `Email`, `Phone`, `Fax`, `Mail` |  | preferredcontactmethodcode | integer | 1 |
|  | Preferred User | preferredsystemuserid | string | false |  | systemusers | preferredsystemuserid | null | None |
|  | Primary Contact | primarycontactid | string | false |  | contacts | primarycontactid | string | 678c7b32-3f72-ea11-a811-000d3a1b1f2c |
|  | Primary Satori ID | primarysatoriid | string | false |  |  | primarysatoriid | null | None |
|  | Primary Twitter ID | primarytwitterid | string | false |  |  | primarytwitterid | null | None |
|  | Annual Revenue | revenue | number | false |  |  | revenue | integer | 35000000 |
|  | Annual Revenue (Base) | revenue_base | number | false |  |  | revenue_base | integer | 35000000 |
|  | Shares Outstanding | sharesoutstanding | number | false |  |  | sharesoutstanding | null | None |
|  | Shipping Method | shippingmethodcode | string | false | `Default Value` |  | shippingmethodcode | integer | 1 |
|  | SIC Code | sic | string | false |  |  | sic | string | 5063 |
|  | Status Reason | statuscode | string | false | `Active`, `Inactive` |  | statuscode | integer | 1 |
|  | Stock Exchange | stockexchange | string | false |  |  | stockexchange | null | None |
|  | Main Phone | telephone1 | string | false |  |  | telephone1 | string | 425-555-0158 |
|  | Other Phone | telephone2 | string | false |  |  | telephone2 | null | None |
|  | Telephone 3 | telephone3 | string | false |  |  | telephone3 | null | None |
|  | Territory Code | territorycode | string | false | `Default Value` |  | territorycode | integer | 1 |
|  | Ticker Symbol | tickersymbol | string | false |  |  | tickersymbol | null | None |
|  | Website | websiteurl | string | false |  |  | websiteurl | string | http://www.adatum.com/ |
|  | Yomi Account Name | yominame | string | false |  |  | yominame | null | None |
| Schema | Managing Partner | <span style='color:red'>***msa_managingpartnerid***</span> | string | false |  | accounts |  |  |  |
| FindByID |  |  |  |  |  |  | @odata.context |  |  |
| FindByID |  |  |  |  |  |  | @odata.etag |  |  |
| FindByID |  |  |  |  |  |  | accountclassificationcode@OData.Community.Display.V1.FormattedValue |  |  |
| FindByID |  |  |  |  |  |  | accountratingcode@OData.Community.Display.V1.FormattedValue |  |  |
| FindByID |  |  |  |  |  |  | address1_addressid | string | 08bc1732-aa9e-4512-80b9-66aaf9832e35 |
| FindByID |  |  |  |  |  |  | address2_addressid | string | 008a6017-1e7f-4e95-87e9-a9d9f613f978 |
| FindByID |  |  |  |  |  |  | address2_addresstypecode@OData.Community.Display.V1.FormattedValue |  |  |
| FindByID |  |  |  |  |  |  | address2_freighttermscode@OData.Community.Display.V1.FormattedValue |  |  |
| FindByID |  |  |  |  |  |  | address2_shippingmethodcode@OData.Community.Display.V1.FormattedValue |  |  |
| FindByID |  |  |  |  |  |  | businesstypecode@OData.Community.Display.V1.FormattedValue |  |  |
| FindByID |  |  |  |  |  |  | createdbyexternalparty | null | None |
| FindByID |  |  |  |  |  |  | createdon@OData.Community.Display.V1.FormattedValue |  |  |
| FindByID |  |  |  |  |  |  | creditlimit@OData.Community.Display.V1.FormattedValue |  |  |
| FindByID |  |  |  |  |  |  | creditlimit_base@OData.Community.Display.V1.FormattedValue |  |  |
| FindByID |  |  |  |  |  |  | creditonhold@OData.Community.Display.V1.FormattedValue |  |  |
| FindByID |  |  |  |  |  |  | customersizecode@OData.Community.Display.V1.FormattedValue |  |  |
| FindByID |  |  |  |  |  |  | defaultpricelevelid | null | None |
| FindByID |  |  |  |  |  |  | donotbulkemail@OData.Community.Display.V1.FormattedValue |  |  |
| FindByID |  |  |  |  |  |  | donotbulkpostalmail@OData.Community.Display.V1.FormattedValue |  |  |
| FindByID |  |  |  |  |  |  | donotemail@OData.Community.Display.V1.FormattedValue |  |  |
| FindByID |  |  |  |  |  |  | donotfax@OData.Community.Display.V1.FormattedValue |  |  |
| FindByID |  |  |  |  |  |  | donotphone@OData.Community.Display.V1.FormattedValue |  |  |
| FindByID |  |  |  |  |  |  | donotpostalmail@OData.Community.Display.V1.FormattedValue |  |  |
| FindByID |  |  |  |  |  |  | donotsendmm@OData.Community.Display.V1.FormattedValue |  |  |
| FindByID |  |  |  |  |  |  | entityimage | null | None |
| FindByID |  |  |  |  |  |  | entityimage_timestamp | null | None |
| FindByID |  |  |  |  |  |  | entityimage_url | null | None |
| FindByID |  |  |  |  |  |  | entityimageid | null | None |
| FindByID |  |  |  |  |  |  | exchangerate@OData.Community.Display.V1.FormattedValue |  |  |
| FindByID |  |  |  |  |  |  | followemail@OData.Community.Display.V1.FormattedValue |  |  |
| FindByID |  |  |  |  |  |  | importsequencenumber | null | None |
| FindByID |  |  |  |  |  |  | marketingonly@OData.Community.Display.V1.FormattedValue |  |  |
| FindByID |  |  |  |  |  |  | masterid | null | None |
| FindByID |  |  |  |  |  |  | merged | boolean | False |
| FindByID |  |  |  |  |  |  | merged@OData.Community.Display.V1.FormattedValue |  |  |
| FindByID |  |  |  |  |  |  | modifiedbyexternalparty | null | None |
| FindByID |  |  |  |  |  |  | modifiedon@OData.Community.Display.V1.FormattedValue |  |  |
| FindByID |  |  |  |  |  |  | msa | null | None |
| FindByID |  |  |  |  |  |  | msdyn | null | None |
| FindByID |  |  |  |  |  |  | msdyn_gdproptout@OData.Community.Display.V1.FormattedValue |  |  |
| FindByID |  |  |  |  |  |  | numberofemployees@OData.Community.Display.V1.FormattedValue |  |  |
| FindByID |  |  |  |  |  |  | opendeals@OData.Community.Display.V1.FormattedValue |  |  |
| FindByID |  |  |  |  |  |  | opendeals_date@OData.Community.Display.V1.FormattedValue |  |  |
| FindByID |  |  |  |  |  |  | opendeals_state@OData.Community.Display.V1.FormattedValue |  |  |
| FindByID |  |  |  |  |  |  | openrevenue@OData.Community.Display.V1.FormattedValue |  |  |
| FindByID |  |  |  |  |  |  | openrevenue_base@OData.Community.Display.V1.FormattedValue |  |  |
| FindByID |  |  |  |  |  |  | openrevenue_date@OData.Community.Display.V1.FormattedValue |  |  |
| FindByID |  |  |  |  |  |  | openrevenue_state@OData.Community.Display.V1.FormattedValue |  |  |
| FindByID |  |  |  |  |  |  | overriddencreatedon | null | None |
| FindByID |  |  |  |  |  |  | ownershipcode@OData.Community.Display.V1.FormattedValue |  |  |
| FindByID |  |  |  |  |  |  | owningbusinessunit | string | a585f7d6-0649-f011-877a-000d3a183b4b |
| FindByID |  |  |  |  |  |  | owningteam | null | None |
| FindByID |  |  |  |  |  |  | owninguser | string | 28e6efdc-0649-f011-877a-000d3a183b4b |
| FindByID |  |  |  |  |  |  | participatesinworkflow | boolean | False |
| FindByID |  |  |  |  |  |  | participatesinworkflow@OData.Community.Display.V1.FormattedValue |  |  |
| FindByID |  |  |  |  |  |  | preferredcontactmethodcode@OData.Community.Display.V1.FormattedValue |  |  |
| FindByID |  |  |  |  |  |  | preferredequipmentid | null | None |
| FindByID |  |  |  |  |  |  | preferredserviceid | null | None |
| FindByID |  |  |  |  |  |  | processid | null | None |
| FindByID |  |  |  |  |  |  | revenue@OData.Community.Display.V1.FormattedValue |  |  |
| FindByID |  |  |  |  |  |  | revenue_base@OData.Community.Display.V1.FormattedValue |  |  |
| FindByID |  |  |  |  |  |  | shippingmethodcode@OData.Community.Display.V1.FormattedValue |  |  |
| FindByID |  |  |  |  |  |  | slaid | null | None |
| FindByID |  |  |  |  |  |  | slainvokedid | null | None |
| FindByID |  |  |  |  |  |  | stageid | null | None |
| FindByID |  |  |  |  |  |  | statecode | integer | 0 |
| FindByID |  |  |  |  |  |  | statecode@OData.Community.Display.V1.FormattedValue |  |  |
| FindByID |  |  |  |  |  |  | statuscode@OData.Community.Display.V1.FormattedValue |  |  |
| FindByID |  |  |  |  |  |  | teamsfollowed | null | None |
| FindByID |  |  |  |  |  |  | territorycode@OData.Community.Display.V1.FormattedValue |  |  |
| FindByID |  |  |  |  |  |  | territoryid | null | None |
| FindByID |  |  |  |  |  |  | timespentbymeonemailandmeetings | null | None |
| FindByID |  |  |  |  |  |  | timezoneruleversionnumber | null | None |
| FindByID |  |  |  |  |  |  | transactioncurrencyid | string | a578dafc-aa49-f011-877a-000d3a183b4b |
| FindByID |  |  |  |  |  |  | traversedpath | null | None |
| FindByID |  |  |  |  |  |  | utcconversiontimezonecode | null | None |
| FindByID |  |  |  |  |  |  | versionnumber | integer | 4619193 |
| FindByID |  |  |  |  |  |  | versionnumber@OData.Community.Display.V1.FormattedValue |  |  |

## Contacts

| Diff | Entity Schema Title | Schema Field ID | Entity Schema Types | Readonly | Possible Values | Reference Collection | FindByID Field ID | Find By ID Types | Value |
|------|---------------------|-----------------|---------------------|----------|-----------------|----------------------|-------------------|------------------|-------|
|  | Role | accountrolecode | string | false | `Decision Maker`, `Employee`, `Influencer` |  | accountrolecode | null | None |
|  | Address 1: Address Type | address1_addresstypecode | string | false | `Bill To`, `Ship To`, `Primary`, `Other` |  | address1_addresstypecode | null | None |
|  | Address 1: City | address1_city | string | false |  |  | address1_city | string | San Francisco |
|  | Address 1 | address1_composite | string | false |  |  | address1_composite | string | 789 3rd St San Francisco, California 94158 United States |
|  | Address 1: Country/Region | address1_country | string | false |  |  | address1_country | string | United States |
|  | Address 1: County | address1_county | string | false |  |  | address1_county | null | None |
|  | Address 1: Fax | address1_fax | string | false |  |  | address1_fax | null | None |
|  | Address 1: Freight Terms | address1_freighttermscode | string | false | `FOB`, `No Charge` |  | address1_freighttermscode | null | None |
|  | Address 1: Latitude | address1_latitude | number | false |  |  | address1_latitude | null | None |
|  | Address 1: Street 1 | address1_line1 | string | false |  |  | address1_line1 | string | 789 3rd St |
|  | Address 1: Street 2 | address1_line2 | string | false |  |  | address1_line2 | null | None |
|  | Address 1: Street 3 | address1_line3 | string | false |  |  | address1_line3 | null | None |
|  | Address 1: Longitude | address1_longitude | number | false |  |  | address1_longitude | null | None |
|  | Address 1: Name | address1_name | string | false |  |  | address1_name | null | None |
|  | Address 1: ZIP/Postal Code | address1_postalcode | string | false |  |  | address1_postalcode | string | 94158 |
|  | Address 1: Post Office Box | address1_postofficebox | string | false |  |  | address1_postofficebox | null | None |
|  | Address 1: Primary Contact Name | address1_primarycontactname | string | false |  |  | address1_primarycontactname | null | None |
|  | Address 1: Shipping Method | address1_shippingmethodcode | string | false | `Airborne`, `DHL`, `FedEx`, `UPS`, `Postal Mail`, `Full Load`, `Will Call` |  | address1_shippingmethodcode | null | None |
|  | Address 1: State/Province | address1_stateorprovince | string | false |  |  | address1_stateorprovince | string | California |
|  | Address 1: Phone | address1_telephone1 | string | false |  |  | address1_telephone1 | null | None |
|  | Address 1: Telephone 2 | address1_telephone2 | string | false |  |  | address1_telephone2 | null | None |
|  | Address 1: Telephone 3 | address1_telephone3 | string | false |  |  | address1_telephone3 | null | None |
|  | Address 1: UPS Zone | address1_upszone | string | false |  |  | address1_upszone | null | None |
|  | Address 1: UTC Offset | address1_utcoffset | number | false |  |  | address1_utcoffset | null | None |
|  | Address 2: Address Type | address2_addresstypecode | string | false | `Default Value` |  | address2_addresstypecode | integer | 1 |
|  | Address 2: City | address2_city | string | false |  |  | address2_city | null | None |
|  | Address 2 | address2_composite | string | false |  |  | address2_composite | null | None |
|  | Address 2: Country/Region | address2_country | string | false |  |  | address2_country | null | None |
|  | Address 2: County | address2_county | string | false |  |  | address2_county | null | None |
|  | Address 2: Fax | address2_fax | string | false |  |  | address2_fax | null | None |
|  | Address 2: Freight Terms | address2_freighttermscode | string | false | `Default Value` |  | address2_freighttermscode | integer | 1 |
|  | Address 2: Latitude | address2_latitude | number | false |  |  | address2_latitude | null | None |
|  | Address 2: Street 1 | address2_line1 | string | false |  |  | address2_line1 | null | None |
|  | Address 2: Street 2 | address2_line2 | string | false |  |  | address2_line2 | null | None |
|  | Address 2: Street 3 | address2_line3 | string | false |  |  | address2_line3 | null | None |
|  | Address 2: Longitude | address2_longitude | number | false |  |  | address2_longitude | null | None |
|  | Address 2: Name | address2_name | string | false |  |  | address2_name | null | None |
|  | Address 2: ZIP/Postal Code | address2_postalcode | string | false |  |  | address2_postalcode | null | None |
|  | Address 2: Post Office Box | address2_postofficebox | string | false |  |  | address2_postofficebox | null | None |
|  | Address 2: Primary Contact Name | address2_primarycontactname | string | false |  |  | address2_primarycontactname | null | None |
|  | Address 2: Shipping Method | address2_shippingmethodcode | string | false | `Default Value` |  | address2_shippingmethodcode | integer | 1 |
|  | Address 2: State/Province | address2_stateorprovince | string | false |  |  | address2_stateorprovince | null | None |
|  | Address 2: Telephone 1 | address2_telephone1 | string | false |  |  | address2_telephone1 | null | None |
|  | Address 2: Telephone 2 | address2_telephone2 | string | false |  |  | address2_telephone2 | null | None |
|  | Address 2: Telephone 3 | address2_telephone3 | string | false |  |  | address2_telephone3 | null | None |
|  | Address 2: UPS Zone | address2_upszone | string | false |  |  | address2_upszone | null | None |
|  | Address 2: UTC Offset | address2_utcoffset | number | false |  |  | address2_utcoffset | null | None |
|  | Address 3: Address Type | address3_addresstypecode | string | false | `Default Value` |  | address3_addresstypecode | null | None |
|  | Address 3: City | address3_city | string | false |  |  | address3_city | null | None |
|  | Address 3 | address3_composite | string | false |  |  | address3_composite | null | None |
|  | Address3: Country/Region | address3_country | string | false |  |  | address3_country | null | None |
|  | Address 3: County | address3_county | string | false |  |  | address3_county | null | None |
|  | Address 3: Fax | address3_fax | string | false |  |  | address3_fax | null | None |
|  | Address 3: Freight Terms | address3_freighttermscode | string | false | `Default Value` |  | address3_freighttermscode | null | None |
|  | Address 3: Latitude | address3_latitude | number | false |  |  | address3_latitude | null | None |
|  | Address3: Street 1 | address3_line1 | string | false |  |  | address3_line1 | null | None |
|  | Address3: Street 2 | address3_line2 | string | false |  |  | address3_line2 | null | None |
|  | Address3: Street 3 | address3_line3 | string | false |  |  | address3_line3 | null | None |
|  | Address 3: Longitude | address3_longitude | number | false |  |  | address3_longitude | null | None |
|  | Address 3: Name | address3_name | string | false |  |  | address3_name | null | None |
|  | Address3: ZIP/Postal Code | address3_postalcode | string | false |  |  | address3_postalcode | null | None |
|  | Address 3: Post Office Box | address3_postofficebox | string | false |  |  | address3_postofficebox | null | None |
|  | Address 3: Primary Contact Name | address3_primarycontactname | string | false |  |  | address3_primarycontactname | null | None |
|  | Address 3: Shipping Method | address3_shippingmethodcode | string | false | `Default Value` |  | address3_shippingmethodcode | null | None |
|  | Address3: State/Province | address3_stateorprovince | string | false |  |  | address3_stateorprovince | null | None |
|  | Address 3: Telephone1 | address3_telephone1 | string | false |  |  | address3_telephone1 | null | None |
|  | Address 3: Telephone2 | address3_telephone2 | string | false |  |  | address3_telephone2 | null | None |
|  | Address 3: Telephone3 | address3_telephone3 | string | false |  |  | address3_telephone3 | null | None |
|  | Address 3: UPS Zone | address3_upszone | string | false |  |  | address3_upszone | null | None |
|  | Address 3: UTC Offset | address3_utcoffset | number | false |  |  | address3_utcoffset | null | None |
|  | Confirm Remove Password | adx_confirmremovepassword | boolean | false |  |  | adx_confirmremovepassword | boolean | False |
|  | Created By IP Address | adx_createdbyipaddress | string | false |  |  | adx_createdbyipaddress | null | None |
|  | Created By Username | adx_createdbyusername | string | false |  |  | adx_createdbyusername | null | None |
|  | Access Failed Count | adx_identity_accessfailedcount | number | false |  |  | adx_identity_accessfailedcount | null | None |
|  | Email Confirmed | adx_identity_emailaddress1confirmed | boolean | false |  |  | adx_identity_emailaddress1confirmed | boolean | False |
|  | Last Successful Login | adx_identity_lastsuccessfullogin | string | false |  |  | adx_identity_lastsuccessfullogin | null | None |
|  | Local Login Disabled | adx_identity_locallogindisabled | boolean | false |  |  | adx_identity_locallogindisabled | boolean | False |
|  | Lockout Enabled | adx_identity_lockoutenabled | boolean | false |  |  | adx_identity_lockoutenabled | boolean | False |
|  | Lockout End Date | adx_identity_lockoutenddate | string | false |  |  | adx_identity_lockoutenddate | null | None |
|  | Login Enabled | adx_identity_logonenabled | boolean | false |  |  | adx_identity_logonenabled | boolean | False |
|  | Mobile Phone Confirmed | adx_identity_mobilephoneconfirmed | boolean | false |  |  | adx_identity_mobilephoneconfirmed | boolean | False |
|  | New Password Input | adx_identity_newpassword | string | false |  |  | adx_identity_newpassword | null | None |
|  | Password Hash | adx_identity_passwordhash | string | false |  |  | adx_identity_passwordhash | null | None |
|  | Security Stamp | adx_identity_securitystamp | string | false |  |  | adx_identity_securitystamp | null | None |
|  | Two Factor Enabled | adx_identity_twofactorenabled | boolean | false |  |  | adx_identity_twofactorenabled | boolean | False |
|  | User Name | adx_identity_username | string | false |  |  | adx_identity_username | null | None |
|  | Modified By IP Address | adx_modifiedbyipaddress | string | false |  |  | adx_modifiedbyipaddress | null | None |
|  | Modified By Username | adx_modifiedbyusername | string | false |  |  | adx_modifiedbyusername | null | None |
|  | Organization Name | adx_organizationname | string | false |  |  | adx_organizationname | null | None |
|  | Preferred LCID (Deprecated) | adx_preferredlcid | number | false |  |  | adx_preferredlcid | null | None |
|  | Profile Alert | adx_profilealert | boolean | false |  |  | adx_profilealert | boolean | False |
|  | Profile Alert Date | adx_profilealertdate | string | false |  |  | adx_profilealertdate | null | None |
|  | Profile Alert Instructions | adx_profilealertinstructions | string | false |  |  | adx_profilealertinstructions | null | None |
|  | Profile Is Anonymous | adx_profileisanonymous | boolean | false |  |  | adx_profileisanonymous | boolean | False |
|  | Profile Last Activity | adx_profilelastactivity | string | false |  |  | adx_profilelastactivity | null | None |
|  | Profile Modified On | adx_profilemodifiedon | string | false |  |  | adx_profilemodifiedon | null | None |
|  | Public Profile Copy | adx_publicprofilecopy | string | false |  |  | adx_publicprofilecopy | null | None |
|  | Time Zone | adx_timezone | number | false |  |  | adx_timezone | null | None |
|  | Aging 30 | aging30 | number | false |  |  | aging30 | null | None |
|  | Aging 30 (Base) | aging30_base | number | false |  |  | aging30_base | null | None |
|  | Aging 60 | aging60 | number | false |  |  | aging60 | null | None |
|  | Aging 60 (Base) | aging60_base | number | false |  |  | aging60_base | null | None |
|  | Aging 90 | aging90 | number | false |  |  | aging90 | null | None |
|  | Aging 90 (Base) | aging90_base | number | false |  |  | aging90_base | null | None |
|  | Anniversary | anniversary | string | false |  |  | anniversary | null | None |
|  | Annual Income | annualincome | number | false |  |  | annualincome | null | None |
|  | Annual Income (Base) | annualincome_base | number | false |  |  | annualincome_base | null | None |
|  | Assistant | assistantname | string | false |  |  | assistantname | null | None |
|  | Assistant Phone | assistantphone | string | false |  |  | assistantphone | null | None |
|  | Birthday | birthdate | string | false |  |  | birthdate | string | 1985-02-26 |
|  | Business Phone 2 | business2 | string | false |  |  | business2 | null | None |
|  | Business Card | businesscard | string | false |  |  | businesscard | null | None |
|  | BusinessCardAttributes | businesscardattributes | string | false |  |  | businesscardattributes | null | None |
|  | Callback Number | callback | string | false |  |  | callback | null | None |
|  | Children's Names | childrensnames | string | false |  |  | childrensnames | null | None |
|  | Company Phone | company | string | false |  |  | company | null | None |
|  | Contact Id | contactid | string | true |  |  | contactid | string | 80ac35a0-01af-ea11-a812-000d3a8b3ec6 |
|  | Created By | createdby | string | false |  | systemusers | createdby | string | 28e6efdc-0649-f011-877a-000d3a183b4b |
|  | Created On | createdon | string | false |  |  | createdon | string | 2025-06-15T06:56:31Z |
|  | Created By (Delegate) | createdonbehalfby | string | false |  | systemusers | createdonbehalfby | null | None |
|  | Credit Limit | creditlimit | number | false |  |  | creditlimit | integer | 10000 |
|  | Credit Limit (Base) | creditlimit_base | number | false |  |  | creditlimit_base | integer | 10000 |
|  | Credit Hold | creditonhold | boolean | false |  |  | creditonhold | boolean | False |
|  | Customer Size | customersizecode | string | false | `Default Value` |  | customersizecode | integer | 1 |
|  | Relationship Type | customertypecode | string | false | `Default Value` |  | customertypecode | integer | 1 |
|  | Department | department | string | false |  |  | department | null | None |
|  | Description | description | string | false |  |  | description | null | None |
|  | Do not allow Bulk Emails | donotbulkemail | boolean | false |  |  | donotbulkemail | boolean | False |
|  | Do not allow Bulk Mails | donotbulkpostalmail | boolean | false |  |  | donotbulkpostalmail | boolean | False |
|  | Do not allow Emails | donotemail | boolean | false |  |  | donotemail | boolean | False |
|  | Do not allow Faxes | donotfax | boolean | false |  |  | donotfax | boolean | False |
|  | Do not allow Phone Calls | donotphone | boolean | false |  |  | donotphone | boolean | False |
|  | Do not allow Mails | donotpostalmail | boolean | false |  |  | donotpostalmail | boolean | False |
|  | Send Marketing Materials | donotsendmm | boolean | false |  |  | donotsendmm | boolean | False |
|  | Education | educationcode | string | false | `Default Value` |  | educationcode | integer | 1 |
|  | Email | emailaddress1 | string | false |  |  | emailaddress1 | string | alex@treyresearch.net |
|  | Email Address 2 | emailaddress2 | string | false |  |  | emailaddress2 | null | None |
|  | Email Address 3 | emailaddress3 | string | false |  |  | emailaddress3 | null | None |
|  | Employee | employeeid | string | false |  |  | employeeid | null | None |
|  | Exchange Rate | exchangerate | number | false |  |  | exchangerate | integer | 1 |
|  | Marital Status | familystatuscode | string | false | `Single`, `Married`, `Divorced`, `Widowed` |  | familystatuscode | integer | 1 |
|  | Fax | fax | string | false |  |  | fax | string | 619-555-0128 |
|  | First Name | firstname | string | false |  |  | firstname | string | Alex |
|  | Follow Email Activity | followemail | boolean | false |  |  | followemail | boolean | True |
|  | FTP Site | ftpsiteurl | string | false |  |  | ftpsiteurl | null | None |
|  | Full Name | fullname | string | false |  |  | fullname | string | Alex Baker |
|  | Gender | gendercode | string | false | `Male`, `Female` |  | gendercode | integer | 2 |
|  | Government | governmentid | string | false |  |  | governmentid | null | None |
|  | Has Children | haschildrencode | string | false | `Default Value` |  | haschildrencode | integer | 1 |
|  | Home Phone 2 | home2 | string | false |  |  | home2 | null | None |
|  | Back Office Customer | isbackofficecustomer | boolean | false |  |  | isbackofficecustomer | boolean | False |
|  | Job Title | jobtitle | string | false |  |  | jobtitle | string | Cafeteria Manager |
|  | Last Name | lastname | string | false |  |  | lastname | string | Baker |
|  | Last On Hold Time | lastonholdtime | string | false |  |  | lastonholdtime | null | None |
|  | Last Date Included in Campaign | lastusedincampaign | string | false |  |  | lastusedincampaign | null | None |
|  | Lead Source | leadsourcecode | string | false | `Default Value` |  | leadsourcecode | integer | 1 |
|  | Manager | managername | string | false |  |  | managername | null | None |
|  | Manager Phone | managerphone | string | false |  |  | managerphone | null | None |
|  | Marketing Only | marketingonly | boolean | false |  |  | marketingonly | boolean | False |
|  | Middle Name | middlename | string | false |  |  | middlename | null | None |
|  | Mobile Phone | mobilephone | string | false |  |  | mobilephone | string | 619-555-0129 |
|  | Modified By | modifiedby | string | false |  | systemusers | modifiedby | string | 28e6efdc-0649-f011-877a-000d3a183b4b |
|  | Modified On | modifiedon | string | false |  |  | modifiedon | string | 2025-06-15T06:56:31Z |
|  | Modified By (Delegate) | modifiedonbehalfby | string | false |  | systemusers | modifiedonbehalfby | null | None |
|  | Decision influence labels | msdyn_decisioninfluencetag | string | false | `Decision maker`, `Influencer`, `Blocker`, `Unknown` |  | msdyn_decisioninfluencetag | null | None |
|  | Disable Web Tracking | msdyn_disablewebtracking | boolean | false |  |  | msdyn_disablewebtracking | boolean | False |
|  | GDPR Optout | msdyn_gdproptout | boolean | false |  |  | msdyn_gdproptout | boolean | False |
|  | Is Assistant | msdyn_isassistantinorgchart | boolean | false |  |  | msdyn_isassistantinorgchart | boolean | False |
|  | Is Minor | msdyn_isminor | boolean | false |  |  | msdyn_isminor | boolean | False |
|  | Is Minor with Parental Consent | msdyn_isminorwithparentalconsent | boolean | false |  |  | msdyn_isminorwithparentalconsent | boolean | False |
|  | Not at Company Flag | msdyn_orgchangestatus | string | false | `No Feedback`, `Not at Company`, `Ignore` |  | msdyn_orgchangestatus | integer | 0 |
|  | Portal Terms Agreement Date | msdyn_portaltermsagreementdate | string | false |  |  | msdyn_portaltermsagreementdate | null | None |
|  | Primary Time Zone | msdyn_primarytimezone | number | false |  |  | msdyn_primarytimezone | null | None |
|  | Preferred Language | mspp_userpreferredlcid | string | false | `Arabic`, `Basque - Basque`, `Bulgarian - Bulgaria`, `Catalan - Catalan`, `Chinese - China`, `Chinese - Hong Kong SAR`, `Chinese - Traditional`, `Croatian - Croatia`, `Czech - Czech Republic`, `Danish - Denmark`, `Dutch - Netherlands`, `English`, `Estonian - Estonia`, `Finnish - Finland`, `French - France`, `Galician - Spain`, `German - Germany`, `Greek - Greece`, `Hebrew`, `Hindi - India`, `Hungarian - Hungary`, `Indonesian - Indonesia`, `Italian - Italy`, `Japanese - Japan`, `Kazakh - Kazakhstan`, `Korean - Korea`, `Latvian - Latvia`, `Lithuanian - Lithuania`, `Malay - Malaysia`, `Norwegian (Bokmål) - Norway`, `Polish - Poland`, `Portuguese - Brazil`, `Portuguese - Portugal`, `Romanian - Romania`, `Russian - Russia`, `Serbian (Cyrillic) - Serbia`, `Serbian (Latin) - Serbia`, `Slovak - Slovakia`, `Slovenian - Slovenia`, `Spanish (Traditional Sort) - Spain`, `Swedish - Sweden`, `Thai - Thailand`, `Turkish - Türkiye`, `Ukrainian - Ukraine`, `Vietnamese - Vietnam` |  | mspp_userpreferredlcid | null | None |
|  | Nickname | nickname | string | false |  |  | nickname | null | None |
|  | No. of Children | numberofchildren | number | false |  |  | numberofchildren | null | None |
|  | On Hold Time (Minutes) | onholdtime | number | false |  |  | onholdtime | null | None |
|  | Originating Lead | originatingleadid | string | false |  | leads | originatingleadid | null | None |
|  | Owner | ownerid | string | false |  | systemusers | ownerid | string | 28e6efdc-0649-f011-877a-000d3a183b4b |
|  | Pager | pager | string | false |  |  | pager | null | None |
|  | Company Name | parentcustomerid | object | false |  |  | parentcustomerid | object | {"id": "a4cea450-cb0c-ea11-a813-000d3a1b1223", "type": "accounts"} |
|  |  | parentcustomerid.id | string | false |  | {'$var': 'parentcustomerid.type'} | parentcustomerid.id | string | a4cea450-cb0c-ea11-a813-000d3a1b1223 |
|  |  | parentcustomerid.type | string | false |  |  | parentcustomerid.type | string | accounts |
|  | Payment Terms | paymenttermscode | string | false | `Net 30`, `2% 10, Net 30`, `Net 45`, `Net 60` |  | paymenttermscode | null | None |
|  | Preferred Day | preferredappointmentdaycode | string | false | `Sunday`, `Monday`, `Tuesday`, `Wednesday`, `Thursday`, `Friday`, `Saturday` |  | preferredappointmentdaycode | null | None |
|  | Preferred Time | preferredappointmenttimecode | string | false | `Morning`, `Afternoon`, `Evening` |  | preferredappointmenttimecode | integer | 1 |
|  | Preferred Method of Contact | preferredcontactmethodcode | string | false | `Any`, `Email`, `Phone`, `Fax`, `Mail` |  | preferredcontactmethodcode | integer | 1 |
|  | Preferred User | preferredsystemuserid | string | false |  | systemusers | preferredsystemuserid | null | None |
|  | Salutation | salutation | string | false |  |  | salutation | null | None |
|  | Shipping Method | shippingmethodcode | string | false | `Default Value` |  | shippingmethodcode | integer | 1 |
|  | Spouse/Partner Name | spousesname | string | false |  |  | spousesname | null | None |
|  | Status Reason | statuscode | string | false | `Active`, `Inactive` |  | statuscode | integer | 1 |
|  | Suffix | suffix | string | false |  |  | suffix | null | None |
|  | Business Phone | telephone1 | string | false |  |  | telephone1 | string | 619-555-0127 |
|  | Home Phone | telephone2 | string | false |  |  | telephone2 | null | None |
|  | Telephone 3 | telephone3 | string | false |  |  | telephone3 | null | None |
|  | Territory | territorycode | string | false | `Default Value` |  | territorycode | integer | 1 |
|  | Website | websiteurl | string | false |  |  | websiteurl | null | None |
|  | Yomi First Name | yomifirstname | string | false |  |  | yomifirstname | null | None |
|  | Yomi Full Name | yomifullname | string | false |  |  | yomifullname | string | Alex Baker |
|  | Yomi Last Name | yomilastname | string | false |  |  | yomilastname | null | None |
|  | Yomi Middle Name | yomimiddlename | string | false |  |  | yomimiddlename | null | None |
| Schema | Managing Partner | <span style='color:red'>***msa_managingpartnerid***</span> | string | false |  | accounts |  |  |  |
| FindByID |  |  |  |  |  |  | @odata.context |  |  |
| FindByID |  |  |  |  |  |  | @odata.etag |  |  |
| FindByID |  |  |  |  |  |  | accountid | null | None |
| FindByID |  |  |  |  |  |  | address1_addressid | string | 3dbcb10d-053e-4b0c-9c0a-893a07f90536 |
| FindByID |  |  |  |  |  |  | address2_addressid | string | 0734ae14-963c-4385-bb10-27cd36160f93 |
| FindByID |  |  |  |  |  |  | address2_addresstypecode@OData.Community.Display.V1.FormattedValue |  |  |
| FindByID |  |  |  |  |  |  | address2_freighttermscode@OData.Community.Display.V1.FormattedValue |  |  |
| FindByID |  |  |  |  |  |  | address2_shippingmethodcode@OData.Community.Display.V1.FormattedValue |  |  |
| FindByID |  |  |  |  |  |  | address3_addressid | string | be394b6a-db7d-469d-839a-2a12fdfb665f |
| FindByID |  |  |  |  |  |  | adx_confirmremovepassword@OData.Community.Display.V1.FormattedValue |  |  |
| FindByID |  |  |  |  |  |  | adx_identity_emailaddress1confirmed@OData.Community.Display.V1.FormattedValue |  |  |
| FindByID |  |  |  |  |  |  | adx_identity_locallogindisabled@OData.Community.Display.V1.FormattedValue |  |  |
| FindByID |  |  |  |  |  |  | adx_identity_lockoutenabled@OData.Community.Display.V1.FormattedValue |  |  |
| FindByID |  |  |  |  |  |  | adx_identity_logonenabled@OData.Community.Display.V1.FormattedValue |  |  |
| FindByID |  |  |  |  |  |  | adx_identity_mobilephoneconfirmed@OData.Community.Display.V1.FormattedValue |  |  |
| FindByID |  |  |  |  |  |  | adx_identity_twofactorenabled@OData.Community.Display.V1.FormattedValue |  |  |
| FindByID |  |  |  |  |  |  | adx_profilealert@OData.Community.Display.V1.FormattedValue |  |  |
| FindByID |  |  |  |  |  |  | adx_profileisanonymous@OData.Community.Display.V1.FormattedValue |  |  |
| FindByID |  |  |  |  |  |  | birthdate@OData.Community.Display.V1.FormattedValue |  |  |
| FindByID |  |  |  |  |  |  | createdbyexternalparty | null | None |
| FindByID |  |  |  |  |  |  | createdon@OData.Community.Display.V1.FormattedValue |  |  |
| FindByID |  |  |  |  |  |  | creditlimit@OData.Community.Display.V1.FormattedValue |  |  |
| FindByID |  |  |  |  |  |  | creditlimit_base@OData.Community.Display.V1.FormattedValue |  |  |
| FindByID |  |  |  |  |  |  | creditonhold@OData.Community.Display.V1.FormattedValue |  |  |
| FindByID |  |  |  |  |  |  | customersizecode@OData.Community.Display.V1.FormattedValue |  |  |
| FindByID |  |  |  |  |  |  | customertypecode@OData.Community.Display.V1.FormattedValue |  |  |
| FindByID |  |  |  |  |  |  | defaultpricelevelid | null | None |
| FindByID |  |  |  |  |  |  | donotbulkemail@OData.Community.Display.V1.FormattedValue |  |  |
| FindByID |  |  |  |  |  |  | donotbulkpostalmail@OData.Community.Display.V1.FormattedValue |  |  |
| FindByID |  |  |  |  |  |  | donotemail@OData.Community.Display.V1.FormattedValue |  |  |
| FindByID |  |  |  |  |  |  | donotfax@OData.Community.Display.V1.FormattedValue |  |  |
| FindByID |  |  |  |  |  |  | donotphone@OData.Community.Display.V1.FormattedValue |  |  |
| FindByID |  |  |  |  |  |  | donotpostalmail@OData.Community.Display.V1.FormattedValue |  |  |
| FindByID |  |  |  |  |  |  | donotsendmm@OData.Community.Display.V1.FormattedValue |  |  |
| FindByID |  |  |  |  |  |  | educationcode@OData.Community.Display.V1.FormattedValue |  |  |
| FindByID |  |  |  |  |  |  | entityimage | string | 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 |
| FindByID |  |  |  |  |  |  | entityimage_timestamp | integer | 638855673911528600 |
| FindByID |  |  |  |  |  |  | entityimage_timestamp@OData.Community.Display.V1.FormattedValue |  |  |
| FindByID |  |  |  |  |  |  | entityimage_url | string | /Image/download.aspx?Entity=contact&Attribute=entityimage&Id=80ac35a0-01af-ea11-a812-000d3a8b3ec6&Timestamp=638855673911528523 |
| FindByID |  |  |  |  |  |  | entityimageid | string | 191e76dc-b549-f011-877a-000d3a183b4b |
| FindByID |  |  |  |  |  |  | exchangerate@OData.Community.Display.V1.FormattedValue |  |  |
| FindByID |  |  |  |  |  |  | externaluseridentifier | null | None |
| FindByID |  |  |  |  |  |  | familystatuscode@OData.Community.Display.V1.FormattedValue |  |  |
| FindByID |  |  |  |  |  |  | followemail@OData.Community.Display.V1.FormattedValue |  |  |
| FindByID |  |  |  |  |  |  | gendercode@OData.Community.Display.V1.FormattedValue |  |  |
| FindByID |  |  |  |  |  |  | haschildrencode@OData.Community.Display.V1.FormattedValue |  |  |
| FindByID |  |  |  |  |  |  | importsequencenumber | null | None |
| FindByID |  |  |  |  |  |  | isbackofficecustomer@OData.Community.Display.V1.FormattedValue |  |  |
| FindByID |  |  |  |  |  |  | leadsourcecode@OData.Community.Display.V1.FormattedValue |  |  |
| FindByID |  |  |  |  |  |  | marketingonly@OData.Community.Display.V1.FormattedValue |  |  |
| FindByID |  |  |  |  |  |  | masterid | null | None |
| FindByID |  |  |  |  |  |  | merged | boolean | False |
| FindByID |  |  |  |  |  |  | merged@OData.Community.Display.V1.FormattedValue |  |  |
| FindByID |  |  |  |  |  |  | modifiedbyexternalparty | null | None |
| FindByID |  |  |  |  |  |  | modifiedon@OData.Community.Display.V1.FormattedValue |  |  |
| FindByID |  |  |  |  |  |  | msa | null | None |
| FindByID |  |  |  |  |  |  | msdyn | null | None |
| FindByID |  |  |  |  |  |  | msdyn_disablewebtracking@OData.Community.Display.V1.FormattedValue |  |  |
| FindByID |  |  |  |  |  |  | msdyn_gdproptout@OData.Community.Display.V1.FormattedValue |  |  |
| FindByID |  |  |  |  |  |  | msdyn_isassistantinorgchart@OData.Community.Display.V1.FormattedValue |  |  |
| FindByID |  |  |  |  |  |  | msdyn_isminor@OData.Community.Display.V1.FormattedValue |  |  |
| FindByID |  |  |  |  |  |  | msdyn_isminorwithparentalconsent@OData.Community.Display.V1.FormattedValue |  |  |
| FindByID |  |  |  |  |  |  | msdyn_orgchangestatus@OData.Community.Display.V1.FormattedValue |  |  |
| FindByID |  |  |  |  |  |  | overriddencreatedon | null | None |
| FindByID |  |  |  |  |  |  | owningbusinessunit | string | a585f7d6-0649-f011-877a-000d3a183b4b |
| FindByID |  |  |  |  |  |  | owningteam | null | None |
| FindByID |  |  |  |  |  |  | owninguser | string | 28e6efdc-0649-f011-877a-000d3a183b4b |
| FindByID |  |  |  |  |  |  | parentcontactid | null | None |
| FindByID |  |  |  |  |  |  | participatesinworkflow | boolean | False |
| FindByID |  |  |  |  |  |  | participatesinworkflow@OData.Community.Display.V1.FormattedValue |  |  |
| FindByID |  |  |  |  |  |  | preferredappointmenttimecode@OData.Community.Display.V1.FormattedValue |  |  |
| FindByID |  |  |  |  |  |  | preferredcontactmethodcode@OData.Community.Display.V1.FormattedValue |  |  |
| FindByID |  |  |  |  |  |  | preferredequipmentid | null | None |
| FindByID |  |  |  |  |  |  | preferredserviceid | null | None |
| FindByID |  |  |  |  |  |  | processid | null | None |
| FindByID |  |  |  |  |  |  | shippingmethodcode@OData.Community.Display.V1.FormattedValue |  |  |
| FindByID |  |  |  |  |  |  | slaid | null | None |
| FindByID |  |  |  |  |  |  | slainvokedid | null | None |
| FindByID |  |  |  |  |  |  | stageid | null | None |
| FindByID |  |  |  |  |  |  | statecode | integer | 0 |
| FindByID |  |  |  |  |  |  | statecode@OData.Community.Display.V1.FormattedValue |  |  |
| FindByID |  |  |  |  |  |  | statuscode@OData.Community.Display.V1.FormattedValue |  |  |
| FindByID |  |  |  |  |  |  | subscriptionid | null | None |
| FindByID |  |  |  |  |  |  | teamsfollowed | null | None |
| FindByID |  |  |  |  |  |  | territorycode@OData.Community.Display.V1.FormattedValue |  |  |
| FindByID |  |  |  |  |  |  | timespentbymeonemailandmeetings | null | None |
| FindByID |  |  |  |  |  |  | timezoneruleversionnumber | integer | 4 |
| FindByID |  |  |  |  |  |  | timezoneruleversionnumber@OData.Community.Display.V1.FormattedValue |  |  |
| FindByID |  |  |  |  |  |  | transactioncurrencyid | string | a578dafc-aa49-f011-877a-000d3a183b4b |
| FindByID |  |  |  |  |  |  | traversedpath | null | None |
| FindByID |  |  |  |  |  |  | utcconversiontimezonecode | null | None |
| FindByID |  |  |  |  |  |  | versionnumber | integer | 4610448 |
| FindByID |  |  |  |  |  |  | versionnumber@OData.Community.Display.V1.FormattedValue |  |  |