# Differences between fields in Zoho CRM.io


## Deals

| Diff | Entity Schema Title | Schema Field ID | Entity Schema Types | Readonly | Possible Values | Reference Collection | FindByID Field ID | Find By ID Types | Value |
|------|---------------------|-----------------|---------------------|----------|-----------------|----------------------|-------------------|------------------|-------|
|  | Account Name | Account_Name | object | false |  |  | Account_Name | object | {"name": "Automation Account", "id": "3281233000003836011"} |
|  |  | Account_Name.id | string | false |  | Accounts | Account_Name.id | string | 3281233000003836011 |
|  |  | Account_Name.name | string | false |  |  | Account_Name.name | string | Automation Account |
|  | Amount | Amount | number | false |  |  | Amount | null | None |
|  | Campaign Source | Campaign_Source | object | false |  |  | Campaign_Source | null | None |
|  | Change Log Time | Change_Log_Time__s | string | false |  |  | Change_Log_Time__s | null | None |
|  | Closing Date | Closing_Date | string | false |  |  | Closing_Date | string | 2025-06-30 |
|  | Company Name | Company_Name | string | false |  |  | Company_Name | null | None |
|  | Contact Name | Contact_Name | object | false |  |  | Contact_Name | null | None |
|  | Created By | Created_By | object | false |  |  | Created_By | object | {"name": "PandaDoc Integrations Integrations", "id": "3281233000000154023", "email": "integrations+zohoplus@pandadoc.com"} |
|  |  | Created_By.email | string | false |  |  | Created_By.email | string | integrations+zohoplus@pandadoc.com |
|  |  | Created_By.id | string | false |  | users | Created_By.id | string | 3281233000000154023 |
|  |  | Created_By.name | string | false |  |  | Created_By.name | string | PandaDoc Integrations Integrations |
|  | Created Time | Created_Time | string | false |  |  | Created_Time | string | 2025-06-10T15:31:56+02:00 |
|  | Currency | Currency | string | false | `TRY`, `USD`, `EUR` |  | Currency | string | USD |
|  | Currency 3 | Currency_3 | number | false |  |  | Currency_3 | null | None |
|  | Deal Name | *Deal_Name | string | false |  |  | Deal_Name | string | Deal Oil Motors |
|  | Description | Description | string | false |  |  | Description | null | None |
|  | Exchange Rate | Exchange_Rate | number | false |  |  | Exchange_Rate | integer | 23 |
|  | Expected Revenue | Expected_Revenue | number | false |  |  | Expected_Revenue | null | None |
|  | LOTR test field | LOTR_test_field | string | false |  |  | LOTR_test_field | null | None |
|  | Last Activity Time | Last_Activity_Time | string | false |  |  | Last_Activity_Time | string | 2025-06-10T17:19:38+02:00 |
|  | Lead Conversion Time | Lead_Conversion_Time | integer | false |  |  | Lead_Conversion_Time | null | None |
|  | Lead Source | Lead_Source | string | false | `-None-`, `Advertisement`, `Cold Call`, `Employee Referral`, `External Referral`, `Online Store`, `Partner`, `Public Relations`, `Sales Email Alias`, `Seminar Partner`, `Internal Seminar`, `Trade Show`, `Web Download`, `Web Research`, `Chat` |  | Lead_Source | string | Advertisement |
|  | Locked | Locked__s | boolean | false |  |  | Locked__s | boolean | False |
|  | Modified By | Modified_By | object | false |  |  | Modified_By | object | {"name": "PandaDoc Integrations Integrations", "id": "3281233000000154023", "email": "integrations+zohoplus@pandadoc.com"} |
|  |  | Modified_By.email | string | false |  |  | Modified_By.email | string | integrations+zohoplus@pandadoc.com |
|  |  | Modified_By.id | string | false |  | users | Modified_By.id | string | 3281233000000154023 |
|  |  | Modified_By.name | string | false |  |  | Modified_By.name | string | PandaDoc Integrations Integrations |
|  | Modified Time | Modified_Time | string | false |  |  | Modified_Time | string | 2025-06-10T15:31:56+02:00 |
|  | Next Step | Next_Step | string | false |  |  | Next_Step | null | None |
|  | OlegCustomCurrency | OlegCustomCurrency | number | false |  |  | OlegCustomCurrency | null | None |
|  | Overall Sales Duration | Overall_Sales_Duration | integer | false |  |  | Overall_Sales_Duration | integer | 20 |
|  | Deal Owner | Owner | object | false |  |  | Owner | object | {"name": "PandaDoc Integrations Integrations", "id": "3281233000000154023", "email": "integrations+zohoplus@pandadoc.com"} |
|  |  | Owner.email | string | false |  |  | Owner.email | string | integrations+zohoplus@pandadoc.com |
|  |  | Owner.id | string | false |  | users | Owner.id | string | 3281233000000154023 |
|  |  | Owner.name | string | false |  |  | Owner.name | string | PandaDoc Integrations Integrations |
|  | Probability (%) | Probability | integer | false |  |  | Probability | integer | 20 |
|  | Record Status | Record_Status__s | string | false | `Trash`, `Available`, `Draft` |  | Record_Status__s | string | Available |
|  | Sales Cycle Duration | Sales_Cycle_Duration | integer | false |  |  | Sales_Cycle_Duration | integer | 20 |
|  | Stage | *Stage | string | false | `Qualification`, `Needs Analysis`, `Value Proposition`, `Identify Decision Makers`, `Proposal/Price Quote`, `Negotiation/Review`, `Closed Won`, `Closed Lost`, `Closed-Lost to Competition` |  | Stage | string | Needs Analysis |
|  | Tag | Tag | array | false |  |  | Tag | array | [] |
|  |  | Tag[] | object | false |  |  | Tag[] | object |  |
|  |  | Tag[].id | string | false |  |  | Tag[].id | string |  |
|  |  | Tag[].name | string | false |  |  | Tag[].name | string |  |
|  | Type | Type | string | false | `-None-`, `Existing Business`, `New Business` |  | Type | string | Existing Business |
|  | QTY | deal_QTY | number | false |  |  | deal_QTY | null | None |
|  | Record Id | id | string | false |  |  | id | string | 3281233000032009023 |
|  | romanDate | romanDate | string | false |  |  | romanDate | null | None |
|  | romanTest | romanTest | number | false |  |  | romanTest | null | None |
| Schema |  | <span style='color:red'>***Campaign_Source.id***</span> | string | false |  | Campaigns |  |  |  |
| Schema |  | <span style='color:red'>***Campaign_Source.name***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***Contact_Name.id***</span> | string | false |  | Contacts |  |  |  |
| Schema |  | <span style='color:red'>***Contact_Name.name***</span> | string | false |  |  |  |  |  |
| Schema | Reason For Loss | <span style='color:red'>***Reason_For_Loss__s***</span> | string | false | `-None-`, `Expectation Mismatch`, `Price`, `Unqualified Customer`, `Lack of response`, `Missed Follow Ups`, `Wrong Target`, `Competition`, `Future Interest`, `Other` |  |  |  |  |
| Schema | Deal Image | <span style='color:red'>***Record_Image***</span> | string | false |  |  |  |  |  |
| FindByID |  |  |  |  |  |  | $approval | object | {"delegate": false, "takeover": false, "approve": false, "reject": false, "resubmit": false} |
| FindByID |  |  |  |  |  |  | $approval.approve | boolean | False |
| FindByID |  |  |  |  |  |  | $approval.delegate | boolean | False |
| FindByID |  |  |  |  |  |  | $approval.reject | boolean | False |
| FindByID |  |  |  |  |  |  | $approval.resubmit | boolean | False |
| FindByID |  |  |  |  |  |  | $approval.takeover | boolean | False |
| FindByID |  |  |  |  |  |  | $approval_state | string | approved |
| FindByID |  |  |  |  |  |  | $currency_symbol | string | $ |
| FindByID |  |  |  |  |  |  | $editable | boolean | True |
| FindByID |  |  |  |  |  |  | $field_states | null | None |
| FindByID |  |  |  |  |  |  | $in_merge | boolean | False |
| FindByID |  |  |  |  |  |  | $layout_id | object | {"display_label": "Standard", "name": "Standard", "id": "3281233000000091023"} |
| FindByID |  |  |  |  |  |  | $layout_id.display_label | string | Standard |
| FindByID |  |  |  |  |  |  | $layout_id.id | string | 3281233000000091023 |
| FindByID |  |  |  |  |  |  | $layout_id.name | string | Standard |
| FindByID |  |  |  |  |  |  | $locked_for_me | boolean | False |
| FindByID |  |  |  |  |  |  | $orchestration | boolean | False |
| FindByID |  |  |  |  |  |  | $pathfinder | boolean | False |
| FindByID |  |  |  |  |  |  | $process_flow | boolean | False |
| FindByID |  |  |  |  |  |  | $review | null | None |
| FindByID |  |  |  |  |  |  | $review_process | object | {"approve": false, "reject": false, "resubmit": false} |
| FindByID |  |  |  |  |  |  | $review_process.approve | boolean | False |
| FindByID |  |  |  |  |  |  | $review_process.reject | boolean | False |
| FindByID |  |  |  |  |  |  | $review_process.resubmit | boolean | False |
| FindByID |  |  |  |  |  |  | $sharing_permission | string | full_access |
| FindByID |  |  |  |  |  |  | $state | string | save |
| FindByID |  |  |  |  |  |  | $wizard_connection_path | null | None |
| FindByID |  |  |  |  |  |  | $zia_owner_assignment | string | owner_recommendation_unavailable |
| FindByID |  |  |  |  |  |  | $zia_visions | null | None |

## Accounts

| Diff | Entity Schema Title | Schema Field ID | Entity Schema Types | Readonly | Possible Values | Reference Collection | FindByID Field ID | Find By ID Types | Value |
|------|---------------------|-----------------|---------------------|----------|-----------------|----------------------|-------------------|------------------|-------|
|  | Account Name | *Account_Name | string | false |  |  | Account_Name | string | Iryna Pakrouskaya |
|  | Account Number | Account_Number | string | false |  |  | Account_Number | string | 0 |
|  | Account Site | Account_Site | string | false |  |  | Account_Site | null | None |
|  | Account Type | Account_Type | string | false | `-None-`, `Analyst`, `Competitor`, `Customer`, `Distributor`, `Integrator`, `Investor`, `Other`, `Partner`, `Press`, `Prospect`, `Reseller`, `Supplier`, `Vendor` |  | Account_Type | null | None |
|  | Annual Revenue | Annual_Revenue | number | false |  |  | Annual_Revenue | null | None |
|  | Billing City | Billing_City | string | false |  |  | Billing_City | null | None |
|  | Billing Code | Billing_Code | string | false |  |  | Billing_Code | null | None |
|  | Billing Country | Billing_Country | string | false |  |  | Billing_Country | null | None |
|  | Billing State | Billing_State | string | false |  |  | Billing_State | null | None |
|  | Billing Street | Billing_Street | string | false |  |  | Billing_Street | null | None |
|  | Change Log Time | Change_Log_Time__s | string | false |  |  | Change_Log_Time__s | null | None |
|  | Created By | Created_By | object | false |  |  | Created_By | object | {"name": "PandaDoc Integrations Integrations", "id": "3281233000000154023", "email": "integrations+zohoplus@pandadoc.com"} |
|  |  | Created_By.email | string | false |  |  | Created_By.email | string | integrations+zohoplus@pandadoc.com |
|  |  | Created_By.id | string | false |  | users | Created_By.id | string | 3281233000000154023 |
|  |  | Created_By.name | string | false |  |  | Created_By.name | string | PandaDoc Integrations Integrations |
|  | Created Time | Created_Time | string | false |  |  | Created_Time | string | 2022-12-02T14:40:24+01:00 |
|  | Currency | Currency | string | false | `TRY`, `USD`, `EUR` |  | Currency | string | USD |
|  | Description | Description | string | false |  |  | Description | null | None |
|  | Employees | Employees | integer | false |  |  | Employees | null | None |
|  | Enrich Status | Enrich_Status__s | string | false | `Available`, `Enriched`, `Data not found` |  | Enrich_Status__s | null | None |
|  | Exchange Rate | Exchange_Rate | number | false |  |  | Exchange_Rate | integer | 23 |
|  | Fax | Fax | string | false |  |  | Fax | null | None |
|  | Industry | Industry | string | false | `-None-`, `ASP (Application Service Provider)`, `Data/Telecom OEM`, `ERP (Enterprise Resource Planning)`, `Government/Military`, `Large Enterprise`, `ManagementISV`, `MSP (Management Service Provider)`, `Network Equipment Enterprise`, `Non-management ISV`, `Optical Networking`, `Service Provider`, `Small/Medium Enterprise`, `Storage Equipment`, `Storage Service Provider`, `Systems Integrator`, `Wireless Industry` |  | Industry | null | None |
|  | Last Activity Time | Last_Activity_Time | string | false |  |  | Last_Activity_Time | string | 2024-03-06T09:54:53+01:00 |
|  | Last Enriched Time | Last_Enriched_Time__s | string | false |  |  | Last_Enriched_Time__s | null | None |
|  | Locked | Locked__s | boolean | false |  |  | Locked__s | boolean | False |
|  | Modified By | Modified_By | object | false |  |  | Modified_By | object | {"name": "PandaDoc Integrations Integrations", "id": "3281233000000154023", "email": "integrations+zohoplus@pandadoc.com"} |
|  |  | Modified_By.email | string | false |  |  | Modified_By.email | string | integrations+zohoplus@pandadoc.com |
|  |  | Modified_By.id | string | false |  | users | Modified_By.id | string | 3281233000000154023 |
|  |  | Modified_By.name | string | false |  |  | Modified_By.name | string | PandaDoc Integrations Integrations |
|  | Modified Time | Modified_Time | string | false |  |  | Modified_Time | string | 2022-12-02T14:40:24+01:00 |
|  | Name Used For Field Managers | Name_Used_For_Field_Managers | string | false |  |  | Name_Used_For_Field_Managers | null | None |
|  | Name Used For Franchisees | Name_Used_For_Franchisees | string | false |  |  | Name_Used_For_Franchisees | null | None |
|  | Account Owner | Owner | object | false |  |  | Owner | object | {"name": "PandaDoc Integrations Integrations", "id": "3281233000000154023", "email": "integrations+zohoplus@pandadoc.com"} |
|  |  | Owner.email | string | false |  |  | Owner.email | string | integrations+zohoplus@pandadoc.com |
|  |  | Owner.id | string | false |  | users | Owner.id | string | 3281233000000154023 |
|  |  | Owner.name | string | false |  |  | Owner.name | string | PandaDoc Integrations Integrations |
|  | Ownership | Ownership | string | false | `-None-`, `Other`, `Private`, `Public`, `Subsidiary` |  | Ownership | null | None |
|  | Parent Account | Parent_Account | object | false |  |  | Parent_Account | null | None |
|  | Phone | Phone | string | false |  |  | Phone | null | None |
|  | Rating | Rating | string | false | `-None-`, `Acquired`, `Active`, `Market Failed`, `Project Cancelled`, `Shut Down` |  | Rating | null | None |
|  | Account Image | Record_Image | string | false |  |  | Record_Image | null | None |
|  | Record Status | Record_Status__s | string | false | `Trash`, `Available`, `Draft` |  | Record_Status__s | string | Available |
|  | SIC Code | SIC_Code | integer | false |  |  | SIC_Code | null | None |
|  | Shipping City | Shipping_City | string | false |  |  | Shipping_City | null | None |
|  | Shipping Code | Shipping_Code | string | false |  |  | Shipping_Code | null | None |
|  | Shipping Country | Shipping_Country | string | false |  |  | Shipping_Country | null | None |
|  | Shipping State | Shipping_State | string | false |  |  | Shipping_State | null | None |
|  | Shipping Street | Shipping_Street | string | false |  |  | Shipping_Street | null | None |
|  | Tag | Tag | array | false |  |  | Tag | array | [] |
|  |  | Tag[] | object | false |  |  | Tag[] | object |  |
|  |  | Tag[].id | string | false |  |  | Tag[].id | string |  |
|  |  | Tag[].name | string | false |  |  | Tag[].name | string |  |
|  | Ticker Symbol | Ticker_Symbol | string | false |  |  | Ticker_Symbol | null | None |
|  | Website | Website | string | false |  |  | Website | null | None |
|  | Record Id | id | string | false |  |  | id | string | 3281233000004079001 |
| Schema |  | <span style='color:red'>***Parent_Account.id***</span> | string | false |  | Accounts |  |  |  |
| Schema |  | <span style='color:red'>***Parent_Account.name***</span> | string | false |  |  |  |  |  |
| FindByID |  |  |  |  |  |  | $approval | object | {"delegate": false, "takeover": false, "approve": false, "reject": false, "resubmit": false} |
| FindByID |  |  |  |  |  |  | $approval.approve | boolean | False |
| FindByID |  |  |  |  |  |  | $approval.delegate | boolean | False |
| FindByID |  |  |  |  |  |  | $approval.reject | boolean | False |
| FindByID |  |  |  |  |  |  | $approval.resubmit | boolean | False |
| FindByID |  |  |  |  |  |  | $approval.takeover | boolean | False |
| FindByID |  |  |  |  |  |  | $approval_state | string | approved |
| FindByID |  |  |  |  |  |  | $currency_symbol | string | $ |
| FindByID |  |  |  |  |  |  | $editable | boolean | True |
| FindByID |  |  |  |  |  |  | $field_states | null | None |
| FindByID |  |  |  |  |  |  | $in_merge | boolean | False |
| FindByID |  |  |  |  |  |  | $is_duplicate | boolean | False |
| FindByID |  |  |  |  |  |  | $layout_id | object | {"display_label": "Standard", "name": "Standard", "id": "3281233000000091029"} |
| FindByID |  |  |  |  |  |  | $layout_id.display_label | string | Standard |
| FindByID |  |  |  |  |  |  | $layout_id.id | string | 3281233000000091029 |
| FindByID |  |  |  |  |  |  | $layout_id.name | string | Standard |
| FindByID |  |  |  |  |  |  | $locked_for_me | boolean | False |
| FindByID |  |  |  |  |  |  | $orchestration | boolean | False |
| FindByID |  |  |  |  |  |  | $pathfinder | boolean | False |
| FindByID |  |  |  |  |  |  | $process_flow | boolean | False |
| FindByID |  |  |  |  |  |  | $review | null | None |
| FindByID |  |  |  |  |  |  | $review_process | object | {"approve": false, "reject": false, "resubmit": false} |
| FindByID |  |  |  |  |  |  | $review_process.approve | boolean | False |
| FindByID |  |  |  |  |  |  | $review_process.reject | boolean | False |
| FindByID |  |  |  |  |  |  | $review_process.resubmit | boolean | False |
| FindByID |  |  |  |  |  |  | $sharing_permission | string | full_access |
| FindByID |  |  |  |  |  |  | $state | string | save |
| FindByID |  |  |  |  |  |  | $wizard_connection_path | null | None |
| FindByID |  |  |  |  |  |  | $zia_owner_assignment | null | None |
| FindByID |  |  |  |  |  |  | $zia_visions | null | None |

## Contacts

| Diff | Entity Schema Title | Schema Field ID | Entity Schema Types | Readonly | Possible Values | Reference Collection | FindByID Field ID | Find By ID Types | Value |
|------|---------------------|-----------------|---------------------|----------|-----------------|----------------------|-------------------|------------------|-------|
|  | Account Name | Account_Name | object | false |  |  | Account_Name | object | {"name": "Test", "id": "3281233000000576003"} |
|  |  | Account_Name.id | string | false |  | Accounts | Account_Name.id | string | 3281233000000576003 |
|  |  | Account_Name.name | string | false |  |  | Account_Name.name | string | Test |
|  | Assistant | Assistant | string | false |  |  | Assistant | null | None |
|  | Asst Phone | Asst_Phone | string | false |  |  | Asst_Phone | null | None |
|  | Average Time Spent (Minutes) | Average_Time_Spent_Minutes | number | false |  |  | Average_Time_Spent_Minutes | null | None |
|  | Change Log Time | Change_Log_Time__s | string | false |  |  | Change_Log_Time__s | null | None |
|  | Created By | Created_By | object | false |  |  | Created_By | object | {"name": "PandaDoc Integrations Integrations", "id": "3281233000000154023", "email": "integrations+zohoplus@pandadoc.com"} |
|  |  | Created_By.email | string | false |  |  | Created_By.email | string | integrations+zohoplus@pandadoc.com |
|  |  | Created_By.id | string | false |  | users | Created_By.id | string | 3281233000000154023 |
|  |  | Created_By.name | string | false |  |  | Created_By.name | string | PandaDoc Integrations Integrations |
|  | Created Time | Created_Time | string | false |  |  | Created_Time | string | 2024-11-06T16:15:57+01:00 |
|  | Date of Birth | Date_of_Birth | string | false |  |  | Date_of_Birth | null | None |
|  | Days Visited | Days_Visited | integer | false |  |  | Days_Visited | null | None |
|  | Department | Department | string | false |  |  | Department | null | None |
|  | Description | Description | string | false |  |  | Description | null | None |
|  | Email | Email | string | false |  |  | Email | string | a@gmail.com |
|  | Email Opt Out | Email_Opt_Out | boolean | false |  |  | Email_Opt_Out | boolean | False |
|  | Enrich Status | Enrich_Status__s | string | false | `Available`, `Enriched`, `Data not found` |  | Enrich_Status__s | null | None |
|  | Fax | Fax | string | false |  |  | Fax | null | None |
|  | First Name | First_Name | string | false |  |  | First_Name | string | Lena |
|  | First Visit | First_Visited_Time | string | false |  |  | First_Visited_Time | null | None |
|  | First Page Visited | First_Visited_URL | string | false |  |  | First_Visited_URL | null | None |
|  | Full Name | Full_Name | string | false |  |  | Full_Name | string | Lena Barashkova |
|  | Home Phone | Home_Phone | string | false |  |  | Home_Phone | null | None |
|  | Last Activity Time | Last_Activity_Time | string | false |  |  | Last_Activity_Time | string | 2024-11-06T16:15:58+01:00 |
|  | Last Enriched Time | Last_Enriched_Time__s | string | false |  |  | Last_Enriched_Time__s | null | None |
|  | Last Name | *Last_Name | string | false |  |  | Last_Name | string | Barashkova |
|  | Most Recent Visit | Last_Visited_Time | string | false |  |  | Last_Visited_Time | null | None |
|  | Lead Source | Lead_Source | string | false | `-None-`, `Advertisement`, `Cold Call`, `Employee Referral`, `External Referral`, `Online Store`, `Partner`, `Public Relations`, `Sales Email Alias`, `Seminar Partner`, `Internal Seminar`, `Trade Show`, `Web Download`, `Web Research`, `Web Cases`, `Web Mail`, `Chat` |  | Lead_Source | null | None |
|  | Locked | Locked__s | boolean | false |  |  | Locked__s | boolean | False |
|  | Mailing City | Mailing_City | string | false |  |  | Mailing_City | null | None |
|  | Mailing Country | Mailing_Country | string | false |  |  | Mailing_Country | null | None |
|  | Mailing State | Mailing_State | string | false |  |  | Mailing_State | null | None |
|  | Mailing Street | Mailing_Street | string | false |  |  | Mailing_Street | null | None |
|  | Mailing Zip | Mailing_Zip | string | false |  |  | Mailing_Zip | null | None |
|  | Mobile | Mobile | string | false |  |  | Mobile | null | None |
|  | Modified By | Modified_By | object | false |  |  | Modified_By | object | {"name": "PandaDoc Integrations Integrations", "id": "3281233000000154023", "email": "integrations+zohoplus@pandadoc.com"} |
|  |  | Modified_By.email | string | false |  |  | Modified_By.email | string | integrations+zohoplus@pandadoc.com |
|  |  | Modified_By.id | string | false |  | users | Modified_By.id | string | 3281233000000154023 |
|  |  | Modified_By.name | string | false |  |  | Modified_By.name | string | PandaDoc Integrations Integrations |
|  | Modified Time | Modified_Time | string | false |  |  | Modified_Time | string | 2024-11-06T16:15:57+01:00 |
|  | Number Of Chats | Number_Of_Chats | integer | false |  |  | Number_Of_Chats | null | None |
|  | Other City | Other_City | string | false |  |  | Other_City | null | None |
|  | Other Country | Other_Country | string | false |  |  | Other_Country | null | None |
|  | Other Phone | Other_Phone | string | false |  |  | Other_Phone | null | None |
|  | Other State | Other_State | string | false |  |  | Other_State | null | None |
|  | Other Street | Other_Street | string | false |  |  | Other_Street | null | None |
|  | Other Zip | Other_Zip | string | false |  |  | Other_Zip | null | None |
|  | Contact Owner | Owner | object | false |  |  | Owner | object | {"name": "PandaDoc Integrations Integrations", "id": "3281233000000154023", "email": "integrations+zohoplus@pandadoc.com"} |
|  |  | Owner.email | string | false |  |  | Owner.email | string | integrations+zohoplus@pandadoc.com |
|  |  | Owner.id | string | false |  | users | Owner.id | string | 3281233000000154023 |
|  |  | Owner.name | string | false |  |  | Owner.name | string | PandaDoc Integrations Integrations |
|  | Phone | Phone | string | false |  |  | Phone | null | None |
|  | Contact Image | Record_Image | string | false |  |  | Record_Image | null | None |
|  | Record Status | Record_Status__s | string | false | `Trash`, `Available`, `Draft` |  | Record_Status__s | string | Available |
|  | Referrer | Referrer | string | false |  |  | Referrer | null | None |
|  | Reporting To | Reporting_To | object | false |  |  | Reporting_To | null | None |
|  | Reports To | Reports_To | string | false |  |  | Reports_To | null | None |
|  | ContactRole | Role | string | false |  |  | Role | null | None |
|  | Salutation | Salutation | string | false | `-None-`, `Mr.`, `Mrs.`, `Ms.`, `Dr.`, `Prof.` |  | Salutation | null | None |
|  | Secondary Email | Secondary_Email | string | false |  |  | Secondary_Email | null | None |
|  | Skype ID | Skype_ID | string | false |  |  | Skype_ID | null | None |
|  | Tag | Tag | array | false |  |  | Tag | array | [] |
|  |  | Tag[] | object | false |  |  | Tag[] | object |  |
|  |  | Tag[].id | string | false |  |  | Tag[].id | string |  |
|  |  | Tag[].name | string | false |  |  | Tag[].name | string |  |
|  | Title | Title | string | false |  |  | Title | null | None |
|  | Twitter | Twitter | string | false |  |  | Twitter | null | None |
|  | Unsubscribed Mode | Unsubscribed_Mode | string | false | `Consent form`, `Manual`, `Unsubscribe link`, `Zoho campaigns` |  | Unsubscribed_Mode | null | None |
|  | Unsubscribed Time | Unsubscribed_Time | string | false |  |  | Unsubscribed_Time | null | None |
|  | Vendor Name | Vendor_Name | object | false |  |  | Vendor_Name | null | None |
|  | Visitor Score | Visitor_Score | string | false |  |  | Visitor_Score | null | None |
|  | Record Id | id | string | false |  |  | id | string | 3281233000021984041 |
| Schema |  | <span style='color:red'>***Reporting_To.id***</span> | string | false |  | Contacts |  |  |  |
| Schema |  | <span style='color:red'>***Reporting_To.name***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***Vendor_Name.id***</span> | string | false |  | Vendors |  |  |  |
| Schema |  | <span style='color:red'>***Vendor_Name.name***</span> | string | false |  |  |  |  |  |
| FindByID |  |  |  |  |  |  | $approval | object | {"delegate": false, "takeover": false, "approve": false, "reject": false, "resubmit": false} |
| FindByID |  |  |  |  |  |  | $approval.approve | boolean | False |
| FindByID |  |  |  |  |  |  | $approval.delegate | boolean | False |
| FindByID |  |  |  |  |  |  | $approval.reject | boolean | False |
| FindByID |  |  |  |  |  |  | $approval.resubmit | boolean | False |
| FindByID |  |  |  |  |  |  | $approval.takeover | boolean | False |
| FindByID |  |  |  |  |  |  | $approval_state | string | approved |
| FindByID |  |  |  |  |  |  | $currency_symbol | string | $ |
| FindByID |  |  |  |  |  |  | $editable | boolean | True |
| FindByID |  |  |  |  |  |  | $field_states | null | None |
| FindByID |  |  |  |  |  |  | $in_merge | boolean | False |
| FindByID |  |  |  |  |  |  | $is_duplicate | boolean | False |
| FindByID |  |  |  |  |  |  | $layout_id | object | {"display_label": "Standard", "name": "Standard", "id": "3281233000000091033"} |
| FindByID |  |  |  |  |  |  | $layout_id.display_label | string | Standard |
| FindByID |  |  |  |  |  |  | $layout_id.id | string | 3281233000000091033 |
| FindByID |  |  |  |  |  |  | $layout_id.name | string | Standard |
| FindByID |  |  |  |  |  |  | $locked_for_me | boolean | False |
| FindByID |  |  |  |  |  |  | $orchestration | boolean | False |
| FindByID |  |  |  |  |  |  | $pathfinder | boolean | True |
| FindByID |  |  |  |  |  |  | $process_flow | boolean | False |
| FindByID |  |  |  |  |  |  | $review | null | None |
| FindByID |  |  |  |  |  |  | $review_process | object | {"approve": false, "reject": false, "resubmit": false} |
| FindByID |  |  |  |  |  |  | $review_process.approve | boolean | False |
| FindByID |  |  |  |  |  |  | $review_process.reject | boolean | False |
| FindByID |  |  |  |  |  |  | $review_process.resubmit | boolean | False |
| FindByID |  |  |  |  |  |  | $sharing_permission | string | full_access |
| FindByID |  |  |  |  |  |  | $state | string | save |
| FindByID |  |  |  |  |  |  | $wizard_connection_path | null | None |
| FindByID |  |  |  |  |  |  | $zia_owner_assignment | null | None |
| FindByID |  |  |  |  |  |  | $zia_visions | null | None |