# Differences between fields in SugarCRM

## Opportunities

| Entity Schema Fields            | Find By ID Object Fields                 |
|---------------------------------|------------------------------------------|
| account_id                      | account_id                               |
| ai_opp_conv_bin_accuracy        | ai_opp_conv_bin_accuracy                 |
| ai_opp_conv_multiplier          | ai_opp_conv_multiplier                   |
| ai_opp_conv_score_absolute      | ai_opp_conv_score_absolute               |
| ai_opp_conv_score_enum          | ai_opp_conv_score_enum                   |
| amount                          | amount                                   |
| amount_usdollar                 | amount_usdollar                          |
| assigned_user_id                | assigned_user_id                         |
| base_rate                       | base_rate                                |
| best_case                       | best_case                                |
| campaign_id                     | campaign_id                              |
| campaign_opportunities.id       | campaign_opportunities.id                |
| campaign_opportunities.name     | campaign_opportunities.name              |
| closed_revenue_line_items       | closed_revenue_line_items                |
| closed_won_revenue_line_items   | closed_won_revenue_line_items            |
| commit_stage                    | commit_stage                             |
| commit_stage_cascade            | commit_stage_cascade                     |
| contact_role                    | contact_role                             |
| created_by                      | created_by                               |
| currency_id                     | currency_id                              |
| currency_name                   | currency_name                            |
| date_closed                     | date_closed                              |
| date_closed_cascade             | date_closed_cascade                      |
| date_closed_timestamp           | date_closed_timestamp                    |
| date_entered                    | date_entered                             |
| date_modified                   | date_modified                            |
| deleted                         | deleted                                  |
| description                     | description                              |
| following                       | following                                |
| forecasted_likely               | forecasted_likely                        |
| geocode_status                  | geocode_status                           |
| id                              | id                                       |
| included_revenue_line_items     | included_revenue_line_items              |
| is_escalated                    | is_escalated                             |
| lead_source                     | lead_source                              |
| lost                            | lost                                     |
| mkto_id                         | mkto_id                                  |
| mkto_sync                       | mkto_sync                                |
| modified_user_id                | modified_user_id                         |
| my_favorite                     | my_favorite                              |
| name                            | name                                     |
| next_step                       | next_step                                |
| opportunity_type                | opportunity_type                         |
| probability                     | probability                              |
| renewal                         | renewal                                  |
| renewal_parent_id               | renewal_parent_id                        |
| renewal_parent_name             | renewal_parent_name                      |
| sales_stage                     | sales_stage                              |
| sales_stage_cascade             | sales_stage_cascade                      |
| sales_status                    | sales_status                             |
| service_duration_unit           | service_duration_unit                    |
| service_duration_unit_cascade   | service_duration_unit_cascade            |
| service_duration_value          | service_duration_value                   |
| service_duration_value_cascade  | service_duration_value_cascade           |
| service_open_flex_duration_rlis | service_open_flex_duration_rlis          |
| service_open_revenue_line_items | service_open_revenue_line_items          |
| service_start_date              | service_start_date                       |
| service_start_date_cascade      | service_start_date_cascade               |
| sl_ai_conv_score_c              | sl_ai_conv_score_c                       |
| sync_key                        | sync_key                                 |
| team_count                      | team_count                               |
| team_name[]                     | team_name[]                              |
| team_name[].id                  | team_name[].id                           |
| team_name[].name                | team_name[].name                         |
| team_name[].name_2              | team_name[].name_2                       |
| team_name[].primary             | team_name[].primary                      |
| team_name[].selected            | team_name[].selected                     |
| total_revenue_line_items        | total_revenue_line_items                 |
| widget_amount                   | widget_amount                            |
| widget_date_closed              | widget_date_closed                       |
| widget_sales_stage              | widget_sales_stage                       |
| worst_case                      | worst_case                               |
| tag                             |                                          |
|                                 | _module                                  |
|                                 | account_name                             |
|                                 | accounts._acl._hash                      |
|                                 | accounts._acl.fields[]                   |
|                                 | accounts.id                              |
|                                 | accounts.name                            |
|                                 | ai_opp_close_week_scores                 |
|                                 | ai_opp_won_score                         |
|                                 | assigned_user_link._acl._hash            |
|                                 | assigned_user_link._acl.fields[]         |
|                                 | assigned_user_link.full_name             |
|                                 | assigned_user_link.id                    |
|                                 | assigned_user_name                       |
|                                 | campaign_name                            |
|                                 | created_by_link._acl._hash               |
|                                 | created_by_link._acl.fields[]            |
|                                 | created_by_link.full_name                |
|                                 | created_by_link.id                       |
|                                 | created_by_name                          |
|                                 | currencies._acl._hash                    |
|                                 | currencies._acl.fields[]                 |
|                                 | currencies.id                            |
|                                 | currencies.name                          |
|                                 | currencies.symbol                        |
|                                 | currency_symbol                          |
|                                 | denorm_account_name                      |
|                                 | discover_data_c                          |
|                                 | dri_workflow_template_id                 |
|                                 | dri_workflow_template_link._acl._hash    |
|                                 | dri_workflow_template_link._acl.fields[] |
|                                 | dri_workflow_template_link.id            |
|                                 | dri_workflow_template_link.name          |
|                                 | dri_workflow_template_name               |
|                                 | locked_fields[]                          |
|                                 | modified_by_name                         |
|                                 | modified_user_link._acl._hash            |
|                                 | modified_user_link._acl.fields[]         |
|                                 | modified_user_link.full_name             |
|                                 | modified_user_link.id                    |
|                                 | perform_sugar_action                     |
|                                 | renewal_parent._acl._hash                |
|                                 | renewal_parent._acl.fields[]             |
|                                 | renewal_parent.id                        |
|                                 | renewal_parent.name                      |
|                                 | tag[]                                    |
|                                 | team_count_link._acl._hash               |
|                                 | team_count_link._acl.fields[]            |
|                                 | team_count_link.id                       |
|                                 | team_count_link.team_count               |

## Accounts

| Entity Schema Fields        | Find By ID Object Fields                               |
|-----------------------------|--------------------------------------------------------|
| account_type                | account_type                                           |
| annual_revenue              | annual_revenue                                         |
| assigned_user_id            | assigned_user_id                                       |
| billing_address_city        | billing_address_city                                   |
| billing_address_country     | billing_address_country                                |
| billing_address_postalcode  | billing_address_postalcode                             |
| billing_address_state       | billing_address_state                                  |
| billing_address_street      | billing_address_street                                 |
| billing_address_street_2    | billing_address_street_2                               |
| billing_address_street_3    | billing_address_street_3                               |
| billing_address_street_4    | billing_address_street_4                               |
| business_center_id          | business_center_id                                     |
| campaign_id                 | campaign_id                                            |
| created_by                  | created_by                                             |
| date_entered                | date_entered                                           |
| date_modified               | date_modified                                          |
| deleted                     | deleted                                                |
| description                 | description                                            |
| duns_num                    | duns_num                                               |
| email1                      | email1                                                 |
| email2                      | email2                                                 |
| email[]                     | email[]                                                |
| email[].email_address       | email[].email_address                                  |
| email[].email_address_id    | email[].email_address_id                               |
| email[].invalid_email       | email[].invalid_email                                  |
| email[].opt_out             | email[].opt_out                                        |
| email[].primary_address     | email[].primary_address                                |
| email[].reply_to_address    | email[].reply_to_address                               |
| email_opt_out               | email_opt_out                                          |
| employees                   | employees                                              |
| facebook                    | facebook                                               |
| following                   | following                                              |
| geocode_status              | geocode_status                                         |
| googleplus                  | googleplus                                             |
| id                          | id                                                     |
| industry                    | industry                                               |
| invalid_email               | invalid_email                                          |
| is_escalated                | is_escalated                                           |
| latitude_c                  | latitude_c                                             |
| longitude_c                 | longitude_c                                            |
| modified_user_id            | modified_user_id                                       |
| my_favorite                 | my_favorite                                            |
| name                        | name                                                   |
| next_renewal_date           | next_renewal_date                                      |
| ownership                   | ownership                                              |
| parent_id                   | parent_id                                              |
| parent_name                 | parent_name                                            |
| phone_alternate             | phone_alternate                                        |
| phone_fax                   | phone_fax                                              |
| phone_office                | phone_office                                           |
| rating                      | rating                                                 |
| service_level               | service_level                                          |
| shipping_address_city       | shipping_address_city                                  |
| shipping_address_country    | shipping_address_country                               |
| shipping_address_postalcode | shipping_address_postalcode                            |
| shipping_address_state      | shipping_address_state                                 |
| shipping_address_street     | shipping_address_street                                |
| shipping_address_street_2   | shipping_address_street_2                              |
| shipping_address_street_3   | shipping_address_street_3                              |
| shipping_address_street_4   | shipping_address_street_4                              |
| sic_code                    | sic_code                                               |
| team_count                  | team_count                                             |
| ticker_symbol               | ticker_symbol                                          |
| twitter                     | twitter                                                |
| website                     | website                                                |
| tag                         |                                                        |
| teams[]                     |                                                        |
| teams[].id                  |                                                        |
| teams[].name                |                                                        |
| teams[].name_2              |                                                        |
| teams[].primary             |                                                        |
| teams[].selected            |                                                        |
|                             | _module                                                |
|                             | assigned_user_link._acl._hash                          |
|                             | assigned_user_link._acl.fields[]                       |
|                             | assigned_user_link.full_name                           |
|                             | assigned_user_link.id                                  |
|                             | assigned_user_name                                     |
|                             | business_center_name                                   |
|                             | business_centers._acl._hash                            |
|                             | business_centers._acl.fields[]                         |
|                             | business_centers.id                                    |
|                             | business_centers.name                                  |
|                             | campaign_accounts._acl._hash                           |
|                             | campaign_accounts._acl.fields.bounced.create           |
|                             | campaign_accounts._acl.fields.bounced.license          |
|                             | campaign_accounts._acl.fields.bounced.write            |
|                             | campaign_accounts._acl.fields.delivered.create         |
|                             | campaign_accounts._acl.fields.delivered.license        |
|                             | campaign_accounts._acl.fields.delivered.write          |
|                             | campaign_accounts._acl.fields.forwards.create          |
|                             | campaign_accounts._acl.fields.forwards.license         |
|                             | campaign_accounts._acl.fields.forwards.write           |
|                             | campaign_accounts._acl.fields.notreported.create       |
|                             | campaign_accounts._acl.fields.notreported.license      |
|                             | campaign_accounts._acl.fields.notreported.write        |
|                             | campaign_accounts._acl.fields.peoplewhoclicked.create  |
|                             | campaign_accounts._acl.fields.peoplewhoclicked.license |
|                             | campaign_accounts._acl.fields.peoplewhoclicked.write   |
|                             | campaign_accounts._acl.fields.peoplewhoopened.create   |
|                             | campaign_accounts._acl.fields.peoplewhoopened.license  |
|                             | campaign_accounts._acl.fields.peoplewhoopened.write    |
|                             | campaign_accounts._acl.fields.postdate.create          |
|                             | campaign_accounts._acl.fields.postdate.license         |
|                             | campaign_accounts._acl.fields.postdate.write           |
|                             | campaign_accounts._acl.fields.sent.create              |
|                             | campaign_accounts._acl.fields.sent.license             |
|                             | campaign_accounts._acl.fields.sent.write               |
|                             | campaign_accounts._acl.fields.social.create            |
|                             | campaign_accounts._acl.fields.social.license           |
|                             | campaign_accounts._acl.fields.social.write             |
|                             | campaign_accounts._acl.fields.totalclicks.create       |
|                             | campaign_accounts._acl.fields.totalclicks.license      |
|                             | campaign_accounts._acl.fields.totalclicks.write        |
|                             | campaign_accounts._acl.fields.totalopens.create        |
|                             | campaign_accounts._acl.fields.totalopens.license       |
|                             | campaign_accounts._acl.fields.totalopens.write         |
|                             | campaign_accounts._acl.fields.unopened.create          |
|                             | campaign_accounts._acl.fields.unopened.license         |
|                             | campaign_accounts._acl.fields.unopened.write           |
|                             | campaign_accounts._acl.fields.unsubscribed.create      |
|                             | campaign_accounts._acl.fields.unsubscribed.license     |
|                             | campaign_accounts._acl.fields.unsubscribed.write       |
|                             | campaign_accounts.id                                   |
|                             | campaign_accounts.name                                 |
|                             | campaign_name                                          |
|                             | created_by_link._acl._hash                             |
|                             | created_by_link._acl.fields[]                          |
|                             | created_by_link.full_name                              |
|                             | created_by_link.id                                     |
|                             | created_by_name                                        |
|                             | dri_workflow_template_id                               |
|                             | dri_workflow_template_link._acl._hash                  |
|                             | dri_workflow_template_link._acl.fields[]               |
|                             | dri_workflow_template_link.id                          |
|                             | dri_workflow_template_link.name                        |
|                             | dri_workflow_template_name                             |
|                             | email_addresses_non_primary                            |
|                             | hint_account_facebook_handle                           |
|                             | hint_account_fiscal_year_end                           |
|                             | hint_account_founded_year                              |
|                             | hint_account_industry                                  |
|                             | hint_account_industry_tags                             |
|                             | hint_account_location                                  |
|                             | hint_account_logo                                      |
|                             | hint_account_naics_code_lbl                            |
|                             | hint_account_pic                                       |
|                             | hint_account_size                                      |
|                             | last_interaction_date                                  |
|                             | last_interaction_parent_id                             |
|                             | last_interaction_parent_name                           |
|                             | last_interaction_parent_type                           |
|                             | locked_fields[]                                        |
|                             | member_of._acl._hash                                   |
|                             | member_of._acl.fields[]                                |
|                             | member_of.id                                           |
|                             | member_of.name                                         |
|                             | modified_by_name                                       |
|                             | modified_user_link._acl._hash                          |
|                             | modified_user_link._acl.fields[]                       |
|                             | modified_user_link.full_name                           |
|                             | modified_user_link.id                                  |
|                             | perform_sugar_action                                   |
|                             | sync_key                                               |
|                             | tag[]                                                  |
|                             | team_count_link._acl._hash                             |
|                             | team_count_link._acl.fields[]                          |
|                             | team_count_link.id                                     |
|                             | team_count_link.team_count                             |
|                             | team_name[]                                            |
|                             | team_name[].id                                         |
|                             | team_name[].name                                       |
|                             | team_name[].name_2                                     |
|                             | team_name[].primary                                    |
|                             | team_name[].selected                                   |
|                             | widget_next_renewal_date                               |

## Contacts

| Entity Schema Fields             | Find By ID Object Fields                                    |
|----------------------------------|-------------------------------------------------------------|
| accept_status_id                 | accept_status_id                                            |
| accept_status_name               | accept_status_name                                          |
| account_id                       | account_id                                                  |
| alt_address_city                 | alt_address_city                                            |
| alt_address_country              | alt_address_country                                         |
| alt_address_postalcode           | alt_address_postalcode                                      |
| alt_address_state                | alt_address_state                                           |
| alt_address_street               | alt_address_street                                          |
| alt_address_street_2             | alt_address_street_2                                        |
| alt_address_street_3             | alt_address_street_3                                        |
| assigned_user_id                 | assigned_user_id                                            |
| assistant                        | assistant                                                   |
| assistant_phone                  | assistant_phone                                             |
| birthdate                        | birthdate                                                   |
| calls.id                         | calls.id                                                    |
| campaign_id                      | campaign_id                                                 |
| created_by                       | created_by                                                  |
| date_entered                     | date_entered                                                |
| date_modified                    | date_modified                                               |
| deleted                          | deleted                                                     |
| department                       | department                                                  |
| description                      | description                                                 |
| do_not_call                      | do_not_call                                                 |
| email1                           | email1                                                      |
| email2                           | email2                                                      |
| email[]                          | email[]                                                     |
| email[].email_address            | email[].email_address                                       |
| email[].email_address_id         | email[].email_address_id                                    |
| email[].invalid_email            | email[].invalid_email                                       |
| email[].opt_out                  | email[].opt_out                                             |
| email[].primary_address          | email[].primary_address                                     |
| email[].reply_to_address         | email[].reply_to_address                                    |
| email_opt_out                    | email_opt_out                                               |
| entry_source                     | entry_source                                                |
| facebook                         | facebook                                                    |
| first_name                       | first_name                                                  |
| following                        | following                                                   |
| full_name                        | full_name                                                   |
| googleplus                       | googleplus                                                  |
| id                               | id                                                          |
| invalid_email                    | invalid_email                                               |
| last_name                        | last_name                                                   |
| latitude_c                       | latitude_c                                                  |
| lead_source                      | lead_source                                                 |
| longitude_c                      | longitude_c                                                 |
| market_interest_prediction_score | market_interest_prediction_score                            |
| market_score                     | market_score                                                |
| meetings.id                      | meetings.id                                                 |
| mkto_sync                        | mkto_sync                                                   |
| modified_user_id                 | modified_user_id                                            |
| my_favorite                      | my_favorite                                                 |
| name                             | name                                                        |
| opportunities.id                 | opportunities.id                                            |
| opportunity_role_id              | opportunity_role_id                                         |
| phone_fax                        | phone_fax                                                   |
| phone_home                       | phone_home                                                  |
| phone_mobile                     | phone_mobile                                                |
| phone_other                      | phone_other                                                 |
| phone_work                       | phone_work                                                  |
| primary_address_city             | primary_address_city                                        |
| primary_address_country          | primary_address_country                                     |
| primary_address_postalcode       | primary_address_postalcode                                  |
| primary_address_state            | primary_address_state                                       |
| primary_address_street           | primary_address_street                                      |
| primary_address_street_2         | primary_address_street_2                                    |
| primary_address_street_3         | primary_address_street_3                                    |
| reports_to_id                    | reports_to_id                                               |
| salutation                       | salutation                                                  |
| site_user_id                     | site_user_id                                                |
| source_id                        | source_id                                                   |
| source_meta                      | source_meta                                                 |
| source_type                      | source_type                                                 |
| sync_key                         | sync_key                                                    |
| tag[]                            | tag[]                                                       |
| tag[].id                         | tag[].id                                                    |
| tag[].name                       | tag[].name                                                  |
| tag[].tags__name_lower           | tag[].tags__name_lower                                      |
| team_count                       | team_count                                                  |
| title                            | title                                                       |
| twitter                          | twitter                                                     |
| team[]                           |                                                             |
| team[].id                        |                                                             |
| team[].name                      |                                                             |
| team[].name_2                    |                                                             |
| team[].primary                   |                                                             |
| team[].selected                  |                                                             |
|                                  | _module                                                     |
|                                  | accept_status_calls                                         |
|                                  | accept_status_meetings                                      |
|                                  | accept_status_messages                                      |
|                                  | account_name                                                |
|                                  | accounts._acl._hash                                         |
|                                  | accounts._acl.fields[]                                      |
|                                  | accounts.id                                                 |
|                                  | accounts.name                                               |
|                                  | assigned_user_link._acl._hash                               |
|                                  | assigned_user_link._acl.fields[]                            |
|                                  | assigned_user_link.full_name                                |
|                                  | assigned_user_link.id                                       |
|                                  | assigned_user_name                                          |
|                                  | business_center_id                                          |
|                                  | business_center_name                                        |
|                                  | business_centers._acl._hash                                 |
|                                  | business_centers._acl.fields[]                              |
|                                  | business_centers.id                                         |
|                                  | business_centers.name                                       |
|                                  | c_accept_status_fields                                      |
|                                  | campaign_contacts._acl._hash                                |
|                                  | campaign_contacts._acl.fields.bounced.create                |
|                                  | campaign_contacts._acl.fields.bounced.license               |
|                                  | campaign_contacts._acl.fields.bounced.write                 |
|                                  | campaign_contacts._acl.fields.delivered.create              |
|                                  | campaign_contacts._acl.fields.delivered.license             |
|                                  | campaign_contacts._acl.fields.delivered.write               |
|                                  | campaign_contacts._acl.fields.forwards.create               |
|                                  | campaign_contacts._acl.fields.forwards.license              |
|                                  | campaign_contacts._acl.fields.forwards.write                |
|                                  | campaign_contacts._acl.fields.notreported.create            |
|                                  | campaign_contacts._acl.fields.notreported.license           |
|                                  | campaign_contacts._acl.fields.notreported.write             |
|                                  | campaign_contacts._acl.fields.peoplewhoclicked.create       |
|                                  | campaign_contacts._acl.fields.peoplewhoclicked.license      |
|                                  | campaign_contacts._acl.fields.peoplewhoclicked.write        |
|                                  | campaign_contacts._acl.fields.peoplewhoopened.create        |
|                                  | campaign_contacts._acl.fields.peoplewhoopened.license       |
|                                  | campaign_contacts._acl.fields.peoplewhoopened.write         |
|                                  | campaign_contacts._acl.fields.postdate.create               |
|                                  | campaign_contacts._acl.fields.postdate.license              |
|                                  | campaign_contacts._acl.fields.postdate.write                |
|                                  | campaign_contacts._acl.fields.sent.create                   |
|                                  | campaign_contacts._acl.fields.sent.license                  |
|                                  | campaign_contacts._acl.fields.sent.write                    |
|                                  | campaign_contacts._acl.fields.social.create                 |
|                                  | campaign_contacts._acl.fields.social.license                |
|                                  | campaign_contacts._acl.fields.social.write                  |
|                                  | campaign_contacts._acl.fields.totalclicks.create            |
|                                  | campaign_contacts._acl.fields.totalclicks.license           |
|                                  | campaign_contacts._acl.fields.totalclicks.write             |
|                                  | campaign_contacts._acl.fields.totalopens.create             |
|                                  | campaign_contacts._acl.fields.totalopens.license            |
|                                  | campaign_contacts._acl.fields.totalopens.write              |
|                                  | campaign_contacts._acl.fields.unopened.create               |
|                                  | campaign_contacts._acl.fields.unopened.license              |
|                                  | campaign_contacts._acl.fields.unopened.write                |
|                                  | campaign_contacts._acl.fields.unsubscribed.create           |
|                                  | campaign_contacts._acl.fields.unsubscribed.license          |
|                                  | campaign_contacts._acl.fields.unsubscribed.write            |
|                                  | campaign_contacts.id                                        |
|                                  | campaign_contacts.name                                      |
|                                  | campaign_name                                               |
|                                  | cookie_consent                                              |
|                                  | cookie_consent_received_on                                  |
|                                  | created_by_link._acl._hash                                  |
|                                  | created_by_link._acl.fields[]                               |
|                                  | created_by_link.full_name                                   |
|                                  | created_by_link.id                                          |
|                                  | created_by_name                                             |
|                                  | denorm_account_name                                         |
|                                  | dnb_principal_id                                            |
|                                  | dp_business_purpose[]                                       |
|                                  | dp_consent_last_updated                                     |
|                                  | dri_workflow_template_id                                    |
|                                  | dri_workflow_template_link._acl._hash                       |
|                                  | dri_workflow_template_link._acl.fields[]                    |
|                                  | dri_workflow_template_link.id                               |
|                                  | dri_workflow_template_link.name                             |
|                                  | dri_workflow_template_name                                  |
|                                  | email_addresses_non_primary                                 |
|                                  | email_and_name1                                             |
|                                  | external_user_id                                            |
|                                  | geocode_status                                              |
|                                  | hint_account_annual_revenue                                 |
|                                  | hint_account_description                                    |
|                                  | hint_account_facebook_handle                                |
|                                  | hint_account_fiscal_year_end                                |
|                                  | hint_account_founded_year                                   |
|                                  | hint_account_industry                                       |
|                                  | hint_account_location                                       |
|                                  | hint_account_logo                                           |
|                                  | hint_account_naics_code_lbl                                 |
|                                  | hint_account_sic_code_label                                 |
|                                  | hint_account_size                                           |
|                                  | hint_account_twitter_handle                                 |
|                                  | hint_account_website                                        |
|                                  | hint_contact_pic                                            |
|                                  | hint_education                                              |
|                                  | hint_education_2                                            |
|                                  | hint_facebook                                               |
|                                  | hint_industry_tags                                          |
|                                  | hint_job_2                                                  |
|                                  | hint_phone_1                                                |
|                                  | hint_phone_2                                                |
|                                  | hint_photo                                                  |
|                                  | hint_twitter                                                |
|                                  | locked_fields[]                                             |
|                                  | m_accept_status_fields                                      |
|                                  | mkto_id                                                     |
|                                  | mkto_lead_score                                             |
|                                  | modified_by_name                                            |
|                                  | modified_user_link._acl._hash                               |
|                                  | modified_user_link._acl.fields[]                            |
|                                  | modified_user_link.full_name                                |
|                                  | modified_user_link.id                                       |
|                                  | opportunity_role                                            |
|                                  | opportunity_role_fields                                     |
|                                  | perform_sugar_action                                        |
|                                  | picture                                                     |
|                                  | portal_active                                               |
|                                  | portal_app                                                  |
|                                  | portal_name                                                 |
|                                  | portal_password                                             |
|                                  | portal_password1                                            |
|                                  | portal_user_company_name                                    |
|                                  | preferred_language                                          |
|                                  | report_to_name                                              |
|                                  | reports_to_link._acl._hash                                  |
|                                  | reports_to_link._acl.fields.sf_lastactivity_default.create  |
|                                  | reports_to_link._acl.fields.sf_lastactivity_default.license |
|                                  | reports_to_link._acl.fields.sf_lastactivity_default.write   |
|                                  | reports_to_link.id                                          |
|                                  | reports_to_link.name                                        |
|                                  | sync_contact                                                |
|                                  | team_count_link._acl._hash                                  |
|                                  | team_count_link._acl.fields[]                               |
|                                  | team_count_link.id                                          |
|                                  | team_count_link.team_count                                  |
|                                  | team_name[]                                                 |
|                                  | team_name[].id                                              |
|                                  | team_name[].name                                            |
|                                  | team_name[].name_2                                          |
|                                  | team_name[].primary                                         |
|                                  | team_name[].selected                                        |