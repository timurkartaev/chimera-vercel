# Differences between fields in SugarCRM.io


## Opportunities

| Diff | Entity Schema Title | Schema Field ID | Entity Schema Types | Readonly | Possible Values | Reference Collection | FindByID Field ID | Find By ID Types | Value |
|------|---------------------|-----------------|---------------------|----------|-----------------|----------------------|-------------------|------------------|-------|
|  |  | account_id | string | false |  | accounts | account_id | string | d890652e-30cc-11f0-9c5b-31b297db6ffd |
|  |  | ai_opp_conv_bin_accuracy | string | false |  |  | ai_opp_conv_bin_accuracy | null | None |
|  |  | ai_opp_conv_multiplier | string | false |  |  | ai_opp_conv_multiplier | null | None |
|  |  | ai_opp_conv_score_absolute | string | false |  |  | ai_opp_conv_score_absolute | null | None |
|  |  | ai_opp_conv_score_enum | string | false |  |  | ai_opp_conv_score_enum | string |  |
|  |  | amount | string | false |  |  | amount | string | 34800.000000 |
|  |  | amount_usdollar | string | false |  |  | amount_usdollar | string | 34800.000000 |
|  |  | assigned_user_id | string | false |  | users | assigned_user_id | string | seed_will_id |
|  |  | base_rate | string | false |  |  | base_rate | string | 1.000000 |
|  |  | best_case | string | false |  |  | best_case | string | 34800.000000 |
|  |  | campaign_id | string | false |  |  | campaign_id | string |  |
|  |  | campaign_opportunities | object | false |  |  | campaign_opportunities | object | {"name": "", "id": ""} |
|  |  | campaign_opportunities.id | string | false |  |  | campaign_opportunities.id | string |  |
|  |  | campaign_opportunities.name | string | false |  |  | campaign_opportunities.name | string |  |
|  |  | closed_revenue_line_items | integer | false |  |  | closed_revenue_line_items | integer | 0 |
|  |  | closed_won_revenue_line_items | integer | false |  |  | closed_won_revenue_line_items | integer | 0 |
|  |  | commit_stage | string | false |  |  | commit_stage | string | exclude |
|  |  | commit_stage_cascade | string | false |  |  | commit_stage_cascade | string |  |
|  |  | contact_role | string | false |  |  | contact_role | string |  |
|  |  | created_by | string | false |  | users | created_by | string | 1 |
|  |  | currency_id | string | false | `US Dollars`, `Euro` |  | currency_id | string | -99 |
|  |  | currency_name | string | false |  |  | currency_name | string |  |
|  |  | date_closed | string | false |  |  | date_closed | string | 2025-05-26 |
|  |  | date_closed_cascade | string | false |  |  | date_closed_cascade | string |  |
|  |  | date_closed_timestamp | integer | false |  |  | date_closed_timestamp | integer | 1748217600 |
|  |  | date_entered | string | false |  |  | date_entered | string | 2025-05-11T03:00:00+05:00 |
|  |  | date_modified | string | false |  |  | date_modified | string | 2025-05-14T21:02:38+05:00 |
|  |  | deleted | boolean | false |  |  | deleted | boolean | False |
|  |  | description | string | false |  |  | description | string |  |
|  |  | following | boolean | false |  |  | following | boolean | False |
|  |  | forecasted_likely | string | false |  |  | forecasted_likely | string | 0.000000 |
|  |  | geocode_status | string | false |  |  | geocode_status | string |  |
|  |  | id | string | true |  |  | id | string | db3f6530-30dc-11f0-9285-fb295c038a96 |
|  |  | included_revenue_line_items | integer | false |  |  | included_revenue_line_items | integer | 0 |
|  |  | is_escalated | boolean | false |  |  | is_escalated | boolean | False |
|  |  | lead_source | string | false |  |  | lead_source | string |  |
|  |  | lost | string | false |  |  | lost | string | 0.000000 |
|  |  | mkto_id | string | false |  |  | mkto_id | null | None |
|  |  | mkto_sync | boolean | false |  |  | mkto_sync | boolean | False |
|  |  | modified_user_id | string | false |  | users | modified_user_id | string | 1 |
|  |  | my_favorite | boolean | false |  |  | my_favorite | boolean | False |
|  |  | *name | string | false |  |  | name | string | RRR Advertising Inc. - $34800 - 647 |
|  |  | next_step | string | false |  |  | next_step | string |  |
|  |  | opportunity_type | string | false |  |  | opportunity_type | string | Existing Business |
|  |  | probability | integer | false |  |  | probability | integer | 10 |
|  |  | renewal | boolean | false |  |  | renewal | boolean | False |
|  |  | renewal_parent_id | string | false |  |  | renewal_parent_id | string |  |
|  |  | renewal_parent_name | string | false |  |  | renewal_parent_name | string |  |
|  |  | sales_stage | string | false |  |  | sales_stage | string | Prospecting |
|  |  | sales_stage_cascade | string | false |  |  | sales_stage_cascade | string |  |
|  |  | sales_status | string | false |  |  | sales_status | string | In Progress |
|  |  | service_duration_unit | string | false |  |  | service_duration_unit | string |  |
|  |  | service_duration_unit_cascade | string | false |  |  | service_duration_unit_cascade | string |  |
|  |  | service_duration_value | integer | false |  |  | service_duration_value | null | None |
|  |  | service_duration_value_cascade | integer | false |  |  | service_duration_value_cascade | null | None |
|  |  | service_open_flex_duration_rlis | integer | false |  |  | service_open_flex_duration_rlis | integer | 0 |
|  |  | service_open_revenue_line_items | integer | false |  |  | service_open_revenue_line_items | integer | 0 |
|  |  | service_start_date | string | false |  |  | service_start_date | string |  |
|  |  | service_start_date_cascade | string | false |  |  | service_start_date_cascade | string |  |
|  |  | sl_ai_conv_score_c | string | false |  |  | sl_ai_conv_score_c | string | 01_not_likely |
|  |  | sync_key | string | false |  |  | sync_key | string |  |
|  |  | tag | array | false |  |  | tag | array | [] |
|  |  | team_count | string | false |  |  | team_count | string |  |
|  |  | team_name | array | false |  |  | team_name | array | [{"id": "1", "name": "Global", "name_2": "", "primary": true, "selected": false}] |
|  |  | team_name[] | object | false |  |  | team_name[] | object | {"id": "1", "name": "Global", "name_2": "", "primary": true, "selected": false} |
|  |  | team_name[].id | string | false |  |  | team_name[].id | string | 1 |
|  |  | team_name[].name | string | false |  |  | team_name[].name | string | Global |
|  |  | team_name[].name_2 | string | false |  |  | team_name[].name_2 | string |  |
|  |  | team_name[].primary | boolean | false |  |  | team_name[].primary | boolean | True |
|  |  | team_name[].selected | boolean | false |  |  | team_name[].selected | boolean | False |
|  |  | total_revenue_line_items | integer | false |  |  | total_revenue_line_items | integer | 1 |
|  |  | widget_amount | string | false |  |  | widget_amount | string |  |
|  |  | widget_date_closed | string | false |  |  | widget_date_closed | string |  |
|  |  | widget_sales_stage | string | false |  |  | widget_sales_stage | string |  |
|  |  | worst_case | string | false |  |  | worst_case | string | 34800.000000 |
| FindByID |  |  |  |  |  |  | _acl | object | {"fields": {}} |
| FindByID |  |  |  |  |  |  | _acl.fields | object | {} |
| FindByID |  |  |  |  |  |  | _module | string | Opportunities |
| FindByID |  |  |  |  |  |  | account_name | string | RRR Advertising Inc. |
| FindByID |  |  |  |  |  |  | accounts | object | {"name": "RRR Advertising Inc.", "id": "d890652e-30cc-11f0-9c5b-31b297db6ffd", "_acl": {"fields": [], "_hash": "654d337e0e912edaa00dbb0fb3dc3c17"}} |
| FindByID |  |  |  |  |  |  | accounts._acl | object | {"fields": [], "_hash": "654d337e0e912edaa00dbb0fb3dc3c17"} |
| FindByID |  |  |  |  |  |  | accounts._acl._hash | string | 654d337e0e912edaa00dbb0fb3dc3c17 |
| FindByID |  |  |  |  |  |  | accounts._acl.fields | array | [] |
| FindByID |  |  |  |  |  |  | accounts.id | string | d890652e-30cc-11f0-9c5b-31b297db6ffd |
| FindByID |  |  |  |  |  |  | accounts.name | string | RRR Advertising Inc. |
| FindByID |  |  |  |  |  |  | ai_opp_close_week_scores | null | None |
| FindByID |  |  |  |  |  |  | ai_opp_won_score | null | None |
| FindByID |  |  |  |  |  |  | assigned_user_link | object | {"full_name": "Will Westin", "id": "seed_will_id", "_acl": {"fields": [], "_hash": "654d337e0e912edaa00dbb0fb3dc3c17"}} |
| FindByID |  |  |  |  |  |  | assigned_user_link._acl | object | {"fields": [], "_hash": "654d337e0e912edaa00dbb0fb3dc3c17"} |
| FindByID |  |  |  |  |  |  | assigned_user_link._acl._hash | string | 654d337e0e912edaa00dbb0fb3dc3c17 |
| FindByID |  |  |  |  |  |  | assigned_user_link._acl.fields | array | [] |
| FindByID |  |  |  |  |  |  | assigned_user_link.full_name | string | Will Westin |
| FindByID |  |  |  |  |  |  | assigned_user_link.id | string | seed_will_id |
| FindByID |  |  |  |  |  |  | assigned_user_name | string | Will Westin |
| FindByID |  |  |  |  |  |  | campaign_name | string |  |
| FindByID |  |  |  |  |  |  | created_by_link | object | {"full_name": "Jen Smith", "id": "1", "_acl": {"fields": [], "_hash": "654d337e0e912edaa00dbb0fb3dc3c17"}} |
| FindByID |  |  |  |  |  |  | created_by_link._acl | object | {"fields": [], "_hash": "654d337e0e912edaa00dbb0fb3dc3c17"} |
| FindByID |  |  |  |  |  |  | created_by_link._acl._hash | string | 654d337e0e912edaa00dbb0fb3dc3c17 |
| FindByID |  |  |  |  |  |  | created_by_link._acl.fields | array | [] |
| FindByID |  |  |  |  |  |  | created_by_link.full_name | string | Jen Smith |
| FindByID |  |  |  |  |  |  | created_by_link.id | string | 1 |
| FindByID |  |  |  |  |  |  | created_by_name | string | Jen Smith |
| FindByID |  |  |  |  |  |  | currencies | object | {"name": "", "id": "-99", "_acl": {"fields": [], "_hash": "654d337e0e912edaa00dbb0fb3dc3c17"}, "symbol": ""} |
| FindByID |  |  |  |  |  |  | currencies._acl | object | {"fields": [], "_hash": "654d337e0e912edaa00dbb0fb3dc3c17"} |
| FindByID |  |  |  |  |  |  | currencies._acl._hash | string | 654d337e0e912edaa00dbb0fb3dc3c17 |
| FindByID |  |  |  |  |  |  | currencies._acl.fields | array | [] |
| FindByID |  |  |  |  |  |  | currencies.id | string | -99 |
| FindByID |  |  |  |  |  |  | currencies.name | string |  |
| FindByID |  |  |  |  |  |  | currencies.symbol | string |  |
| FindByID |  |  |  |  |  |  | currency_symbol | string |  |
| FindByID |  |  |  |  |  |  | denorm_account_name | string | RRR Advertising Inc. |
| FindByID |  |  |  |  |  |  | discover_data_c | boolean | True |
| FindByID |  |  |  |  |  |  | dri_workflow_template_id | string |  |
| FindByID |  |  |  |  |  |  | dri_workflow_template_link | object | {"name": "", "id": "", "_acl": {"fields": [], "_hash": "654d337e0e912edaa00dbb0fb3dc3c17"}} |
| FindByID |  |  |  |  |  |  | dri_workflow_template_link._acl | object | {"fields": [], "_hash": "654d337e0e912edaa00dbb0fb3dc3c17"} |
| FindByID |  |  |  |  |  |  | dri_workflow_template_link._acl._hash | string | 654d337e0e912edaa00dbb0fb3dc3c17 |
| FindByID |  |  |  |  |  |  | dri_workflow_template_link._acl.fields | array | [] |
| FindByID |  |  |  |  |  |  | dri_workflow_template_link.id | string |  |
| FindByID |  |  |  |  |  |  | dri_workflow_template_link.name | string |  |
| FindByID |  |  |  |  |  |  | dri_workflow_template_name | string |  |
| FindByID |  |  |  |  |  |  | locked_fields | array | [] |
| FindByID |  |  |  |  |  |  | modified_by_name | string | Jen Smith |
| FindByID |  |  |  |  |  |  | modified_user_link | object | {"full_name": "Jen Smith", "id": "1", "_acl": {"fields": [], "_hash": "654d337e0e912edaa00dbb0fb3dc3c17"}} |
| FindByID |  |  |  |  |  |  | modified_user_link._acl | object | {"fields": [], "_hash": "654d337e0e912edaa00dbb0fb3dc3c17"} |
| FindByID |  |  |  |  |  |  | modified_user_link._acl._hash | string | 654d337e0e912edaa00dbb0fb3dc3c17 |
| FindByID |  |  |  |  |  |  | modified_user_link._acl.fields | array | [] |
| FindByID |  |  |  |  |  |  | modified_user_link.full_name | string | Jen Smith |
| FindByID |  |  |  |  |  |  | modified_user_link.id | string | 1 |
| FindByID |  |  |  |  |  |  | perform_sugar_action | boolean | False |
| FindByID |  |  |  |  |  |  | renewal_parent | object | {"name": "", "id": "", "_acl": {"fields": [], "_hash": "654d337e0e912edaa00dbb0fb3dc3c17"}} |
| FindByID |  |  |  |  |  |  | renewal_parent._acl | object | {"fields": [], "_hash": "654d337e0e912edaa00dbb0fb3dc3c17"} |
| FindByID |  |  |  |  |  |  | renewal_parent._acl._hash | string | 654d337e0e912edaa00dbb0fb3dc3c17 |
| FindByID |  |  |  |  |  |  | renewal_parent._acl.fields | array | [] |
| FindByID |  |  |  |  |  |  | renewal_parent.id | string |  |
| FindByID |  |  |  |  |  |  | renewal_parent.name | string |  |
| FindByID |  |  |  |  |  |  | team_count_link | object | {"team_count": "", "id": "1", "_acl": {"fields": [], "_hash": "654d337e0e912edaa00dbb0fb3dc3c17"}} |
| FindByID |  |  |  |  |  |  | team_count_link._acl | object | {"fields": [], "_hash": "654d337e0e912edaa00dbb0fb3dc3c17"} |
| FindByID |  |  |  |  |  |  | team_count_link._acl._hash | string | 654d337e0e912edaa00dbb0fb3dc3c17 |
| FindByID |  |  |  |  |  |  | team_count_link._acl.fields | array | [] |
| FindByID |  |  |  |  |  |  | team_count_link.id | string | 1 |
| FindByID |  |  |  |  |  |  | team_count_link.team_count | string |  |

## Accounts

| Diff | Entity Schema Title | Schema Field ID | Entity Schema Types | Readonly | Possible Values | Reference Collection | FindByID Field ID | Find By ID Types | Value |
|------|---------------------|-----------------|---------------------|----------|-----------------|----------------------|-------------------|------------------|-------|
|  |  | account_type | string | false |  |  | account_type | string | Customer |
|  |  | annual_revenue | integer | false |  |  | annual_revenue | string | > $10,000,000,000 |
|  |  | assigned_user_id | string | false |  | users | assigned_user_id | string | seed_chris_id |
|  |  | billing_address_city | string | false |  |  | billing_address_city | string | Orlando |
|  |  | billing_address_country | string | false |  |  | billing_address_country | string | USA |
|  |  | billing_address_postalcode | string | false |  |  | billing_address_postalcode | string | 32806 |
|  |  | billing_address_state | string | false |  |  | billing_address_state | string | Florida |
|  |  | billing_address_street | string | false |  |  | billing_address_street | string | 481 Ontario Ave |
|  |  | billing_address_street_2 | string | false |  |  | billing_address_street_2 | string |  |
|  |  | billing_address_street_3 | string | false |  |  | billing_address_street_3 | string |  |
|  |  | billing_address_street_4 | string | false |  |  | billing_address_street_4 | string |  |
|  |  | business_center_id | string | false |  |  | business_center_id | string | 4a40f8aa-8831-11e9-9e1a-069335ab1e28 |
|  |  | campaign_id | string | false |  |  | campaign_id | string |  |
|  |  | created_by | string | false |  |  | created_by | string | 1 |
|  |  | date_entered | string | false |  |  | date_entered | string | 2025-05-14T19:07:59+05:00 |
|  |  | date_modified | string | false |  |  | date_modified | string | 2025-05-14T19:48:35+05:00 |
|  |  | deleted | boolean | false |  |  | deleted | boolean | False |
|  |  | description | string | false |  |  | description | string | This potential customer is a referral from ABC Bank (Judy Smith). |
|  |  | duns_num | string | false |  |  | duns_num | string | 952100852 |
|  |  | email | array | false |  |  | email | array | [{"email_address": "contact@insightmarketinginc.com", "invalid_email": false, "opt_out": false, "email_address_id": "d76efbec-30cc-11f0-b385-99f7c3e06566", "primary_address": true, "reply_to_address": false}] |
|  |  | email1 | string | false |  |  | email1 | string | contact@insightmarketinginc.com |
|  |  | email2 | string | false |  |  | email2 | string |  |
|  |  | email[] | object | false |  |  | email[] | object | {"email_address": "contact@insightmarketinginc.com", "invalid_email": false, "opt_out": false, "email_address_id": "d76efbec-30cc-11f0-b385-99f7c3e06566", "primary_address": true, "reply_to_address": false} |
|  |  | email[].email_address | string | false |  |  | email[].email_address | string | contact@insightmarketinginc.com |
|  |  | email[].email_address_id | string | false |  |  | email[].email_address_id | string | d76efbec-30cc-11f0-b385-99f7c3e06566 |
|  |  | email[].invalid_email | boolean | false |  |  | email[].invalid_email | boolean | False |
|  |  | email[].opt_out | boolean | false |  |  | email[].opt_out | boolean | False |
|  |  | email[].primary_address | boolean | false |  |  | email[].primary_address | boolean | True |
|  |  | email[].reply_to_address | boolean | false |  |  | email[].reply_to_address | boolean | False |
|  |  | email_opt_out | boolean | false |  |  | email_opt_out | boolean | False |
|  |  | employees | integer | false |  |  | employees | string | >10,000 |
|  |  | facebook | string | false |  |  | facebook | string |  |
|  |  | following | boolean | false |  |  | following | boolean | False |
|  |  | geocode_status | string | false |  |  | geocode_status | string |  |
|  |  | googleplus | string | false |  |  | googleplus | string |  |
|  |  | id | string | true |  |  | id | string | d76d391a-30cc-11f0-a99c-1d1bbea39a2d |
|  |  | industry | string | false |  |  | industry | string | Utilities |
|  |  | invalid_email | boolean | false |  |  | invalid_email | boolean | False |
|  |  | is_escalated | boolean | false |  |  | is_escalated | boolean | False |
|  |  | latitude_c | string | false |  |  | latitude_c | string | 28.5021966 |
|  |  | longitude_c | string | false |  |  | longitude_c | string | -81.355642 |
|  |  | modified_user_id | string | false |  |  | modified_user_id | string | 1 |
|  |  | my_favorite | boolean | false |  |  | my_favorite | boolean | False |
|  |  | *name | string | false |  |  | name | string | Insight Marketing Inc |
|  |  | next_renewal_date | string | false |  |  | next_renewal_date | string | 2024-07-10 |
|  |  | ownership | string | false |  |  | ownership | string | Bronnbaum Technologies |
|  |  | parent_id | string | false |  |  | parent_id | string |  |
|  |  | parent_name | string | false |  |  | parent_name | string |  |
|  |  | phone_alternate | string | false |  |  | phone_alternate | string | +1 - 573 - 583 - 6446 |
|  |  | phone_fax | string | false |  |  | phone_fax | string | +1 - 694 - 135 - 3012 |
|  |  | phone_office | string | false |  |  | phone_office | string | +1 - 672 - 854 - 9798 |
|  |  | rating | string | false |  |  | rating | string | 5 |
|  |  | service_level | string | false |  |  | service_level | string | T4 |
|  |  | shipping_address_city | string | false |  |  | shipping_address_city | string | Orlando |
|  |  | shipping_address_country | string | false |  |  | shipping_address_country | string | USA |
|  |  | shipping_address_postalcode | string | false |  |  | shipping_address_postalcode | string | 32806 |
|  |  | shipping_address_state | string | false |  |  | shipping_address_state | string | Florida |
|  |  | shipping_address_street | string | false |  |  | shipping_address_street | string | 481 Ontario Ave |
|  |  | shipping_address_street_2 | string | false |  |  | shipping_address_street_2 | string |  |
|  |  | shipping_address_street_3 | string | false |  |  | shipping_address_street_3 | string |  |
|  |  | shipping_address_street_4 | string | false |  |  | shipping_address_street_4 | string |  |
|  |  | sic_code | string | false |  |  | sic_code | string | 76451 |
|  |  | tag | array | false |  |  | tag | array | [] |
|  |  | team_count | string | false |  |  | team_count | string |  |
|  |  | ticker_symbol | string | false |  |  | ticker_symbol | string | BFC |
|  |  | twitter | string | false |  |  | twitter | string | insight |
|  |  | website | string | false |  |  | website | string | http://www.insightmarketinginc.com |
| Schema |  | <span style='color:red'>***teams***</span> | array | false |  |  |  |  |  |
| FindByID |  |  |  |  |  |  | _acl | object | {"fields": {}} |
| FindByID |  |  |  |  |  |  | _acl.fields | object | {} |
| FindByID |  |  |  |  |  |  | _module | string | Accounts |
| FindByID |  |  |  |  |  |  | assigned_user_link | object | {"full_name": "Chris Olliver", "id": "seed_chris_id", "_acl": {"fields": [], "_hash": "654d337e0e912edaa00dbb0fb3dc3c17"}} |
| FindByID |  |  |  |  |  |  | assigned_user_link._acl | object | {"fields": [], "_hash": "654d337e0e912edaa00dbb0fb3dc3c17"} |
| FindByID |  |  |  |  |  |  | assigned_user_link._acl._hash | string | 654d337e0e912edaa00dbb0fb3dc3c17 |
| FindByID |  |  |  |  |  |  | assigned_user_link._acl.fields | array | [] |
| FindByID |  |  |  |  |  |  | assigned_user_link.full_name | string | Chris Olliver |
| FindByID |  |  |  |  |  |  | assigned_user_link.id | string | seed_chris_id |
| FindByID |  |  |  |  |  |  | assigned_user_name | string | Chris Olliver |
| FindByID |  |  |  |  |  |  | business_center_name | string | EMEA Business Center |
| FindByID |  |  |  |  |  |  | business_centers | object | {"name": "EMEA Business Center", "id": "4a40f8aa-8831-11e9-9e1a-069335ab1e28", "_acl": {"fields": [], "_hash": "654d337e0e912edaa00dbb0fb3dc3c17"}} |
| FindByID |  |  |  |  |  |  | business_centers._acl | object | {"fields": [], "_hash": "654d337e0e912edaa00dbb0fb3dc3c17"} |
| FindByID |  |  |  |  |  |  | business_centers._acl._hash | string | 654d337e0e912edaa00dbb0fb3dc3c17 |
| FindByID |  |  |  |  |  |  | business_centers._acl.fields | array | [] |
| FindByID |  |  |  |  |  |  | business_centers.id | string | 4a40f8aa-8831-11e9-9e1a-069335ab1e28 |
| FindByID |  |  |  |  |  |  | business_centers.name | string | EMEA Business Center |
| FindByID |  |  |  |  |  |  | campaign_accounts | object | {"name": "", "id": "", "_acl": {"fields": {"peoplewhoopened": {"create": "no", "write": "no", "license": "no"}, "peoplewhoclicked": {"create": "no", "write": "no", "license": "no"}, "bounced": {"create": "no", "write": "no", "license": "no"}, "notreported": {"create": "no", "write": "no", "license": "no"}, "delivered": {"create": "no", "write": "no", "license": "no"}, "social": {"create": "no", "write": "no", "license": "no"}, "sent": {"create": "no", "write": "no", "license": "no"}, "postdate": {"create": "no", "write": "no", "license": "no"}, "forwards": {"create": "no", "write": "no", "license": "no"}, "unopened": {"create": "no", "write": "no", "license": "no"}, "unsubscribed": {"create": "no", "write": "no", "license": "no"}, "totalopens": {"create": "no", "write": "no", "license": "no"}, "totalclicks": {"create": "no", "write": "no", "license": "no"}}, "_hash": "ea0dd9a7291770652f6587c8f1f4e1f9"}} |
| FindByID |  |  |  |  |  |  | campaign_accounts._acl | object | {"fields": {"peoplewhoopened": {"create": "no", "write": "no", "license": "no"}, "peoplewhoclicked": {"create": "no", "write": "no", "license": "no"}, "bounced": {"create": "no", "write": "no", "license": "no"}, "notreported": {"create": "no", "write": "no", "license": "no"}, "delivered": {"create": "no", "write": "no", "license": "no"}, "social": {"create": "no", "write": "no", "license": "no"}, "sent": {"create": "no", "write": "no", "license": "no"}, "postdate": {"create": "no", "write": "no", "license": "no"}, "forwards": {"create": "no", "write": "no", "license": "no"}, "unopened": {"create": "no", "write": "no", "license": "no"}, "unsubscribed": {"create": "no", "write": "no", "license": "no"}, "totalopens": {"create": "no", "write": "no", "license": "no"}, "totalclicks": {"create": "no", "write": "no", "license": "no"}}, "_hash": "ea0dd9a7291770652f6587c8f1f4e1f9"} |
| FindByID |  |  |  |  |  |  | campaign_accounts._acl._hash | string | ea0dd9a7291770652f6587c8f1f4e1f9 |
| FindByID |  |  |  |  |  |  | campaign_accounts._acl.fields | object | {"peoplewhoopened": {"create": "no", "write": "no", "license": "no"}, "peoplewhoclicked": {"create": "no", "write": "no", "license": "no"}, "bounced": {"create": "no", "write": "no", "license": "no"}, "notreported": {"create": "no", "write": "no", "license": "no"}, "delivered": {"create": "no", "write": "no", "license": "no"}, "social": {"create": "no", "write": "no", "license": "no"}, "sent": {"create": "no", "write": "no", "license": "no"}, "postdate": {"create": "no", "write": "no", "license": "no"}, "forwards": {"create": "no", "write": "no", "license": "no"}, "unopened": {"create": "no", "write": "no", "license": "no"}, "unsubscribed": {"create": "no", "write": "no", "license": "no"}, "totalopens": {"create": "no", "write": "no", "license": "no"}, "totalclicks": {"create": "no", "write": "no", "license": "no"}} |
| FindByID |  |  |  |  |  |  | campaign_accounts._acl.fields.bounced | object | {"create": "no", "write": "no", "license": "no"} |
| FindByID |  |  |  |  |  |  | campaign_accounts._acl.fields.bounced.create | string | no |
| FindByID |  |  |  |  |  |  | campaign_accounts._acl.fields.bounced.license | string | no |
| FindByID |  |  |  |  |  |  | campaign_accounts._acl.fields.bounced.write | string | no |
| FindByID |  |  |  |  |  |  | campaign_accounts._acl.fields.delivered | object | {"create": "no", "write": "no", "license": "no"} |
| FindByID |  |  |  |  |  |  | campaign_accounts._acl.fields.delivered.create | string | no |
| FindByID |  |  |  |  |  |  | campaign_accounts._acl.fields.delivered.license | string | no |
| FindByID |  |  |  |  |  |  | campaign_accounts._acl.fields.delivered.write | string | no |
| FindByID |  |  |  |  |  |  | campaign_accounts._acl.fields.forwards | object | {"create": "no", "write": "no", "license": "no"} |
| FindByID |  |  |  |  |  |  | campaign_accounts._acl.fields.forwards.create | string | no |
| FindByID |  |  |  |  |  |  | campaign_accounts._acl.fields.forwards.license | string | no |
| FindByID |  |  |  |  |  |  | campaign_accounts._acl.fields.forwards.write | string | no |
| FindByID |  |  |  |  |  |  | campaign_accounts._acl.fields.notreported | object | {"create": "no", "write": "no", "license": "no"} |
| FindByID |  |  |  |  |  |  | campaign_accounts._acl.fields.notreported.create | string | no |
| FindByID |  |  |  |  |  |  | campaign_accounts._acl.fields.notreported.license | string | no |
| FindByID |  |  |  |  |  |  | campaign_accounts._acl.fields.notreported.write | string | no |
| FindByID |  |  |  |  |  |  | campaign_accounts._acl.fields.peoplewhoclicked | object | {"create": "no", "write": "no", "license": "no"} |
| FindByID |  |  |  |  |  |  | campaign_accounts._acl.fields.peoplewhoclicked.create | string | no |
| FindByID |  |  |  |  |  |  | campaign_accounts._acl.fields.peoplewhoclicked.license | string | no |
| FindByID |  |  |  |  |  |  | campaign_accounts._acl.fields.peoplewhoclicked.write | string | no |
| FindByID |  |  |  |  |  |  | campaign_accounts._acl.fields.peoplewhoopened | object | {"create": "no", "write": "no", "license": "no"} |
| FindByID |  |  |  |  |  |  | campaign_accounts._acl.fields.peoplewhoopened.create | string | no |
| FindByID |  |  |  |  |  |  | campaign_accounts._acl.fields.peoplewhoopened.license | string | no |
| FindByID |  |  |  |  |  |  | campaign_accounts._acl.fields.peoplewhoopened.write | string | no |
| FindByID |  |  |  |  |  |  | campaign_accounts._acl.fields.postdate | object | {"create": "no", "write": "no", "license": "no"} |
| FindByID |  |  |  |  |  |  | campaign_accounts._acl.fields.postdate.create | string | no |
| FindByID |  |  |  |  |  |  | campaign_accounts._acl.fields.postdate.license | string | no |
| FindByID |  |  |  |  |  |  | campaign_accounts._acl.fields.postdate.write | string | no |
| FindByID |  |  |  |  |  |  | campaign_accounts._acl.fields.sent | object | {"create": "no", "write": "no", "license": "no"} |
| FindByID |  |  |  |  |  |  | campaign_accounts._acl.fields.sent.create | string | no |
| FindByID |  |  |  |  |  |  | campaign_accounts._acl.fields.sent.license | string | no |
| FindByID |  |  |  |  |  |  | campaign_accounts._acl.fields.sent.write | string | no |
| FindByID |  |  |  |  |  |  | campaign_accounts._acl.fields.social | object | {"create": "no", "write": "no", "license": "no"} |
| FindByID |  |  |  |  |  |  | campaign_accounts._acl.fields.social.create | string | no |
| FindByID |  |  |  |  |  |  | campaign_accounts._acl.fields.social.license | string | no |
| FindByID |  |  |  |  |  |  | campaign_accounts._acl.fields.social.write | string | no |
| FindByID |  |  |  |  |  |  | campaign_accounts._acl.fields.totalclicks | object | {"create": "no", "write": "no", "license": "no"} |
| FindByID |  |  |  |  |  |  | campaign_accounts._acl.fields.totalclicks.create | string | no |
| FindByID |  |  |  |  |  |  | campaign_accounts._acl.fields.totalclicks.license | string | no |
| FindByID |  |  |  |  |  |  | campaign_accounts._acl.fields.totalclicks.write | string | no |
| FindByID |  |  |  |  |  |  | campaign_accounts._acl.fields.totalopens | object | {"create": "no", "write": "no", "license": "no"} |
| FindByID |  |  |  |  |  |  | campaign_accounts._acl.fields.totalopens.create | string | no |
| FindByID |  |  |  |  |  |  | campaign_accounts._acl.fields.totalopens.license | string | no |
| FindByID |  |  |  |  |  |  | campaign_accounts._acl.fields.totalopens.write | string | no |
| FindByID |  |  |  |  |  |  | campaign_accounts._acl.fields.unopened | object | {"create": "no", "write": "no", "license": "no"} |
| FindByID |  |  |  |  |  |  | campaign_accounts._acl.fields.unopened.create | string | no |
| FindByID |  |  |  |  |  |  | campaign_accounts._acl.fields.unopened.license | string | no |
| FindByID |  |  |  |  |  |  | campaign_accounts._acl.fields.unopened.write | string | no |
| FindByID |  |  |  |  |  |  | campaign_accounts._acl.fields.unsubscribed | object | {"create": "no", "write": "no", "license": "no"} |
| FindByID |  |  |  |  |  |  | campaign_accounts._acl.fields.unsubscribed.create | string | no |
| FindByID |  |  |  |  |  |  | campaign_accounts._acl.fields.unsubscribed.license | string | no |
| FindByID |  |  |  |  |  |  | campaign_accounts._acl.fields.unsubscribed.write | string | no |
| FindByID |  |  |  |  |  |  | campaign_accounts.id | string |  |
| FindByID |  |  |  |  |  |  | campaign_accounts.name | string |  |
| FindByID |  |  |  |  |  |  | campaign_name | string |  |
| FindByID |  |  |  |  |  |  | created_by_link | object | {"full_name": "Jen Smith", "id": "1", "_acl": {"fields": [], "_hash": "654d337e0e912edaa00dbb0fb3dc3c17"}} |
| FindByID |  |  |  |  |  |  | created_by_link._acl | object | {"fields": [], "_hash": "654d337e0e912edaa00dbb0fb3dc3c17"} |
| FindByID |  |  |  |  |  |  | created_by_link._acl._hash | string | 654d337e0e912edaa00dbb0fb3dc3c17 |
| FindByID |  |  |  |  |  |  | created_by_link._acl.fields | array | [] |
| FindByID |  |  |  |  |  |  | created_by_link.full_name | string | Jen Smith |
| FindByID |  |  |  |  |  |  | created_by_link.id | string | 1 |
| FindByID |  |  |  |  |  |  | created_by_name | string | Jen Smith |
| FindByID |  |  |  |  |  |  | dri_workflow_template_id | string |  |
| FindByID |  |  |  |  |  |  | dri_workflow_template_link | object | {"name": "", "id": "", "_acl": {"fields": [], "_hash": "654d337e0e912edaa00dbb0fb3dc3c17"}} |
| FindByID |  |  |  |  |  |  | dri_workflow_template_link._acl | object | {"fields": [], "_hash": "654d337e0e912edaa00dbb0fb3dc3c17"} |
| FindByID |  |  |  |  |  |  | dri_workflow_template_link._acl._hash | string | 654d337e0e912edaa00dbb0fb3dc3c17 |
| FindByID |  |  |  |  |  |  | dri_workflow_template_link._acl.fields | array | [] |
| FindByID |  |  |  |  |  |  | dri_workflow_template_link.id | string |  |
| FindByID |  |  |  |  |  |  | dri_workflow_template_link.name | string |  |
| FindByID |  |  |  |  |  |  | dri_workflow_template_name | string |  |
| FindByID |  |  |  |  |  |  | email_addresses_non_primary | string |  |
| FindByID |  |  |  |  |  |  | hint_account_facebook_handle | string |  |
| FindByID |  |  |  |  |  |  | hint_account_fiscal_year_end | string |  |
| FindByID |  |  |  |  |  |  | hint_account_founded_year | string |  |
| FindByID |  |  |  |  |  |  | hint_account_industry | string |  |
| FindByID |  |  |  |  |  |  | hint_account_industry_tags | string |  |
| FindByID |  |  |  |  |  |  | hint_account_location | string |  |
| FindByID |  |  |  |  |  |  | hint_account_logo | string |  |
| FindByID |  |  |  |  |  |  | hint_account_naics_code_lbl | string |  |
| FindByID |  |  |  |  |  |  | hint_account_pic | string |  |
| FindByID |  |  |  |  |  |  | hint_account_size | string |  |
| FindByID |  |  |  |  |  |  | last_interaction_date | string | 2025-04-04T16:30:00+05:00 |
| FindByID |  |  |  |  |  |  | last_interaction_parent_id | string | f68f9e40-30cd-11f0-b5df-f34e281fb0c4 |
| FindByID |  |  |  |  |  |  | last_interaction_parent_name | string | Contract detail review |
| FindByID |  |  |  |  |  |  | last_interaction_parent_type | string | Calls |
| FindByID |  |  |  |  |  |  | locked_fields | array | [] |
| FindByID |  |  |  |  |  |  | member_of | object | {"name": "", "id": "", "_acl": {"fields": [], "_hash": "654d337e0e912edaa00dbb0fb3dc3c17"}} |
| FindByID |  |  |  |  |  |  | member_of._acl | object | {"fields": [], "_hash": "654d337e0e912edaa00dbb0fb3dc3c17"} |
| FindByID |  |  |  |  |  |  | member_of._acl._hash | string | 654d337e0e912edaa00dbb0fb3dc3c17 |
| FindByID |  |  |  |  |  |  | member_of._acl.fields | array | [] |
| FindByID |  |  |  |  |  |  | member_of.id | string |  |
| FindByID |  |  |  |  |  |  | member_of.name | string |  |
| FindByID |  |  |  |  |  |  | modified_by_name | string | Jen Smith |
| FindByID |  |  |  |  |  |  | modified_user_link | object | {"full_name": "Jen Smith", "id": "1", "_acl": {"fields": [], "_hash": "654d337e0e912edaa00dbb0fb3dc3c17"}} |
| FindByID |  |  |  |  |  |  | modified_user_link._acl | object | {"fields": [], "_hash": "654d337e0e912edaa00dbb0fb3dc3c17"} |
| FindByID |  |  |  |  |  |  | modified_user_link._acl._hash | string | 654d337e0e912edaa00dbb0fb3dc3c17 |
| FindByID |  |  |  |  |  |  | modified_user_link._acl.fields | array | [] |
| FindByID |  |  |  |  |  |  | modified_user_link.full_name | string | Jen Smith |
| FindByID |  |  |  |  |  |  | modified_user_link.id | string | 1 |
| FindByID |  |  |  |  |  |  | perform_sugar_action | boolean | False |
| FindByID |  |  |  |  |  |  | sync_key | string |  |
| FindByID |  |  |  |  |  |  | team_count_link | object | {"team_count": "", "id": "1", "_acl": {"fields": [], "_hash": "654d337e0e912edaa00dbb0fb3dc3c17"}} |
| FindByID |  |  |  |  |  |  | team_count_link._acl | object | {"fields": [], "_hash": "654d337e0e912edaa00dbb0fb3dc3c17"} |
| FindByID |  |  |  |  |  |  | team_count_link._acl._hash | string | 654d337e0e912edaa00dbb0fb3dc3c17 |
| FindByID |  |  |  |  |  |  | team_count_link._acl.fields | array | [] |
| FindByID |  |  |  |  |  |  | team_count_link.id | string | 1 |
| FindByID |  |  |  |  |  |  | team_count_link.team_count | string |  |
| FindByID |  |  |  |  |  |  | team_name | array | [{"id": "1", "name": "Global", "name_2": "", "primary": true, "selected": false}] |
| FindByID |  |  |  |  |  |  | team_name[] | object | {"id": "1", "name": "Global", "name_2": "", "primary": true, "selected": false} |
| FindByID |  |  |  |  |  |  | team_name[].id | string | 1 |
| FindByID |  |  |  |  |  |  | team_name[].name | string | Global |
| FindByID |  |  |  |  |  |  | team_name[].name_2 | string |  |
| FindByID |  |  |  |  |  |  | team_name[].primary | boolean | True |
| FindByID |  |  |  |  |  |  | team_name[].selected | boolean | False |
| FindByID |  |  |  |  |  |  | widget_next_renewal_date | string |  |

## Contacts

| Diff | Entity Schema Title | Schema Field ID | Entity Schema Types | Readonly | Possible Values | Reference Collection | FindByID Field ID | Find By ID Types | Value |
|------|---------------------|-----------------|---------------------|----------|-----------------|----------------------|-------------------|------------------|-------|
|  |  | accept_status_id | string | false |  |  | accept_status_id | string |  |
|  |  | accept_status_name | string | false |  |  | accept_status_name | string |  |
|  |  | account_id | string | false |  | accounts | account_id | string | d8132546-30cc-11f0-8a5f-b7c7c1b99788 |
|  |  | alt_address_city | string | false |  |  | alt_address_city | string | San Francisco |
|  |  | alt_address_country | string | false |  |  | alt_address_country | string | USA |
|  |  | alt_address_postalcode | string | false |  |  | alt_address_postalcode | string | 94110 |
|  |  | alt_address_state | string | false |  |  | alt_address_state | string | California |
|  |  | alt_address_street | string | false |  |  | alt_address_street | string | 763 Guerrero St |
|  |  | alt_address_street_2 | string | false |  |  | alt_address_street_2 | string |  |
|  |  | alt_address_street_3 | string | false |  |  | alt_address_street_3 | string |  |
|  |  | assigned_user_id | string | false |  | users | assigned_user_id | string | seed_chris_id |
|  |  | assistant | string | false |  |  | assistant | string |  |
|  |  | assistant_phone | string | false |  |  | assistant_phone | string |  |
|  |  | birthdate | string | false |  |  | birthdate | string |  |
|  |  | calls | object | false |  |  | calls | object | {"id": ""} |
|  |  | calls.id | string | false |  |  | calls.id | string |  |
|  |  | campaign_id | string | false |  |  | campaign_id | string |  |
|  |  | created_by | string | false |  | users | created_by | string | 1 |
|  |  | date_entered | string | false |  |  | date_entered | string | 2025-05-14T19:25:56+05:00 |
|  |  | date_modified | string | false |  |  | date_modified | string | 2025-05-14T19:47:40+05:00 |
|  |  | deleted | boolean | false |  |  | deleted | boolean | False |
|  |  | department | string | false |  |  | department | string | Sales |
|  |  | description | string | false |  |  | description | string |  |
|  |  | do_not_call | boolean | false |  |  | do_not_call | boolean | False |
|  |  | email | array | false |  |  | email | array | [{"email_address": "linda.holiday@yahoo.com", "invalid_email": false, "opt_out": false, "email_address_id": "633ec3fa-30d2-11f0-a0c2-8fa31453d866", "primary_address": true, "reply_to_address": false}] |
|  |  | email1 | string | false |  |  | email1 | string | linda.holiday@yahoo.com |
|  |  | email2 | string | false |  |  | email2 | string |  |
|  |  | email[] | object | false |  |  | email[] | object | {"email_address": "linda.holiday@yahoo.com", "invalid_email": false, "opt_out": false, "email_address_id": "633ec3fa-30d2-11f0-a0c2-8fa31453d866", "primary_address": true, "reply_to_address": false} |
|  |  | email[].email_address | string | false |  |  | email[].email_address | string | linda.holiday@yahoo.com |
|  |  | email[].email_address_id | string | false |  |  | email[].email_address_id | string | 633ec3fa-30d2-11f0-a0c2-8fa31453d866 |
|  |  | email[].invalid_email | boolean | false |  |  | email[].invalid_email | boolean | False |
|  |  | email[].opt_out | boolean | false |  |  | email[].opt_out | boolean | False |
|  |  | email[].primary_address | boolean | false |  |  | email[].primary_address | boolean | True |
|  |  | email[].reply_to_address | boolean | false |  |  | email[].reply_to_address | boolean | False |
|  |  | email_opt_out | boolean | false |  |  | email_opt_out | boolean | False |
|  |  | entry_source | string | false |  |  | entry_source | string | internal |
|  |  | facebook | string | false |  |  | facebook | string |  |
|  |  | first_name | string | false |  |  | first_name | string | Linda |
|  |  | following | boolean | false |  |  | following | boolean | False |
|  |  | full_name | string | false |  |  | full_name | string | Linda Holiday |
|  |  | googleplus | string | false |  |  | googleplus | string |  |
|  |  | id | string | true |  |  | id | string | 593db44a-30cf-11f0-8746-4f8477825d38 |
|  |  | invalid_email | boolean | false |  |  | invalid_email | boolean | False |
|  |  | last_name | string | false |  |  | last_name | string | Holiday |
|  |  | latitude_c | string | false |  |  | latitude_c | string | 41.87118 |
|  |  | lead_source | string | false |  |  | lead_source | string | Email |
|  |  | longitude_c | string | false |  |  | longitude_c | string | -87.7055352 |
|  |  | market_interest_prediction_score | string | false |  |  | market_interest_prediction_score | string |  |
|  |  | market_score | string | false |  |  | market_score | null | None |
|  |  | meetings | object | false |  |  | meetings | object | {"id": ""} |
|  |  | meetings.id | string | false |  |  | meetings.id | string |  |
|  |  | mkto_sync | boolean | false |  |  | mkto_sync | boolean | False |
|  |  | modified_user_id | string | false |  | users | modified_user_id | string | 1 |
|  |  | my_favorite | boolean | false |  |  | my_favorite | boolean | False |
|  |  | name | string | false |  |  | name | string | Linda Holiday |
|  |  | opportunities | object | false |  |  | opportunities | object | {"id": ""} |
|  |  | opportunities.id | string | false |  |  | opportunities.id | string |  |
|  |  | opportunity_role_id | string | false |  |  | opportunity_role_id | string |  |
|  |  | phone_fax | string | false |  |  | phone_fax | string | +1 - 741 - 478 - 3827 |
|  |  | phone_home | string | false |  |  | phone_home | string | +1 - 236 - 100 - 7476 |
|  |  | phone_mobile | string | false |  |  | phone_mobile | string | +1 - 912 - 574 - 1060 |
|  |  | phone_other | string | false |  |  | phone_other | string |  |
|  |  | phone_work | string | false |  |  | phone_work | string | +1 - 928 - 629 - 8243 |
|  |  | primary_address_city | string | false |  |  | primary_address_city | string | Chicago |
|  |  | primary_address_country | string | false |  |  | primary_address_country | string | USA |
|  |  | primary_address_postalcode | string | false |  |  | primary_address_postalcode | string | 60612 |
|  |  | primary_address_state | string | false |  |  | primary_address_state | string | Illinois |
|  |  | primary_address_street | string | false |  |  | primary_address_street | string | 803 S Kedzie Ave |
|  |  | primary_address_street_2 | string | false |  |  | primary_address_street_2 | string |  |
|  |  | primary_address_street_3 | string | false |  |  | primary_address_street_3 | string |  |
|  |  | reports_to_id | string | false |  | users | reports_to_id | string |  |
|  |  | salutation | string | false |  |  | salutation | string |  |
|  |  | site_user_id | string | false |  |  | site_user_id | string | 4a006b5846ecee03b7e63e4653755dab676aee8d98d15a2eac7ecafd19dd2fee |
|  |  | source_id | string | false |  |  | source_id | string |  |
|  |  | source_meta | string | false |  |  | source_meta | string |  |
|  |  | source_type | string | false |  |  | source_type | string |  |
|  |  | sync_key | string | false |  |  | sync_key | string |  |
|  |  | tag | array | false |  |  | tag | array | [{"id": "d93687a6-30cc-11f0-8530-69003c7f6309", "name": "goto data", "tags__name_lower": "goto data"}] |
|  |  | tag[] | object | false |  |  | tag[] | object | {"id": "d93687a6-30cc-11f0-8530-69003c7f6309", "name": "goto data", "tags__name_lower": "goto data"} |
|  |  | tag[].id | string | false |  |  | tag[].id | string | d93687a6-30cc-11f0-8530-69003c7f6309 |
|  |  | tag[].name | string | false |  |  | tag[].name | string | goto data |
|  |  | tag[].tags__name_lower | string | false |  |  | tag[].tags__name_lower | string | goto data |
|  |  | team_count | string | false |  |  | team_count | string |  |
|  |  | title | string | false |  |  | title | string | Senior Sales Associate |
|  |  | twitter | string | false |  |  | twitter | string | LindaHoliday23 |
| Schema |  | <span style='color:red'>***team***</span> | array | false |  |  |  |  |  |
| FindByID |  |  |  |  |  |  | _acl | object | {"fields": {}} |
| FindByID |  |  |  |  |  |  | _acl.fields | object | {} |
| FindByID |  |  |  |  |  |  | _module | string | Contacts |
| FindByID |  |  |  |  |  |  | accept_status_calls | string |  |
| FindByID |  |  |  |  |  |  | accept_status_meetings | string |  |
| FindByID |  |  |  |  |  |  | accept_status_messages | string |  |
| FindByID |  |  |  |  |  |  | account_name | string | Kringle Bell IncKA Tower & Co |
| FindByID |  |  |  |  |  |  | accounts | object | {"name": "Kringle Bell IncKA Tower & Co", "id": "d8132546-30cc-11f0-8a5f-b7c7c1b99788", "_acl": {"fields": [], "_hash": "654d337e0e912edaa00dbb0fb3dc3c17"}} |
| FindByID |  |  |  |  |  |  | accounts._acl | object | {"fields": [], "_hash": "654d337e0e912edaa00dbb0fb3dc3c17"} |
| FindByID |  |  |  |  |  |  | accounts._acl._hash | string | 654d337e0e912edaa00dbb0fb3dc3c17 |
| FindByID |  |  |  |  |  |  | accounts._acl.fields | array | [] |
| FindByID |  |  |  |  |  |  | accounts.id | string | d8132546-30cc-11f0-8a5f-b7c7c1b99788 |
| FindByID |  |  |  |  |  |  | accounts.name | string | Kringle Bell IncKA Tower & Co |
| FindByID |  |  |  |  |  |  | assigned_user_link | object | {"full_name": "Chris Olliver", "id": "seed_chris_id", "_acl": {"fields": [], "_hash": "654d337e0e912edaa00dbb0fb3dc3c17"}} |
| FindByID |  |  |  |  |  |  | assigned_user_link._acl | object | {"fields": [], "_hash": "654d337e0e912edaa00dbb0fb3dc3c17"} |
| FindByID |  |  |  |  |  |  | assigned_user_link._acl._hash | string | 654d337e0e912edaa00dbb0fb3dc3c17 |
| FindByID |  |  |  |  |  |  | assigned_user_link._acl.fields | array | [] |
| FindByID |  |  |  |  |  |  | assigned_user_link.full_name | string | Chris Olliver |
| FindByID |  |  |  |  |  |  | assigned_user_link.id | string | seed_chris_id |
| FindByID |  |  |  |  |  |  | assigned_user_name | string | Chris Olliver |
| FindByID |  |  |  |  |  |  | business_center_id | string | 4a40f8aa-8831-11e9-9e1a-069335ab1e28 |
| FindByID |  |  |  |  |  |  | business_center_name | string | EMEA Business Center |
| FindByID |  |  |  |  |  |  | business_centers | object | {"name": "EMEA Business Center", "id": "4a40f8aa-8831-11e9-9e1a-069335ab1e28", "_acl": {"fields": [], "_hash": "654d337e0e912edaa00dbb0fb3dc3c17"}} |
| FindByID |  |  |  |  |  |  | business_centers._acl | object | {"fields": [], "_hash": "654d337e0e912edaa00dbb0fb3dc3c17"} |
| FindByID |  |  |  |  |  |  | business_centers._acl._hash | string | 654d337e0e912edaa00dbb0fb3dc3c17 |
| FindByID |  |  |  |  |  |  | business_centers._acl.fields | array | [] |
| FindByID |  |  |  |  |  |  | business_centers.id | string | 4a40f8aa-8831-11e9-9e1a-069335ab1e28 |
| FindByID |  |  |  |  |  |  | business_centers.name | string | EMEA Business Center |
| FindByID |  |  |  |  |  |  | c_accept_status_fields | string |  |
| FindByID |  |  |  |  |  |  | campaign_contacts | object | {"name": "", "id": "", "_acl": {"fields": {"peoplewhoopened": {"create": "no", "write": "no", "license": "no"}, "peoplewhoclicked": {"create": "no", "write": "no", "license": "no"}, "bounced": {"create": "no", "write": "no", "license": "no"}, "notreported": {"create": "no", "write": "no", "license": "no"}, "delivered": {"create": "no", "write": "no", "license": "no"}, "social": {"create": "no", "write": "no", "license": "no"}, "sent": {"create": "no", "write": "no", "license": "no"}, "postdate": {"create": "no", "write": "no", "license": "no"}, "forwards": {"create": "no", "write": "no", "license": "no"}, "unopened": {"create": "no", "write": "no", "license": "no"}, "unsubscribed": {"create": "no", "write": "no", "license": "no"}, "totalopens": {"create": "no", "write": "no", "license": "no"}, "totalclicks": {"create": "no", "write": "no", "license": "no"}}, "_hash": "ea0dd9a7291770652f6587c8f1f4e1f9"}} |
| FindByID |  |  |  |  |  |  | campaign_contacts._acl | object | {"fields": {"peoplewhoopened": {"create": "no", "write": "no", "license": "no"}, "peoplewhoclicked": {"create": "no", "write": "no", "license": "no"}, "bounced": {"create": "no", "write": "no", "license": "no"}, "notreported": {"create": "no", "write": "no", "license": "no"}, "delivered": {"create": "no", "write": "no", "license": "no"}, "social": {"create": "no", "write": "no", "license": "no"}, "sent": {"create": "no", "write": "no", "license": "no"}, "postdate": {"create": "no", "write": "no", "license": "no"}, "forwards": {"create": "no", "write": "no", "license": "no"}, "unopened": {"create": "no", "write": "no", "license": "no"}, "unsubscribed": {"create": "no", "write": "no", "license": "no"}, "totalopens": {"create": "no", "write": "no", "license": "no"}, "totalclicks": {"create": "no", "write": "no", "license": "no"}}, "_hash": "ea0dd9a7291770652f6587c8f1f4e1f9"} |
| FindByID |  |  |  |  |  |  | campaign_contacts._acl._hash | string | ea0dd9a7291770652f6587c8f1f4e1f9 |
| FindByID |  |  |  |  |  |  | campaign_contacts._acl.fields | object | {"peoplewhoopened": {"create": "no", "write": "no", "license": "no"}, "peoplewhoclicked": {"create": "no", "write": "no", "license": "no"}, "bounced": {"create": "no", "write": "no", "license": "no"}, "notreported": {"create": "no", "write": "no", "license": "no"}, "delivered": {"create": "no", "write": "no", "license": "no"}, "social": {"create": "no", "write": "no", "license": "no"}, "sent": {"create": "no", "write": "no", "license": "no"}, "postdate": {"create": "no", "write": "no", "license": "no"}, "forwards": {"create": "no", "write": "no", "license": "no"}, "unopened": {"create": "no", "write": "no", "license": "no"}, "unsubscribed": {"create": "no", "write": "no", "license": "no"}, "totalopens": {"create": "no", "write": "no", "license": "no"}, "totalclicks": {"create": "no", "write": "no", "license": "no"}} |
| FindByID |  |  |  |  |  |  | campaign_contacts._acl.fields.bounced | object | {"create": "no", "write": "no", "license": "no"} |
| FindByID |  |  |  |  |  |  | campaign_contacts._acl.fields.bounced.create | string | no |
| FindByID |  |  |  |  |  |  | campaign_contacts._acl.fields.bounced.license | string | no |
| FindByID |  |  |  |  |  |  | campaign_contacts._acl.fields.bounced.write | string | no |
| FindByID |  |  |  |  |  |  | campaign_contacts._acl.fields.delivered | object | {"create": "no", "write": "no", "license": "no"} |
| FindByID |  |  |  |  |  |  | campaign_contacts._acl.fields.delivered.create | string | no |
| FindByID |  |  |  |  |  |  | campaign_contacts._acl.fields.delivered.license | string | no |
| FindByID |  |  |  |  |  |  | campaign_contacts._acl.fields.delivered.write | string | no |
| FindByID |  |  |  |  |  |  | campaign_contacts._acl.fields.forwards | object | {"create": "no", "write": "no", "license": "no"} |
| FindByID |  |  |  |  |  |  | campaign_contacts._acl.fields.forwards.create | string | no |
| FindByID |  |  |  |  |  |  | campaign_contacts._acl.fields.forwards.license | string | no |
| FindByID |  |  |  |  |  |  | campaign_contacts._acl.fields.forwards.write | string | no |
| FindByID |  |  |  |  |  |  | campaign_contacts._acl.fields.notreported | object | {"create": "no", "write": "no", "license": "no"} |
| FindByID |  |  |  |  |  |  | campaign_contacts._acl.fields.notreported.create | string | no |
| FindByID |  |  |  |  |  |  | campaign_contacts._acl.fields.notreported.license | string | no |
| FindByID |  |  |  |  |  |  | campaign_contacts._acl.fields.notreported.write | string | no |
| FindByID |  |  |  |  |  |  | campaign_contacts._acl.fields.peoplewhoclicked | object | {"create": "no", "write": "no", "license": "no"} |
| FindByID |  |  |  |  |  |  | campaign_contacts._acl.fields.peoplewhoclicked.create | string | no |
| FindByID |  |  |  |  |  |  | campaign_contacts._acl.fields.peoplewhoclicked.license | string | no |
| FindByID |  |  |  |  |  |  | campaign_contacts._acl.fields.peoplewhoclicked.write | string | no |
| FindByID |  |  |  |  |  |  | campaign_contacts._acl.fields.peoplewhoopened | object | {"create": "no", "write": "no", "license": "no"} |
| FindByID |  |  |  |  |  |  | campaign_contacts._acl.fields.peoplewhoopened.create | string | no |
| FindByID |  |  |  |  |  |  | campaign_contacts._acl.fields.peoplewhoopened.license | string | no |
| FindByID |  |  |  |  |  |  | campaign_contacts._acl.fields.peoplewhoopened.write | string | no |
| FindByID |  |  |  |  |  |  | campaign_contacts._acl.fields.postdate | object | {"create": "no", "write": "no", "license": "no"} |
| FindByID |  |  |  |  |  |  | campaign_contacts._acl.fields.postdate.create | string | no |
| FindByID |  |  |  |  |  |  | campaign_contacts._acl.fields.postdate.license | string | no |
| FindByID |  |  |  |  |  |  | campaign_contacts._acl.fields.postdate.write | string | no |
| FindByID |  |  |  |  |  |  | campaign_contacts._acl.fields.sent | object | {"create": "no", "write": "no", "license": "no"} |
| FindByID |  |  |  |  |  |  | campaign_contacts._acl.fields.sent.create | string | no |
| FindByID |  |  |  |  |  |  | campaign_contacts._acl.fields.sent.license | string | no |
| FindByID |  |  |  |  |  |  | campaign_contacts._acl.fields.sent.write | string | no |
| FindByID |  |  |  |  |  |  | campaign_contacts._acl.fields.social | object | {"create": "no", "write": "no", "license": "no"} |
| FindByID |  |  |  |  |  |  | campaign_contacts._acl.fields.social.create | string | no |
| FindByID |  |  |  |  |  |  | campaign_contacts._acl.fields.social.license | string | no |
| FindByID |  |  |  |  |  |  | campaign_contacts._acl.fields.social.write | string | no |
| FindByID |  |  |  |  |  |  | campaign_contacts._acl.fields.totalclicks | object | {"create": "no", "write": "no", "license": "no"} |
| FindByID |  |  |  |  |  |  | campaign_contacts._acl.fields.totalclicks.create | string | no |
| FindByID |  |  |  |  |  |  | campaign_contacts._acl.fields.totalclicks.license | string | no |
| FindByID |  |  |  |  |  |  | campaign_contacts._acl.fields.totalclicks.write | string | no |
| FindByID |  |  |  |  |  |  | campaign_contacts._acl.fields.totalopens | object | {"create": "no", "write": "no", "license": "no"} |
| FindByID |  |  |  |  |  |  | campaign_contacts._acl.fields.totalopens.create | string | no |
| FindByID |  |  |  |  |  |  | campaign_contacts._acl.fields.totalopens.license | string | no |
| FindByID |  |  |  |  |  |  | campaign_contacts._acl.fields.totalopens.write | string | no |
| FindByID |  |  |  |  |  |  | campaign_contacts._acl.fields.unopened | object | {"create": "no", "write": "no", "license": "no"} |
| FindByID |  |  |  |  |  |  | campaign_contacts._acl.fields.unopened.create | string | no |
| FindByID |  |  |  |  |  |  | campaign_contacts._acl.fields.unopened.license | string | no |
| FindByID |  |  |  |  |  |  | campaign_contacts._acl.fields.unopened.write | string | no |
| FindByID |  |  |  |  |  |  | campaign_contacts._acl.fields.unsubscribed | object | {"create": "no", "write": "no", "license": "no"} |
| FindByID |  |  |  |  |  |  | campaign_contacts._acl.fields.unsubscribed.create | string | no |
| FindByID |  |  |  |  |  |  | campaign_contacts._acl.fields.unsubscribed.license | string | no |
| FindByID |  |  |  |  |  |  | campaign_contacts._acl.fields.unsubscribed.write | string | no |
| FindByID |  |  |  |  |  |  | campaign_contacts.id | string |  |
| FindByID |  |  |  |  |  |  | campaign_contacts.name | string |  |
| FindByID |  |  |  |  |  |  | campaign_name | string |  |
| FindByID |  |  |  |  |  |  | cookie_consent | boolean | False |
| FindByID |  |  |  |  |  |  | cookie_consent_received_on | string |  |
| FindByID |  |  |  |  |  |  | created_by_link | object | {"full_name": "Jen Smith", "id": "1", "_acl": {"fields": [], "_hash": "654d337e0e912edaa00dbb0fb3dc3c17"}} |
| FindByID |  |  |  |  |  |  | created_by_link._acl | object | {"fields": [], "_hash": "654d337e0e912edaa00dbb0fb3dc3c17"} |
| FindByID |  |  |  |  |  |  | created_by_link._acl._hash | string | 654d337e0e912edaa00dbb0fb3dc3c17 |
| FindByID |  |  |  |  |  |  | created_by_link._acl.fields | array | [] |
| FindByID |  |  |  |  |  |  | created_by_link.full_name | string | Jen Smith |
| FindByID |  |  |  |  |  |  | created_by_link.id | string | 1 |
| FindByID |  |  |  |  |  |  | created_by_name | string | Jen Smith |
| FindByID |  |  |  |  |  |  | denorm_account_name | string | Kringle Bell IncKA Tower & Co |
| FindByID |  |  |  |  |  |  | dnb_principal_id | string | 263865980 |
| FindByID |  |  |  |  |  |  | dp_business_purpose | array | [] |
| FindByID |  |  |  |  |  |  | dp_consent_last_updated | string | 2025-05-14 |
| FindByID |  |  |  |  |  |  | dri_workflow_template_id | string |  |
| FindByID |  |  |  |  |  |  | dri_workflow_template_link | object | {"name": "", "id": "", "_acl": {"fields": [], "_hash": "654d337e0e912edaa00dbb0fb3dc3c17"}} |
| FindByID |  |  |  |  |  |  | dri_workflow_template_link._acl | object | {"fields": [], "_hash": "654d337e0e912edaa00dbb0fb3dc3c17"} |
| FindByID |  |  |  |  |  |  | dri_workflow_template_link._acl._hash | string | 654d337e0e912edaa00dbb0fb3dc3c17 |
| FindByID |  |  |  |  |  |  | dri_workflow_template_link._acl.fields | array | [] |
| FindByID |  |  |  |  |  |  | dri_workflow_template_link.id | string |  |
| FindByID |  |  |  |  |  |  | dri_workflow_template_link.name | string |  |
| FindByID |  |  |  |  |  |  | dri_workflow_template_name | string |  |
| FindByID |  |  |  |  |  |  | email_addresses_non_primary | string |  |
| FindByID |  |  |  |  |  |  | email_and_name1 | string |  |
| FindByID |  |  |  |  |  |  | external_user_id | string |  |
| FindByID |  |  |  |  |  |  | geocode_status | string |  |
| FindByID |  |  |  |  |  |  | hint_account_annual_revenue | string |  |
| FindByID |  |  |  |  |  |  | hint_account_description | string |  |
| FindByID |  |  |  |  |  |  | hint_account_facebook_handle | string |  |
| FindByID |  |  |  |  |  |  | hint_account_fiscal_year_end | string |  |
| FindByID |  |  |  |  |  |  | hint_account_founded_year | string |  |
| FindByID |  |  |  |  |  |  | hint_account_industry | string |  |
| FindByID |  |  |  |  |  |  | hint_account_location | string |  |
| FindByID |  |  |  |  |  |  | hint_account_logo | string |  |
| FindByID |  |  |  |  |  |  | hint_account_naics_code_lbl | string |  |
| FindByID |  |  |  |  |  |  | hint_account_sic_code_label | string |  |
| FindByID |  |  |  |  |  |  | hint_account_size | string |  |
| FindByID |  |  |  |  |  |  | hint_account_twitter_handle | string |  |
| FindByID |  |  |  |  |  |  | hint_account_website | string |  |
| FindByID |  |  |  |  |  |  | hint_contact_pic | string |  |
| FindByID |  |  |  |  |  |  | hint_education | string |  |
| FindByID |  |  |  |  |  |  | hint_education_2 | string |  |
| FindByID |  |  |  |  |  |  | hint_facebook | string |  |
| FindByID |  |  |  |  |  |  | hint_industry_tags | string |  |
| FindByID |  |  |  |  |  |  | hint_job_2 | string |  |
| FindByID |  |  |  |  |  |  | hint_phone_1 | string |  |
| FindByID |  |  |  |  |  |  | hint_phone_2 | string |  |
| FindByID |  |  |  |  |  |  | hint_photo | string |  |
| FindByID |  |  |  |  |  |  | hint_twitter | string |  |
| FindByID |  |  |  |  |  |  | locked_fields | array | [] |
| FindByID |  |  |  |  |  |  | m_accept_status_fields | string |  |
| FindByID |  |  |  |  |  |  | mkto_id | null | None |
| FindByID |  |  |  |  |  |  | mkto_lead_score | string | Email |
| FindByID |  |  |  |  |  |  | modified_by_name | string | Jen Smith |
| FindByID |  |  |  |  |  |  | modified_user_link | object | {"full_name": "Jen Smith", "id": "1", "_acl": {"fields": [], "_hash": "654d337e0e912edaa00dbb0fb3dc3c17"}} |
| FindByID |  |  |  |  |  |  | modified_user_link._acl | object | {"fields": [], "_hash": "654d337e0e912edaa00dbb0fb3dc3c17"} |
| FindByID |  |  |  |  |  |  | modified_user_link._acl._hash | string | 654d337e0e912edaa00dbb0fb3dc3c17 |
| FindByID |  |  |  |  |  |  | modified_user_link._acl.fields | array | [] |
| FindByID |  |  |  |  |  |  | modified_user_link.full_name | string | Jen Smith |
| FindByID |  |  |  |  |  |  | modified_user_link.id | string | 1 |
| FindByID |  |  |  |  |  |  | opportunity_role | string |  |
| FindByID |  |  |  |  |  |  | opportunity_role_fields | string |  |
| FindByID |  |  |  |  |  |  | perform_sugar_action | boolean | False |
| FindByID |  |  |  |  |  |  | picture | string | LindaHoliday1747234061 |
| FindByID |  |  |  |  |  |  | portal_active | boolean | True |
| FindByID |  |  |  |  |  |  | portal_app | string |  |
| FindByID |  |  |  |  |  |  | portal_name | string | LindaHoliday23 |
| FindByID |  |  |  |  |  |  | portal_password | boolean | True |
| FindByID |  |  |  |  |  |  | portal_password1 | null | None |
| FindByID |  |  |  |  |  |  | portal_user_company_name | string |  |
| FindByID |  |  |  |  |  |  | preferred_language | string | en_us |
| FindByID |  |  |  |  |  |  | report_to_name | string |  |
| FindByID |  |  |  |  |  |  | reports_to_link | object | {"name": "", "id": "", "_acl": {"fields": {"sf_lastactivity_default": {"create": "no", "write": "no", "license": "no"}}, "_hash": "c69ded8d08ee4170c5d490bf7c5941d7"}} |
| FindByID |  |  |  |  |  |  | reports_to_link._acl | object | {"fields": {"sf_lastactivity_default": {"create": "no", "write": "no", "license": "no"}}, "_hash": "c69ded8d08ee4170c5d490bf7c5941d7"} |
| FindByID |  |  |  |  |  |  | reports_to_link._acl._hash | string | c69ded8d08ee4170c5d490bf7c5941d7 |
| FindByID |  |  |  |  |  |  | reports_to_link._acl.fields | object | {"sf_lastactivity_default": {"create": "no", "write": "no", "license": "no"}} |
| FindByID |  |  |  |  |  |  | reports_to_link._acl.fields.sf_lastactivity_default | object | {"create": "no", "write": "no", "license": "no"} |
| FindByID |  |  |  |  |  |  | reports_to_link._acl.fields.sf_lastactivity_default.create | string | no |
| FindByID |  |  |  |  |  |  | reports_to_link._acl.fields.sf_lastactivity_default.license | string | no |
| FindByID |  |  |  |  |  |  | reports_to_link._acl.fields.sf_lastactivity_default.write | string | no |
| FindByID |  |  |  |  |  |  | reports_to_link.id | string |  |
| FindByID |  |  |  |  |  |  | reports_to_link.name | string |  |
| FindByID |  |  |  |  |  |  | sync_contact | boolean | False |
| FindByID |  |  |  |  |  |  | team_count_link | object | {"team_count": "", "id": "1", "_acl": {"fields": [], "_hash": "654d337e0e912edaa00dbb0fb3dc3c17"}} |
| FindByID |  |  |  |  |  |  | team_count_link._acl | object | {"fields": [], "_hash": "654d337e0e912edaa00dbb0fb3dc3c17"} |
| FindByID |  |  |  |  |  |  | team_count_link._acl._hash | string | 654d337e0e912edaa00dbb0fb3dc3c17 |
| FindByID |  |  |  |  |  |  | team_count_link._acl.fields | array | [] |
| FindByID |  |  |  |  |  |  | team_count_link.id | string | 1 |
| FindByID |  |  |  |  |  |  | team_count_link.team_count | string |  |
| FindByID |  |  |  |  |  |  | team_name | array | [{"id": "East", "name": "East", "name_2": "", "primary": false, "selected": false}, {"id": "1", "name": "Global", "name_2": "", "primary": true, "selected": false}] |
| FindByID |  |  |  |  |  |  | team_name[] | object | {"id": "East", "name": "East", "name_2": "", "primary": false, "selected": false} |
| FindByID |  |  |  |  |  |  | team_name[].id | string | East |
| FindByID |  |  |  |  |  |  | team_name[].name | string | East |
| FindByID |  |  |  |  |  |  | team_name[].name_2 | string |  |
| FindByID |  |  |  |  |  |  | team_name[].primary | boolean | False |
| FindByID |  |  |  |  |  |  | team_name[].selected | boolean | False |

## Revenuelineitems

| Diff | Entity Schema Title | Schema Field ID | Entity Schema Types | Readonly | Possible Values | Reference Collection | FindByID Field ID | Find By ID Types | Value |
|------|---------------------|-----------------|---------------------|----------|-----------------|----------------------|-------------------|------------------|-------|
|  |  | _acl | object | false |  |  | _acl | object | {"fields": {}} |
|  |  | _acl.fields | object | false |  |  | _acl.fields | object | {} |
|  |  | _module | string | false |  |  | _module | string | RevenueLineItems |
|  |  | account_id | string | false |  |  | account_id | string | d890652e-30cc-11f0-9c5b-31b297db6ffd |
|  |  | account_link | object | false |  |  | account_link | object | {"name": "RRR Advertising Inc.", "id": "d890652e-30cc-11f0-9c5b-31b297db6ffd", "_acl": {"fields": [], "_hash": "654d337e0e912edaa00dbb0fb3dc3c17"}} |
|  |  | account_link._acl | object | false |  |  | account_link._acl | object | {"fields": [], "_hash": "654d337e0e912edaa00dbb0fb3dc3c17"} |
|  |  | account_link._acl._hash | string | false |  |  | account_link._acl._hash | string | 654d337e0e912edaa00dbb0fb3dc3c17 |
|  |  | account_link._acl.fields | array | false |  |  | account_link._acl.fields | array | [] |
|  |  | account_link.id | string | false |  |  | account_link.id | string | d890652e-30cc-11f0-9c5b-31b297db6ffd |
|  |  | account_link.name | string | false |  |  | account_link.name | string | RRR Advertising Inc. |
|  |  | account_name | string | false |  |  | account_name | string | RRR Advertising Inc. |
|  |  | add_on_to_id | string | false |  |  | add_on_to_id | string |  |
|  |  | add_on_to_name | string | false |  |  | add_on_to_name | string |  |
|  |  | asset_number | string | false |  |  | asset_number | string |  |
|  |  | assigned_user_id | string | false |  |  | assigned_user_id | string | seed_will_id |
|  |  | assigned_user_link | object | false |  |  | assigned_user_link | object | {"full_name": "Will Westin", "id": "seed_will_id", "_acl": {"fields": [], "_hash": "654d337e0e912edaa00dbb0fb3dc3c17"}} |
|  |  | assigned_user_link._acl | object | false |  |  | assigned_user_link._acl | object | {"fields": [], "_hash": "654d337e0e912edaa00dbb0fb3dc3c17"} |
|  |  | assigned_user_link._acl._hash | string | false |  |  | assigned_user_link._acl._hash | string | 654d337e0e912edaa00dbb0fb3dc3c17 |
|  |  | assigned_user_link._acl.fields | array | false |  |  | assigned_user_link._acl.fields | array | [] |
|  |  | assigned_user_link.full_name | string | false |  |  | assigned_user_link.full_name | string | Will Westin |
|  |  | assigned_user_link.id | string | false |  |  | assigned_user_link.id | string | seed_will_id |
|  |  | assigned_user_name | string | false |  |  | assigned_user_name | string | Will Westin |
|  |  | base_rate | string | false |  |  | base_rate | string | 1.000000 |
|  |  | best_case | string | false |  |  | best_case | string | 34800.000000 |
|  |  | book_value | string | false |  |  | book_value | string |  |
|  |  | book_value_date | string | false |  |  | book_value_date | string |  |
|  |  | book_value_usdollar | string | false |  |  | book_value_usdollar | string |  |
|  |  | campaign_id | string | false |  |  | campaign_id | string |  |
|  |  | campaign_name | string | false |  |  | campaign_name | string |  |
|  |  | campaign_revenuelineitems | object | false |  |  | campaign_revenuelineitems | object | {"name": "", "id": "", "_acl": {"fields": {"peoplewhoopened": {"create": "no", "write": "no", "license": "no"}, "peoplewhoclicked": {"create": "no", "write": "no", "license": "no"}, "bounced": {"create": "no", "write": "no", "license": "no"}, "notreported": {"create": "no", "write": "no", "license": "no"}, "delivered": {"create": "no", "write": "no", "license": "no"}, "social": {"create": "no", "write": "no", "license": "no"}, "sent": {"create": "no", "write": "no", "license": "no"}, "postdate": {"create": "no", "write": "no", "license": "no"}, "forwards": {"create": "no", "write": "no", "license": "no"}, "unopened": {"create": "no", "write": "no", "license": "no"}, "unsubscribed": {"create": "no", "write": "no", "license": "no"}, "totalopens": {"create": "no", "write": "no", "license": "no"}, "totalclicks": {"create": "no", "write": "no", "license": "no"}}, "_hash": "ea0dd9a7291770652f6587c8f1f4e1f9"}} |
|  |  | campaign_revenuelineitems._acl | object | false |  |  | campaign_revenuelineitems._acl | object | {"fields": {"peoplewhoopened": {"create": "no", "write": "no", "license": "no"}, "peoplewhoclicked": {"create": "no", "write": "no", "license": "no"}, "bounced": {"create": "no", "write": "no", "license": "no"}, "notreported": {"create": "no", "write": "no", "license": "no"}, "delivered": {"create": "no", "write": "no", "license": "no"}, "social": {"create": "no", "write": "no", "license": "no"}, "sent": {"create": "no", "write": "no", "license": "no"}, "postdate": {"create": "no", "write": "no", "license": "no"}, "forwards": {"create": "no", "write": "no", "license": "no"}, "unopened": {"create": "no", "write": "no", "license": "no"}, "unsubscribed": {"create": "no", "write": "no", "license": "no"}, "totalopens": {"create": "no", "write": "no", "license": "no"}, "totalclicks": {"create": "no", "write": "no", "license": "no"}}, "_hash": "ea0dd9a7291770652f6587c8f1f4e1f9"} |
|  |  | campaign_revenuelineitems._acl._hash | string | false |  |  | campaign_revenuelineitems._acl._hash | string | ea0dd9a7291770652f6587c8f1f4e1f9 |
|  |  | campaign_revenuelineitems._acl.fields | object | false |  |  | campaign_revenuelineitems._acl.fields | object | {"peoplewhoopened": {"create": "no", "write": "no", "license": "no"}, "peoplewhoclicked": {"create": "no", "write": "no", "license": "no"}, "bounced": {"create": "no", "write": "no", "license": "no"}, "notreported": {"create": "no", "write": "no", "license": "no"}, "delivered": {"create": "no", "write": "no", "license": "no"}, "social": {"create": "no", "write": "no", "license": "no"}, "sent": {"create": "no", "write": "no", "license": "no"}, "postdate": {"create": "no", "write": "no", "license": "no"}, "forwards": {"create": "no", "write": "no", "license": "no"}, "unopened": {"create": "no", "write": "no", "license": "no"}, "unsubscribed": {"create": "no", "write": "no", "license": "no"}, "totalopens": {"create": "no", "write": "no", "license": "no"}, "totalclicks": {"create": "no", "write": "no", "license": "no"}} |
|  |  | campaign_revenuelineitems._acl.fields.bounced | object | false |  |  | campaign_revenuelineitems._acl.fields.bounced | object | {"create": "no", "write": "no", "license": "no"} |
|  |  | campaign_revenuelineitems._acl.fields.bounced.create | string | false |  |  | campaign_revenuelineitems._acl.fields.bounced.create | string | no |
|  |  | campaign_revenuelineitems._acl.fields.bounced.license | string | false |  |  | campaign_revenuelineitems._acl.fields.bounced.license | string | no |
|  |  | campaign_revenuelineitems._acl.fields.bounced.write | string | false |  |  | campaign_revenuelineitems._acl.fields.bounced.write | string | no |
|  |  | campaign_revenuelineitems._acl.fields.delivered | object | false |  |  | campaign_revenuelineitems._acl.fields.delivered | object | {"create": "no", "write": "no", "license": "no"} |
|  |  | campaign_revenuelineitems._acl.fields.delivered.create | string | false |  |  | campaign_revenuelineitems._acl.fields.delivered.create | string | no |
|  |  | campaign_revenuelineitems._acl.fields.delivered.license | string | false |  |  | campaign_revenuelineitems._acl.fields.delivered.license | string | no |
|  |  | campaign_revenuelineitems._acl.fields.delivered.write | string | false |  |  | campaign_revenuelineitems._acl.fields.delivered.write | string | no |
|  |  | campaign_revenuelineitems._acl.fields.forwards | object | false |  |  | campaign_revenuelineitems._acl.fields.forwards | object | {"create": "no", "write": "no", "license": "no"} |
|  |  | campaign_revenuelineitems._acl.fields.forwards.create | string | false |  |  | campaign_revenuelineitems._acl.fields.forwards.create | string | no |
|  |  | campaign_revenuelineitems._acl.fields.forwards.license | string | false |  |  | campaign_revenuelineitems._acl.fields.forwards.license | string | no |
|  |  | campaign_revenuelineitems._acl.fields.forwards.write | string | false |  |  | campaign_revenuelineitems._acl.fields.forwards.write | string | no |
|  |  | campaign_revenuelineitems._acl.fields.notreported | object | false |  |  | campaign_revenuelineitems._acl.fields.notreported | object | {"create": "no", "write": "no", "license": "no"} |
|  |  | campaign_revenuelineitems._acl.fields.notreported.create | string | false |  |  | campaign_revenuelineitems._acl.fields.notreported.create | string | no |
|  |  | campaign_revenuelineitems._acl.fields.notreported.license | string | false |  |  | campaign_revenuelineitems._acl.fields.notreported.license | string | no |
|  |  | campaign_revenuelineitems._acl.fields.notreported.write | string | false |  |  | campaign_revenuelineitems._acl.fields.notreported.write | string | no |
|  |  | campaign_revenuelineitems._acl.fields.peoplewhoclicked | object | false |  |  | campaign_revenuelineitems._acl.fields.peoplewhoclicked | object | {"create": "no", "write": "no", "license": "no"} |
|  |  | campaign_revenuelineitems._acl.fields.peoplewhoclicked.create | string | false |  |  | campaign_revenuelineitems._acl.fields.peoplewhoclicked.create | string | no |
|  |  | campaign_revenuelineitems._acl.fields.peoplewhoclicked.license | string | false |  |  | campaign_revenuelineitems._acl.fields.peoplewhoclicked.license | string | no |
|  |  | campaign_revenuelineitems._acl.fields.peoplewhoclicked.write | string | false |  |  | campaign_revenuelineitems._acl.fields.peoplewhoclicked.write | string | no |
|  |  | campaign_revenuelineitems._acl.fields.peoplewhoopened | object | false |  |  | campaign_revenuelineitems._acl.fields.peoplewhoopened | object | {"create": "no", "write": "no", "license": "no"} |
|  |  | campaign_revenuelineitems._acl.fields.peoplewhoopened.create | string | false |  |  | campaign_revenuelineitems._acl.fields.peoplewhoopened.create | string | no |
|  |  | campaign_revenuelineitems._acl.fields.peoplewhoopened.license | string | false |  |  | campaign_revenuelineitems._acl.fields.peoplewhoopened.license | string | no |
|  |  | campaign_revenuelineitems._acl.fields.peoplewhoopened.write | string | false |  |  | campaign_revenuelineitems._acl.fields.peoplewhoopened.write | string | no |
|  |  | campaign_revenuelineitems._acl.fields.postdate | object | false |  |  | campaign_revenuelineitems._acl.fields.postdate | object | {"create": "no", "write": "no", "license": "no"} |
|  |  | campaign_revenuelineitems._acl.fields.postdate.create | string | false |  |  | campaign_revenuelineitems._acl.fields.postdate.create | string | no |
|  |  | campaign_revenuelineitems._acl.fields.postdate.license | string | false |  |  | campaign_revenuelineitems._acl.fields.postdate.license | string | no |
|  |  | campaign_revenuelineitems._acl.fields.postdate.write | string | false |  |  | campaign_revenuelineitems._acl.fields.postdate.write | string | no |
|  |  | campaign_revenuelineitems._acl.fields.sent | object | false |  |  | campaign_revenuelineitems._acl.fields.sent | object | {"create": "no", "write": "no", "license": "no"} |
|  |  | campaign_revenuelineitems._acl.fields.sent.create | string | false |  |  | campaign_revenuelineitems._acl.fields.sent.create | string | no |
|  |  | campaign_revenuelineitems._acl.fields.sent.license | string | false |  |  | campaign_revenuelineitems._acl.fields.sent.license | string | no |
|  |  | campaign_revenuelineitems._acl.fields.sent.write | string | false |  |  | campaign_revenuelineitems._acl.fields.sent.write | string | no |
|  |  | campaign_revenuelineitems._acl.fields.social | object | false |  |  | campaign_revenuelineitems._acl.fields.social | object | {"create": "no", "write": "no", "license": "no"} |
|  |  | campaign_revenuelineitems._acl.fields.social.create | string | false |  |  | campaign_revenuelineitems._acl.fields.social.create | string | no |
|  |  | campaign_revenuelineitems._acl.fields.social.license | string | false |  |  | campaign_revenuelineitems._acl.fields.social.license | string | no |
|  |  | campaign_revenuelineitems._acl.fields.social.write | string | false |  |  | campaign_revenuelineitems._acl.fields.social.write | string | no |
|  |  | campaign_revenuelineitems._acl.fields.totalclicks | object | false |  |  | campaign_revenuelineitems._acl.fields.totalclicks | object | {"create": "no", "write": "no", "license": "no"} |
|  |  | campaign_revenuelineitems._acl.fields.totalclicks.create | string | false |  |  | campaign_revenuelineitems._acl.fields.totalclicks.create | string | no |
|  |  | campaign_revenuelineitems._acl.fields.totalclicks.license | string | false |  |  | campaign_revenuelineitems._acl.fields.totalclicks.license | string | no |
|  |  | campaign_revenuelineitems._acl.fields.totalclicks.write | string | false |  |  | campaign_revenuelineitems._acl.fields.totalclicks.write | string | no |
|  |  | campaign_revenuelineitems._acl.fields.totalopens | object | false |  |  | campaign_revenuelineitems._acl.fields.totalopens | object | {"create": "no", "write": "no", "license": "no"} |
|  |  | campaign_revenuelineitems._acl.fields.totalopens.create | string | false |  |  | campaign_revenuelineitems._acl.fields.totalopens.create | string | no |
|  |  | campaign_revenuelineitems._acl.fields.totalopens.license | string | false |  |  | campaign_revenuelineitems._acl.fields.totalopens.license | string | no |
|  |  | campaign_revenuelineitems._acl.fields.totalopens.write | string | false |  |  | campaign_revenuelineitems._acl.fields.totalopens.write | string | no |
|  |  | campaign_revenuelineitems._acl.fields.unopened | object | false |  |  | campaign_revenuelineitems._acl.fields.unopened | object | {"create": "no", "write": "no", "license": "no"} |
|  |  | campaign_revenuelineitems._acl.fields.unopened.create | string | false |  |  | campaign_revenuelineitems._acl.fields.unopened.create | string | no |
|  |  | campaign_revenuelineitems._acl.fields.unopened.license | string | false |  |  | campaign_revenuelineitems._acl.fields.unopened.license | string | no |
|  |  | campaign_revenuelineitems._acl.fields.unopened.write | string | false |  |  | campaign_revenuelineitems._acl.fields.unopened.write | string | no |
|  |  | campaign_revenuelineitems._acl.fields.unsubscribed | object | false |  |  | campaign_revenuelineitems._acl.fields.unsubscribed | object | {"create": "no", "write": "no", "license": "no"} |
|  |  | campaign_revenuelineitems._acl.fields.unsubscribed.create | string | false |  |  | campaign_revenuelineitems._acl.fields.unsubscribed.create | string | no |
|  |  | campaign_revenuelineitems._acl.fields.unsubscribed.license | string | false |  |  | campaign_revenuelineitems._acl.fields.unsubscribed.license | string | no |
|  |  | campaign_revenuelineitems._acl.fields.unsubscribed.write | string | false |  |  | campaign_revenuelineitems._acl.fields.unsubscribed.write | string | no |
|  |  | campaign_revenuelineitems.id | string | false |  |  | campaign_revenuelineitems.id | string |  |
|  |  | campaign_revenuelineitems.name | string | false |  |  | campaign_revenuelineitems.name | string |  |
|  |  | catalog_service_duration_unit | string | false |  |  | catalog_service_duration_unit | string |  |
|  |  | category_id | string | false |  |  | category_id | string | 2e20b728-30d2-11f0-8b3f-394ac7cc9e7c |
|  |  | category_name | string | false |  |  | category_name | string | Desktops |
|  |  | commit_stage | string | false |  |  | commit_stage | string | exclude |
|  |  | cost_price | string | false |  |  | cost_price | string | 600.000000 |
|  |  | cost_usdollar | string | false |  |  | cost_usdollar | string | 600.000000 |
|  |  | created_by | string | false |  |  | created_by | string | 1 |
|  |  | created_by_link | object | false |  |  | created_by_link | object | {"full_name": "Jen Smith", "id": "1", "_acl": {"fields": [], "_hash": "654d337e0e912edaa00dbb0fb3dc3c17"}} |
|  |  | created_by_link._acl | object | false |  |  | created_by_link._acl | object | {"fields": [], "_hash": "654d337e0e912edaa00dbb0fb3dc3c17"} |
|  |  | created_by_link._acl._hash | string | false |  |  | created_by_link._acl._hash | string | 654d337e0e912edaa00dbb0fb3dc3c17 |
|  |  | created_by_link._acl.fields | object | false |  |  | created_by_link._acl.fields | array | [] |
|  |  | created_by_link.full_name | string | false |  |  | created_by_link.full_name | string | Jen Smith |
|  |  | created_by_link.id | string | false |  |  | created_by_link.id | string | 1 |
|  |  | created_by_name | string | false |  |  | created_by_name | string | Jen Smith |
|  |  | currencies | object | false |  |  | currencies | object | {"name": "", "id": "-99", "_acl": {"fields": [], "_hash": "654d337e0e912edaa00dbb0fb3dc3c17"}, "symbol": ""} |
|  |  | currencies._acl | object | false |  |  | currencies._acl | object | {"fields": [], "_hash": "654d337e0e912edaa00dbb0fb3dc3c17"} |
|  |  | currencies._acl._hash | string | false |  |  | currencies._acl._hash | string | 654d337e0e912edaa00dbb0fb3dc3c17 |
|  |  | currencies._acl.fields | array | false |  |  | currencies._acl.fields | array | [] |
|  |  | currencies.id | string | false |  |  | currencies.id | string | -99 |
|  |  | currencies.name | string | false |  |  | currencies.name | string |  |
|  |  | currencies.symbol | string | false |  |  | currencies.symbol | string |  |
|  |  | currency_id | string | false |  |  | currency_id | string | -99 |
|  |  | currency_name | string | false |  |  | currency_name | string |  |
|  |  | currency_symbol | string | false |  |  | currency_symbol | string |  |
|  |  | date_closed | string | false |  |  | date_closed | string | 2025-05-26 |
|  |  | date_closed_timestamp | integer | false |  |  | date_closed_timestamp | integer | 1748217600 |
|  |  | date_entered | string | false |  |  | date_entered | string | 2025-05-11T03:00:00+05:00 |
|  |  | date_modified | string | false |  |  | date_modified | string | 2025-05-14T21:02:37+05:00 |
|  |  | date_purchased | string | false |  |  | date_purchased | string |  |
|  |  | date_support_expires | string | false |  |  | date_support_expires | string |  |
|  |  | date_support_starts | string | false |  |  | date_support_starts | string |  |
|  |  | deal_calc | string | false |  |  | deal_calc | string | 0.000000 |
|  |  | deal_calc_usdollar | string | false |  |  | deal_calc_usdollar | string | 0.000000 |
|  |  | deleted | boolean | false |  |  | deleted | boolean | False |
|  |  | denorm_account_name | string | false |  |  | denorm_account_name | string | RRR Advertising Inc. |
|  |  | description | string | false |  |  | description | string |  |
|  |  | discount_amount | string | false |  |  | discount_amount | string | 0.000000 |
|  |  | discount_amount_signed | string | false |  |  | discount_amount_signed | string | 0.000000 |
|  |  | discount_amount_usdollar | integer | false |  |  | discount_amount_usdollar | integer | 0 |
|  |  | discount_price | string | false |  |  | discount_price | string | 900.000000 |
|  |  | discount_rate_percent | integer | false |  |  | discount_rate_percent | integer | 0 |
|  |  | discount_select | boolean | false |  |  | discount_select | boolean | True |
|  |  | discount_usdollar | string | false |  |  | discount_usdollar | string | 900.000000 |
|  |  | following | boolean | false |  |  | following | boolean | False |
|  |  | forecasted_likely | string | false |  |  | forecasted_likely | string | 0.000000 |
|  |  | generate_purchase | string | false |  |  | generate_purchase | string | Yes |
|  |  | id | string | false |  |  | id | string | db5458b4-30dc-11f0-8a69-f366efd4954a |
|  |  | lead_source | string | false |  |  | lead_source | string |  |
|  |  | likely_case | string | false |  |  | likely_case | string | 34800.000000 |
|  |  | list_price | string | false |  |  | list_price | string | 900.000000 |
|  |  | list_usdollar | string | false |  |  | list_usdollar | string | 900.000000 |
|  |  | lock_duration | boolean | false |  |  | lock_duration | boolean | False |
|  |  | locked_fields | array | false |  |  | locked_fields | array | [] |
|  |  | manufacturer_id | string | false |  |  | manufacturer_id | string | 90361354-4b2e-11e8-9ab7-0211b31cacdf |
|  |  | manufacturer_name | string | false |  |  | manufacturer_name | string |  |
|  |  | manufacturers | object | false |  |  | manufacturers | object | {"name": "", "id": "90361354-4b2e-11e8-9ab7-0211b31cacdf", "_acl": {"fields": [], "_hash": "654d337e0e912edaa00dbb0fb3dc3c17"}} |
|  |  | manufacturers._acl | object | false |  |  | manufacturers._acl | object | {"fields": [], "_hash": "654d337e0e912edaa00dbb0fb3dc3c17"} |
|  |  | manufacturers._acl._hash | string | false |  |  | manufacturers._acl._hash | string | 654d337e0e912edaa00dbb0fb3dc3c17 |
|  |  | manufacturers._acl.fields | array | false |  |  | manufacturers._acl.fields | array | [] |
|  |  | manufacturers.id | string | false |  |  | manufacturers.id | string | 90361354-4b2e-11e8-9ab7-0211b31cacdf |
|  |  | manufacturers.name | string | false |  |  | manufacturers.name | string |  |
|  |  | mft_part_num | string | false |  |  | mft_part_num | string | XYZ7890123456 |
|  |  | modified_by_name | string | false |  |  | modified_by_name | string | Jen Smith |
|  |  | modified_user_id | string | false |  |  | modified_user_id | string | 1 |
|  |  | modified_user_link | object | false |  |  | modified_user_link | object | {"full_name": "Jen Smith", "id": "1", "_acl": {"fields": [], "_hash": "654d337e0e912edaa00dbb0fb3dc3c17"}} |
|  |  | modified_user_link._acl | object | false |  |  | modified_user_link._acl | object | {"fields": [], "_hash": "654d337e0e912edaa00dbb0fb3dc3c17"} |
|  |  | modified_user_link._acl._hash | string | false |  |  | modified_user_link._acl._hash | string | 654d337e0e912edaa00dbb0fb3dc3c17 |
|  |  | modified_user_link._acl.fields | object | false |  |  | modified_user_link._acl.fields | array | [] |
|  |  | modified_user_link.full_name | string | false |  |  | modified_user_link.full_name | string | Jen Smith |
|  |  | modified_user_link.id | string | false |  |  | modified_user_link.id | string | 1 |
|  |  | my_favorite | boolean | false |  |  | my_favorite | boolean | False |
|  |  | name | string | false |  |  | name | string | RRR Advertising Inc. |
|  |  | next_step | string | false |  |  | next_step | string |  |
|  |  | opportunities | object | false |  |  | opportunities | object | {"name": "RRR Advertising Inc. - $34800 - 647", "id": "db3f6530-30dc-11f0-9285-fb295c038a96", "_acl": {"fields": [], "_hash": "654d337e0e912edaa00dbb0fb3dc3c17"}} |
|  |  | opportunities._acl | object | false |  |  | opportunities._acl | object | {"fields": [], "_hash": "654d337e0e912edaa00dbb0fb3dc3c17"} |
|  |  | opportunities._acl._hash | string | false |  |  | opportunities._acl._hash | string | 654d337e0e912edaa00dbb0fb3dc3c17 |
|  |  | opportunities._acl.fields | array | false |  |  | opportunities._acl.fields | array | [] |
|  |  | opportunities.id | string | false |  |  | opportunities.id | string | db3f6530-30dc-11f0-9285-fb295c038a96 |
|  |  | opportunities.name | string | false |  |  | opportunities.name | string | RRR Advertising Inc. - $34800 - 647 |
|  |  | opportunity_id | string | false |  | opportunities | opportunity_id | string | db3f6530-30dc-11f0-9285-fb295c038a96 |
|  |  | opportunity_name | string | false |  |  | opportunity_name | string | RRR Advertising Inc. - $34800 - 647 |
|  |  | pli_addons_link | object | false |  |  | pli_addons_link | object | {"name": "", "id": "", "_acl": {"fields": [], "_hash": "654d337e0e912edaa00dbb0fb3dc3c17"}} |
|  |  | pli_addons_link._acl | object | false |  |  | pli_addons_link._acl | object | {"fields": [], "_hash": "654d337e0e912edaa00dbb0fb3dc3c17"} |
|  |  | pli_addons_link._acl._hash | string | false |  |  | pli_addons_link._acl._hash | string | 654d337e0e912edaa00dbb0fb3dc3c17 |
|  |  | pli_addons_link._acl.fields | array | false |  |  | pli_addons_link._acl.fields | array | [] |
|  |  | pli_addons_link.id | string | false |  |  | pli_addons_link.id | string |  |
|  |  | pli_addons_link.name | string | false |  |  | pli_addons_link.name | string |  |
|  |  | pricing_formula | string | false |  |  | pricing_formula | string |  |
|  |  | probability | integer | false |  |  | probability | integer | 10 |
|  |  | product_template_id | string | false |  |  | product_template_id | string | 2e27e8f4-30d2-11f0-bda3-7de7078e76fd |
|  |  | product_template_name | string | false |  |  | product_template_name | string | TK 1000 Desktop |
|  |  | product_type | string | false |  |  | product_type | string | Existing Business |
|  |  | purchasedlineitem | object | false |  |  | purchasedlineitem | object | {"name": "", "id": "", "_acl": {"fields": [], "_hash": "654d337e0e912edaa00dbb0fb3dc3c17"}} |
|  |  | purchasedlineitem._acl | object | false |  |  | purchasedlineitem._acl | object | {"fields": [], "_hash": "654d337e0e912edaa00dbb0fb3dc3c17"} |
|  |  | purchasedlineitem._acl._hash | string | false |  |  | purchasedlineitem._acl._hash | string | 654d337e0e912edaa00dbb0fb3dc3c17 |
|  |  | purchasedlineitem._acl.fields | array | false |  |  | purchasedlineitem._acl.fields | array | [] |
|  |  | purchasedlineitem.id | string | false |  |  | purchasedlineitem.id | string |  |
|  |  | purchasedlineitem.name | string | false |  |  | purchasedlineitem.name | string |  |
|  |  | purchasedlineitem_id | string | false |  |  | purchasedlineitem_id | string |  |
|  |  | purchasedlineitem_name | string | false |  |  | purchasedlineitem_name | string |  |
|  |  | quantity | integer | false |  |  | quantity | integer | 1 |
|  |  | quote_id | string | false |  |  | quote_id | string |  |
|  |  | quote_name | string | false |  |  | quote_name | string |  |
|  |  | quotes | object | false |  |  | quotes | object | {"name": "", "id": "", "_acl": {"fields": [], "_hash": "654d337e0e912edaa00dbb0fb3dc3c17"}} |
|  |  | quotes._acl | object | false |  |  | quotes._acl | object | {"fields": [], "_hash": "654d337e0e912edaa00dbb0fb3dc3c17"} |
|  |  | quotes._acl._hash | string | false |  |  | quotes._acl._hash | string | 654d337e0e912edaa00dbb0fb3dc3c17 |
|  |  | quotes._acl.fields | array | false |  |  | quotes._acl.fields | array | [] |
|  |  | quotes.id | string | false |  |  | quotes.id | string |  |
|  |  | quotes.name | string | false |  |  | quotes.name | string |  |
|  |  | renewable | boolean | false |  |  | renewable | boolean | False |
|  |  | renewal | boolean | false |  |  | renewal | boolean | False |
|  |  | renewal_rli_id | string | false |  |  | renewal_rli_id | string |  |
|  |  | renewal_rli_link | object | false |  |  | renewal_rli_link | object | {"name": "", "id": "", "_acl": {"fields": [], "_hash": "654d337e0e912edaa00dbb0fb3dc3c17"}} |
|  |  | renewal_rli_link._acl | object | false |  |  | renewal_rli_link._acl | object | {"fields": [], "_hash": "654d337e0e912edaa00dbb0fb3dc3c17"} |
|  |  | renewal_rli_link._acl._hash | string | false |  |  | renewal_rli_link._acl._hash | string | 654d337e0e912edaa00dbb0fb3dc3c17 |
|  |  | renewal_rli_link._acl.fields | array | false |  |  | renewal_rli_link._acl.fields | array | [] |
|  |  | renewal_rli_link.id | string | false |  |  | renewal_rli_link.id | string |  |
|  |  | renewal_rli_link.name | string | false |  |  | renewal_rli_link.name | string |  |
|  |  | renewal_rli_name | string | false |  |  | renewal_rli_name | string |  |
|  |  | revenuelineitem_types_link | object | false |  |  | revenuelineitem_types_link | object | {"name": "", "id": "", "_acl": {"fields": [], "_hash": "654d337e0e912edaa00dbb0fb3dc3c17"}} |
|  |  | revenuelineitem_types_link._acl | object | false |  |  | revenuelineitem_types_link._acl | object | {"fields": [], "_hash": "654d337e0e912edaa00dbb0fb3dc3c17"} |
|  |  | revenuelineitem_types_link._acl._hash | string | false |  |  | revenuelineitem_types_link._acl._hash | string | 654d337e0e912edaa00dbb0fb3dc3c17 |
|  |  | revenuelineitem_types_link._acl.fields | array | false |  |  | revenuelineitem_types_link._acl.fields | array | [] |
|  |  | revenuelineitem_types_link.id | string | false |  |  | revenuelineitem_types_link.id | string |  |
|  |  | revenuelineitem_types_link.name | string | false |  |  | revenuelineitem_types_link.name | string |  |
|  |  | rli_categories_link | object | false |  |  | rli_categories_link | object | {"name": "Desktops", "id": "2e20b728-30d2-11f0-8b3f-394ac7cc9e7c", "_acl": {"fields": [], "_hash": "654d337e0e912edaa00dbb0fb3dc3c17"}} |
|  |  | rli_categories_link._acl | object | false |  |  | rli_categories_link._acl | object | {"fields": [], "_hash": "654d337e0e912edaa00dbb0fb3dc3c17"} |
|  |  | rli_categories_link._acl._hash | string | false |  |  | rli_categories_link._acl._hash | string | 654d337e0e912edaa00dbb0fb3dc3c17 |
|  |  | rli_categories_link._acl.fields | array | false |  |  | rli_categories_link._acl.fields | array | [] |
|  |  | rli_categories_link.id | string | false |  |  | rli_categories_link.id | string | 2e20b728-30d2-11f0-8b3f-394ac7cc9e7c |
|  |  | rli_categories_link.name | string | false |  |  | rli_categories_link.name | string | Desktops |
|  |  | rli_templates_link | object | false |  |  | rli_templates_link | object | {"name": "TK 1000 Desktop", "id": "2e27e8f4-30d2-11f0-bda3-7de7078e76fd", "_acl": {"fields": [], "_hash": "654d337e0e912edaa00dbb0fb3dc3c17"}} |
|  |  | rli_templates_link._acl | object | false |  |  | rli_templates_link._acl | object | {"fields": [], "_hash": "654d337e0e912edaa00dbb0fb3dc3c17"} |
|  |  | rli_templates_link._acl._hash | string | false |  |  | rli_templates_link._acl._hash | string | 654d337e0e912edaa00dbb0fb3dc3c17 |
|  |  | rli_templates_link._acl.fields | array | false |  |  | rli_templates_link._acl.fields | array | [] |
|  |  | rli_templates_link.id | string | false |  |  | rli_templates_link.id | string | 2e27e8f4-30d2-11f0-bda3-7de7078e76fd |
|  |  | rli_templates_link.name | string | false |  |  | rli_templates_link.name | string | TK 1000 Desktop |
|  |  | sales_stage | string | false |  |  | sales_stage | string | Prospecting |
|  |  | serial_number | string | false |  |  | serial_number | string |  |
|  |  | service | boolean | false |  |  | service | boolean | False |
|  |  | service_duration_multiplier | integer | false |  |  | service_duration_multiplier | integer | 1 |
|  |  | service_duration_unit | string | false |  |  | service_duration_unit | string |  |
|  |  | service_end_date | string | false |  |  | service_end_date | string |  |
|  |  | service_start_date | string | false |  |  | service_start_date | string |  |
|  |  | status | string | false |  |  | status | string |  |
|  |  | subtotal | string | false |  |  | subtotal | string | 900.000000 |
|  |  | support_contact | string | false |  |  | support_contact | string |  |
|  |  | support_description | string | false |  |  | support_description | string |  |
|  |  | support_name | string | false |  |  | support_name | string |  |
|  |  | support_term | string | false |  |  | support_term | string |  |
|  |  | sync_key | string | false |  |  | sync_key | string |  |
|  |  | tag | array | false |  |  | tag | array | [] |
|  |  | tax_class | string | false |  |  | tax_class | string | Taxable |
|  |  | team_count | string | false |  |  | team_count | string |  |
|  |  | team_count_link | object | false |  |  | team_count_link | object | {"team_count": "", "id": "1", "_acl": {"fields": [], "_hash": "654d337e0e912edaa00dbb0fb3dc3c17"}} |
|  |  | team_count_link._acl | object | false |  |  | team_count_link._acl | object | {"fields": [], "_hash": "654d337e0e912edaa00dbb0fb3dc3c17"} |
|  |  | team_count_link._acl._hash | string | false |  |  | team_count_link._acl._hash | string | 654d337e0e912edaa00dbb0fb3dc3c17 |
|  |  | team_count_link._acl.fields | array | false |  |  | team_count_link._acl.fields | array | [] |
|  |  | team_count_link.id | string | false |  |  | team_count_link.id | string | 1 |
|  |  | team_count_link.team_count | string | false |  |  | team_count_link.team_count | string |  |
|  |  | team_name | array | false |  |  | team_name | array | [{"id": "1", "name": "Global", "name_2": "", "primary": true, "selected": false}] |
|  |  | team_name[] | object | false |  |  | team_name[] | object | {"id": "1", "name": "Global", "name_2": "", "primary": true, "selected": false} |
|  |  | team_name[].id | string | false |  |  | team_name[].id | string | 1 |
|  |  | team_name[].name | string | false |  |  | team_name[].name | string | Global |
|  |  | team_name[].name_2 | string | false |  |  | team_name[].name_2 | string |  |
|  |  | team_name[].primary | boolean | false |  |  | team_name[].primary | boolean | True |
|  |  | team_name[].selected | boolean | false |  |  | team_name[].selected | boolean | False |
|  |  | total_amount | string | false |  |  | total_amount | string | 900.000000 |
|  |  | type_id | string | false |  |  | type_id | string |  |
|  |  | type_name | string | false |  |  | type_name | string |  |
|  |  | vendor_part_num | string | false |  |  | vendor_part_num | string |  |
|  |  | website | string | false |  |  | website | string |  |
|  |  | weight | integer | false |  |  | weight | integer | 20 |
|  |  | worst_case | string | false |  |  | worst_case | string | 34800.000000 |
| Schema |  | <span style='color:red'>***createdTime***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***created_by_link._acl.fields.last_login***</span> | object | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***created_by_link._acl.fields.last_login.create***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***created_by_link._acl.fields.last_login.write***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***created_by_link._acl.fields.pwd_last_changed***</span> | object | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***created_by_link._acl.fields.pwd_last_changed.create***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***created_by_link._acl.fields.pwd_last_changed.write***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields***</span> | object | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields._acl***</span> | object | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields._acl.fields***</span> | object | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields._module***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.account_id***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.account_link***</span> | object | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.account_link._acl***</span> | object | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.account_link._acl._hash***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.account_link._acl.fields***</span> | array | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.account_link.id***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.account_link.name***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.account_name***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.add_on_to_id***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.add_on_to_name***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.asset_number***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.assigned_user_id***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.assigned_user_link***</span> | object | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.assigned_user_link._acl***</span> | object | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.assigned_user_link._acl._hash***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.assigned_user_link._acl.fields***</span> | array | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.assigned_user_link.full_name***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.assigned_user_link.id***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.assigned_user_name***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.base_rate***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.best_case***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.book_value***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.book_value_date***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.book_value_usdollar***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.campaign_id***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.campaign_name***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.campaign_revenuelineitems***</span> | object | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.campaign_revenuelineitems._acl***</span> | object | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.campaign_revenuelineitems._acl._hash***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.campaign_revenuelineitems._acl.fields***</span> | object | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.campaign_revenuelineitems._acl.fields.bounced***</span> | object | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.campaign_revenuelineitems._acl.fields.bounced.create***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.campaign_revenuelineitems._acl.fields.bounced.license***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.campaign_revenuelineitems._acl.fields.bounced.write***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.campaign_revenuelineitems._acl.fields.delivered***</span> | object | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.campaign_revenuelineitems._acl.fields.delivered.create***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.campaign_revenuelineitems._acl.fields.delivered.license***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.campaign_revenuelineitems._acl.fields.delivered.write***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.campaign_revenuelineitems._acl.fields.forwards***</span> | object | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.campaign_revenuelineitems._acl.fields.forwards.create***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.campaign_revenuelineitems._acl.fields.forwards.license***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.campaign_revenuelineitems._acl.fields.forwards.write***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.campaign_revenuelineitems._acl.fields.notreported***</span> | object | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.campaign_revenuelineitems._acl.fields.notreported.create***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.campaign_revenuelineitems._acl.fields.notreported.license***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.campaign_revenuelineitems._acl.fields.notreported.write***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.campaign_revenuelineitems._acl.fields.peoplewhoclicked***</span> | object | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.campaign_revenuelineitems._acl.fields.peoplewhoclicked.create***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.campaign_revenuelineitems._acl.fields.peoplewhoclicked.license***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.campaign_revenuelineitems._acl.fields.peoplewhoclicked.write***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.campaign_revenuelineitems._acl.fields.peoplewhoopened***</span> | object | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.campaign_revenuelineitems._acl.fields.peoplewhoopened.create***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.campaign_revenuelineitems._acl.fields.peoplewhoopened.license***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.campaign_revenuelineitems._acl.fields.peoplewhoopened.write***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.campaign_revenuelineitems._acl.fields.postdate***</span> | object | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.campaign_revenuelineitems._acl.fields.postdate.create***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.campaign_revenuelineitems._acl.fields.postdate.license***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.campaign_revenuelineitems._acl.fields.postdate.write***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.campaign_revenuelineitems._acl.fields.sent***</span> | object | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.campaign_revenuelineitems._acl.fields.sent.create***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.campaign_revenuelineitems._acl.fields.sent.license***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.campaign_revenuelineitems._acl.fields.sent.write***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.campaign_revenuelineitems._acl.fields.social***</span> | object | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.campaign_revenuelineitems._acl.fields.social.create***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.campaign_revenuelineitems._acl.fields.social.license***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.campaign_revenuelineitems._acl.fields.social.write***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.campaign_revenuelineitems._acl.fields.totalclicks***</span> | object | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.campaign_revenuelineitems._acl.fields.totalclicks.create***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.campaign_revenuelineitems._acl.fields.totalclicks.license***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.campaign_revenuelineitems._acl.fields.totalclicks.write***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.campaign_revenuelineitems._acl.fields.totalopens***</span> | object | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.campaign_revenuelineitems._acl.fields.totalopens.create***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.campaign_revenuelineitems._acl.fields.totalopens.license***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.campaign_revenuelineitems._acl.fields.totalopens.write***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.campaign_revenuelineitems._acl.fields.unopened***</span> | object | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.campaign_revenuelineitems._acl.fields.unopened.create***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.campaign_revenuelineitems._acl.fields.unopened.license***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.campaign_revenuelineitems._acl.fields.unopened.write***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.campaign_revenuelineitems._acl.fields.unsubscribed***</span> | object | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.campaign_revenuelineitems._acl.fields.unsubscribed.create***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.campaign_revenuelineitems._acl.fields.unsubscribed.license***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.campaign_revenuelineitems._acl.fields.unsubscribed.write***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.campaign_revenuelineitems.id***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.campaign_revenuelineitems.name***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.catalog_service_duration_unit***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.category_id***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.category_name***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.commit_stage***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.cost_price***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.cost_usdollar***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.created_by***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.created_by_link***</span> | object | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.created_by_link._acl***</span> | object | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.created_by_link._acl._hash***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.created_by_link._acl.fields***</span> | object | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.created_by_link._acl.fields.last_login***</span> | object | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.created_by_link._acl.fields.last_login.create***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.created_by_link._acl.fields.last_login.write***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.created_by_link._acl.fields.pwd_last_changed***</span> | object | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.created_by_link._acl.fields.pwd_last_changed.create***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.created_by_link._acl.fields.pwd_last_changed.write***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.created_by_link.full_name***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.created_by_link.id***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.created_by_name***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.currencies***</span> | object | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.currencies._acl***</span> | object | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.currencies._acl._hash***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.currencies._acl.fields***</span> | array | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.currencies.id***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.currencies.name***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.currencies.symbol***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.currency_id***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.currency_name***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.currency_symbol***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.date_closed***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.date_closed_timestamp***</span> | integer | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.date_entered***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.date_modified***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.date_purchased***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.date_support_expires***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.date_support_starts***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.deal_calc***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.deal_calc_usdollar***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.deleted***</span> | boolean | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.denorm_account_name***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.description***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.discount_amount***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.discount_amount_signed***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.discount_amount_usdollar***</span> | integer | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.discount_price***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.discount_rate_percent***</span> | integer | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.discount_select***</span> | boolean | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.discount_usdollar***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.following***</span> | boolean | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.forecasted_likely***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.generate_purchase***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.id***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.lead_source***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.likely_case***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.list_price***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.list_usdollar***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.lock_duration***</span> | boolean | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.locked_fields***</span> | array | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.manufacturer_id***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.manufacturer_name***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.manufacturers***</span> | object | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.manufacturers._acl***</span> | object | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.manufacturers._acl._hash***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.manufacturers._acl.fields***</span> | array | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.manufacturers.id***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.manufacturers.name***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.mft_part_num***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.modified_by_name***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.modified_user_id***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.modified_user_link***</span> | object | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.modified_user_link._acl***</span> | object | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.modified_user_link._acl._hash***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.modified_user_link._acl.fields***</span> | object | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.modified_user_link._acl.fields.last_login***</span> | object | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.modified_user_link._acl.fields.last_login.create***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.modified_user_link._acl.fields.last_login.write***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.modified_user_link._acl.fields.pwd_last_changed***</span> | object | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.modified_user_link._acl.fields.pwd_last_changed.create***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.modified_user_link._acl.fields.pwd_last_changed.write***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.modified_user_link.full_name***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.modified_user_link.id***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.my_favorite***</span> | boolean | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.name***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.next_step***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.opportunities***</span> | object | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.opportunities._acl***</span> | object | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.opportunities._acl._hash***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.opportunities._acl.fields***</span> | array | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.opportunities.id***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.opportunities.name***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.opportunity_id***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.opportunity_name***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.pli_addons_link***</span> | object | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.pli_addons_link._acl***</span> | object | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.pli_addons_link._acl._hash***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.pli_addons_link._acl.fields***</span> | array | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.pli_addons_link.id***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.pli_addons_link.name***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.pricing_formula***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.probability***</span> | integer | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.product_template_id***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.product_template_name***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.product_type***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.purchasedlineitem***</span> | object | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.purchasedlineitem._acl***</span> | object | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.purchasedlineitem._acl._hash***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.purchasedlineitem._acl.fields***</span> | array | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.purchasedlineitem.id***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.purchasedlineitem.name***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.purchasedlineitem_id***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.purchasedlineitem_name***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.quantity***</span> | integer | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.quote_id***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.quote_name***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.quotes***</span> | object | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.quotes._acl***</span> | object | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.quotes._acl._hash***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.quotes._acl.fields***</span> | array | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.quotes.id***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.quotes.name***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.renewable***</span> | boolean | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.renewal***</span> | boolean | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.renewal_rli_id***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.renewal_rli_link***</span> | object | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.renewal_rli_link._acl***</span> | object | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.renewal_rli_link._acl._hash***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.renewal_rli_link._acl.fields***</span> | array | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.renewal_rli_link.id***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.renewal_rli_link.name***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.renewal_rli_name***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.revenuelineitem_types_link***</span> | object | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.revenuelineitem_types_link._acl***</span> | object | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.revenuelineitem_types_link._acl._hash***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.revenuelineitem_types_link._acl.fields***</span> | array | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.revenuelineitem_types_link.id***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.revenuelineitem_types_link.name***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.rli_categories_link***</span> | object | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.rli_categories_link._acl***</span> | object | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.rli_categories_link._acl._hash***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.rli_categories_link._acl.fields***</span> | array | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.rli_categories_link.id***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.rli_categories_link.name***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.rli_templates_link***</span> | object | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.rli_templates_link._acl***</span> | object | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.rli_templates_link._acl._hash***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.rli_templates_link._acl.fields***</span> | array | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.rli_templates_link.id***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.rli_templates_link.name***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.sales_stage***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.serial_number***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.service***</span> | boolean | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.service_duration_multiplier***</span> | integer | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.service_duration_unit***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.service_end_date***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.service_start_date***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.status***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.subtotal***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.support_contact***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.support_description***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.support_name***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.support_term***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.sync_key***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.tag***</span> | array | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.tax_class***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.team_count***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.team_count_link***</span> | object | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.team_count_link._acl***</span> | object | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.team_count_link._acl._hash***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.team_count_link._acl.fields***</span> | array | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.team_count_link.id***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.team_count_link.team_count***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.team_name***</span> | array | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.total_amount***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.type_id***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.type_name***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.vendor_part_num***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.website***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.weight***</span> | integer | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***fields.worst_case***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***modified_user_link._acl.fields.last_login***</span> | object | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***modified_user_link._acl.fields.last_login.create***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***modified_user_link._acl.fields.last_login.write***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***modified_user_link._acl.fields.pwd_last_changed***</span> | object | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***modified_user_link._acl.fields.pwd_last_changed.create***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***modified_user_link._acl.fields.pwd_last_changed.write***</span> | string | false |  |  |  |  |  |
| Schema |  | <span style='color:red'>***updatedTime***</span> | string | false |  |  |  |  |  |
| FindByID |  |  |  |  |  |  | catalog_service_duration_value | null | None |
| FindByID |  |  |  |  |  |  | pricing_factor | null | None |
| FindByID |  |  |  |  |  |  | service_duration_value | null | None |