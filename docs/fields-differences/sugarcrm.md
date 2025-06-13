# Differences between fields in SugarCRM.io


## Opportunities

| Entity Schema Title | Entity Schema Fields | Entity Schema Types | Readonly | Possible Values | Reference Collection | Find By ID Object Fields | Find By ID Types | Value |
|---------------------|----------------------|---------------------|----------|-----------------|----------------------|--------------------------|------------------|-------|
|  | account_id | string | false |  | accounts | account_id | string | d890652e-30cc-11f0-9c5b-31b297db6ffd |
|  | ai_opp_conv_bin_accuracy | string | false |  |  | ai_opp_conv_bin_accuracy | null | None |
|  | ai_opp_conv_multiplier | string | false |  |  | ai_opp_conv_multiplier | null | None |
|  | ai_opp_conv_score_absolute | string | false |  |  | ai_opp_conv_score_absolute | null | None |
|  | ai_opp_conv_score_enum | string | false |  |  | ai_opp_conv_score_enum | string |  |
|  | amount | string | false |  |  | amount | string | 34800.000000 |
|  | amount_usdollar | string | false |  |  | amount_usdollar | string | 34800.000000 |
|  | assigned_user_id | string | false |  | users | assigned_user_id | string | seed_will_id |
|  | base_rate | string | false |  |  | base_rate | string | 1.000000 |
|  | best_case | string | false |  |  | best_case | string | 34800.000000 |
|  | campaign_id | string | false |  |  | campaign_id | string |  |
|  | campaign_opportunities | object | false |  |  | campaign_opportunities | object | {"name": "", "id": ""} |
|  | campaign_opportunities.id | string | false |  |  | campaign_opportunities.id | string |  |
|  | campaign_opportunities.name | string | false |  |  | campaign_opportunities.name | string |  |
|  | closed_revenue_line_items | integer | false |  |  | closed_revenue_line_items | integer | 0 |
|  | closed_won_revenue_line_items | integer | false |  |  | closed_won_revenue_line_items | integer | 0 |
|  | commit_stage | string | false |  |  | commit_stage | string | exclude |
|  | commit_stage_cascade | string | false |  |  | commit_stage_cascade | string |  |
|  | contact_role | string | false |  |  | contact_role | string |  |
|  | created_by | string | false |  | users | created_by | string | 1 |
|  | currency_id | string | false | `US Dollars`, `Euro` |  | currency_id | string | -99 |
|  | currency_name | string | false |  |  | currency_name | string |  |
|  | date_closed | string | false |  |  | date_closed | string | 2025-05-26 |
|  | date_closed_cascade | string | false |  |  | date_closed_cascade | string |  |
|  | date_closed_timestamp | integer | false |  |  | date_closed_timestamp | integer | 1748217600 |
|  | date_entered | string | false |  |  | date_entered | string | 2025-05-11T03:00:00+05:00 |
|  | date_modified | string | false |  |  | date_modified | string | 2025-05-14T21:02:38+05:00 |
|  | deleted | boolean | false |  |  | deleted | boolean | False |
|  | description | string | false |  |  | description | string |  |
|  | following | boolean | false |  |  | following | boolean | False |
|  | forecasted_likely | string | false |  |  | forecasted_likely | string | 0.000000 |
|  | geocode_status | string | false |  |  | geocode_status | string |  |
|  | id | string | true |  |  | id | string | db3f6530-30dc-11f0-9285-fb295c038a96 |
|  | included_revenue_line_items | integer | false |  |  | included_revenue_line_items | integer | 0 |
|  | is_escalated | boolean | false |  |  | is_escalated | boolean | False |
|  | lead_source | string | false |  |  | lead_source | string |  |
|  | lost | string | false |  |  | lost | string | 0.000000 |
|  | mkto_id | string | false |  |  | mkto_id | null | None |
|  | mkto_sync | boolean | false |  |  | mkto_sync | boolean | False |
|  | modified_user_id | string | false |  | users | modified_user_id | string | 1 |
|  | my_favorite | boolean | false |  |  | my_favorite | boolean | False |
|  | *name | string | false |  |  | name | string | RRR Advertising Inc. - $34800 - 647 |
|  | next_step | string | false |  |  | next_step | string |  |
|  | opportunity_type | string | false |  |  | opportunity_type | string | Existing Business |
|  | probability | integer | false |  |  | probability | integer | 10 |
|  | renewal | boolean | false |  |  | renewal | boolean | False |
|  | renewal_parent_id | string | false |  |  | renewal_parent_id | string |  |
|  | renewal_parent_name | string | false |  |  | renewal_parent_name | string |  |
|  | sales_stage | string | false |  |  | sales_stage | string | Prospecting |
|  | sales_stage_cascade | string | false |  |  | sales_stage_cascade | string |  |
|  | sales_status | string | false |  |  | sales_status | string | In Progress |
|  | service_duration_unit | string | false |  |  | service_duration_unit | string |  |
|  | service_duration_unit_cascade | string | false |  |  | service_duration_unit_cascade | string |  |
|  | service_duration_value | integer | false |  |  | service_duration_value | null | None |
|  | service_duration_value_cascade | integer | false |  |  | service_duration_value_cascade | null | None |
|  | service_open_flex_duration_rlis | integer | false |  |  | service_open_flex_duration_rlis | integer | 0 |
|  | service_open_revenue_line_items | integer | false |  |  | service_open_revenue_line_items | integer | 0 |
|  | service_start_date | string | false |  |  | service_start_date | string |  |
|  | service_start_date_cascade | string | false |  |  | service_start_date_cascade | string |  |
|  | sl_ai_conv_score_c | string | false |  |  | sl_ai_conv_score_c | string | 01_not_likely |
|  | sync_key | string | false |  |  | sync_key | string |  |
|  | tag | array | false |  |  | tag | array | [] |
|  | team_count | string | false |  |  | team_count | string |  |
|  | team_name | array | false |  |  | team_name | array | [{"id": "1", "name": "Global", "name_2": "", "primary": true, "selected": false}] |
|  | team_name[] | object | false |  |  | team_name[] | object |  |
|  | team_name[].id | string | false |  |  | team_name[].id | string |  |
|  | team_name[].name | string | false |  |  | team_name[].name | string |  |
|  | team_name[].name_2 | string | false |  |  | team_name[].name_2 | string |  |
|  | team_name[].primary | boolean | false |  |  | team_name[].primary | boolean |  |
|  | team_name[].selected | boolean | false |  |  | team_name[].selected | boolean |  |
|  | total_revenue_line_items | integer | false |  |  | total_revenue_line_items | integer | 1 |
|  | widget_amount | string | false |  |  | widget_amount | string |  |
|  | widget_date_closed | string | false |  |  | widget_date_closed | string |  |
|  | widget_sales_stage | string | false |  |  | widget_sales_stage | string |  |
|  | worst_case | string | false |  |  | worst_case | string | 34800.000000 |
|  |  |  |  |  |  | _acl | object | {"fields": {}} |
|  |  |  |  |  |  | _acl.fields | object |  |
|  |  |  |  |  |  | _module | string | Opportunities |
|  |  |  |  |  |  | account_name | string | RRR Advertising Inc. |
|  |  |  |  |  |  | accounts | object | {"name": "RRR Advertising Inc.", "id": "d890652e-30cc-11f0-9c5b-31b297db6ffd", "_acl": {"fields": [], "_hash": "654d337e0e912edaa00dbb0fb3dc3c17"}} |
|  |  |  |  |  |  | accounts._acl | object |  |
|  |  |  |  |  |  | accounts._acl._hash | string |  |
|  |  |  |  |  |  | accounts._acl.fields | array |  |
|  |  |  |  |  |  | accounts.id | string |  |
|  |  |  |  |  |  | accounts.name | string |  |
|  |  |  |  |  |  | ai_opp_close_week_scores | null | None |
|  |  |  |  |  |  | ai_opp_won_score | null | None |
|  |  |  |  |  |  | assigned_user_link | object | {"full_name": "Will Westin", "id": "seed_will_id", "_acl": {"fields": [], "_hash": "654d337e0e912edaa00dbb0fb3dc3c17"}} |
|  |  |  |  |  |  | assigned_user_link._acl | object |  |
|  |  |  |  |  |  | assigned_user_link._acl._hash | string |  |
|  |  |  |  |  |  | assigned_user_link._acl.fields | array |  |
|  |  |  |  |  |  | assigned_user_link.full_name | string |  |
|  |  |  |  |  |  | assigned_user_link.id | string |  |
|  |  |  |  |  |  | assigned_user_name | string | Will Westin |
|  |  |  |  |  |  | campaign_name | string |  |
|  |  |  |  |  |  | created_by_link | object | {"full_name": "Jen Smith", "id": "1", "_acl": {"fields": [], "_hash": "654d337e0e912edaa00dbb0fb3dc3c17"}} |
|  |  |  |  |  |  | created_by_link._acl | object |  |
|  |  |  |  |  |  | created_by_link._acl._hash | string |  |
|  |  |  |  |  |  | created_by_link._acl.fields | array |  |
|  |  |  |  |  |  | created_by_link.full_name | string |  |
|  |  |  |  |  |  | created_by_link.id | string |  |
|  |  |  |  |  |  | created_by_name | string | Jen Smith |
|  |  |  |  |  |  | currencies | object | {"name": "", "id": "-99", "_acl": {"fields": [], "_hash": "654d337e0e912edaa00dbb0fb3dc3c17"}, "symbol": ""} |
|  |  |  |  |  |  | currencies._acl | object |  |
|  |  |  |  |  |  | currencies._acl._hash | string |  |
|  |  |  |  |  |  | currencies._acl.fields | array |  |
|  |  |  |  |  |  | currencies.id | string |  |
|  |  |  |  |  |  | currencies.name | string |  |
|  |  |  |  |  |  | currencies.symbol | string |  |
|  |  |  |  |  |  | currency_symbol | string |  |
|  |  |  |  |  |  | denorm_account_name | string | RRR Advertising Inc. |
|  |  |  |  |  |  | discover_data_c | boolean | True |
|  |  |  |  |  |  | dri_workflow_template_id | string |  |
|  |  |  |  |  |  | dri_workflow_template_link | object | {"name": "", "id": "", "_acl": {"fields": [], "_hash": "654d337e0e912edaa00dbb0fb3dc3c17"}} |
|  |  |  |  |  |  | dri_workflow_template_link._acl | object |  |
|  |  |  |  |  |  | dri_workflow_template_link._acl._hash | string |  |
|  |  |  |  |  |  | dri_workflow_template_link._acl.fields | array |  |
|  |  |  |  |  |  | dri_workflow_template_link.id | string |  |
|  |  |  |  |  |  | dri_workflow_template_link.name | string |  |
|  |  |  |  |  |  | dri_workflow_template_name | string |  |
|  |  |  |  |  |  | locked_fields | array | [] |
|  |  |  |  |  |  | modified_by_name | string | Jen Smith |
|  |  |  |  |  |  | modified_user_link | object | {"full_name": "Jen Smith", "id": "1", "_acl": {"fields": [], "_hash": "654d337e0e912edaa00dbb0fb3dc3c17"}} |
|  |  |  |  |  |  | modified_user_link._acl | object |  |
|  |  |  |  |  |  | modified_user_link._acl._hash | string |  |
|  |  |  |  |  |  | modified_user_link._acl.fields | array |  |
|  |  |  |  |  |  | modified_user_link.full_name | string |  |
|  |  |  |  |  |  | modified_user_link.id | string |  |
|  |  |  |  |  |  | perform_sugar_action | boolean | False |
|  |  |  |  |  |  | renewal_parent | object | {"name": "", "id": "", "_acl": {"fields": [], "_hash": "654d337e0e912edaa00dbb0fb3dc3c17"}} |
|  |  |  |  |  |  | renewal_parent._acl | object |  |
|  |  |  |  |  |  | renewal_parent._acl._hash | string |  |
|  |  |  |  |  |  | renewal_parent._acl.fields | array |  |
|  |  |  |  |  |  | renewal_parent.id | string |  |
|  |  |  |  |  |  | renewal_parent.name | string |  |
|  |  |  |  |  |  | team_count_link | object | {"team_count": "", "id": "1", "_acl": {"fields": [], "_hash": "654d337e0e912edaa00dbb0fb3dc3c17"}} |
|  |  |  |  |  |  | team_count_link._acl | object |  |
|  |  |  |  |  |  | team_count_link._acl._hash | string |  |
|  |  |  |  |  |  | team_count_link._acl.fields | array |  |
|  |  |  |  |  |  | team_count_link.id | string |  |
|  |  |  |  |  |  | team_count_link.team_count | string |  |

## Accounts

| Entity Schema Title | Entity Schema Fields | Entity Schema Types | Readonly | Possible Values | Reference Collection | Find By ID Object Fields | Find By ID Types | Value |
|---------------------|----------------------|---------------------|----------|-----------------|----------------------|--------------------------|------------------|-------|
|  | account_type | string | false |  |  | account_type | string | Customer |
|  | annual_revenue | integer | false |  |  | annual_revenue | string | > $10,000,000,000 |
|  | assigned_user_id | string | false |  | users | assigned_user_id | string | seed_chris_id |
|  | billing_address_city | string | false |  |  | billing_address_city | string | Orlando |
|  | billing_address_country | string | false |  |  | billing_address_country | string | USA |
|  | billing_address_postalcode | string | false |  |  | billing_address_postalcode | string | 32806 |
|  | billing_address_state | string | false |  |  | billing_address_state | string | Florida |
|  | billing_address_street | string | false |  |  | billing_address_street | string | 481 Ontario Ave |
|  | billing_address_street_2 | string | false |  |  | billing_address_street_2 | string |  |
|  | billing_address_street_3 | string | false |  |  | billing_address_street_3 | string |  |
|  | billing_address_street_4 | string | false |  |  | billing_address_street_4 | string |  |
|  | business_center_id | string | false |  |  | business_center_id | string | 4a40f8aa-8831-11e9-9e1a-069335ab1e28 |
|  | campaign_id | string | false |  |  | campaign_id | string |  |
|  | created_by | string | false |  |  | created_by | string | 1 |
|  | date_entered | string | false |  |  | date_entered | string | 2025-05-14T19:07:59+05:00 |
|  | date_modified | string | false |  |  | date_modified | string | 2025-05-14T19:48:35+05:00 |
|  | deleted | boolean | false |  |  | deleted | boolean | False |
|  | description | string | false |  |  | description | string | This potential customer is a referral from ABC Bank (Judy Smith). |
|  | duns_num | string | false |  |  | duns_num | string | 952100852 |
|  | email | array | false |  |  | email | array | [{"email_address": "contact@insightmarketinginc.com", "invalid_email": false, "opt_out": false, "email_address_id": "d76efbec-30cc-11f0-b385-99f7c3e06566", "primary_address": true, "reply_to_address": false}] |
|  | email1 | string | false |  |  | email1 | string | contact@insightmarketinginc.com |
|  | email2 | string | false |  |  | email2 | string |  |
|  | email[] | object | false |  |  | email[] | object |  |
|  | email[].email_address | string | false |  |  | email[].email_address | string |  |
|  | email[].email_address_id | string | false |  |  | email[].email_address_id | string |  |
|  | email[].invalid_email | boolean | false |  |  | email[].invalid_email | boolean |  |
|  | email[].opt_out | boolean | false |  |  | email[].opt_out | boolean |  |
|  | email[].primary_address | boolean | false |  |  | email[].primary_address | boolean |  |
|  | email[].reply_to_address | boolean | false |  |  | email[].reply_to_address | boolean |  |
|  | email_opt_out | boolean | false |  |  | email_opt_out | boolean | False |
|  | employees | integer | false |  |  | employees | string | >10,000 |
|  | facebook | string | false |  |  | facebook | string |  |
|  | following | boolean | false |  |  | following | boolean | False |
|  | geocode_status | string | false |  |  | geocode_status | string |  |
|  | googleplus | string | false |  |  | googleplus | string |  |
|  | id | string | true |  |  | id | string | d76d391a-30cc-11f0-a99c-1d1bbea39a2d |
|  | industry | string | false |  |  | industry | string | Utilities |
|  | invalid_email | boolean | false |  |  | invalid_email | boolean | False |
|  | is_escalated | boolean | false |  |  | is_escalated | boolean | False |
|  | latitude_c | string | false |  |  | latitude_c | string | 28.5021966 |
|  | longitude_c | string | false |  |  | longitude_c | string | -81.355642 |
|  | modified_user_id | string | false |  |  | modified_user_id | string | 1 |
|  | my_favorite | boolean | false |  |  | my_favorite | boolean | False |
|  | *name | string | false |  |  | name | string | Insight Marketing Inc |
|  | next_renewal_date | string | false |  |  | next_renewal_date | string | 2024-07-10 |
|  | ownership | string | false |  |  | ownership | string | Bronnbaum Technologies |
|  | parent_id | string | false |  |  | parent_id | string |  |
|  | parent_name | string | false |  |  | parent_name | string |  |
|  | phone_alternate | string | false |  |  | phone_alternate | string | +1 - 573 - 583 - 6446 |
|  | phone_fax | string | false |  |  | phone_fax | string | +1 - 694 - 135 - 3012 |
|  | phone_office | string | false |  |  | phone_office | string | +1 - 672 - 854 - 9798 |
|  | rating | string | false |  |  | rating | string | 5 |
|  | service_level | string | false |  |  | service_level | string | T4 |
|  | shipping_address_city | string | false |  |  | shipping_address_city | string | Orlando |
|  | shipping_address_country | string | false |  |  | shipping_address_country | string | USA |
|  | shipping_address_postalcode | string | false |  |  | shipping_address_postalcode | string | 32806 |
|  | shipping_address_state | string | false |  |  | shipping_address_state | string | Florida |
|  | shipping_address_street | string | false |  |  | shipping_address_street | string | 481 Ontario Ave |
|  | shipping_address_street_2 | string | false |  |  | shipping_address_street_2 | string |  |
|  | shipping_address_street_3 | string | false |  |  | shipping_address_street_3 | string |  |
|  | shipping_address_street_4 | string | false |  |  | shipping_address_street_4 | string |  |
|  | sic_code | string | false |  |  | sic_code | string | 76451 |
|  | tag | array | false |  |  | tag | array | [] |
|  | team_count | string | false |  |  | team_count | string |  |
|  | ticker_symbol | string | false |  |  | ticker_symbol | string | BFC |
|  | twitter | string | false |  |  | twitter | string | insight |
|  | website | string | false |  |  | website | string | http://www.insightmarketinginc.com |
|  | <span style='color:red'>***teams***</span> | array | false |  |  |  |  |  |
|  |  |  |  |  |  | _acl | object | {"fields": {}} |
|  |  |  |  |  |  | _acl.fields | object |  |
|  |  |  |  |  |  | _module | string | Accounts |
|  |  |  |  |  |  | assigned_user_link | object | {"full_name": "Chris Olliver", "id": "seed_chris_id", "_acl": {"fields": [], "_hash": "654d337e0e912edaa00dbb0fb3dc3c17"}} |
|  |  |  |  |  |  | assigned_user_link._acl | object |  |
|  |  |  |  |  |  | assigned_user_link._acl._hash | string |  |
|  |  |  |  |  |  | assigned_user_link._acl.fields | array |  |
|  |  |  |  |  |  | assigned_user_link.full_name | string |  |
|  |  |  |  |  |  | assigned_user_link.id | string |  |
|  |  |  |  |  |  | assigned_user_name | string | Chris Olliver |
|  |  |  |  |  |  | business_center_name | string | EMEA Business Center |
|  |  |  |  |  |  | business_centers | object | {"name": "EMEA Business Center", "id": "4a40f8aa-8831-11e9-9e1a-069335ab1e28", "_acl": {"fields": [], "_hash": "654d337e0e912edaa00dbb0fb3dc3c17"}} |
|  |  |  |  |  |  | business_centers._acl | object |  |
|  |  |  |  |  |  | business_centers._acl._hash | string |  |
|  |  |  |  |  |  | business_centers._acl.fields | array |  |
|  |  |  |  |  |  | business_centers.id | string |  |
|  |  |  |  |  |  | business_centers.name | string |  |
|  |  |  |  |  |  | campaign_accounts | object | {"name": "", "id": "", "_acl": {"fields": {"peoplewhoopened": {"create": "no", "write": "no", "license": "no"}, "peoplewhoclicked": {"create": "no", "write": "no", "license": "no"}, "bounced": {"create": "no", "write": "no", "license": "no"}, "notreported": {"create": "no", "write": "no", "license": "no"}, "delivered": {"create": "no", "write": "no", "license": "no"}, "social": {"create": "no", "write": "no", "license": "no"}, "sent": {"create": "no", "write": "no", "license": "no"}, "postdate": {"create": "no", "write": "no", "license": "no"}, "forwards": {"create": "no", "write": "no", "license": "no"}, "unopened": {"create": "no", "write": "no", "license": "no"}, "unsubscribed": {"create": "no", "write": "no", "license": "no"}, "totalopens": {"create": "no", "write": "no", "license": "no"}, "totalclicks": {"create": "no", "write": "no", "license": "no"}}, "_hash": "ea0dd9a7291770652f6587c8f1f4e1f9"}} |
|  |  |  |  |  |  | campaign_accounts._acl | object |  |
|  |  |  |  |  |  | campaign_accounts._acl._hash | string |  |
|  |  |  |  |  |  | campaign_accounts._acl.fields | object |  |
|  |  |  |  |  |  | campaign_accounts._acl.fields.bounced | object |  |
|  |  |  |  |  |  | campaign_accounts._acl.fields.bounced.create | string |  |
|  |  |  |  |  |  | campaign_accounts._acl.fields.bounced.license | string |  |
|  |  |  |  |  |  | campaign_accounts._acl.fields.bounced.write | string |  |
|  |  |  |  |  |  | campaign_accounts._acl.fields.delivered | object |  |
|  |  |  |  |  |  | campaign_accounts._acl.fields.delivered.create | string |  |
|  |  |  |  |  |  | campaign_accounts._acl.fields.delivered.license | string |  |
|  |  |  |  |  |  | campaign_accounts._acl.fields.delivered.write | string |  |
|  |  |  |  |  |  | campaign_accounts._acl.fields.forwards | object |  |
|  |  |  |  |  |  | campaign_accounts._acl.fields.forwards.create | string |  |
|  |  |  |  |  |  | campaign_accounts._acl.fields.forwards.license | string |  |
|  |  |  |  |  |  | campaign_accounts._acl.fields.forwards.write | string |  |
|  |  |  |  |  |  | campaign_accounts._acl.fields.notreported | object |  |
|  |  |  |  |  |  | campaign_accounts._acl.fields.notreported.create | string |  |
|  |  |  |  |  |  | campaign_accounts._acl.fields.notreported.license | string |  |
|  |  |  |  |  |  | campaign_accounts._acl.fields.notreported.write | string |  |
|  |  |  |  |  |  | campaign_accounts._acl.fields.peoplewhoclicked | object |  |
|  |  |  |  |  |  | campaign_accounts._acl.fields.peoplewhoclicked.create | string |  |
|  |  |  |  |  |  | campaign_accounts._acl.fields.peoplewhoclicked.license | string |  |
|  |  |  |  |  |  | campaign_accounts._acl.fields.peoplewhoclicked.write | string |  |
|  |  |  |  |  |  | campaign_accounts._acl.fields.peoplewhoopened | object |  |
|  |  |  |  |  |  | campaign_accounts._acl.fields.peoplewhoopened.create | string |  |
|  |  |  |  |  |  | campaign_accounts._acl.fields.peoplewhoopened.license | string |  |
|  |  |  |  |  |  | campaign_accounts._acl.fields.peoplewhoopened.write | string |  |
|  |  |  |  |  |  | campaign_accounts._acl.fields.postdate | object |  |
|  |  |  |  |  |  | campaign_accounts._acl.fields.postdate.create | string |  |
|  |  |  |  |  |  | campaign_accounts._acl.fields.postdate.license | string |  |
|  |  |  |  |  |  | campaign_accounts._acl.fields.postdate.write | string |  |
|  |  |  |  |  |  | campaign_accounts._acl.fields.sent | object |  |
|  |  |  |  |  |  | campaign_accounts._acl.fields.sent.create | string |  |
|  |  |  |  |  |  | campaign_accounts._acl.fields.sent.license | string |  |
|  |  |  |  |  |  | campaign_accounts._acl.fields.sent.write | string |  |
|  |  |  |  |  |  | campaign_accounts._acl.fields.social | object |  |
|  |  |  |  |  |  | campaign_accounts._acl.fields.social.create | string |  |
|  |  |  |  |  |  | campaign_accounts._acl.fields.social.license | string |  |
|  |  |  |  |  |  | campaign_accounts._acl.fields.social.write | string |  |
|  |  |  |  |  |  | campaign_accounts._acl.fields.totalclicks | object |  |
|  |  |  |  |  |  | campaign_accounts._acl.fields.totalclicks.create | string |  |
|  |  |  |  |  |  | campaign_accounts._acl.fields.totalclicks.license | string |  |
|  |  |  |  |  |  | campaign_accounts._acl.fields.totalclicks.write | string |  |
|  |  |  |  |  |  | campaign_accounts._acl.fields.totalopens | object |  |
|  |  |  |  |  |  | campaign_accounts._acl.fields.totalopens.create | string |  |
|  |  |  |  |  |  | campaign_accounts._acl.fields.totalopens.license | string |  |
|  |  |  |  |  |  | campaign_accounts._acl.fields.totalopens.write | string |  |
|  |  |  |  |  |  | campaign_accounts._acl.fields.unopened | object |  |
|  |  |  |  |  |  | campaign_accounts._acl.fields.unopened.create | string |  |
|  |  |  |  |  |  | campaign_accounts._acl.fields.unopened.license | string |  |
|  |  |  |  |  |  | campaign_accounts._acl.fields.unopened.write | string |  |
|  |  |  |  |  |  | campaign_accounts._acl.fields.unsubscribed | object |  |
|  |  |  |  |  |  | campaign_accounts._acl.fields.unsubscribed.create | string |  |
|  |  |  |  |  |  | campaign_accounts._acl.fields.unsubscribed.license | string |  |
|  |  |  |  |  |  | campaign_accounts._acl.fields.unsubscribed.write | string |  |
|  |  |  |  |  |  | campaign_accounts.id | string |  |
|  |  |  |  |  |  | campaign_accounts.name | string |  |
|  |  |  |  |  |  | campaign_name | string |  |
|  |  |  |  |  |  | created_by_link | object | {"full_name": "Jen Smith", "id": "1", "_acl": {"fields": [], "_hash": "654d337e0e912edaa00dbb0fb3dc3c17"}} |
|  |  |  |  |  |  | created_by_link._acl | object |  |
|  |  |  |  |  |  | created_by_link._acl._hash | string |  |
|  |  |  |  |  |  | created_by_link._acl.fields | array |  |
|  |  |  |  |  |  | created_by_link.full_name | string |  |
|  |  |  |  |  |  | created_by_link.id | string |  |
|  |  |  |  |  |  | created_by_name | string | Jen Smith |
|  |  |  |  |  |  | dri_workflow_template_id | string |  |
|  |  |  |  |  |  | dri_workflow_template_link | object | {"name": "", "id": "", "_acl": {"fields": [], "_hash": "654d337e0e912edaa00dbb0fb3dc3c17"}} |
|  |  |  |  |  |  | dri_workflow_template_link._acl | object |  |
|  |  |  |  |  |  | dri_workflow_template_link._acl._hash | string |  |
|  |  |  |  |  |  | dri_workflow_template_link._acl.fields | array |  |
|  |  |  |  |  |  | dri_workflow_template_link.id | string |  |
|  |  |  |  |  |  | dri_workflow_template_link.name | string |  |
|  |  |  |  |  |  | dri_workflow_template_name | string |  |
|  |  |  |  |  |  | email_addresses_non_primary | string |  |
|  |  |  |  |  |  | hint_account_facebook_handle | string |  |
|  |  |  |  |  |  | hint_account_fiscal_year_end | string |  |
|  |  |  |  |  |  | hint_account_founded_year | string |  |
|  |  |  |  |  |  | hint_account_industry | string |  |
|  |  |  |  |  |  | hint_account_industry_tags | string |  |
|  |  |  |  |  |  | hint_account_location | string |  |
|  |  |  |  |  |  | hint_account_logo | string |  |
|  |  |  |  |  |  | hint_account_naics_code_lbl | string |  |
|  |  |  |  |  |  | hint_account_pic | string |  |
|  |  |  |  |  |  | hint_account_size | string |  |
|  |  |  |  |  |  | last_interaction_date | string | 2025-04-04T16:30:00+05:00 |
|  |  |  |  |  |  | last_interaction_parent_id | string | f68f9e40-30cd-11f0-b5df-f34e281fb0c4 |
|  |  |  |  |  |  | last_interaction_parent_name | string | Contract detail review |
|  |  |  |  |  |  | last_interaction_parent_type | string | Calls |
|  |  |  |  |  |  | locked_fields | array | [] |
|  |  |  |  |  |  | member_of | object | {"name": "", "id": "", "_acl": {"fields": [], "_hash": "654d337e0e912edaa00dbb0fb3dc3c17"}} |
|  |  |  |  |  |  | member_of._acl | object |  |
|  |  |  |  |  |  | member_of._acl._hash | string |  |
|  |  |  |  |  |  | member_of._acl.fields | array |  |
|  |  |  |  |  |  | member_of.id | string |  |
|  |  |  |  |  |  | member_of.name | string |  |
|  |  |  |  |  |  | modified_by_name | string | Jen Smith |
|  |  |  |  |  |  | modified_user_link | object | {"full_name": "Jen Smith", "id": "1", "_acl": {"fields": [], "_hash": "654d337e0e912edaa00dbb0fb3dc3c17"}} |
|  |  |  |  |  |  | modified_user_link._acl | object |  |
|  |  |  |  |  |  | modified_user_link._acl._hash | string |  |
|  |  |  |  |  |  | modified_user_link._acl.fields | array |  |
|  |  |  |  |  |  | modified_user_link.full_name | string |  |
|  |  |  |  |  |  | modified_user_link.id | string |  |
|  |  |  |  |  |  | perform_sugar_action | boolean | False |
|  |  |  |  |  |  | sync_key | string |  |
|  |  |  |  |  |  | team_count_link | object | {"team_count": "", "id": "1", "_acl": {"fields": [], "_hash": "654d337e0e912edaa00dbb0fb3dc3c17"}} |
|  |  |  |  |  |  | team_count_link._acl | object |  |
|  |  |  |  |  |  | team_count_link._acl._hash | string |  |
|  |  |  |  |  |  | team_count_link._acl.fields | array |  |
|  |  |  |  |  |  | team_count_link.id | string |  |
|  |  |  |  |  |  | team_count_link.team_count | string |  |
|  |  |  |  |  |  | team_name | array | [{"id": "1", "name": "Global", "name_2": "", "primary": true, "selected": false}] |
|  |  |  |  |  |  | team_name[] | object |  |
|  |  |  |  |  |  | team_name[].id | string |  |
|  |  |  |  |  |  | team_name[].name | string |  |
|  |  |  |  |  |  | team_name[].name_2 | string |  |
|  |  |  |  |  |  | team_name[].primary | boolean |  |
|  |  |  |  |  |  | team_name[].selected | boolean |  |
|  |  |  |  |  |  | widget_next_renewal_date | string |  |

## Contacts

| Entity Schema Title | Entity Schema Fields | Entity Schema Types | Readonly | Possible Values | Reference Collection | Find By ID Object Fields | Find By ID Types | Value |
|---------------------|----------------------|---------------------|----------|-----------------|----------------------|--------------------------|------------------|-------|
|  | accept_status_id | string | false |  |  | accept_status_id | string |  |
|  | accept_status_name | string | false |  |  | accept_status_name | string |  |
|  | account_id | string | false |  | accounts | account_id | string | d8132546-30cc-11f0-8a5f-b7c7c1b99788 |
|  | alt_address_city | string | false |  |  | alt_address_city | string | San Francisco |
|  | alt_address_country | string | false |  |  | alt_address_country | string | USA |
|  | alt_address_postalcode | string | false |  |  | alt_address_postalcode | string | 94110 |
|  | alt_address_state | string | false |  |  | alt_address_state | string | California |
|  | alt_address_street | string | false |  |  | alt_address_street | string | 763 Guerrero St |
|  | alt_address_street_2 | string | false |  |  | alt_address_street_2 | string |  |
|  | alt_address_street_3 | string | false |  |  | alt_address_street_3 | string |  |
|  | assigned_user_id | string | false |  | users | assigned_user_id | string | seed_chris_id |
|  | assistant | string | false |  |  | assistant | string |  |
|  | assistant_phone | string | false |  |  | assistant_phone | string |  |
|  | birthdate | string | false |  |  | birthdate | string |  |
|  | calls | object | false |  |  | calls | object | {"id": ""} |
|  | calls.id | string | false |  |  | calls.id | string |  |
|  | campaign_id | string | false |  |  | campaign_id | string |  |
|  | created_by | string | false |  | users | created_by | string | 1 |
|  | date_entered | string | false |  |  | date_entered | string | 2025-05-14T19:25:56+05:00 |
|  | date_modified | string | false |  |  | date_modified | string | 2025-05-14T19:47:40+05:00 |
|  | deleted | boolean | false |  |  | deleted | boolean | False |
|  | department | string | false |  |  | department | string | Sales |
|  | description | string | false |  |  | description | string |  |
|  | do_not_call | boolean | false |  |  | do_not_call | boolean | False |
|  | email | array | false |  |  | email | array | [{"email_address": "linda.holiday@yahoo.com", "invalid_email": false, "opt_out": false, "email_address_id": "633ec3fa-30d2-11f0-a0c2-8fa31453d866", "primary_address": true, "reply_to_address": false}] |
|  | email1 | string | false |  |  | email1 | string | linda.holiday@yahoo.com |
|  | email2 | string | false |  |  | email2 | string |  |
|  | email[] | object | false |  |  | email[] | object |  |
|  | email[].email_address | string | false |  |  | email[].email_address | string |  |
|  | email[].email_address_id | string | false |  |  | email[].email_address_id | string |  |
|  | email[].invalid_email | boolean | false |  |  | email[].invalid_email | boolean |  |
|  | email[].opt_out | boolean | false |  |  | email[].opt_out | boolean |  |
|  | email[].primary_address | boolean | false |  |  | email[].primary_address | boolean |  |
|  | email[].reply_to_address | boolean | false |  |  | email[].reply_to_address | boolean |  |
|  | email_opt_out | boolean | false |  |  | email_opt_out | boolean | False |
|  | entry_source | string | false |  |  | entry_source | string | internal |
|  | facebook | string | false |  |  | facebook | string |  |
|  | first_name | string | false |  |  | first_name | string | Linda |
|  | following | boolean | false |  |  | following | boolean | False |
|  | full_name | string | false |  |  | full_name | string | Linda Holiday |
|  | googleplus | string | false |  |  | googleplus | string |  |
|  | id | string | true |  |  | id | string | 593db44a-30cf-11f0-8746-4f8477825d38 |
|  | invalid_email | boolean | false |  |  | invalid_email | boolean | False |
|  | last_name | string | false |  |  | last_name | string | Holiday |
|  | latitude_c | string | false |  |  | latitude_c | string | 41.87118 |
|  | lead_source | string | false |  |  | lead_source | string | Email |
|  | longitude_c | string | false |  |  | longitude_c | string | -87.7055352 |
|  | market_interest_prediction_score | string | false |  |  | market_interest_prediction_score | string |  |
|  | market_score | string | false |  |  | market_score | null | None |
|  | meetings | object | false |  |  | meetings | object | {"id": ""} |
|  | meetings.id | string | false |  |  | meetings.id | string |  |
|  | mkto_sync | boolean | false |  |  | mkto_sync | boolean | False |
|  | modified_user_id | string | false |  | users | modified_user_id | string | 1 |
|  | my_favorite | boolean | false |  |  | my_favorite | boolean | False |
|  | name | string | false |  |  | name | string | Linda Holiday |
|  | opportunities | object | false |  |  | opportunities | object | {"id": ""} |
|  | opportunities.id | string | false |  |  | opportunities.id | string |  |
|  | opportunity_role_id | string | false |  |  | opportunity_role_id | string |  |
|  | phone_fax | string | false |  |  | phone_fax | string | +1 - 741 - 478 - 3827 |
|  | phone_home | string | false |  |  | phone_home | string | +1 - 236 - 100 - 7476 |
|  | phone_mobile | string | false |  |  | phone_mobile | string | +1 - 912 - 574 - 1060 |
|  | phone_other | string | false |  |  | phone_other | string |  |
|  | phone_work | string | false |  |  | phone_work | string | +1 - 928 - 629 - 8243 |
|  | primary_address_city | string | false |  |  | primary_address_city | string | Chicago |
|  | primary_address_country | string | false |  |  | primary_address_country | string | USA |
|  | primary_address_postalcode | string | false |  |  | primary_address_postalcode | string | 60612 |
|  | primary_address_state | string | false |  |  | primary_address_state | string | Illinois |
|  | primary_address_street | string | false |  |  | primary_address_street | string | 803 S Kedzie Ave |
|  | primary_address_street_2 | string | false |  |  | primary_address_street_2 | string |  |
|  | primary_address_street_3 | string | false |  |  | primary_address_street_3 | string |  |
|  | reports_to_id | string | false |  | users | reports_to_id | string |  |
|  | salutation | string | false |  |  | salutation | string |  |
|  | site_user_id | string | false |  |  | site_user_id | string | 4a006b5846ecee03b7e63e4653755dab676aee8d98d15a2eac7ecafd19dd2fee |
|  | source_id | string | false |  |  | source_id | string |  |
|  | source_meta | string | false |  |  | source_meta | string |  |
|  | source_type | string | false |  |  | source_type | string |  |
|  | sync_key | string | false |  |  | sync_key | string |  |
|  | tag | array | false |  |  | tag | array | [{"id": "d93687a6-30cc-11f0-8530-69003c7f6309", "name": "goto data", "tags__name_lower": "goto data"}] |
|  | tag[] | object | false |  |  | tag[] | object |  |
|  | tag[].id | string | false |  |  | tag[].id | string |  |
|  | tag[].name | string | false |  |  | tag[].name | string |  |
|  | tag[].tags__name_lower | string | false |  |  | tag[].tags__name_lower | string |  |
|  | team_count | string | false |  |  | team_count | string |  |
|  | title | string | false |  |  | title | string | Senior Sales Associate |
|  | twitter | string | false |  |  | twitter | string | LindaHoliday23 |
|  | <span style='color:red'>***team***</span> | array | false |  |  |  |  |  |
|  |  |  |  |  |  | _acl | object | {"fields": {}} |
|  |  |  |  |  |  | _acl.fields | object |  |
|  |  |  |  |  |  | _module | string | Contacts |
|  |  |  |  |  |  | accept_status_calls | string |  |
|  |  |  |  |  |  | accept_status_meetings | string |  |
|  |  |  |  |  |  | accept_status_messages | string |  |
|  |  |  |  |  |  | account_name | string | Kringle Bell IncKA Tower & Co |
|  |  |  |  |  |  | accounts | object | {"name": "Kringle Bell IncKA Tower & Co", "id": "d8132546-30cc-11f0-8a5f-b7c7c1b99788", "_acl": {"fields": [], "_hash": "654d337e0e912edaa00dbb0fb3dc3c17"}} |
|  |  |  |  |  |  | accounts._acl | object |  |
|  |  |  |  |  |  | accounts._acl._hash | string |  |
|  |  |  |  |  |  | accounts._acl.fields | array |  |
|  |  |  |  |  |  | accounts.id | string |  |
|  |  |  |  |  |  | accounts.name | string |  |
|  |  |  |  |  |  | assigned_user_link | object | {"full_name": "Chris Olliver", "id": "seed_chris_id", "_acl": {"fields": [], "_hash": "654d337e0e912edaa00dbb0fb3dc3c17"}} |
|  |  |  |  |  |  | assigned_user_link._acl | object |  |
|  |  |  |  |  |  | assigned_user_link._acl._hash | string |  |
|  |  |  |  |  |  | assigned_user_link._acl.fields | array |  |
|  |  |  |  |  |  | assigned_user_link.full_name | string |  |
|  |  |  |  |  |  | assigned_user_link.id | string |  |
|  |  |  |  |  |  | assigned_user_name | string | Chris Olliver |
|  |  |  |  |  |  | business_center_id | string | 4a40f8aa-8831-11e9-9e1a-069335ab1e28 |
|  |  |  |  |  |  | business_center_name | string | EMEA Business Center |
|  |  |  |  |  |  | business_centers | object | {"name": "EMEA Business Center", "id": "4a40f8aa-8831-11e9-9e1a-069335ab1e28", "_acl": {"fields": [], "_hash": "654d337e0e912edaa00dbb0fb3dc3c17"}} |
|  |  |  |  |  |  | business_centers._acl | object |  |
|  |  |  |  |  |  | business_centers._acl._hash | string |  |
|  |  |  |  |  |  | business_centers._acl.fields | array |  |
|  |  |  |  |  |  | business_centers.id | string |  |
|  |  |  |  |  |  | business_centers.name | string |  |
|  |  |  |  |  |  | c_accept_status_fields | string |  |
|  |  |  |  |  |  | campaign_contacts | object | {"name": "", "id": "", "_acl": {"fields": {"peoplewhoopened": {"create": "no", "write": "no", "license": "no"}, "peoplewhoclicked": {"create": "no", "write": "no", "license": "no"}, "bounced": {"create": "no", "write": "no", "license": "no"}, "notreported": {"create": "no", "write": "no", "license": "no"}, "delivered": {"create": "no", "write": "no", "license": "no"}, "social": {"create": "no", "write": "no", "license": "no"}, "sent": {"create": "no", "write": "no", "license": "no"}, "postdate": {"create": "no", "write": "no", "license": "no"}, "forwards": {"create": "no", "write": "no", "license": "no"}, "unopened": {"create": "no", "write": "no", "license": "no"}, "unsubscribed": {"create": "no", "write": "no", "license": "no"}, "totalopens": {"create": "no", "write": "no", "license": "no"}, "totalclicks": {"create": "no", "write": "no", "license": "no"}}, "_hash": "ea0dd9a7291770652f6587c8f1f4e1f9"}} |
|  |  |  |  |  |  | campaign_contacts._acl | object |  |
|  |  |  |  |  |  | campaign_contacts._acl._hash | string |  |
|  |  |  |  |  |  | campaign_contacts._acl.fields | object |  |
|  |  |  |  |  |  | campaign_contacts._acl.fields.bounced | object |  |
|  |  |  |  |  |  | campaign_contacts._acl.fields.bounced.create | string |  |
|  |  |  |  |  |  | campaign_contacts._acl.fields.bounced.license | string |  |
|  |  |  |  |  |  | campaign_contacts._acl.fields.bounced.write | string |  |
|  |  |  |  |  |  | campaign_contacts._acl.fields.delivered | object |  |
|  |  |  |  |  |  | campaign_contacts._acl.fields.delivered.create | string |  |
|  |  |  |  |  |  | campaign_contacts._acl.fields.delivered.license | string |  |
|  |  |  |  |  |  | campaign_contacts._acl.fields.delivered.write | string |  |
|  |  |  |  |  |  | campaign_contacts._acl.fields.forwards | object |  |
|  |  |  |  |  |  | campaign_contacts._acl.fields.forwards.create | string |  |
|  |  |  |  |  |  | campaign_contacts._acl.fields.forwards.license | string |  |
|  |  |  |  |  |  | campaign_contacts._acl.fields.forwards.write | string |  |
|  |  |  |  |  |  | campaign_contacts._acl.fields.notreported | object |  |
|  |  |  |  |  |  | campaign_contacts._acl.fields.notreported.create | string |  |
|  |  |  |  |  |  | campaign_contacts._acl.fields.notreported.license | string |  |
|  |  |  |  |  |  | campaign_contacts._acl.fields.notreported.write | string |  |
|  |  |  |  |  |  | campaign_contacts._acl.fields.peoplewhoclicked | object |  |
|  |  |  |  |  |  | campaign_contacts._acl.fields.peoplewhoclicked.create | string |  |
|  |  |  |  |  |  | campaign_contacts._acl.fields.peoplewhoclicked.license | string |  |
|  |  |  |  |  |  | campaign_contacts._acl.fields.peoplewhoclicked.write | string |  |
|  |  |  |  |  |  | campaign_contacts._acl.fields.peoplewhoopened | object |  |
|  |  |  |  |  |  | campaign_contacts._acl.fields.peoplewhoopened.create | string |  |
|  |  |  |  |  |  | campaign_contacts._acl.fields.peoplewhoopened.license | string |  |
|  |  |  |  |  |  | campaign_contacts._acl.fields.peoplewhoopened.write | string |  |
|  |  |  |  |  |  | campaign_contacts._acl.fields.postdate | object |  |
|  |  |  |  |  |  | campaign_contacts._acl.fields.postdate.create | string |  |
|  |  |  |  |  |  | campaign_contacts._acl.fields.postdate.license | string |  |
|  |  |  |  |  |  | campaign_contacts._acl.fields.postdate.write | string |  |
|  |  |  |  |  |  | campaign_contacts._acl.fields.sent | object |  |
|  |  |  |  |  |  | campaign_contacts._acl.fields.sent.create | string |  |
|  |  |  |  |  |  | campaign_contacts._acl.fields.sent.license | string |  |
|  |  |  |  |  |  | campaign_contacts._acl.fields.sent.write | string |  |
|  |  |  |  |  |  | campaign_contacts._acl.fields.social | object |  |
|  |  |  |  |  |  | campaign_contacts._acl.fields.social.create | string |  |
|  |  |  |  |  |  | campaign_contacts._acl.fields.social.license | string |  |
|  |  |  |  |  |  | campaign_contacts._acl.fields.social.write | string |  |
|  |  |  |  |  |  | campaign_contacts._acl.fields.totalclicks | object |  |
|  |  |  |  |  |  | campaign_contacts._acl.fields.totalclicks.create | string |  |
|  |  |  |  |  |  | campaign_contacts._acl.fields.totalclicks.license | string |  |
|  |  |  |  |  |  | campaign_contacts._acl.fields.totalclicks.write | string |  |
|  |  |  |  |  |  | campaign_contacts._acl.fields.totalopens | object |  |
|  |  |  |  |  |  | campaign_contacts._acl.fields.totalopens.create | string |  |
|  |  |  |  |  |  | campaign_contacts._acl.fields.totalopens.license | string |  |
|  |  |  |  |  |  | campaign_contacts._acl.fields.totalopens.write | string |  |
|  |  |  |  |  |  | campaign_contacts._acl.fields.unopened | object |  |
|  |  |  |  |  |  | campaign_contacts._acl.fields.unopened.create | string |  |
|  |  |  |  |  |  | campaign_contacts._acl.fields.unopened.license | string |  |
|  |  |  |  |  |  | campaign_contacts._acl.fields.unopened.write | string |  |
|  |  |  |  |  |  | campaign_contacts._acl.fields.unsubscribed | object |  |
|  |  |  |  |  |  | campaign_contacts._acl.fields.unsubscribed.create | string |  |
|  |  |  |  |  |  | campaign_contacts._acl.fields.unsubscribed.license | string |  |
|  |  |  |  |  |  | campaign_contacts._acl.fields.unsubscribed.write | string |  |
|  |  |  |  |  |  | campaign_contacts.id | string |  |
|  |  |  |  |  |  | campaign_contacts.name | string |  |
|  |  |  |  |  |  | campaign_name | string |  |
|  |  |  |  |  |  | cookie_consent | boolean | False |
|  |  |  |  |  |  | cookie_consent_received_on | string |  |
|  |  |  |  |  |  | created_by_link | object | {"full_name": "Jen Smith", "id": "1", "_acl": {"fields": [], "_hash": "654d337e0e912edaa00dbb0fb3dc3c17"}} |
|  |  |  |  |  |  | created_by_link._acl | object |  |
|  |  |  |  |  |  | created_by_link._acl._hash | string |  |
|  |  |  |  |  |  | created_by_link._acl.fields | array |  |
|  |  |  |  |  |  | created_by_link.full_name | string |  |
|  |  |  |  |  |  | created_by_link.id | string |  |
|  |  |  |  |  |  | created_by_name | string | Jen Smith |
|  |  |  |  |  |  | denorm_account_name | string | Kringle Bell IncKA Tower & Co |
|  |  |  |  |  |  | dnb_principal_id | string | 263865980 |
|  |  |  |  |  |  | dp_business_purpose | array | [] |
|  |  |  |  |  |  | dp_consent_last_updated | string | 2025-05-14 |
|  |  |  |  |  |  | dri_workflow_template_id | string |  |
|  |  |  |  |  |  | dri_workflow_template_link | object | {"name": "", "id": "", "_acl": {"fields": [], "_hash": "654d337e0e912edaa00dbb0fb3dc3c17"}} |
|  |  |  |  |  |  | dri_workflow_template_link._acl | object |  |
|  |  |  |  |  |  | dri_workflow_template_link._acl._hash | string |  |
|  |  |  |  |  |  | dri_workflow_template_link._acl.fields | array |  |
|  |  |  |  |  |  | dri_workflow_template_link.id | string |  |
|  |  |  |  |  |  | dri_workflow_template_link.name | string |  |
|  |  |  |  |  |  | dri_workflow_template_name | string |  |
|  |  |  |  |  |  | email_addresses_non_primary | string |  |
|  |  |  |  |  |  | email_and_name1 | string |  |
|  |  |  |  |  |  | external_user_id | string |  |
|  |  |  |  |  |  | geocode_status | string |  |
|  |  |  |  |  |  | hint_account_annual_revenue | string |  |
|  |  |  |  |  |  | hint_account_description | string |  |
|  |  |  |  |  |  | hint_account_facebook_handle | string |  |
|  |  |  |  |  |  | hint_account_fiscal_year_end | string |  |
|  |  |  |  |  |  | hint_account_founded_year | string |  |
|  |  |  |  |  |  | hint_account_industry | string |  |
|  |  |  |  |  |  | hint_account_location | string |  |
|  |  |  |  |  |  | hint_account_logo | string |  |
|  |  |  |  |  |  | hint_account_naics_code_lbl | string |  |
|  |  |  |  |  |  | hint_account_sic_code_label | string |  |
|  |  |  |  |  |  | hint_account_size | string |  |
|  |  |  |  |  |  | hint_account_twitter_handle | string |  |
|  |  |  |  |  |  | hint_account_website | string |  |
|  |  |  |  |  |  | hint_contact_pic | string |  |
|  |  |  |  |  |  | hint_education | string |  |
|  |  |  |  |  |  | hint_education_2 | string |  |
|  |  |  |  |  |  | hint_facebook | string |  |
|  |  |  |  |  |  | hint_industry_tags | string |  |
|  |  |  |  |  |  | hint_job_2 | string |  |
|  |  |  |  |  |  | hint_phone_1 | string |  |
|  |  |  |  |  |  | hint_phone_2 | string |  |
|  |  |  |  |  |  | hint_photo | string |  |
|  |  |  |  |  |  | hint_twitter | string |  |
|  |  |  |  |  |  | locked_fields | array | [] |
|  |  |  |  |  |  | m_accept_status_fields | string |  |
|  |  |  |  |  |  | mkto_id | null | None |
|  |  |  |  |  |  | mkto_lead_score | string | Email |
|  |  |  |  |  |  | modified_by_name | string | Jen Smith |
|  |  |  |  |  |  | modified_user_link | object | {"full_name": "Jen Smith", "id": "1", "_acl": {"fields": [], "_hash": "654d337e0e912edaa00dbb0fb3dc3c17"}} |
|  |  |  |  |  |  | modified_user_link._acl | object |  |
|  |  |  |  |  |  | modified_user_link._acl._hash | string |  |
|  |  |  |  |  |  | modified_user_link._acl.fields | array |  |
|  |  |  |  |  |  | modified_user_link.full_name | string |  |
|  |  |  |  |  |  | modified_user_link.id | string |  |
|  |  |  |  |  |  | opportunity_role | string |  |
|  |  |  |  |  |  | opportunity_role_fields | string |  |
|  |  |  |  |  |  | perform_sugar_action | boolean | False |
|  |  |  |  |  |  | picture | string | LindaHoliday1747234061 |
|  |  |  |  |  |  | portal_active | boolean | True |
|  |  |  |  |  |  | portal_app | string |  |
|  |  |  |  |  |  | portal_name | string | LindaHoliday23 |
|  |  |  |  |  |  | portal_password | boolean | True |
|  |  |  |  |  |  | portal_password1 | null | None |
|  |  |  |  |  |  | portal_user_company_name | string |  |
|  |  |  |  |  |  | preferred_language | string | en_us |
|  |  |  |  |  |  | report_to_name | string |  |
|  |  |  |  |  |  | reports_to_link | object | {"name": "", "id": "", "_acl": {"fields": {"sf_lastactivity_default": {"create": "no", "write": "no", "license": "no"}}, "_hash": "c69ded8d08ee4170c5d490bf7c5941d7"}} |
|  |  |  |  |  |  | reports_to_link._acl | object |  |
|  |  |  |  |  |  | reports_to_link._acl._hash | string |  |
|  |  |  |  |  |  | reports_to_link._acl.fields | object |  |
|  |  |  |  |  |  | reports_to_link._acl.fields.sf_lastactivity_default | object |  |
|  |  |  |  |  |  | reports_to_link._acl.fields.sf_lastactivity_default.create | string |  |
|  |  |  |  |  |  | reports_to_link._acl.fields.sf_lastactivity_default.license | string |  |
|  |  |  |  |  |  | reports_to_link._acl.fields.sf_lastactivity_default.write | string |  |
|  |  |  |  |  |  | reports_to_link.id | string |  |
|  |  |  |  |  |  | reports_to_link.name | string |  |
|  |  |  |  |  |  | sync_contact | boolean | False |
|  |  |  |  |  |  | team_count_link | object | {"team_count": "", "id": "1", "_acl": {"fields": [], "_hash": "654d337e0e912edaa00dbb0fb3dc3c17"}} |
|  |  |  |  |  |  | team_count_link._acl | object |  |
|  |  |  |  |  |  | team_count_link._acl._hash | string |  |
|  |  |  |  |  |  | team_count_link._acl.fields | array |  |
|  |  |  |  |  |  | team_count_link.id | string |  |
|  |  |  |  |  |  | team_count_link.team_count | string |  |
|  |  |  |  |  |  | team_name | array | [{"id": "East", "name": "East", "name_2": "", "primary": false, "selected": false}, {"id": "1", "name": "Global", "name_2": "", "primary": true, "selected": false}] |
|  |  |  |  |  |  | team_name[] | object |  |
|  |  |  |  |  |  | team_name[].id | string |  |
|  |  |  |  |  |  | team_name[].name | string |  |
|  |  |  |  |  |  | team_name[].name_2 | string |  |
|  |  |  |  |  |  | team_name[].primary | boolean |  |
|  |  |  |  |  |  | team_name[].selected | boolean |  |