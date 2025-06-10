# Differences between fields in SugarCRM

## Opportunities

| Entity Schema Fields            | Entity Schema Types | Find By ID Object Fields                 | Find By ID Types |
|---------------------------------|---------------------|------------------------------------------|------------------|
| account_id                      | string              | account_id                               | str              |
| ai_opp_conv_bin_accuracy        | string              | ai_opp_conv_bin_accuracy                 | null             |
| ai_opp_conv_multiplier          | string              | ai_opp_conv_multiplier                   | null             |
| ai_opp_conv_score_absolute      | string              | ai_opp_conv_score_absolute               | null             |
| ai_opp_conv_score_enum          | string              | ai_opp_conv_score_enum                   | str              |
| amount                          | string              | amount                                   | str              |
| amount_usdollar                 | string              | amount_usdollar                          | str              |
| assigned_user_id                | string              | assigned_user_id                         | str              |
| base_rate                       | string              | base_rate                                | str              |
| best_case                       | string              | best_case                                | str              |
| campaign_id                     | string              | campaign_id                              | str              |
| campaign_opportunities.id       | string              | campaign_opportunities.id                | str              |
| campaign_opportunities.name     | string              | campaign_opportunities.name              | str              |
| closed_revenue_line_items       | integer             | closed_revenue_line_items                | int              |
| closed_won_revenue_line_items   | integer             | closed_won_revenue_line_items            | int              |
| commit_stage                    | string              | commit_stage                             | str              |
| commit_stage_cascade            | string              | commit_stage_cascade                     | str              |
| contact_role                    | string              | contact_role                             | str              |
| created_by                      | string              | created_by                               | str              |
| currency_id                     | string              | currency_id                              | str              |
| currency_name                   | string              | currency_name                            | str              |
| date_closed                     | string              | date_closed                              | str              |
| date_closed_cascade             | string              | date_closed_cascade                      | str              |
| date_closed_timestamp           | integer             | date_closed_timestamp                    | int              |
| date_entered                    | string              | date_entered                             | str              |
| date_modified                   | string              | date_modified                            | str              |
| deleted                         | boolean             | deleted                                  | bool             |
| description                     | string              | description                              | str              |
| following                       | boolean             | following                                | bool             |
| forecasted_likely               | string              | forecasted_likely                        | str              |
| geocode_status                  | string              | geocode_status                           | str              |
| id                              | string              | id                                       | str              |
| included_revenue_line_items     | integer             | included_revenue_line_items              | int              |
| is_escalated                    | boolean             | is_escalated                             | bool             |
| lead_source                     | string              | lead_source                              | str              |
| lost                            | string              | lost                                     | str              |
| mkto_id                         | string              | mkto_id                                  | null             |
| mkto_sync                       | boolean             | mkto_sync                                | bool             |
| modified_user_id                | string              | modified_user_id                         | str              |
| my_favorite                     | boolean             | my_favorite                              | bool             |
| name                            | string              | name                                     | str              |
| next_step                       | string              | next_step                                | str              |
| opportunity_type                | string              | opportunity_type                         | str              |
| probability                     | integer             | probability                              | int              |
| renewal                         | boolean             | renewal                                  | bool             |
| renewal_parent_id               | string              | renewal_parent_id                        | str              |
| renewal_parent_name             | string              | renewal_parent_name                      | str              |
| sales_stage                     | string              | sales_stage                              | str              |
| sales_stage_cascade             | string              | sales_stage_cascade                      | str              |
| sales_status                    | string              | sales_status                             | str              |
| service_duration_unit           | string              | service_duration_unit                    | str              |
| service_duration_unit_cascade   | string              | service_duration_unit_cascade            | str              |
| service_duration_value          | integer             | service_duration_value                   | null             |
| service_duration_value_cascade  | integer             | service_duration_value_cascade           | null             |
| service_open_flex_duration_rlis | integer             | service_open_flex_duration_rlis          | int              |
| service_open_revenue_line_items | integer             | service_open_revenue_line_items          | int              |
| service_start_date              | string              | service_start_date                       | str              |
| service_start_date_cascade      | string              | service_start_date_cascade               | str              |
| sl_ai_conv_score_c              | string              | sl_ai_conv_score_c                       | str              |
| sync_key                        | string              | sync_key                                 | str              |
| team_count                      | string              | team_count                               | str              |
| team_name[]                     | object              | team_name[]                              | array            |
| team_name[].id                  | string              | team_name[].id                           | object           |
| team_name[].name                | string              | team_name[].name                         | object           |
| team_name[].name_2              | string              | team_name[].name_2                       | object           |
| team_name[].primary             | boolean             | team_name[].primary                      | object           |
| team_name[].selected            | boolean             | team_name[].selected                     | object           |
| total_revenue_line_items        | integer             | total_revenue_line_items                 | int              |
| widget_amount                   | string              | widget_amount                            | str              |
| widget_date_closed              | string              | widget_date_closed                       | str              |
| widget_sales_stage              | string              | widget_sales_stage                       | str              |
| worst_case                      | string              | worst_case                               | str              |
| tag                             | array               |                                          |                  |
|                                 |                     | _module                                  | str              |
|                                 |                     | account_name                             | str              |
|                                 |                     | accounts._acl._hash                      | str              |
|                                 |                     | accounts._acl.fields[]                   | array            |
|                                 |                     | accounts.id                              | str              |
|                                 |                     | accounts.name                            | str              |
|                                 |                     | ai_opp_close_week_scores                 | null             |
|                                 |                     | ai_opp_won_score                         | null             |
|                                 |                     | assigned_user_link._acl._hash            | str              |
|                                 |                     | assigned_user_link._acl.fields[]         | array            |
|                                 |                     | assigned_user_link.full_name             | str              |
|                                 |                     | assigned_user_link.id                    | str              |
|                                 |                     | assigned_user_name                       | str              |
|                                 |                     | campaign_name                            | str              |
|                                 |                     | created_by_link._acl._hash               | str              |
|                                 |                     | created_by_link._acl.fields[]            | array            |
|                                 |                     | created_by_link.full_name                | str              |
|                                 |                     | created_by_link.id                       | str              |
|                                 |                     | created_by_name                          | str              |
|                                 |                     | currencies._acl._hash                    | str              |
|                                 |                     | currencies._acl.fields[]                 | array            |
|                                 |                     | currencies.id                            | str              |
|                                 |                     | currencies.name                          | str              |
|                                 |                     | currencies.symbol                        | str              |
|                                 |                     | currency_symbol                          | str              |
|                                 |                     | denorm_account_name                      | str              |
|                                 |                     | discover_data_c                          | bool             |
|                                 |                     | dri_workflow_template_id                 | str              |
|                                 |                     | dri_workflow_template_link._acl._hash    | str              |
|                                 |                     | dri_workflow_template_link._acl.fields[] | array            |
|                                 |                     | dri_workflow_template_link.id            | str              |
|                                 |                     | dri_workflow_template_link.name          | str              |
|                                 |                     | dri_workflow_template_name               | str              |
|                                 |                     | locked_fields[]                          | array            |
|                                 |                     | modified_by_name                         | str              |
|                                 |                     | modified_user_link._acl._hash            | str              |
|                                 |                     | modified_user_link._acl.fields[]         | array            |
|                                 |                     | modified_user_link.full_name             | str              |
|                                 |                     | modified_user_link.id                    | str              |
|                                 |                     | perform_sugar_action                     | bool             |
|                                 |                     | renewal_parent._acl._hash                | str              |
|                                 |                     | renewal_parent._acl.fields[]             | array            |
|                                 |                     | renewal_parent.id                        | str              |
|                                 |                     | renewal_parent.name                      | str              |
|                                 |                     | tag[]                                    | array            |
|                                 |                     | team_count_link._acl._hash               | str              |
|                                 |                     | team_count_link._acl.fields[]            | array            |
|                                 |                     | team_count_link.id                       | str              |
|                                 |                     | team_count_link.team_count               | str              |

## Accounts

| Entity Schema Fields        | Entity Schema Types | Find By ID Object Fields                               | Find By ID Types |
|-----------------------------|---------------------|--------------------------------------------------------|------------------|
| account_type                | string              | account_type                                           | str              |
| annual_revenue              | integer             | annual_revenue                                         | str              |
| assigned_user_id            | string              | assigned_user_id                                       | str              |
| billing_address_city        | string              | billing_address_city                                   | str              |
| billing_address_country     | string              | billing_address_country                                | str              |
| billing_address_postalcode  | string              | billing_address_postalcode                             | str              |
| billing_address_state       | string              | billing_address_state                                  | str              |
| billing_address_street      | string              | billing_address_street                                 | str              |
| billing_address_street_2    | string              | billing_address_street_2                               | str              |
| billing_address_street_3    | string              | billing_address_street_3                               | str              |
| billing_address_street_4    | string              | billing_address_street_4                               | str              |
| business_center_id          | string              | business_center_id                                     | str              |
| campaign_id                 | string              | campaign_id                                            | str              |
| created_by                  | string              | created_by                                             | str              |
| date_entered                | string              | date_entered                                           | str              |
| date_modified               | string              | date_modified                                          | str              |
| deleted                     | boolean             | deleted                                                | bool             |
| description                 | string              | description                                            | str              |
| duns_num                    | string              | duns_num                                               | str              |
| email1                      | string              | email1                                                 | str              |
| email2                      | string              | email2                                                 | str              |
| email[]                     | object              | email[]                                                | array            |
| email[].email_address       | string              | email[].email_address                                  | object           |
| email[].email_address_id    | string              | email[].email_address_id                               | object           |
| email[].invalid_email       | boolean             | email[].invalid_email                                  | object           |
| email[].opt_out             | boolean             | email[].opt_out                                        | object           |
| email[].primary_address     | boolean             | email[].primary_address                                | object           |
| email[].reply_to_address    | boolean             | email[].reply_to_address                               | object           |
| email_opt_out               | boolean             | email_opt_out                                          | bool             |
| employees                   | integer             | employees                                              | str              |
| facebook                    | string              | facebook                                               | str              |
| following                   | boolean             | following                                              | bool             |
| geocode_status              | string              | geocode_status                                         | str              |
| googleplus                  | string              | googleplus                                             | str              |
| id                          | string              | id                                                     | str              |
| industry                    | string              | industry                                               | str              |
| invalid_email               | boolean             | invalid_email                                          | bool             |
| is_escalated                | boolean             | is_escalated                                           | bool             |
| latitude_c                  | string              | latitude_c                                             | str              |
| longitude_c                 | string              | longitude_c                                            | str              |
| modified_user_id            | string              | modified_user_id                                       | str              |
| my_favorite                 | boolean             | my_favorite                                            | bool             |
| name                        | string              | name                                                   | str              |
| next_renewal_date           | string              | next_renewal_date                                      | str              |
| ownership                   | string              | ownership                                              | str              |
| parent_id                   | string              | parent_id                                              | str              |
| parent_name                 | string              | parent_name                                            | str              |
| phone_alternate             | string              | phone_alternate                                        | str              |
| phone_fax                   | string              | phone_fax                                              | str              |
| phone_office                | string              | phone_office                                           | str              |
| rating                      | string              | rating                                                 | str              |
| service_level               | string              | service_level                                          | str              |
| shipping_address_city       | string              | shipping_address_city                                  | str              |
| shipping_address_country    | string              | shipping_address_country                               | str              |
| shipping_address_postalcode | string              | shipping_address_postalcode                            | str              |
| shipping_address_state      | string              | shipping_address_state                                 | str              |
| shipping_address_street     | string              | shipping_address_street                                | str              |
| shipping_address_street_2   | string              | shipping_address_street_2                              | str              |
| shipping_address_street_3   | string              | shipping_address_street_3                              | str              |
| shipping_address_street_4   | string              | shipping_address_street_4                              | str              |
| sic_code                    | string              | sic_code                                               | str              |
| team_count                  | string              | team_count                                             | str              |
| ticker_symbol               | string              | ticker_symbol                                          | str              |
| twitter                     | string              | twitter                                                | str              |
| website                     | string              | website                                                | str              |
| tag                         | array               |                                                        |                  |
| teams[]                     | object              |                                                        |                  |
| teams[].id                  | string              |                                                        |                  |
| teams[].name                | string              |                                                        |                  |
| teams[].name_2              | string              |                                                        |                  |
| teams[].primary             | boolean             |                                                        |                  |
| teams[].selected            | boolean             |                                                        |                  |
|                             |                     | _module                                                | str              |
|                             |                     | assigned_user_link._acl._hash                          | str              |
|                             |                     | assigned_user_link._acl.fields[]                       | array            |
|                             |                     | assigned_user_link.full_name                           | str              |
|                             |                     | assigned_user_link.id                                  | str              |
|                             |                     | assigned_user_name                                     | str              |
|                             |                     | business_center_name                                   | str              |
|                             |                     | business_centers._acl._hash                            | str              |
|                             |                     | business_centers._acl.fields[]                         | array            |
|                             |                     | business_centers.id                                    | str              |
|                             |                     | business_centers.name                                  | str              |
|                             |                     | campaign_accounts._acl._hash                           | str              |
|                             |                     | campaign_accounts._acl.fields.bounced.create           | str              |
|                             |                     | campaign_accounts._acl.fields.bounced.license          | str              |
|                             |                     | campaign_accounts._acl.fields.bounced.write            | str              |
|                             |                     | campaign_accounts._acl.fields.delivered.create         | str              |
|                             |                     | campaign_accounts._acl.fields.delivered.license        | str              |
|                             |                     | campaign_accounts._acl.fields.delivered.write          | str              |
|                             |                     | campaign_accounts._acl.fields.forwards.create          | str              |
|                             |                     | campaign_accounts._acl.fields.forwards.license         | str              |
|                             |                     | campaign_accounts._acl.fields.forwards.write           | str              |
|                             |                     | campaign_accounts._acl.fields.notreported.create       | str              |
|                             |                     | campaign_accounts._acl.fields.notreported.license      | str              |
|                             |                     | campaign_accounts._acl.fields.notreported.write        | str              |
|                             |                     | campaign_accounts._acl.fields.peoplewhoclicked.create  | str              |
|                             |                     | campaign_accounts._acl.fields.peoplewhoclicked.license | str              |
|                             |                     | campaign_accounts._acl.fields.peoplewhoclicked.write   | str              |
|                             |                     | campaign_accounts._acl.fields.peoplewhoopened.create   | str              |
|                             |                     | campaign_accounts._acl.fields.peoplewhoopened.license  | str              |
|                             |                     | campaign_accounts._acl.fields.peoplewhoopened.write    | str              |
|                             |                     | campaign_accounts._acl.fields.postdate.create          | str              |
|                             |                     | campaign_accounts._acl.fields.postdate.license         | str              |
|                             |                     | campaign_accounts._acl.fields.postdate.write           | str              |
|                             |                     | campaign_accounts._acl.fields.sent.create              | str              |
|                             |                     | campaign_accounts._acl.fields.sent.license             | str              |
|                             |                     | campaign_accounts._acl.fields.sent.write               | str              |
|                             |                     | campaign_accounts._acl.fields.social.create            | str              |
|                             |                     | campaign_accounts._acl.fields.social.license           | str              |
|                             |                     | campaign_accounts._acl.fields.social.write             | str              |
|                             |                     | campaign_accounts._acl.fields.totalclicks.create       | str              |
|                             |                     | campaign_accounts._acl.fields.totalclicks.license      | str              |
|                             |                     | campaign_accounts._acl.fields.totalclicks.write        | str              |
|                             |                     | campaign_accounts._acl.fields.totalopens.create        | str              |
|                             |                     | campaign_accounts._acl.fields.totalopens.license       | str              |
|                             |                     | campaign_accounts._acl.fields.totalopens.write         | str              |
|                             |                     | campaign_accounts._acl.fields.unopened.create          | str              |
|                             |                     | campaign_accounts._acl.fields.unopened.license         | str              |
|                             |                     | campaign_accounts._acl.fields.unopened.write           | str              |
|                             |                     | campaign_accounts._acl.fields.unsubscribed.create      | str              |
|                             |                     | campaign_accounts._acl.fields.unsubscribed.license     | str              |
|                             |                     | campaign_accounts._acl.fields.unsubscribed.write       | str              |
|                             |                     | campaign_accounts.id                                   | str              |
|                             |                     | campaign_accounts.name                                 | str              |
|                             |                     | campaign_name                                          | str              |
|                             |                     | created_by_link._acl._hash                             | str              |
|                             |                     | created_by_link._acl.fields[]                          | array            |
|                             |                     | created_by_link.full_name                              | str              |
|                             |                     | created_by_link.id                                     | str              |
|                             |                     | created_by_name                                        | str              |
|                             |                     | dri_workflow_template_id                               | str              |
|                             |                     | dri_workflow_template_link._acl._hash                  | str              |
|                             |                     | dri_workflow_template_link._acl.fields[]               | array            |
|                             |                     | dri_workflow_template_link.id                          | str              |
|                             |                     | dri_workflow_template_link.name                        | str              |
|                             |                     | dri_workflow_template_name                             | str              |
|                             |                     | email_addresses_non_primary                            | str              |
|                             |                     | hint_account_facebook_handle                           | str              |
|                             |                     | hint_account_fiscal_year_end                           | str              |
|                             |                     | hint_account_founded_year                              | str              |
|                             |                     | hint_account_industry                                  | str              |
|                             |                     | hint_account_industry_tags                             | str              |
|                             |                     | hint_account_location                                  | str              |
|                             |                     | hint_account_logo                                      | str              |
|                             |                     | hint_account_naics_code_lbl                            | str              |
|                             |                     | hint_account_pic                                       | str              |
|                             |                     | hint_account_size                                      | str              |
|                             |                     | last_interaction_date                                  | str              |
|                             |                     | last_interaction_parent_id                             | str              |
|                             |                     | last_interaction_parent_name                           | str              |
|                             |                     | last_interaction_parent_type                           | str              |
|                             |                     | locked_fields[]                                        | array            |
|                             |                     | member_of._acl._hash                                   | str              |
|                             |                     | member_of._acl.fields[]                                | array            |
|                             |                     | member_of.id                                           | str              |
|                             |                     | member_of.name                                         | str              |
|                             |                     | modified_by_name                                       | str              |
|                             |                     | modified_user_link._acl._hash                          | str              |
|                             |                     | modified_user_link._acl.fields[]                       | array            |
|                             |                     | modified_user_link.full_name                           | str              |
|                             |                     | modified_user_link.id                                  | str              |
|                             |                     | perform_sugar_action                                   | bool             |
|                             |                     | sync_key                                               | str              |
|                             |                     | tag[]                                                  | array            |
|                             |                     | team_count_link._acl._hash                             | str              |
|                             |                     | team_count_link._acl.fields[]                          | array            |
|                             |                     | team_count_link.id                                     | str              |
|                             |                     | team_count_link.team_count                             | str              |
|                             |                     | team_name[]                                            | array            |
|                             |                     | team_name[].id                                         | object           |
|                             |                     | team_name[].name                                       | object           |
|                             |                     | team_name[].name_2                                     | object           |
|                             |                     | team_name[].primary                                    | object           |
|                             |                     | team_name[].selected                                   | object           |
|                             |                     | widget_next_renewal_date                               | str              |

## Contacts

| Entity Schema Fields             | Entity Schema Types | Find By ID Object Fields                                    | Find By ID Types |
|----------------------------------|---------------------|-------------------------------------------------------------|------------------|
| accept_status_id                 | string              | accept_status_id                                            | str              |
| accept_status_name               | string              | accept_status_name                                          | str              |
| account_id                       | string              | account_id                                                  | str              |
| alt_address_city                 | string              | alt_address_city                                            | str              |
| alt_address_country              | string              | alt_address_country                                         | str              |
| alt_address_postalcode           | string              | alt_address_postalcode                                      | str              |
| alt_address_state                | string              | alt_address_state                                           | str              |
| alt_address_street               | string              | alt_address_street                                          | str              |
| alt_address_street_2             | string              | alt_address_street_2                                        | str              |
| alt_address_street_3             | string              | alt_address_street_3                                        | str              |
| assigned_user_id                 | string              | assigned_user_id                                            | str              |
| assistant                        | string              | assistant                                                   | str              |
| assistant_phone                  | string              | assistant_phone                                             | str              |
| birthdate                        | string              | birthdate                                                   | str              |
| calls.id                         | string              | calls.id                                                    | str              |
| campaign_id                      | string              | campaign_id                                                 | str              |
| created_by                       | string              | created_by                                                  | str              |
| date_entered                     | string              | date_entered                                                | str              |
| date_modified                    | string              | date_modified                                               | str              |
| deleted                          | boolean             | deleted                                                     | bool             |
| department                       | string              | department                                                  | str              |
| description                      | string              | description                                                 | str              |
| do_not_call                      | boolean             | do_not_call                                                 | bool             |
| email1                           | string              | email1                                                      | str              |
| email2                           | string              | email2                                                      | str              |
| email[]                          | object              | email[]                                                     | array            |
| email[].email_address            | string              | email[].email_address                                       | object           |
| email[].email_address_id         | string              | email[].email_address_id                                    | object           |
| email[].invalid_email            | boolean             | email[].invalid_email                                       | object           |
| email[].opt_out                  | boolean             | email[].opt_out                                             | object           |
| email[].primary_address          | boolean             | email[].primary_address                                     | object           |
| email[].reply_to_address         | boolean             | email[].reply_to_address                                    | object           |
| email_opt_out                    | boolean             | email_opt_out                                               | bool             |
| entry_source                     | string              | entry_source                                                | str              |
| facebook                         | string              | facebook                                                    | str              |
| first_name                       | string              | first_name                                                  | str              |
| following                        | boolean             | following                                                   | bool             |
| full_name                        | string              | full_name                                                   | str              |
| googleplus                       | string              | googleplus                                                  | str              |
| id                               | string              | id                                                          | str              |
| invalid_email                    | boolean             | invalid_email                                               | bool             |
| last_name                        | string              | last_name                                                   | str              |
| latitude_c                       | string              | latitude_c                                                  | str              |
| lead_source                      | string              | lead_source                                                 | str              |
| longitude_c                      | string              | longitude_c                                                 | str              |
| market_interest_prediction_score | string              | market_interest_prediction_score                            | str              |
| market_score                     | string              | market_score                                                | null             |
| meetings.id                      | string              | meetings.id                                                 | str              |
| mkto_sync                        | boolean             | mkto_sync                                                   | bool             |
| modified_user_id                 | string              | modified_user_id                                            | str              |
| my_favorite                      | boolean             | my_favorite                                                 | bool             |
| name                             | string              | name                                                        | str              |
| opportunities.id                 | string              | opportunities.id                                            | str              |
| opportunity_role_id              | string              | opportunity_role_id                                         | str              |
| phone_fax                        | string              | phone_fax                                                   | str              |
| phone_home                       | string              | phone_home                                                  | str              |
| phone_mobile                     | string              | phone_mobile                                                | str              |
| phone_other                      | string              | phone_other                                                 | str              |
| phone_work                       | string              | phone_work                                                  | str              |
| primary_address_city             | string              | primary_address_city                                        | str              |
| primary_address_country          | string              | primary_address_country                                     | str              |
| primary_address_postalcode       | string              | primary_address_postalcode                                  | str              |
| primary_address_state            | string              | primary_address_state                                       | str              |
| primary_address_street           | string              | primary_address_street                                      | str              |
| primary_address_street_2         | string              | primary_address_street_2                                    | str              |
| primary_address_street_3         | string              | primary_address_street_3                                    | str              |
| reports_to_id                    | string              | reports_to_id                                               | str              |
| salutation                       | string              | salutation                                                  | str              |
| site_user_id                     | string              | site_user_id                                                | str              |
| source_id                        | string              | source_id                                                   | str              |
| source_meta                      | string              | source_meta                                                 | str              |
| source_type                      | string              | source_type                                                 | str              |
| sync_key                         | string              | sync_key                                                    | str              |
| tag[]                            | object              | tag[]                                                       | array            |
| tag[].id                         | string              | tag[].id                                                    | object           |
| tag[].name                       | string              | tag[].name                                                  | object           |
| tag[].tags__name_lower           | string              | tag[].tags__name_lower                                      | object           |
| team_count                       | string              | team_count                                                  | str              |
| title                            | string              | title                                                       | str              |
| twitter                          | string              | twitter                                                     | str              |
| team[]                           | object              |                                                             |                  |
| team[].id                        | string              |                                                             |                  |
| team[].name                      | string              |                                                             |                  |
| team[].name_2                    | string              |                                                             |                  |
| team[].primary                   | boolean             |                                                             |                  |
| team[].selected                  | boolean             |                                                             |                  |
|                                  |                     | _module                                                     | str              |
|                                  |                     | accept_status_calls                                         | str              |
|                                  |                     | accept_status_meetings                                      | str              |
|                                  |                     | accept_status_messages                                      | str              |
|                                  |                     | account_name                                                | str              |
|                                  |                     | accounts._acl._hash                                         | str              |
|                                  |                     | accounts._acl.fields[]                                      | array            |
|                                  |                     | accounts.id                                                 | str              |
|                                  |                     | accounts.name                                               | str              |
|                                  |                     | assigned_user_link._acl._hash                               | str              |
|                                  |                     | assigned_user_link._acl.fields[]                            | array            |
|                                  |                     | assigned_user_link.full_name                                | str              |
|                                  |                     | assigned_user_link.id                                       | str              |
|                                  |                     | assigned_user_name                                          | str              |
|                                  |                     | business_center_id                                          | str              |
|                                  |                     | business_center_name                                        | str              |
|                                  |                     | business_centers._acl._hash                                 | str              |
|                                  |                     | business_centers._acl.fields[]                              | array            |
|                                  |                     | business_centers.id                                         | str              |
|                                  |                     | business_centers.name                                       | str              |
|                                  |                     | c_accept_status_fields                                      | str              |
|                                  |                     | campaign_contacts._acl._hash                                | str              |
|                                  |                     | campaign_contacts._acl.fields.bounced.create                | str              |
|                                  |                     | campaign_contacts._acl.fields.bounced.license               | str              |
|                                  |                     | campaign_contacts._acl.fields.bounced.write                 | str              |
|                                  |                     | campaign_contacts._acl.fields.delivered.create              | str              |
|                                  |                     | campaign_contacts._acl.fields.delivered.license             | str              |
|                                  |                     | campaign_contacts._acl.fields.delivered.write               | str              |
|                                  |                     | campaign_contacts._acl.fields.forwards.create               | str              |
|                                  |                     | campaign_contacts._acl.fields.forwards.license              | str              |
|                                  |                     | campaign_contacts._acl.fields.forwards.write                | str              |
|                                  |                     | campaign_contacts._acl.fields.notreported.create            | str              |
|                                  |                     | campaign_contacts._acl.fields.notreported.license           | str              |
|                                  |                     | campaign_contacts._acl.fields.notreported.write             | str              |
|                                  |                     | campaign_contacts._acl.fields.peoplewhoclicked.create       | str              |
|                                  |                     | campaign_contacts._acl.fields.peoplewhoclicked.license      | str              |
|                                  |                     | campaign_contacts._acl.fields.peoplewhoclicked.write        | str              |
|                                  |                     | campaign_contacts._acl.fields.peoplewhoopened.create        | str              |
|                                  |                     | campaign_contacts._acl.fields.peoplewhoopened.license       | str              |
|                                  |                     | campaign_contacts._acl.fields.peoplewhoopened.write         | str              |
|                                  |                     | campaign_contacts._acl.fields.postdate.create               | str              |
|                                  |                     | campaign_contacts._acl.fields.postdate.license              | str              |
|                                  |                     | campaign_contacts._acl.fields.postdate.write                | str              |
|                                  |                     | campaign_contacts._acl.fields.sent.create                   | str              |
|                                  |                     | campaign_contacts._acl.fields.sent.license                  | str              |
|                                  |                     | campaign_contacts._acl.fields.sent.write                    | str              |
|                                  |                     | campaign_contacts._acl.fields.social.create                 | str              |
|                                  |                     | campaign_contacts._acl.fields.social.license                | str              |
|                                  |                     | campaign_contacts._acl.fields.social.write                  | str              |
|                                  |                     | campaign_contacts._acl.fields.totalclicks.create            | str              |
|                                  |                     | campaign_contacts._acl.fields.totalclicks.license           | str              |
|                                  |                     | campaign_contacts._acl.fields.totalclicks.write             | str              |
|                                  |                     | campaign_contacts._acl.fields.totalopens.create             | str              |
|                                  |                     | campaign_contacts._acl.fields.totalopens.license            | str              |
|                                  |                     | campaign_contacts._acl.fields.totalopens.write              | str              |
|                                  |                     | campaign_contacts._acl.fields.unopened.create               | str              |
|                                  |                     | campaign_contacts._acl.fields.unopened.license              | str              |
|                                  |                     | campaign_contacts._acl.fields.unopened.write                | str              |
|                                  |                     | campaign_contacts._acl.fields.unsubscribed.create           | str              |
|                                  |                     | campaign_contacts._acl.fields.unsubscribed.license          | str              |
|                                  |                     | campaign_contacts._acl.fields.unsubscribed.write            | str              |
|                                  |                     | campaign_contacts.id                                        | str              |
|                                  |                     | campaign_contacts.name                                      | str              |
|                                  |                     | campaign_name                                               | str              |
|                                  |                     | cookie_consent                                              | bool             |
|                                  |                     | cookie_consent_received_on                                  | str              |
|                                  |                     | created_by_link._acl._hash                                  | str              |
|                                  |                     | created_by_link._acl.fields[]                               | array            |
|                                  |                     | created_by_link.full_name                                   | str              |
|                                  |                     | created_by_link.id                                          | str              |
|                                  |                     | created_by_name                                             | str              |
|                                  |                     | denorm_account_name                                         | str              |
|                                  |                     | dnb_principal_id                                            | str              |
|                                  |                     | dp_business_purpose[]                                       | array            |
|                                  |                     | dp_consent_last_updated                                     | str              |
|                                  |                     | dri_workflow_template_id                                    | str              |
|                                  |                     | dri_workflow_template_link._acl._hash                       | str              |
|                                  |                     | dri_workflow_template_link._acl.fields[]                    | array            |
|                                  |                     | dri_workflow_template_link.id                               | str              |
|                                  |                     | dri_workflow_template_link.name                             | str              |
|                                  |                     | dri_workflow_template_name                                  | str              |
|                                  |                     | email_addresses_non_primary                                 | str              |
|                                  |                     | email_and_name1                                             | str              |
|                                  |                     | external_user_id                                            | str              |
|                                  |                     | geocode_status                                              | str              |
|                                  |                     | hint_account_annual_revenue                                 | str              |
|                                  |                     | hint_account_description                                    | str              |
|                                  |                     | hint_account_facebook_handle                                | str              |
|                                  |                     | hint_account_fiscal_year_end                                | str              |
|                                  |                     | hint_account_founded_year                                   | str              |
|                                  |                     | hint_account_industry                                       | str              |
|                                  |                     | hint_account_location                                       | str              |
|                                  |                     | hint_account_logo                                           | str              |
|                                  |                     | hint_account_naics_code_lbl                                 | str              |
|                                  |                     | hint_account_sic_code_label                                 | str              |
|                                  |                     | hint_account_size                                           | str              |
|                                  |                     | hint_account_twitter_handle                                 | str              |
|                                  |                     | hint_account_website                                        | str              |
|                                  |                     | hint_contact_pic                                            | str              |
|                                  |                     | hint_education                                              | str              |
|                                  |                     | hint_education_2                                            | str              |
|                                  |                     | hint_facebook                                               | str              |
|                                  |                     | hint_industry_tags                                          | str              |
|                                  |                     | hint_job_2                                                  | str              |
|                                  |                     | hint_phone_1                                                | str              |
|                                  |                     | hint_phone_2                                                | str              |
|                                  |                     | hint_photo                                                  | str              |
|                                  |                     | hint_twitter                                                | str              |
|                                  |                     | locked_fields[]                                             | array            |
|                                  |                     | m_accept_status_fields                                      | str              |
|                                  |                     | mkto_id                                                     | null             |
|                                  |                     | mkto_lead_score                                             | str              |
|                                  |                     | modified_by_name                                            | str              |
|                                  |                     | modified_user_link._acl._hash                               | str              |
|                                  |                     | modified_user_link._acl.fields[]                            | array            |
|                                  |                     | modified_user_link.full_name                                | str              |
|                                  |                     | modified_user_link.id                                       | str              |
|                                  |                     | opportunity_role                                            | str              |
|                                  |                     | opportunity_role_fields                                     | str              |
|                                  |                     | perform_sugar_action                                        | bool             |
|                                  |                     | picture                                                     | str              |
|                                  |                     | portal_active                                               | bool             |
|                                  |                     | portal_app                                                  | str              |
|                                  |                     | portal_name                                                 | str              |
|                                  |                     | portal_password                                             | bool             |
|                                  |                     | portal_password1                                            | null             |
|                                  |                     | portal_user_company_name                                    | str              |
|                                  |                     | preferred_language                                          | str              |
|                                  |                     | report_to_name                                              | str              |
|                                  |                     | reports_to_link._acl._hash                                  | str              |
|                                  |                     | reports_to_link._acl.fields.sf_lastactivity_default.create  | str              |
|                                  |                     | reports_to_link._acl.fields.sf_lastactivity_default.license | str              |
|                                  |                     | reports_to_link._acl.fields.sf_lastactivity_default.write   | str              |
|                                  |                     | reports_to_link.id                                          | str              |
|                                  |                     | reports_to_link.name                                        | str              |
|                                  |                     | sync_contact                                                | bool             |
|                                  |                     | team_count_link._acl._hash                                  | str              |
|                                  |                     | team_count_link._acl.fields[]                               | array            |
|                                  |                     | team_count_link.id                                          | str              |
|                                  |                     | team_count_link.team_count                                  | str              |
|                                  |                     | team_name[]                                                 | array            |
|                                  |                     | team_name[].id                                              | object           |
|                                  |                     | team_name[].name                                            | object           |
|                                  |                     | team_name[].name_2                                          | object           |
|                                  |                     | team_name[].primary                                         | object           |
|                                  |                     | team_name[].selected                                        | object           |