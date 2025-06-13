# Differences between fields in SugarCRM.io


## Opportunities

| Entity Schema Title | Entity Schema Fields | Entity Schema Types | Readonly | Possible Values | Reference Collection | Find By ID Object Fields | Find By ID Types | Value |
|---------------------|----------------------|---------------------|----------|-----------------|----------------------|--------------------------|------------------|-------|
|  | account_id | string | false |  | accounts | account_id | str | d890652e-30cc-11f0-9c5b-31b297db6ffd |
|  | ai_opp_conv_bin_accuracy | string | false |  |  | ai_opp_conv_bin_accuracy | null | None |
|  | ai_opp_conv_multiplier | string | false |  |  | ai_opp_conv_multiplier | null | None |
|  | ai_opp_conv_score_absolute | string | false |  |  | ai_opp_conv_score_absolute | null | None |
|  | ai_opp_conv_score_enum | string | false |  |  | ai_opp_conv_score_enum | str |  |
|  | amount | string | false |  |  | amount | str | 34800.000000 |
|  | amount_usdollar | string | false |  |  | amount_usdollar | str | 34800.000000 |
|  | assigned_user_id | string | false |  | users | assigned_user_id | str | seed_will_id |
|  | base_rate | string | false |  |  | base_rate | str | 1.000000 |
|  | best_case | string | false |  |  | best_case | str | 34800.000000 |
|  | campaign_id | string | false |  |  | campaign_id | str |  |
|  | campaign_opportunities | object | false |  |  | campaign_opportunities | object | {"name": "", "id": ""} |
|  | campaign_opportunities.id | string | false |  |  | campaign_opportunities.id | str |  |
|  | campaign_opportunities.name | string | false |  |  | campaign_opportunities.name | str |  |
|  | closed_revenue_line_items | integer | false |  |  | closed_revenue_line_items | int | 0 |
|  | closed_won_revenue_line_items | integer | false |  |  | closed_won_revenue_line_items | int | 0 |
|  | commit_stage | string | false |  |  | commit_stage | str | exclude |
|  | commit_stage_cascade | string | false |  |  | commit_stage_cascade | str |  |
|  | contact_role | string | false |  |  | contact_role | str |  |
|  | created_by | string | false |  | users | created_by | str | 1 |
|  | currency_id | string | false | `US Dollars`, `Euro` |  | currency_id | str | -99 |
|  | currency_name | string | false |  |  | currency_name | str |  |
|  | date_closed | string | false |  |  | date_closed | str | 2025-05-26 |
|  | date_closed_cascade | string | false |  |  | date_closed_cascade | str |  |
|  | date_closed_timestamp | integer | false |  |  | date_closed_timestamp | int | 1748217600 |
|  | date_entered | string | false |  |  | date_entered | str | 2025-05-11T03:00:00+05:00 |
|  | date_modified | string | false |  |  | date_modified | str | 2025-05-14T21:02:38+05:00 |
|  | deleted | boolean | false |  |  | deleted | bool | False |
|  | description | string | false |  |  | description | str |  |
|  | following | boolean | false |  |  | following | bool | False |
|  | forecasted_likely | string | false |  |  | forecasted_likely | str | 0.000000 |
|  | geocode_status | string | false |  |  | geocode_status | str |  |
|  | id | string | true |  |  | id | str | db3f6530-30dc-11f0-9285-fb295c038a96 |
|  | included_revenue_line_items | integer | false |  |  | included_revenue_line_items | int | 0 |
|  | is_escalated | boolean | false |  |  | is_escalated | bool | False |
|  | lead_source | string | false |  |  | lead_source | str |  |
|  | lost | string | false |  |  | lost | str | 0.000000 |
|  | mkto_id | string | false |  |  | mkto_id | null | None |
|  | mkto_sync | boolean | false |  |  | mkto_sync | bool | False |
|  | modified_user_id | string | false |  | users | modified_user_id | str | 1 |
|  | my_favorite | boolean | false |  |  | my_favorite | bool | False |
|  | *name | string | false |  |  | name | str | RRR Advertising Inc. - $34800 - 647 |
|  | next_step | string | false |  |  | next_step | str |  |
|  | opportunity_type | string | false |  |  | opportunity_type | str | Existing Business |
|  | probability | integer | false |  |  | probability | int | 10 |
|  | renewal | boolean | false |  |  | renewal | bool | False |
|  | renewal_parent_id | string | false |  |  | renewal_parent_id | str |  |
|  | renewal_parent_name | string | false |  |  | renewal_parent_name | str |  |
|  | sales_stage | string | false |  |  | sales_stage | str | Prospecting |
|  | sales_stage_cascade | string | false |  |  | sales_stage_cascade | str |  |
|  | sales_status | string | false |  |  | sales_status | str | In Progress |
|  | service_duration_unit | string | false |  |  | service_duration_unit | str |  |
|  | service_duration_unit_cascade | string | false |  |  | service_duration_unit_cascade | str |  |
|  | service_duration_value | integer | false |  |  | service_duration_value | null | None |
|  | service_duration_value_cascade | integer | false |  |  | service_duration_value_cascade | null | None |
|  | service_open_flex_duration_rlis | integer | false |  |  | service_open_flex_duration_rlis | int | 0 |
|  | service_open_revenue_line_items | integer | false |  |  | service_open_revenue_line_items | int | 0 |
|  | service_start_date | string | false |  |  | service_start_date | str |  |
|  | service_start_date_cascade | string | false |  |  | service_start_date_cascade | str |  |
|  | sl_ai_conv_score_c | string | false |  |  | sl_ai_conv_score_c | str | 01_not_likely |
|  | sync_key | string | false |  |  | sync_key | str |  |
|  | tag | array | false |  |  | tag | array | [] |
|  | team_count | string | false |  |  | team_count | str |  |
|  | team_name | array | false |  |  | team_name | array | [{"id": "1", "name": "Global", "name_2": "", "primary": true, "selected": false}] |
|  | total_revenue_line_items | integer | false |  |  | total_revenue_line_items | int | 1 |
|  | widget_amount | string | false |  |  | widget_amount | str |  |
|  | widget_date_closed | string | false |  |  | widget_date_closed | str |  |
|  | widget_sales_stage | string | false |  |  | widget_sales_stage | str |  |
|  | worst_case | string | false |  |  | worst_case | str | 34800.000000 |
|  |  |  |  |  |  | _acl | object | {"fields": {}} |
|  |  |  |  |  |  | _module | str | Opportunities |
|  |  |  |  |  |  | account_name | str | RRR Advertising Inc. |
|  |  |  |  |  |  | accounts | object | {"name": "RRR Advertising Inc.", "id": "d890652e-30cc-11f0-9c5b-31b297db6ffd", "_acl": {"fields": [], "_hash": "654d337e0e912edaa00dbb0fb3dc3c17"}} |
|  |  |  |  |  |  | accounts._acl._hash | str |  |
|  |  |  |  |  |  | accounts.id | str |  |
|  |  |  |  |  |  | accounts.name | str |  |
|  |  |  |  |  |  | ai_opp_close_week_scores | null | None |
|  |  |  |  |  |  | ai_opp_won_score | null | None |
|  |  |  |  |  |  | assigned_user_link | object | {"full_name": "Will Westin", "id": "seed_will_id", "_acl": {"fields": [], "_hash": "654d337e0e912edaa00dbb0fb3dc3c17"}} |
|  |  |  |  |  |  | assigned_user_link._acl._hash | str |  |
|  |  |  |  |  |  | assigned_user_link.full_name | str |  |
|  |  |  |  |  |  | assigned_user_link.id | str |  |
|  |  |  |  |  |  | assigned_user_name | str | Will Westin |
|  |  |  |  |  |  | campaign_name | str |  |
|  |  |  |  |  |  | created_by_link | object | {"full_name": "Jen Smith", "id": "1", "_acl": {"fields": [], "_hash": "654d337e0e912edaa00dbb0fb3dc3c17"}} |
|  |  |  |  |  |  | created_by_link._acl._hash | str |  |
|  |  |  |  |  |  | created_by_link.full_name | str |  |
|  |  |  |  |  |  | created_by_link.id | str |  |
|  |  |  |  |  |  | created_by_name | str | Jen Smith |
|  |  |  |  |  |  | currencies | object | {"name": "", "id": "-99", "_acl": {"fields": [], "_hash": "654d337e0e912edaa00dbb0fb3dc3c17"}, "symbol": ""} |
|  |  |  |  |  |  | currencies._acl._hash | str |  |
|  |  |  |  |  |  | currencies.id | str |  |
|  |  |  |  |  |  | currencies.name | str |  |
|  |  |  |  |  |  | currencies.symbol | str |  |
|  |  |  |  |  |  | currency_symbol | str |  |
|  |  |  |  |  |  | denorm_account_name | str | RRR Advertising Inc. |
|  |  |  |  |  |  | discover_data_c | bool | True |
|  |  |  |  |  |  | dri_workflow_template_id | str |  |
|  |  |  |  |  |  | dri_workflow_template_link | object | {"name": "", "id": "", "_acl": {"fields": [], "_hash": "654d337e0e912edaa00dbb0fb3dc3c17"}} |
|  |  |  |  |  |  | dri_workflow_template_link._acl._hash | str |  |
|  |  |  |  |  |  | dri_workflow_template_link.id | str |  |
|  |  |  |  |  |  | dri_workflow_template_link.name | str |  |
|  |  |  |  |  |  | dri_workflow_template_name | str |  |
|  |  |  |  |  |  | locked_fields | array | [] |
|  |  |  |  |  |  | modified_by_name | str | Jen Smith |
|  |  |  |  |  |  | modified_user_link | object | {"full_name": "Jen Smith", "id": "1", "_acl": {"fields": [], "_hash": "654d337e0e912edaa00dbb0fb3dc3c17"}} |
|  |  |  |  |  |  | modified_user_link._acl._hash | str |  |
|  |  |  |  |  |  | modified_user_link.full_name | str |  |
|  |  |  |  |  |  | modified_user_link.id | str |  |
|  |  |  |  |  |  | perform_sugar_action | bool | False |
|  |  |  |  |  |  | renewal_parent | object | {"name": "", "id": "", "_acl": {"fields": [], "_hash": "654d337e0e912edaa00dbb0fb3dc3c17"}} |
|  |  |  |  |  |  | renewal_parent._acl._hash | str |  |
|  |  |  |  |  |  | renewal_parent.id | str |  |
|  |  |  |  |  |  | renewal_parent.name | str |  |
|  |  |  |  |  |  | team_count_link | object | {"team_count": "", "id": "1", "_acl": {"fields": [], "_hash": "654d337e0e912edaa00dbb0fb3dc3c17"}} |
|  |  |  |  |  |  | team_count_link._acl._hash | str |  |
|  |  |  |  |  |  | team_count_link.id | str |  |
|  |  |  |  |  |  | team_count_link.team_count | str |  |

## Accounts

| Entity Schema Title | Entity Schema Fields | Entity Schema Types | Readonly | Possible Values | Reference Collection | Find By ID Object Fields | Find By ID Types | Value |
|---------------------|----------------------|---------------------|----------|-----------------|----------------------|--------------------------|------------------|-------|
|  | account_type | string | false |  |  | account_type | str | Customer |
|  | annual_revenue | integer | false |  |  | annual_revenue | str | > $10,000,000,000 |
|  | assigned_user_id | string | false |  | users | assigned_user_id | str | seed_chris_id |
|  | billing_address_city | string | false |  |  | billing_address_city | str | Orlando |
|  | billing_address_country | string | false |  |  | billing_address_country | str | USA |
|  | billing_address_postalcode | string | false |  |  | billing_address_postalcode | str | 32806 |
|  | billing_address_state | string | false |  |  | billing_address_state | str | Florida |
|  | billing_address_street | string | false |  |  | billing_address_street | str | 481 Ontario Ave |
|  | billing_address_street_2 | string | false |  |  | billing_address_street_2 | str |  |
|  | billing_address_street_3 | string | false |  |  | billing_address_street_3 | str |  |
|  | billing_address_street_4 | string | false |  |  | billing_address_street_4 | str |  |
|  | business_center_id | string | false |  |  | business_center_id | str | 4a40f8aa-8831-11e9-9e1a-069335ab1e28 |
|  | campaign_id | string | false |  |  | campaign_id | str |  |
|  | created_by | string | false |  |  | created_by | str | 1 |
|  | date_entered | string | false |  |  | date_entered | str | 2025-05-14T19:07:59+05:00 |
|  | date_modified | string | false |  |  | date_modified | str | 2025-05-14T19:48:35+05:00 |
|  | deleted | boolean | false |  |  | deleted | bool | False |
|  | description | string | false |  |  | description | str | This potential customer is a referral from ABC Bank (Judy Smith). |
|  | duns_num | string | false |  |  | duns_num | str | 952100852 |
|  | email | array | false |  |  | email | array | [{"email_address": "contact@insightmarketinginc.com", "invalid_email": false, "opt_out": false, "email_address_id": "d76efbec-30cc-11f0-b385-99f7c3e06566", "primary_address": true, "reply_to_address": false}] |
|  | email1 | string | false |  |  | email1 | str | contact@insightmarketinginc.com |
|  | email2 | string | false |  |  | email2 | str |  |
|  | email_opt_out | boolean | false |  |  | email_opt_out | bool | False |
|  | employees | integer | false |  |  | employees | str | >10,000 |
|  | facebook | string | false |  |  | facebook | str |  |
|  | following | boolean | false |  |  | following | bool | False |
|  | geocode_status | string | false |  |  | geocode_status | str |  |
|  | googleplus | string | false |  |  | googleplus | str |  |
|  | id | string | true |  |  | id | str | d76d391a-30cc-11f0-a99c-1d1bbea39a2d |
|  | industry | string | false |  |  | industry | str | Utilities |
|  | invalid_email | boolean | false |  |  | invalid_email | bool | False |
|  | is_escalated | boolean | false |  |  | is_escalated | bool | False |
|  | latitude_c | string | false |  |  | latitude_c | str | 28.5021966 |
|  | longitude_c | string | false |  |  | longitude_c | str | -81.355642 |
|  | modified_user_id | string | false |  |  | modified_user_id | str | 1 |
|  | my_favorite | boolean | false |  |  | my_favorite | bool | False |
|  | *name | string | false |  |  | name | str | Insight Marketing Inc |
|  | next_renewal_date | string | false |  |  | next_renewal_date | str | 2024-07-10 |
|  | ownership | string | false |  |  | ownership | str | Bronnbaum Technologies |
|  | parent_id | string | false |  |  | parent_id | str |  |
|  | parent_name | string | false |  |  | parent_name | str |  |
|  | phone_alternate | string | false |  |  | phone_alternate | str | +1 - 573 - 583 - 6446 |
|  | phone_fax | string | false |  |  | phone_fax | str | +1 - 694 - 135 - 3012 |
|  | phone_office | string | false |  |  | phone_office | str | +1 - 672 - 854 - 9798 |
|  | rating | string | false |  |  | rating | str | 5 |
|  | service_level | string | false |  |  | service_level | str | T4 |
|  | shipping_address_city | string | false |  |  | shipping_address_city | str | Orlando |
|  | shipping_address_country | string | false |  |  | shipping_address_country | str | USA |
|  | shipping_address_postalcode | string | false |  |  | shipping_address_postalcode | str | 32806 |
|  | shipping_address_state | string | false |  |  | shipping_address_state | str | Florida |
|  | shipping_address_street | string | false |  |  | shipping_address_street | str | 481 Ontario Ave |
|  | shipping_address_street_2 | string | false |  |  | shipping_address_street_2 | str |  |
|  | shipping_address_street_3 | string | false |  |  | shipping_address_street_3 | str |  |
|  | shipping_address_street_4 | string | false |  |  | shipping_address_street_4 | str |  |
|  | sic_code | string | false |  |  | sic_code | str | 76451 |
|  | tag | array | false |  |  | tag | array | [] |
|  | team_count | string | false |  |  | team_count | str |  |
|  | ticker_symbol | string | false |  |  | ticker_symbol | str | BFC |
|  | twitter | string | false |  |  | twitter | str | insight |
|  | website | string | false |  |  | website | str | http://www.insightmarketinginc.com |
|  |  |  |  |  |  | _acl | object | {"fields": {}} |
|  |  |  |  |  |  | _module | str | Accounts |
|  |  |  |  |  |  | assigned_user_link | object | {"full_name": "Chris Olliver", "id": "seed_chris_id", "_acl": {"fields": [], "_hash": "654d337e0e912edaa00dbb0fb3dc3c17"}} |
|  |  |  |  |  |  | assigned_user_link._acl._hash | str |  |
|  |  |  |  |  |  | assigned_user_link.full_name | str |  |
|  |  |  |  |  |  | assigned_user_link.id | str |  |
|  |  |  |  |  |  | assigned_user_name | str | Chris Olliver |
|  |  |  |  |  |  | business_center_name | str | EMEA Business Center |
|  |  |  |  |  |  | business_centers | object | {"name": "EMEA Business Center", "id": "4a40f8aa-8831-11e9-9e1a-069335ab1e28", "_acl": {"fields": [], "_hash": "654d337e0e912edaa00dbb0fb3dc3c17"}} |
|  |  |  |  |  |  | business_centers._acl._hash | str |  |
|  |  |  |  |  |  | business_centers.id | str |  |
|  |  |  |  |  |  | business_centers.name | str |  |
|  |  |  |  |  |  | campaign_accounts | object | {"name": "", "id": "", "_acl": {"fields": {"peoplewhoopened": {"create": "no", "write": "no", "license": "no"}, "peoplewhoclicked": {"create": "no", "write": "no", "license": "no"}, "bounced": {"create": "no", "write": "no", "license": "no"}, "notreported": {"create": "no", "write": "no", "license": "no"}, "delivered": {"create": "no", "write": "no", "license": "no"}, "social": {"create": "no", "write": "no", "license": "no"}, "sent": {"create": "no", "write": "no", "license": "no"}, "postdate": {"create": "no", "write": "no", "license": "no"}, "forwards": {"create": "no", "write": "no", "license": "no"}, "unopened": {"create": "no", "write": "no", "license": "no"}, "unsubscribed": {"create": "no", "write": "no", "license": "no"}, "totalopens": {"create": "no", "write": "no", "license": "no"}, "totalclicks": {"create": "no", "write": "no", "license": "no"}}, "_hash": "ea0dd9a7291770652f6587c8f1f4e1f9"}} |
|  |  |  |  |  |  | campaign_accounts._acl._hash | str |  |
|  |  |  |  |  |  | campaign_accounts._acl.fields.bounced.create | str |  |
|  |  |  |  |  |  | campaign_accounts._acl.fields.bounced.license | str |  |
|  |  |  |  |  |  | campaign_accounts._acl.fields.bounced.write | str |  |
|  |  |  |  |  |  | campaign_accounts._acl.fields.delivered.create | str |  |
|  |  |  |  |  |  | campaign_accounts._acl.fields.delivered.license | str |  |
|  |  |  |  |  |  | campaign_accounts._acl.fields.delivered.write | str |  |
|  |  |  |  |  |  | campaign_accounts._acl.fields.forwards.create | str |  |
|  |  |  |  |  |  | campaign_accounts._acl.fields.forwards.license | str |  |
|  |  |  |  |  |  | campaign_accounts._acl.fields.forwards.write | str |  |
|  |  |  |  |  |  | campaign_accounts._acl.fields.notreported.create | str |  |
|  |  |  |  |  |  | campaign_accounts._acl.fields.notreported.license | str |  |
|  |  |  |  |  |  | campaign_accounts._acl.fields.notreported.write | str |  |
|  |  |  |  |  |  | campaign_accounts._acl.fields.peoplewhoclicked.create | str |  |
|  |  |  |  |  |  | campaign_accounts._acl.fields.peoplewhoclicked.license | str |  |
|  |  |  |  |  |  | campaign_accounts._acl.fields.peoplewhoclicked.write | str |  |
|  |  |  |  |  |  | campaign_accounts._acl.fields.peoplewhoopened.create | str |  |
|  |  |  |  |  |  | campaign_accounts._acl.fields.peoplewhoopened.license | str |  |
|  |  |  |  |  |  | campaign_accounts._acl.fields.peoplewhoopened.write | str |  |
|  |  |  |  |  |  | campaign_accounts._acl.fields.postdate.create | str |  |
|  |  |  |  |  |  | campaign_accounts._acl.fields.postdate.license | str |  |
|  |  |  |  |  |  | campaign_accounts._acl.fields.postdate.write | str |  |
|  |  |  |  |  |  | campaign_accounts._acl.fields.sent.create | str |  |
|  |  |  |  |  |  | campaign_accounts._acl.fields.sent.license | str |  |
|  |  |  |  |  |  | campaign_accounts._acl.fields.sent.write | str |  |
|  |  |  |  |  |  | campaign_accounts._acl.fields.social.create | str |  |
|  |  |  |  |  |  | campaign_accounts._acl.fields.social.license | str |  |
|  |  |  |  |  |  | campaign_accounts._acl.fields.social.write | str |  |
|  |  |  |  |  |  | campaign_accounts._acl.fields.totalclicks.create | str |  |
|  |  |  |  |  |  | campaign_accounts._acl.fields.totalclicks.license | str |  |
|  |  |  |  |  |  | campaign_accounts._acl.fields.totalclicks.write | str |  |
|  |  |  |  |  |  | campaign_accounts._acl.fields.totalopens.create | str |  |
|  |  |  |  |  |  | campaign_accounts._acl.fields.totalopens.license | str |  |
|  |  |  |  |  |  | campaign_accounts._acl.fields.totalopens.write | str |  |
|  |  |  |  |  |  | campaign_accounts._acl.fields.unopened.create | str |  |
|  |  |  |  |  |  | campaign_accounts._acl.fields.unopened.license | str |  |
|  |  |  |  |  |  | campaign_accounts._acl.fields.unopened.write | str |  |
|  |  |  |  |  |  | campaign_accounts._acl.fields.unsubscribed.create | str |  |
|  |  |  |  |  |  | campaign_accounts._acl.fields.unsubscribed.license | str |  |
|  |  |  |  |  |  | campaign_accounts._acl.fields.unsubscribed.write | str |  |
|  |  |  |  |  |  | campaign_accounts.id | str |  |
|  |  |  |  |  |  | campaign_accounts.name | str |  |
|  |  |  |  |  |  | campaign_name | str |  |
|  |  |  |  |  |  | created_by_link | object | {"full_name": "Jen Smith", "id": "1", "_acl": {"fields": [], "_hash": "654d337e0e912edaa00dbb0fb3dc3c17"}} |
|  |  |  |  |  |  | created_by_link._acl._hash | str |  |
|  |  |  |  |  |  | created_by_link.full_name | str |  |
|  |  |  |  |  |  | created_by_link.id | str |  |
|  |  |  |  |  |  | created_by_name | str | Jen Smith |
|  |  |  |  |  |  | dri_workflow_template_id | str |  |
|  |  |  |  |  |  | dri_workflow_template_link | object | {"name": "", "id": "", "_acl": {"fields": [], "_hash": "654d337e0e912edaa00dbb0fb3dc3c17"}} |
|  |  |  |  |  |  | dri_workflow_template_link._acl._hash | str |  |
|  |  |  |  |  |  | dri_workflow_template_link.id | str |  |
|  |  |  |  |  |  | dri_workflow_template_link.name | str |  |
|  |  |  |  |  |  | dri_workflow_template_name | str |  |
|  |  |  |  |  |  | email_addresses_non_primary | str |  |
|  |  |  |  |  |  | hint_account_facebook_handle | str |  |
|  |  |  |  |  |  | hint_account_fiscal_year_end | str |  |
|  |  |  |  |  |  | hint_account_founded_year | str |  |
|  |  |  |  |  |  | hint_account_industry | str |  |
|  |  |  |  |  |  | hint_account_industry_tags | str |  |
|  |  |  |  |  |  | hint_account_location | str |  |
|  |  |  |  |  |  | hint_account_logo | str |  |
|  |  |  |  |  |  | hint_account_naics_code_lbl | str |  |
|  |  |  |  |  |  | hint_account_pic | str |  |
|  |  |  |  |  |  | hint_account_size | str |  |
|  |  |  |  |  |  | last_interaction_date | str | 2025-04-04T16:30:00+05:00 |
|  |  |  |  |  |  | last_interaction_parent_id | str | f68f9e40-30cd-11f0-b5df-f34e281fb0c4 |
|  |  |  |  |  |  | last_interaction_parent_name | str | Contract detail review |
|  |  |  |  |  |  | last_interaction_parent_type | str | Calls |
|  |  |  |  |  |  | locked_fields | array | [] |
|  |  |  |  |  |  | member_of | object | {"name": "", "id": "", "_acl": {"fields": [], "_hash": "654d337e0e912edaa00dbb0fb3dc3c17"}} |
|  |  |  |  |  |  | member_of._acl._hash | str |  |
|  |  |  |  |  |  | member_of.id | str |  |
|  |  |  |  |  |  | member_of.name | str |  |
|  |  |  |  |  |  | modified_by_name | str | Jen Smith |
|  |  |  |  |  |  | modified_user_link | object | {"full_name": "Jen Smith", "id": "1", "_acl": {"fields": [], "_hash": "654d337e0e912edaa00dbb0fb3dc3c17"}} |
|  |  |  |  |  |  | modified_user_link._acl._hash | str |  |
|  |  |  |  |  |  | modified_user_link.full_name | str |  |
|  |  |  |  |  |  | modified_user_link.id | str |  |
|  |  |  |  |  |  | perform_sugar_action | bool | False |
|  |  |  |  |  |  | sync_key | str |  |
|  |  |  |  |  |  | team_count_link | object | {"team_count": "", "id": "1", "_acl": {"fields": [], "_hash": "654d337e0e912edaa00dbb0fb3dc3c17"}} |
|  |  |  |  |  |  | team_count_link._acl._hash | str |  |
|  |  |  |  |  |  | team_count_link.id | str |  |
|  |  |  |  |  |  | team_count_link.team_count | str |  |
|  |  |  |  |  |  | team_name | array | [{"id": "1", "name": "Global", "name_2": "", "primary": true, "selected": false}] |
|  |  |  |  |  |  | widget_next_renewal_date | str |  |

## Contacts

| Entity Schema Title | Entity Schema Fields | Entity Schema Types | Readonly | Possible Values | Reference Collection | Find By ID Object Fields | Find By ID Types | Value |
|---------------------|----------------------|---------------------|----------|-----------------|----------------------|--------------------------|------------------|-------|
|  | accept_status_id | string | false |  |  | accept_status_id | str |  |
|  | accept_status_name | string | false |  |  | accept_status_name | str |  |
|  | account_id | string | false |  | accounts | account_id | str | d8132546-30cc-11f0-8a5f-b7c7c1b99788 |
|  | alt_address_city | string | false |  |  | alt_address_city | str | San Francisco |
|  | alt_address_country | string | false |  |  | alt_address_country | str | USA |
|  | alt_address_postalcode | string | false |  |  | alt_address_postalcode | str | 94110 |
|  | alt_address_state | string | false |  |  | alt_address_state | str | California |
|  | alt_address_street | string | false |  |  | alt_address_street | str | 763 Guerrero St |
|  | alt_address_street_2 | string | false |  |  | alt_address_street_2 | str |  |
|  | alt_address_street_3 | string | false |  |  | alt_address_street_3 | str |  |
|  | assigned_user_id | string | false |  | users | assigned_user_id | str | seed_chris_id |
|  | assistant | string | false |  |  | assistant | str |  |
|  | assistant_phone | string | false |  |  | assistant_phone | str |  |
|  | birthdate | string | false |  |  | birthdate | str |  |
|  | calls | object | false |  |  | calls | object | {"id": ""} |
|  | calls.id | string | false |  |  | calls.id | str |  |
|  | campaign_id | string | false |  |  | campaign_id | str |  |
|  | created_by | string | false |  | users | created_by | str | 1 |
|  | date_entered | string | false |  |  | date_entered | str | 2025-05-14T19:25:56+05:00 |
|  | date_modified | string | false |  |  | date_modified | str | 2025-05-14T19:47:40+05:00 |
|  | deleted | boolean | false |  |  | deleted | bool | False |
|  | department | string | false |  |  | department | str | Sales |
|  | description | string | false |  |  | description | str |  |
|  | do_not_call | boolean | false |  |  | do_not_call | bool | False |
|  | email | array | false |  |  | email | array | [{"email_address": "linda.holiday@yahoo.com", "invalid_email": false, "opt_out": false, "email_address_id": "633ec3fa-30d2-11f0-a0c2-8fa31453d866", "primary_address": true, "reply_to_address": false}] |
|  | email1 | string | false |  |  | email1 | str | linda.holiday@yahoo.com |
|  | email2 | string | false |  |  | email2 | str |  |
|  | email_opt_out | boolean | false |  |  | email_opt_out | bool | False |
|  | entry_source | string | false |  |  | entry_source | str | internal |
|  | facebook | string | false |  |  | facebook | str |  |
|  | first_name | string | false |  |  | first_name | str | Linda |
|  | following | boolean | false |  |  | following | bool | False |
|  | full_name | string | false |  |  | full_name | str | Linda Holiday |
|  | googleplus | string | false |  |  | googleplus | str |  |
|  | id | string | true |  |  | id | str | 593db44a-30cf-11f0-8746-4f8477825d38 |
|  | invalid_email | boolean | false |  |  | invalid_email | bool | False |
|  | last_name | string | false |  |  | last_name | str | Holiday |
|  | latitude_c | string | false |  |  | latitude_c | str | 41.87118 |
|  | lead_source | string | false |  |  | lead_source | str | Email |
|  | longitude_c | string | false |  |  | longitude_c | str | -87.7055352 |
|  | market_interest_prediction_score | string | false |  |  | market_interest_prediction_score | str |  |
|  | market_score | string | false |  |  | market_score | null | None |
|  | meetings | object | false |  |  | meetings | object | {"id": ""} |
|  | meetings.id | string | false |  |  | meetings.id | str |  |
|  | mkto_sync | boolean | false |  |  | mkto_sync | bool | False |
|  | modified_user_id | string | false |  | users | modified_user_id | str | 1 |
|  | my_favorite | boolean | false |  |  | my_favorite | bool | False |
|  | name | string | false |  |  | name | str | Linda Holiday |
|  | opportunities | object | false |  |  | opportunities | object | {"id": ""} |
|  | opportunities.id | string | false |  |  | opportunities.id | str |  |
|  | opportunity_role_id | string | false |  |  | opportunity_role_id | str |  |
|  | phone_fax | string | false |  |  | phone_fax | str | +1 - 741 - 478 - 3827 |
|  | phone_home | string | false |  |  | phone_home | str | +1 - 236 - 100 - 7476 |
|  | phone_mobile | string | false |  |  | phone_mobile | str | +1 - 912 - 574 - 1060 |
|  | phone_other | string | false |  |  | phone_other | str |  |
|  | phone_work | string | false |  |  | phone_work | str | +1 - 928 - 629 - 8243 |
|  | primary_address_city | string | false |  |  | primary_address_city | str | Chicago |
|  | primary_address_country | string | false |  |  | primary_address_country | str | USA |
|  | primary_address_postalcode | string | false |  |  | primary_address_postalcode | str | 60612 |
|  | primary_address_state | string | false |  |  | primary_address_state | str | Illinois |
|  | primary_address_street | string | false |  |  | primary_address_street | str | 803 S Kedzie Ave |
|  | primary_address_street_2 | string | false |  |  | primary_address_street_2 | str |  |
|  | primary_address_street_3 | string | false |  |  | primary_address_street_3 | str |  |
|  | reports_to_id | string | false |  | users | reports_to_id | str |  |
|  | salutation | string | false |  |  | salutation | str |  |
|  | site_user_id | string | false |  |  | site_user_id | str | 4a006b5846ecee03b7e63e4653755dab676aee8d98d15a2eac7ecafd19dd2fee |
|  | source_id | string | false |  |  | source_id | str |  |
|  | source_meta | string | false |  |  | source_meta | str |  |
|  | source_type | string | false |  |  | source_type | str |  |
|  | sync_key | string | false |  |  | sync_key | str |  |
|  | tag | array | false |  |  | tag | array | [{"id": "d93687a6-30cc-11f0-8530-69003c7f6309", "name": "goto data", "tags__name_lower": "goto data"}] |
|  | team_count | string | false |  |  | team_count | str |  |
|  | title | string | false |  |  | title | str | Senior Sales Associate |
|  | twitter | string | false |  |  | twitter | str | LindaHoliday23 |
|  |  |  |  |  |  | _acl | object | {"fields": {}} |
|  |  |  |  |  |  | _module | str | Contacts |
|  |  |  |  |  |  | accept_status_calls | str |  |
|  |  |  |  |  |  | accept_status_meetings | str |  |
|  |  |  |  |  |  | accept_status_messages | str |  |
|  |  |  |  |  |  | account_name | str | Kringle Bell IncKA Tower & Co |
|  |  |  |  |  |  | accounts | object | {"name": "Kringle Bell IncKA Tower & Co", "id": "d8132546-30cc-11f0-8a5f-b7c7c1b99788", "_acl": {"fields": [], "_hash": "654d337e0e912edaa00dbb0fb3dc3c17"}} |
|  |  |  |  |  |  | accounts._acl._hash | str |  |
|  |  |  |  |  |  | accounts.id | str |  |
|  |  |  |  |  |  | accounts.name | str |  |
|  |  |  |  |  |  | assigned_user_link | object | {"full_name": "Chris Olliver", "id": "seed_chris_id", "_acl": {"fields": [], "_hash": "654d337e0e912edaa00dbb0fb3dc3c17"}} |
|  |  |  |  |  |  | assigned_user_link._acl._hash | str |  |
|  |  |  |  |  |  | assigned_user_link.full_name | str |  |
|  |  |  |  |  |  | assigned_user_link.id | str |  |
|  |  |  |  |  |  | assigned_user_name | str | Chris Olliver |
|  |  |  |  |  |  | business_center_id | str | 4a40f8aa-8831-11e9-9e1a-069335ab1e28 |
|  |  |  |  |  |  | business_center_name | str | EMEA Business Center |
|  |  |  |  |  |  | business_centers | object | {"name": "EMEA Business Center", "id": "4a40f8aa-8831-11e9-9e1a-069335ab1e28", "_acl": {"fields": [], "_hash": "654d337e0e912edaa00dbb0fb3dc3c17"}} |
|  |  |  |  |  |  | business_centers._acl._hash | str |  |
|  |  |  |  |  |  | business_centers.id | str |  |
|  |  |  |  |  |  | business_centers.name | str |  |
|  |  |  |  |  |  | c_accept_status_fields | str |  |
|  |  |  |  |  |  | campaign_contacts | object | {"name": "", "id": "", "_acl": {"fields": {"peoplewhoopened": {"create": "no", "write": "no", "license": "no"}, "peoplewhoclicked": {"create": "no", "write": "no", "license": "no"}, "bounced": {"create": "no", "write": "no", "license": "no"}, "notreported": {"create": "no", "write": "no", "license": "no"}, "delivered": {"create": "no", "write": "no", "license": "no"}, "social": {"create": "no", "write": "no", "license": "no"}, "sent": {"create": "no", "write": "no", "license": "no"}, "postdate": {"create": "no", "write": "no", "license": "no"}, "forwards": {"create": "no", "write": "no", "license": "no"}, "unopened": {"create": "no", "write": "no", "license": "no"}, "unsubscribed": {"create": "no", "write": "no", "license": "no"}, "totalopens": {"create": "no", "write": "no", "license": "no"}, "totalclicks": {"create": "no", "write": "no", "license": "no"}}, "_hash": "ea0dd9a7291770652f6587c8f1f4e1f9"}} |
|  |  |  |  |  |  | campaign_contacts._acl._hash | str |  |
|  |  |  |  |  |  | campaign_contacts._acl.fields.bounced.create | str |  |
|  |  |  |  |  |  | campaign_contacts._acl.fields.bounced.license | str |  |
|  |  |  |  |  |  | campaign_contacts._acl.fields.bounced.write | str |  |
|  |  |  |  |  |  | campaign_contacts._acl.fields.delivered.create | str |  |
|  |  |  |  |  |  | campaign_contacts._acl.fields.delivered.license | str |  |
|  |  |  |  |  |  | campaign_contacts._acl.fields.delivered.write | str |  |
|  |  |  |  |  |  | campaign_contacts._acl.fields.forwards.create | str |  |
|  |  |  |  |  |  | campaign_contacts._acl.fields.forwards.license | str |  |
|  |  |  |  |  |  | campaign_contacts._acl.fields.forwards.write | str |  |
|  |  |  |  |  |  | campaign_contacts._acl.fields.notreported.create | str |  |
|  |  |  |  |  |  | campaign_contacts._acl.fields.notreported.license | str |  |
|  |  |  |  |  |  | campaign_contacts._acl.fields.notreported.write | str |  |
|  |  |  |  |  |  | campaign_contacts._acl.fields.peoplewhoclicked.create | str |  |
|  |  |  |  |  |  | campaign_contacts._acl.fields.peoplewhoclicked.license | str |  |
|  |  |  |  |  |  | campaign_contacts._acl.fields.peoplewhoclicked.write | str |  |
|  |  |  |  |  |  | campaign_contacts._acl.fields.peoplewhoopened.create | str |  |
|  |  |  |  |  |  | campaign_contacts._acl.fields.peoplewhoopened.license | str |  |
|  |  |  |  |  |  | campaign_contacts._acl.fields.peoplewhoopened.write | str |  |
|  |  |  |  |  |  | campaign_contacts._acl.fields.postdate.create | str |  |
|  |  |  |  |  |  | campaign_contacts._acl.fields.postdate.license | str |  |
|  |  |  |  |  |  | campaign_contacts._acl.fields.postdate.write | str |  |
|  |  |  |  |  |  | campaign_contacts._acl.fields.sent.create | str |  |
|  |  |  |  |  |  | campaign_contacts._acl.fields.sent.license | str |  |
|  |  |  |  |  |  | campaign_contacts._acl.fields.sent.write | str |  |
|  |  |  |  |  |  | campaign_contacts._acl.fields.social.create | str |  |
|  |  |  |  |  |  | campaign_contacts._acl.fields.social.license | str |  |
|  |  |  |  |  |  | campaign_contacts._acl.fields.social.write | str |  |
|  |  |  |  |  |  | campaign_contacts._acl.fields.totalclicks.create | str |  |
|  |  |  |  |  |  | campaign_contacts._acl.fields.totalclicks.license | str |  |
|  |  |  |  |  |  | campaign_contacts._acl.fields.totalclicks.write | str |  |
|  |  |  |  |  |  | campaign_contacts._acl.fields.totalopens.create | str |  |
|  |  |  |  |  |  | campaign_contacts._acl.fields.totalopens.license | str |  |
|  |  |  |  |  |  | campaign_contacts._acl.fields.totalopens.write | str |  |
|  |  |  |  |  |  | campaign_contacts._acl.fields.unopened.create | str |  |
|  |  |  |  |  |  | campaign_contacts._acl.fields.unopened.license | str |  |
|  |  |  |  |  |  | campaign_contacts._acl.fields.unopened.write | str |  |
|  |  |  |  |  |  | campaign_contacts._acl.fields.unsubscribed.create | str |  |
|  |  |  |  |  |  | campaign_contacts._acl.fields.unsubscribed.license | str |  |
|  |  |  |  |  |  | campaign_contacts._acl.fields.unsubscribed.write | str |  |
|  |  |  |  |  |  | campaign_contacts.id | str |  |
|  |  |  |  |  |  | campaign_contacts.name | str |  |
|  |  |  |  |  |  | campaign_name | str |  |
|  |  |  |  |  |  | cookie_consent | bool | False |
|  |  |  |  |  |  | cookie_consent_received_on | str |  |
|  |  |  |  |  |  | created_by_link | object | {"full_name": "Jen Smith", "id": "1", "_acl": {"fields": [], "_hash": "654d337e0e912edaa00dbb0fb3dc3c17"}} |
|  |  |  |  |  |  | created_by_link._acl._hash | str |  |
|  |  |  |  |  |  | created_by_link.full_name | str |  |
|  |  |  |  |  |  | created_by_link.id | str |  |
|  |  |  |  |  |  | created_by_name | str | Jen Smith |
|  |  |  |  |  |  | denorm_account_name | str | Kringle Bell IncKA Tower & Co |
|  |  |  |  |  |  | dnb_principal_id | str | 263865980 |
|  |  |  |  |  |  | dp_business_purpose | array | [] |
|  |  |  |  |  |  | dp_consent_last_updated | str | 2025-05-14 |
|  |  |  |  |  |  | dri_workflow_template_id | str |  |
|  |  |  |  |  |  | dri_workflow_template_link | object | {"name": "", "id": "", "_acl": {"fields": [], "_hash": "654d337e0e912edaa00dbb0fb3dc3c17"}} |
|  |  |  |  |  |  | dri_workflow_template_link._acl._hash | str |  |
|  |  |  |  |  |  | dri_workflow_template_link.id | str |  |
|  |  |  |  |  |  | dri_workflow_template_link.name | str |  |
|  |  |  |  |  |  | dri_workflow_template_name | str |  |
|  |  |  |  |  |  | email_addresses_non_primary | str |  |
|  |  |  |  |  |  | email_and_name1 | str |  |
|  |  |  |  |  |  | external_user_id | str |  |
|  |  |  |  |  |  | geocode_status | str |  |
|  |  |  |  |  |  | hint_account_annual_revenue | str |  |
|  |  |  |  |  |  | hint_account_description | str |  |
|  |  |  |  |  |  | hint_account_facebook_handle | str |  |
|  |  |  |  |  |  | hint_account_fiscal_year_end | str |  |
|  |  |  |  |  |  | hint_account_founded_year | str |  |
|  |  |  |  |  |  | hint_account_industry | str |  |
|  |  |  |  |  |  | hint_account_location | str |  |
|  |  |  |  |  |  | hint_account_logo | str |  |
|  |  |  |  |  |  | hint_account_naics_code_lbl | str |  |
|  |  |  |  |  |  | hint_account_sic_code_label | str |  |
|  |  |  |  |  |  | hint_account_size | str |  |
|  |  |  |  |  |  | hint_account_twitter_handle | str |  |
|  |  |  |  |  |  | hint_account_website | str |  |
|  |  |  |  |  |  | hint_contact_pic | str |  |
|  |  |  |  |  |  | hint_education | str |  |
|  |  |  |  |  |  | hint_education_2 | str |  |
|  |  |  |  |  |  | hint_facebook | str |  |
|  |  |  |  |  |  | hint_industry_tags | str |  |
|  |  |  |  |  |  | hint_job_2 | str |  |
|  |  |  |  |  |  | hint_phone_1 | str |  |
|  |  |  |  |  |  | hint_phone_2 | str |  |
|  |  |  |  |  |  | hint_photo | str |  |
|  |  |  |  |  |  | hint_twitter | str |  |
|  |  |  |  |  |  | locked_fields | array | [] |
|  |  |  |  |  |  | m_accept_status_fields | str |  |
|  |  |  |  |  |  | mkto_id | null | None |
|  |  |  |  |  |  | mkto_lead_score | str | Email |
|  |  |  |  |  |  | modified_by_name | str | Jen Smith |
|  |  |  |  |  |  | modified_user_link | object | {"full_name": "Jen Smith", "id": "1", "_acl": {"fields": [], "_hash": "654d337e0e912edaa00dbb0fb3dc3c17"}} |
|  |  |  |  |  |  | modified_user_link._acl._hash | str |  |
|  |  |  |  |  |  | modified_user_link.full_name | str |  |
|  |  |  |  |  |  | modified_user_link.id | str |  |
|  |  |  |  |  |  | opportunity_role | str |  |
|  |  |  |  |  |  | opportunity_role_fields | str |  |
|  |  |  |  |  |  | perform_sugar_action | bool | False |
|  |  |  |  |  |  | picture | str | LindaHoliday1747234061 |
|  |  |  |  |  |  | portal_active | bool | True |
|  |  |  |  |  |  | portal_app | str |  |
|  |  |  |  |  |  | portal_name | str | LindaHoliday23 |
|  |  |  |  |  |  | portal_password | bool | True |
|  |  |  |  |  |  | portal_password1 | null | None |
|  |  |  |  |  |  | portal_user_company_name | str |  |
|  |  |  |  |  |  | preferred_language | str | en_us |
|  |  |  |  |  |  | report_to_name | str |  |
|  |  |  |  |  |  | reports_to_link | object | {"name": "", "id": "", "_acl": {"fields": {"sf_lastactivity_default": {"create": "no", "write": "no", "license": "no"}}, "_hash": "c69ded8d08ee4170c5d490bf7c5941d7"}} |
|  |  |  |  |  |  | reports_to_link._acl._hash | str |  |
|  |  |  |  |  |  | reports_to_link._acl.fields.sf_lastactivity_default.create | str |  |
|  |  |  |  |  |  | reports_to_link._acl.fields.sf_lastactivity_default.license | str |  |
|  |  |  |  |  |  | reports_to_link._acl.fields.sf_lastactivity_default.write | str |  |
|  |  |  |  |  |  | reports_to_link.id | str |  |
|  |  |  |  |  |  | reports_to_link.name | str |  |
|  |  |  |  |  |  | sync_contact | bool | False |
|  |  |  |  |  |  | team_count_link | object | {"team_count": "", "id": "1", "_acl": {"fields": [], "_hash": "654d337e0e912edaa00dbb0fb3dc3c17"}} |
|  |  |  |  |  |  | team_count_link._acl._hash | str |  |
|  |  |  |  |  |  | team_count_link.id | str |  |
|  |  |  |  |  |  | team_count_link.team_count | str |  |
|  |  |  |  |  |  | team_name | array | [{"id": "East", "name": "East", "name_2": "", "primary": false, "selected": false}, {"id": "1", "name": "Global", "name_2": "", "primary": true, "selected": false}] |