# Differences between fields in Deals/Opportunities

## Close

Fields that CRM Object has but not shown in Data Collection Schema:
`{'attachments', 'contact_name', 'pipeline_id', 'integration_links', 'pipeline_name', 'created_by_name', 'date_lost', 'updated_by_name', 'status_display_name'}`

| Entity Schema Fields      | Find By ID Object Fields  |
|---------------------------|---------------------------|
| annualized_expected_value | annualized_expected_value |
| annualized_value          | annualized_value          |
| confidence                | confidence                |
| contact_id                | contact_id                |
| created_by                | created_by                |
| date_created              | date_created              |
| date_updated              | date_updated              |
| date_won                  | date_won                  |
| expected_value            | expected_value            |
| id                        | id                        |
| lead_id                   | lead_id                   |
| lead_name                 | lead_name                 |
| note                      | note                      |
| organization_id           | organization_id           |
| status_id                 | status_id                 |
| status_label              | status_label              |
| status_type               | status_type               |
| updated_by                | updated_by                |
| user_id                   | user_id                   |
| user_name                 | user_name                 |
| value                     | value                     |
| value_currency            | value_currency            |
| value_formatted           | value_formatted           |
| value_period              | value_period              |
|                           | attachments               |
|                           | contact_name              |
|                           | pipeline_id               |
|                           | integration_links         |
|                           | pipeline_name             |
|                           | created_by_name           |
|                           | date_lost                 |
|                           | updated_by_name           |
|                           | status_display_name       |

---

## Salesforce

Fields are the same in both Entity Schema and Find By ID Object.

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

---

## HubSpot

Fields in Data Collection Schema but not in CRM Object Schema: `{'multi_select_field'}`
Fields in CRM Object Schema but not in Data Collection Schema: `{'hs_all_collaborator_owner_ids', '
hs_notes_next_activity', 'hs_notes_last_activity', 'line_item_ids'}`

| Entity Schema Fields                                             | Find By ID Object Fields                                         |
|------------------------------------------------------------------|------------------------------------------------------------------|
| amount                                                           | amount                                                           |
| amount_in_home_currency                                          | amount_in_home_currency                                          |
| billing_email                                                    | billing_email                                                    |
| calculated_property                                              | calculated_property                                              |
| closed_lost_reason                                               | closed_lost_reason                                               |
| closed_won_reason                                                | closed_won_reason                                                |
| closedate                                                        | closedate                                                        |
| company_ids                                                      | company_ids                                                      |
| contact_ids                                                      | contact_ids                                                      |
| country_of_residence                                             | country_of_residence                                             |
| createdate                                                       | createdate                                                       |
| custom__                                                         | custom__                                                         |
| custom_boolean                                                   | custom_boolean                                                   |
| custommonetaryfield                                              | custommonetaryfield                                              |
| data_test_2                                                      | data_test_2                                                      |
| days_to_close                                                    | days_to_close                                                    |
| deal_currency_code                                               | deal_currency_code                                               |
| dealname                                                         | dealname                                                         |
| dealstage                                                        | dealstage                                                        |
| dealtype                                                         | dealtype                                                         |
| delivery_date                                                    | delivery_date                                                    |
| delivery_method                                                  | delivery_method                                                  |
| description                                                      | description                                                      |
| dropdowntest_                                                    | dropdowntest_                                                    |
| dropdowntestnew                                                  | dropdowntestnew                                                  |
| engagements_last_meeting_booked                                  | engagements_last_meeting_booked                                  |
| engagements_last_meeting_booked_campaign                         | engagements_last_meeting_booked_campaign                         |
| engagements_last_meeting_booked_medium                           | engagements_last_meeting_booked_medium                           |
| engagements_last_meeting_booked_source                           | engagements_last_meeting_booked_source                           |
| export                                                           | export                                                           |
| hs_acv                                                           | hs_acv                                                           |
| hs_all_accessible_team_ids                                       | hs_all_accessible_team_ids                                       |
| hs_all_assigned_business_unit_ids                                | hs_all_assigned_business_unit_ids                                |
| hs_all_deal_split_owner_ids                                      | hs_all_deal_split_owner_ids                                      |
| hs_all_owner_ids                                                 | hs_all_owner_ids                                                 |
| hs_all_team_ids                                                  | hs_all_team_ids                                                  |
| hs_analytics_latest_source                                       | hs_analytics_latest_source                                       |
| hs_analytics_latest_source_company                               | hs_analytics_latest_source_company                               |
| hs_analytics_latest_source_contact                               | hs_analytics_latest_source_contact                               |
| hs_analytics_latest_source_data_1                                | hs_analytics_latest_source_data_1                                |
| hs_analytics_latest_source_data_1_company                        | hs_analytics_latest_source_data_1_company                        |
| hs_analytics_latest_source_data_1_contact                        | hs_analytics_latest_source_data_1_contact                        |
| hs_analytics_latest_source_data_2                                | hs_analytics_latest_source_data_2                                |
| hs_analytics_latest_source_data_2_company                        | hs_analytics_latest_source_data_2_company                        |
| hs_analytics_latest_source_data_2_contact                        | hs_analytics_latest_source_data_2_contact                        |
| hs_analytics_latest_source_timestamp                             | hs_analytics_latest_source_timestamp                             |
| hs_analytics_latest_source_timestamp_company                     | hs_analytics_latest_source_timestamp_company                     |
| hs_analytics_latest_source_timestamp_contact                     | hs_analytics_latest_source_timestamp_contact                     |
| hs_analytics_source                                              | hs_analytics_source                                              |
| hs_analytics_source_data_1                                       | hs_analytics_source_data_1                                       |
| hs_analytics_source_data_2                                       | hs_analytics_source_data_2                                       |
| hs_arr                                                           | hs_arr                                                           |
| hs_associated_deal_registration_deal_type                        | hs_associated_deal_registration_deal_type                        |
| hs_associated_deal_registration_product_interests                | hs_associated_deal_registration_product_interests                |
| hs_attributed_team_ids                                           | hs_attributed_team_ids                                           |
| hs_average_call_duration                                         | hs_average_call_duration                                         |
| hs_campaign                                                      | hs_campaign                                                      |
| hs_closed_amount                                                 | hs_closed_amount                                                 |
| hs_closed_amount_in_home_currency                                | hs_closed_amount_in_home_currency                                |
| hs_closed_deal_close_date                                        | hs_closed_deal_close_date                                        |
| hs_closed_deal_create_date                                       | hs_closed_deal_create_date                                       |
| hs_closed_won_count                                              | hs_closed_won_count                                              |
| hs_closed_won_date                                               | hs_closed_won_date                                               |
| hs_created_by_user_id                                            | hs_created_by_user_id                                            |
| hs_createdate                                                    | hs_createdate                                                    |
| hs_date_entered_159448327                                        | hs_date_entered_159448327                                        |
| hs_date_entered_159448328                                        | hs_date_entered_159448328                                        |
| hs_date_entered_159448329                                        | hs_date_entered_159448329                                        |
| hs_date_entered_159448330                                        | hs_date_entered_159448330                                        |
| hs_date_entered_159448331                                        | hs_date_entered_159448331                                        |
| hs_date_entered_159448332                                        | hs_date_entered_159448332                                        |
| hs_date_entered_159448333                                        | hs_date_entered_159448333                                        |
| hs_date_entered_159448334                                        | hs_date_entered_159448334                                        |
| hs_date_entered_241999791                                        | hs_date_entered_241999791                                        |
| hs_date_entered_241999792                                        | hs_date_entered_241999792                                        |
| hs_date_entered_241999793                                        | hs_date_entered_241999793                                        |
| hs_date_entered_241999794                                        | hs_date_entered_241999794                                        |
| hs_date_entered_241999795                                        | hs_date_entered_241999795                                        |
| hs_date_entered_241999796                                        | hs_date_entered_241999796                                        |
| hs_date_entered_241999797                                        | hs_date_entered_241999797                                        |
| hs_date_entered_243792759                                        | hs_date_entered_243792759                                        |
| hs_date_entered_244184403                                        | hs_date_entered_244184403                                        |
| hs_date_entered_252300703                                        | hs_date_entered_252300703                                        |
| hs_date_entered_266848368                                        | hs_date_entered_266848368                                        |
| hs_date_entered_appointmentscheduled                             | hs_date_entered_appointmentscheduled                             |
| hs_date_entered_closedlost                                       | hs_date_entered_closedlost                                       |
| hs_date_entered_closedwon                                        | hs_date_entered_closedwon                                        |
| hs_date_entered_contractsent                                     | hs_date_entered_contractsent                                     |
| hs_date_entered_decisionmakerboughtin                            | hs_date_entered_decisionmakerboughtin                            |
| hs_date_entered_presentationscheduled                            | hs_date_entered_presentationscheduled                            |
| hs_date_entered_qualifiedtobuy                                   | hs_date_entered_qualifiedtobuy                                   |
| hs_date_exited_159448327                                         | hs_date_exited_159448327                                         |
| hs_date_exited_159448328                                         | hs_date_exited_159448328                                         |
| hs_date_exited_159448329                                         | hs_date_exited_159448329                                         |
| hs_date_exited_159448330                                         | hs_date_exited_159448330                                         |
| hs_date_exited_159448331                                         | hs_date_exited_159448331                                         |
| hs_date_exited_159448332                                         | hs_date_exited_159448332                                         |
| hs_date_exited_159448333                                         | hs_date_exited_159448333                                         |
| hs_date_exited_159448334                                         | hs_date_exited_159448334                                         |
| hs_date_exited_241999791                                         | hs_date_exited_241999791                                         |
| hs_date_exited_241999792                                         | hs_date_exited_241999792                                         |
| hs_date_exited_241999793                                         | hs_date_exited_241999793                                         |
| hs_date_exited_241999794                                         | hs_date_exited_241999794                                         |
| hs_date_exited_241999795                                         | hs_date_exited_241999795                                         |
| hs_date_exited_241999796                                         | hs_date_exited_241999796                                         |
| hs_date_exited_241999797                                         | hs_date_exited_241999797                                         |
| hs_date_exited_243792759                                         | hs_date_exited_243792759                                         |
| hs_date_exited_244184403                                         | hs_date_exited_244184403                                         |
| hs_date_exited_252300703                                         | hs_date_exited_252300703                                         |
| hs_date_exited_266848368                                         | hs_date_exited_266848368                                         |
| hs_date_exited_appointmentscheduled                              | hs_date_exited_appointmentscheduled                              |
| hs_date_exited_closedlost                                        | hs_date_exited_closedlost                                        |
| hs_date_exited_closedwon                                         | hs_date_exited_closedwon                                         |
| hs_date_exited_contractsent                                      | hs_date_exited_contractsent                                      |
| hs_date_exited_decisionmakerboughtin                             | hs_date_exited_decisionmakerboughtin                             |
| hs_date_exited_presentationscheduled                             | hs_date_exited_presentationscheduled                             |
| hs_date_exited_qualifiedtobuy                                    | hs_date_exited_qualifiedtobuy                                    |
| hs_days_to_close_raw                                             | hs_days_to_close_raw                                             |
| hs_deal_amount_calculation_preference                            | hs_deal_amount_calculation_preference                            |
| hs_deal_registration_mrr                                         | hs_deal_registration_mrr                                         |
| hs_deal_registration_mrr_currency_code                           | hs_deal_registration_mrr_currency_code                           |
| hs_deal_score                                                    | hs_deal_score                                                    |
| hs_deal_stage_probability                                        | hs_deal_stage_probability                                        |
| hs_deal_stage_probability_shadow                                 | hs_deal_stage_probability_shadow                                 |
| hs_duration                                                      | hs_duration                                                      |
| hs_exchange_rate                                                 | hs_exchange_rate                                                 |
| hs_forecast_amount                                               | hs_forecast_amount                                               |
| hs_forecast_probability                                          | hs_forecast_probability                                          |
| hs_has_empty_conditional_stage_properties                        | hs_has_empty_conditional_stage_properties                        |
| hs_is_active_shared_deal                                         | hs_is_active_shared_deal                                         |
| hs_is_closed                                                     | hs_is_closed                                                     |
| hs_is_closed_count                                               | hs_is_closed_count                                               |
| hs_is_closed_lost                                                | hs_is_closed_lost                                                |
| hs_is_closed_won                                                 | hs_is_closed_won                                                 |
| hs_is_deal_split                                                 | hs_is_deal_split                                                 |
| hs_is_in_first_deal_stage                                        | hs_is_in_first_deal_stage                                        |
| hs_is_open_count                                                 | hs_is_open_count                                                 |
| hs_lastmodifieddate                                              | hs_lastmodifieddate                                              |
| hs_latest_approval_status                                        | hs_latest_approval_status                                        |
| hs_latest_approval_status_approval_id                            | hs_latest_approval_status_approval_id                            |
| hs_latest_meeting_activity                                       | hs_latest_meeting_activity                                       |
| hs_likelihood_to_close                                           | hs_likelihood_to_close                                           |
| hs_line_item_global_term_hs_discount_percentage                  | hs_line_item_global_term_hs_discount_percentage                  |
| hs_line_item_global_term_hs_discount_percentage_enabled          | hs_line_item_global_term_hs_discount_percentage_enabled          |
| hs_line_item_global_term_hs_recurring_billing_period             | hs_line_item_global_term_hs_recurring_billing_period             |
| hs_line_item_global_term_hs_recurring_billing_period_enabled     | hs_line_item_global_term_hs_recurring_billing_period_enabled     |
| hs_line_item_global_term_hs_recurring_billing_start_date         | hs_line_item_global_term_hs_recurring_billing_start_date         |
| hs_line_item_global_term_hs_recurring_billing_start_date_enabled | hs_line_item_global_term_hs_recurring_billing_start_date_enabled |
| hs_line_item_global_term_recurringbillingfrequency               | hs_line_item_global_term_recurringbillingfrequency               |
| hs_line_item_global_term_recurringbillingfrequency_enabled       | hs_line_item_global_term_recurringbillingfrequency_enabled       |
| hs_manual_campaign_ids                                           | hs_manual_campaign_ids                                           |
| hs_manual_forecast_category                                      | hs_manual_forecast_category                                      |
| hs_merged_object_ids                                             | hs_merged_object_ids                                             |
| hs_mrr                                                           | hs_mrr                                                           |
| hs_net_pipeline_impact                                           | hs_net_pipeline_impact                                           |
| hs_next_meeting_id                                               | hs_next_meeting_id                                               |
| hs_next_meeting_name                                             | hs_next_meeting_name                                             |
| hs_next_meeting_start_time                                       | hs_next_meeting_start_time                                       |
| hs_next_step                                                     | hs_next_step                                                     |
| hs_next_step_updated_at                                          | hs_next_step_updated_at                                          |
| hs_notes_next_activity_type                                      | hs_notes_next_activity_type                                      |
| hs_num_associated_active_deal_registrations                      | hs_num_associated_active_deal_registrations                      |
| hs_num_associated_deal_registrations                             | hs_num_associated_deal_registrations                             |
| hs_num_associated_deal_splits                                    | hs_num_associated_deal_splits                                    |
| hs_num_of_associated_line_items                                  | hs_num_of_associated_line_items                                  |
| hs_num_target_accounts                                           | hs_num_target_accounts                                           |
| hs_number_of_call_engagements                                    | hs_number_of_call_engagements                                    |
| hs_number_of_inbound_calls                                       | hs_number_of_inbound_calls                                       |
| hs_number_of_outbound_calls                                      | hs_number_of_outbound_calls                                      |
| hs_number_of_overdue_tasks                                       | hs_number_of_overdue_tasks                                       |
| hs_number_of_scheduled_meetings                                  | hs_number_of_scheduled_meetings                                  |
| hs_object_id                                                     | hs_object_id                                                     |
| hs_object_source                                                 | hs_object_source                                                 |
| hs_object_source_detail_1                                        | hs_object_source_detail_1                                        |
| hs_object_source_detail_2                                        | hs_object_source_detail_2                                        |
| hs_object_source_detail_3                                        | hs_object_source_detail_3                                        |
| hs_object_source_id                                              | hs_object_source_id                                              |
| hs_object_source_label                                           | hs_object_source_label                                           |
| hs_object_source_user_id                                         | hs_object_source_user_id                                         |
| hs_open_amount_in_home_currency                                  | hs_open_amount_in_home_currency                                  |
| hs_open_deal_create_date                                         | hs_open_deal_create_date                                         |
| hs_owning_teams                                                  | hs_owning_teams                                                  |
| hs_pinned_engagement_id                                          | hs_pinned_engagement_id                                          |
| hs_predicted_amount                                              | hs_predicted_amount                                              |
| hs_predicted_amount_in_home_currency                             | hs_predicted_amount_in_home_currency                             |
| hs_primary_associated_company                                    | hs_primary_associated_company                                    |
| hs_priority                                                      | hs_priority                                                      |
| hs_projected_amount                                              | hs_projected_amount                                              |
| hs_projected_amount_in_home_currency                             | hs_projected_amount_in_home_currency                             |
| hs_read_only                                                     | hs_read_only                                                     |
| hs_sales_email_last_replied                                      | hs_sales_email_last_replied                                      |
| hs_shared_team_ids                                               | hs_shared_team_ids                                               |
| hs_shared_user_ids                                               | hs_shared_user_ids                                               |
| hs_source_object_id                                              | hs_source_object_id                                              |
| hs_synced_deal_owner_name_and_email                              | hs_synced_deal_owner_name_and_email                              |
| hs_tag_ids                                                       | hs_tag_ids                                                       |
| hs_tcv                                                           | hs_tcv                                                           |
| hs_time_in_159448327                                             | hs_time_in_159448327                                             |
| hs_time_in_159448328                                             | hs_time_in_159448328                                             |
| hs_time_in_159448329                                             | hs_time_in_159448329                                             |
| hs_time_in_159448330                                             | hs_time_in_159448330                                             |
| hs_time_in_159448331                                             | hs_time_in_159448331                                             |
| hs_time_in_159448332                                             | hs_time_in_159448332                                             |
| hs_time_in_159448333                                             | hs_time_in_159448333                                             |
| hs_time_in_159448334                                             | hs_time_in_159448334                                             |
| hs_time_in_241999791                                             | hs_time_in_241999791                                             |
| hs_time_in_241999792                                             | hs_time_in_241999792                                             |
| hs_time_in_241999793                                             | hs_time_in_241999793                                             |
| hs_time_in_241999794                                             | hs_time_in_241999794                                             |
| hs_time_in_241999795                                             | hs_time_in_241999795                                             |
| hs_time_in_241999796                                             | hs_time_in_241999796                                             |
| hs_time_in_241999797                                             | hs_time_in_241999797                                             |
| hs_time_in_243792759                                             | hs_time_in_243792759                                             |
| hs_time_in_244184403                                             | hs_time_in_244184403                                             |
| hs_time_in_252300703                                             | hs_time_in_252300703                                             |
| hs_time_in_266848368                                             | hs_time_in_266848368                                             |
| hs_time_in_appointmentscheduled                                  | hs_time_in_appointmentscheduled                                  |
| hs_time_in_closedlost                                            | hs_time_in_closedlost                                            |
| hs_time_in_closedwon                                             | hs_time_in_closedwon                                             |
| hs_time_in_contractsent                                          | hs_time_in_contractsent                                          |
| hs_time_in_decisionmakerboughtin                                 | hs_time_in_decisionmakerboughtin                                 |
| hs_time_in_presentationscheduled                                 | hs_time_in_presentationscheduled                                 |
| hs_time_in_qualifiedtobuy                                        | hs_time_in_qualifiedtobuy                                        |
| hs_unique_creation_key                                           | hs_unique_creation_key                                           |
| hs_updated_by_user_id                                            | hs_updated_by_user_id                                            |
| hs_user_ids_of_all_notification_followers                        | hs_user_ids_of_all_notification_followers                        |
| hs_user_ids_of_all_notification_unfollowers                      | hs_user_ids_of_all_notification_unfollowers                      |
| hs_user_ids_of_all_owners                                        | hs_user_ids_of_all_owners                                        |
| hs_v2_cumulative_time_in_159448327                               | hs_v2_cumulative_time_in_159448327                               |
| hs_v2_cumulative_time_in_159448328                               | hs_v2_cumulative_time_in_159448328                               |
| hs_v2_cumulative_time_in_159448329                               | hs_v2_cumulative_time_in_159448329                               |
| hs_v2_cumulative_time_in_159448330                               | hs_v2_cumulative_time_in_159448330                               |
| hs_v2_cumulative_time_in_159448331                               | hs_v2_cumulative_time_in_159448331                               |
| hs_v2_cumulative_time_in_159448332                               | hs_v2_cumulative_time_in_159448332                               |
| hs_v2_cumulative_time_in_159448333                               | hs_v2_cumulative_time_in_159448333                               |
| hs_v2_cumulative_time_in_159448334                               | hs_v2_cumulative_time_in_159448334                               |
| hs_v2_cumulative_time_in_241999791                               | hs_v2_cumulative_time_in_241999791                               |
| hs_v2_cumulative_time_in_241999792                               | hs_v2_cumulative_time_in_241999792                               |
| hs_v2_cumulative_time_in_241999793                               | hs_v2_cumulative_time_in_241999793                               |
| hs_v2_cumulative_time_in_241999794                               | hs_v2_cumulative_time_in_241999794                               |
| hs_v2_cumulative_time_in_241999795                               | hs_v2_cumulative_time_in_241999795                               |
| hs_v2_cumulative_time_in_241999796                               | hs_v2_cumulative_time_in_241999796                               |
| hs_v2_cumulative_time_in_241999797                               | hs_v2_cumulative_time_in_241999797                               |
| hs_v2_cumulative_time_in_appointmentscheduled                    | hs_v2_cumulative_time_in_appointmentscheduled                    |
| hs_v2_cumulative_time_in_closedlost                              | hs_v2_cumulative_time_in_closedlost                              |
| hs_v2_cumulative_time_in_closedwon                               | hs_v2_cumulative_time_in_closedwon                               |
| hs_v2_cumulative_time_in_contractsent                            | hs_v2_cumulative_time_in_contractsent                            |
| hs_v2_cumulative_time_in_decisionmakerboughtin                   | hs_v2_cumulative_time_in_decisionmakerboughtin                   |
| hs_v2_cumulative_time_in_presentationscheduled                   | hs_v2_cumulative_time_in_presentationscheduled                   |
| hs_v2_cumulative_time_in_qualifiedtobuy                          | hs_v2_cumulative_time_in_qualifiedtobuy                          |
| hs_v2_date_entered_159448327                                     | hs_v2_date_entered_159448327                                     |
| hs_v2_date_entered_159448328                                     | hs_v2_date_entered_159448328                                     |
| hs_v2_date_entered_159448329                                     | hs_v2_date_entered_159448329                                     |
| hs_v2_date_entered_159448330                                     | hs_v2_date_entered_159448330                                     |
| hs_v2_date_entered_159448331                                     | hs_v2_date_entered_159448331                                     |
| hs_v2_date_entered_159448332                                     | hs_v2_date_entered_159448332                                     |
| hs_v2_date_entered_159448333                                     | hs_v2_date_entered_159448333                                     |
| hs_v2_date_entered_159448334                                     | hs_v2_date_entered_159448334                                     |
| hs_v2_date_entered_241999791                                     | hs_v2_date_entered_241999791                                     |
| hs_v2_date_entered_241999792                                     | hs_v2_date_entered_241999792                                     |
| hs_v2_date_entered_241999793                                     | hs_v2_date_entered_241999793                                     |
| hs_v2_date_entered_241999794                                     | hs_v2_date_entered_241999794                                     |
| hs_v2_date_entered_241999795                                     | hs_v2_date_entered_241999795                                     |
| hs_v2_date_entered_241999796                                     | hs_v2_date_entered_241999796                                     |
| hs_v2_date_entered_241999797                                     | hs_v2_date_entered_241999797                                     |
| hs_v2_date_entered_appointmentscheduled                          | hs_v2_date_entered_appointmentscheduled                          |
| hs_v2_date_entered_closedlost                                    | hs_v2_date_entered_closedlost                                    |
| hs_v2_date_entered_closedwon                                     | hs_v2_date_entered_closedwon                                     |
| hs_v2_date_entered_contractsent                                  | hs_v2_date_entered_contractsent                                  |
| hs_v2_date_entered_current_stage                                 | hs_v2_date_entered_current_stage                                 |
| hs_v2_date_entered_decisionmakerboughtin                         | hs_v2_date_entered_decisionmakerboughtin                         |
| hs_v2_date_entered_presentationscheduled                         | hs_v2_date_entered_presentationscheduled                         |
| hs_v2_date_entered_qualifiedtobuy                                | hs_v2_date_entered_qualifiedtobuy                                |
| hs_v2_date_exited_159448327                                      | hs_v2_date_exited_159448327                                      |
| hs_v2_date_exited_159448328                                      | hs_v2_date_exited_159448328                                      |
| hs_v2_date_exited_159448329                                      | hs_v2_date_exited_159448329                                      |
| hs_v2_date_exited_159448330                                      | hs_v2_date_exited_159448330                                      |
| hs_v2_date_exited_159448331                                      | hs_v2_date_exited_159448331                                      |
| hs_v2_date_exited_159448332                                      | hs_v2_date_exited_159448332                                      |
| hs_v2_date_exited_159448333                                      | hs_v2_date_exited_159448333                                      |
| hs_v2_date_exited_159448334                                      | hs_v2_date_exited_159448334                                      |
| hs_v2_date_exited_241999791                                      | hs_v2_date_exited_241999791                                      |
| hs_v2_date_exited_241999792                                      | hs_v2_date_exited_241999792                                      |
| hs_v2_date_exited_241999793                                      | hs_v2_date_exited_241999793                                      |
| hs_v2_date_exited_241999794                                      | hs_v2_date_exited_241999794                                      |
| hs_v2_date_exited_241999795                                      | hs_v2_date_exited_241999795                                      |
| hs_v2_date_exited_241999796                                      | hs_v2_date_exited_241999796                                      |
| hs_v2_date_exited_241999797                                      | hs_v2_date_exited_241999797                                      |
| hs_v2_date_exited_appointmentscheduled                           | hs_v2_date_exited_appointmentscheduled                           |
| hs_v2_date_exited_closedlost                                     | hs_v2_date_exited_closedlost                                     |
| hs_v2_date_exited_closedwon                                      | hs_v2_date_exited_closedwon                                      |
| hs_v2_date_exited_contractsent                                   | hs_v2_date_exited_contractsent                                   |
| hs_v2_date_exited_decisionmakerboughtin                          | hs_v2_date_exited_decisionmakerboughtin                          |
| hs_v2_date_exited_presentationscheduled                          | hs_v2_date_exited_presentationscheduled                          |
| hs_v2_date_exited_qualifiedtobuy                                 | hs_v2_date_exited_qualifiedtobuy                                 |
| hs_v2_latest_time_in_159448327                                   | hs_v2_latest_time_in_159448327                                   |
| hs_v2_latest_time_in_159448328                                   | hs_v2_latest_time_in_159448328                                   |
| hs_v2_latest_time_in_159448329                                   | hs_v2_latest_time_in_159448329                                   |
| hs_v2_latest_time_in_159448330                                   | hs_v2_latest_time_in_159448330                                   |
| hs_v2_latest_time_in_159448331                                   | hs_v2_latest_time_in_159448331                                   |
| hs_v2_latest_time_in_159448332                                   | hs_v2_latest_time_in_159448332                                   |
| hs_v2_latest_time_in_159448333                                   | hs_v2_latest_time_in_159448333                                   |
| hs_v2_latest_time_in_159448334                                   | hs_v2_latest_time_in_159448334                                   |
| hs_v2_latest_time_in_241999791                                   | hs_v2_latest_time_in_241999791                                   |
| hs_v2_latest_time_in_241999792                                   | hs_v2_latest_time_in_241999792                                   |
| hs_v2_latest_time_in_241999793                                   | hs_v2_latest_time_in_241999793                                   |
| hs_v2_latest_time_in_241999794                                   | hs_v2_latest_time_in_241999794                                   |
| hs_v2_latest_time_in_241999795                                   | hs_v2_latest_time_in_241999795                                   |
| hs_v2_latest_time_in_241999796                                   | hs_v2_latest_time_in_241999796                                   |
| hs_v2_latest_time_in_241999797                                   | hs_v2_latest_time_in_241999797                                   |
| hs_v2_latest_time_in_appointmentscheduled                        | hs_v2_latest_time_in_appointmentscheduled                        |
| hs_v2_latest_time_in_closedlost                                  | hs_v2_latest_time_in_closedlost                                  |
| hs_v2_latest_time_in_closedwon                                   | hs_v2_latest_time_in_closedwon                                   |
| hs_v2_latest_time_in_contractsent                                | hs_v2_latest_time_in_contractsent                                |
| hs_v2_latest_time_in_decisionmakerboughtin                       | hs_v2_latest_time_in_decisionmakerboughtin                       |
| hs_v2_latest_time_in_presentationscheduled                       | hs_v2_latest_time_in_presentationscheduled                       |
| hs_v2_latest_time_in_qualifiedtobuy                              | hs_v2_latest_time_in_qualifiedtobuy                              |
| hs_v2_time_in_current_stage                                      | hs_v2_time_in_current_stage                                      |
| hs_was_imported                                                  | hs_was_imported                                                  |
| hubspot_owner_assigneddate                                       | hubspot_owner_assigneddate                                       |
| hubspot_owner_id                                                 | hubspot_owner_id                                                 |
| hubspot_team_id                                                  | hubspot_team_id                                                  |
| lena_custom_prop                                                 | lena_custom_prop                                                 |
| lenas_new_prop                                                   | lenas_new_prop                                                   |
| multi_select_field                                               |                                                                  |
| n1                                                               | n1                                                               |
| nat_checkbox_test                                                | nat_checkbox_test                                                |
| nat_dropdown_test                                                | nat_dropdown_test                                                |
| nat_radiobutton_test                                             | nat_radiobutton_test                                             |
| nat_test___spec__                                                | nat_test___spec__                                                |
| nat_test_date                                                    | nat_test_date                                                    |
| nat_test_phone                                                   | nat_test_phone                                                   |
| nat_test_spec_symbol_                                            | nat_test_spec_symbol_                                            |
| nat_text_test                                                    | nat_text_test                                                    |
| notes_last_contacted                                             | notes_last_contacted                                             |
| notes_last_updated                                               | notes_last_updated                                               |
| notes_next_activity_date                                         | notes_next_activity_date                                         |
| num_associated_contacts                                          | num_associated_contacts                                          |
| num_contacted_notes                                              | num_contacted_notes                                              |
| num_notes                                                        | num_notes                                                        |
| number_of_repro_steps                                            | number_of_repro_steps                                            |
| number_of_rooms                                                  | number_of_rooms                                                  |
| panda_deal_datetime_check                                        | panda_deal_datetime_check                                        |
| pd_55716                                                         | pd_55716                                                         |
| pipeline                                                         | pipeline                                                         |
| present_wrap                                                     | present_wrap                                                     |
| sensitive_field_test                                             | sensitive_field_test                                             |
| single_checkbox                                                  | single_checkbox                                                  |
| super_new                                                        | super_new                                                        |
| tatata                                                           | tatata                                                           |
| test_contact                                                     | test_contact                                                     |
| test_currency                                                    | test_currency                                                    |
| test_date                                                        | test_date                                                        |
| test_date_1                                                      | test_date_1                                                      |
| test_hubspot_property_integration                                | test_hubspot_property_integration                                |
| test_property                                                    | test_property                                                    |
| test_timur_property                                              | test_timur_property                                              |
| this_is_my_property                                              | this_is_my_property                                              |
| truefalse                                                        | truefalse                                                        |
| tytyty                                                           | tytyty                                                           |
| utilisation_rate                                                 | utilisation_rate                                                 |
| utilisation_rate_formateed                                       | utilisation_rate_formateed                                       |
|                                                                  | hs_all_collaborator_owner_ids                                    |
|                                                                  | hs_notes_next_activity                                           |
|                                                                  | hs_notes_last_activity                                           |
|                                                                  | line_item_ids                                                    |

---

## SugarCRM

Fields in CRM Object Schema but not in Data Collection Schema:
`{'dri_workflow_template_name', 'discover_data_c', 'assigned_user_name', 'dri_workflow_template_id', 'renewal_parent', 'account_name', 'team_count_link', 'assigned_user_link', '_acl', 'ai_opp_won_score', 'modified_user_link', 'currency_symbol', '_module', 'campaign_name', 'created_by_link', 'accounts', 'created_by_name', 'dri_workflow_template_link', 'modified_by_name', 'denorm_account_name', 'perform_sugar_action', 'locked_fields', 'ai_opp_close_week_scores', 'currencies'}`

| Entity Schema Fields            | Find By ID Object Fields        |
|---------------------------------|---------------------------------|
| account_id                      | account_id                      |
| ai_opp_conv_bin_accuracy        | ai_opp_conv_bin_accuracy        |
| ai_opp_conv_multiplier          | ai_opp_conv_multiplier          |
| ai_opp_conv_score_absolute      | ai_opp_conv_score_absolute      |
| ai_opp_conv_score_enum          | ai_opp_conv_score_enum          |
| amount                          | amount                          |
| amount_usdollar                 | amount_usdollar                 |
| assigned_user_id                | assigned_user_id                |
| base_rate                       | base_rate                       |
| best_case                       | best_case                       |
| campaign_id                     | campaign_id                     |
| campaign_opportunities          | campaign_opportunities          |
| closed_revenue_line_items       | closed_revenue_line_items       |
| closed_won_revenue_line_items   | closed_won_revenue_line_items   |
| commit_stage                    | commit_stage                    |
| commit_stage_cascade            | commit_stage_cascade            |
| contact_role                    | contact_role                    |
| created_by                      | created_by                      |
| currency_id                     | currency_id                     |
| currency_name                   | currency_name                   |
| date_closed                     | date_closed                     |
| date_closed_cascade             | date_closed_cascade             |
| date_closed_timestamp           | date_closed_timestamp           |
| date_entered                    | date_entered                    |
| date_modified                   | date_modified                   |
| deleted                         | deleted                         |
| description                     | description                     |
| following                       | following                       |
| forecasted_likely               | forecasted_likely               |
| geocode_status                  | geocode_status                  |
| id                              | id                              |
| included_revenue_line_items     | included_revenue_line_items     |
| is_escalated                    | is_escalated                    |
| lead_source                     | lead_source                     |
| lost                            | lost                            |
| mkto_id                         | mkto_id                         |
| mkto_sync                       | mkto_sync                       |
| modified_user_id                | modified_user_id                |
| my_favorite                     | my_favorite                     |
| name                            | name                            |
| next_step                       | next_step                       |
| opportunity_type                | opportunity_type                |
| probability                     | probability                     |
| renewal                         | renewal                         |
| renewal_parent_id               | renewal_parent_id               |
| renewal_parent_name             | renewal_parent_name             |
| sales_stage                     | sales_stage                     |
| sales_stage_cascade             | sales_stage_cascade             |
| sales_status                    | sales_status                    |
| service_duration_unit           | service_duration_unit           |
| service_duration_unit_cascade   | service_duration_unit_cascade   |
| service_duration_value          | service_duration_value          |
| service_duration_value_cascade  | service_duration_value_cascade  |
| service_open_flex_duration_rlis | service_open_flex_duration_rlis |
| service_open_revenue_line_items | service_open_revenue_line_items |
| service_start_date              | service_start_date              |
| service_start_date_cascade      | service_start_date_cascade      |
| sl_ai_conv_score_c              | sl_ai_conv_score_c              |
| sync_key                        | sync_key                        |
| tag                             | tag                             |
| team_count                      | team_count                      |
| team_name                       | team_name                       |
| total_revenue_line_items        | total_revenue_line_items        |
| widget_amount                   | widget_amount                   |
| widget_date_closed              | widget_date_closed              |
| widget_sales_stage              | widget_sales_stage              |
| worst_case                      | worst_case                      |
|                                 | dri_workflow_template_name      |
|                                 | discover_data_c                 |
|                                 | assigned_user_name              |
|                                 | dri_workflow_template_id        |
|                                 | renewal_parent                  |
|                                 | account_name                    |
|                                 | team_count_link                 |
|                                 | assigned_user_link              |
|                                 | _acl                            |
|                                 | ai_opp_won_score                |
|                                 | modified_user_link              |
|                                 | currency_symbol                 |
|                                 | module                          |
|                                 | campaign_name                   |
|                                 | created_by_link                 |
|                                 | accounts                        |
|                                 | created_by_name                 |
|                                 | dri_workflow_template_link      |
|                                 | modified_by_name                |
|                                 | denorm_account_name             |
|                                 | perform_sugar_action            |
|                                 | locked_fields                   |
|                                 | ai_opp_close_week_scores        |
|                                 | currencies                      |

---

## Copper

Fields in CRM Object Schema but not in Data Collection Schema:
`{'date_last_contacted', 'leads_converted_from', 'date_stage_changed', 'date_lead_created', 'pipeline_is_revenue', 'converted_value', 'pipeline_type', 'converted_unit'}`

| Entity Schema Fields | Find By ID Object Fields |
|----------------------|--------------------------|
| assignee_id          | assignee_id              |
| close_date           | close_date               |
| company_id           | company_id               |
| company_name         | company_name             |
| custom_104810        | custom_104810            |
| custom_107587        | custom_107587            |
| custom_107887        | custom_107887            |
| custom_107890        | custom_107890            |
| custom_111060        | custom_111060            |
| custom_113843        | custom_113843            |
| custom_114310        | custom_114310            |
| custom_182699        | custom_182699            |
| custom_226946        | custom_226946            |
| custom_248275        | custom_248275            |
| custom_248282        | custom_248282            |
| custom_257541        | custom_257541            |
| custom_257554        | custom_257554            |
| custom_285046        | custom_285046            |
| custom_288717        | custom_288717            |
| custom_288719        | custom_288719            |
| custom_288721        | custom_288721            |
| custom_288722        | custom_288722            |
| custom_288724        | custom_288724            |
| custom_288725        | custom_288725            |
| custom_288727        | custom_288727            |
| custom_288766        | custom_288766            |
| custom_295917        | custom_295917            |
| custom_305253        | custom_305253            |
| custom_330338        | custom_330338            |
| custom_330339        | custom_330339            |
| custom_330343        | custom_330343            |
| custom_330344        | custom_330344            |
| custom_330345        | custom_330345            |
| custom_330352        | custom_330352            |
| custom_330356        | custom_330356            |
| custom_330357        | custom_330357            |
| custom_330358        | custom_330358            |
| custom_330359        | custom_330359            |
| custom_330360        | custom_330360            |
| custom_344230        | custom_344230            |
| custom_344231        | custom_344231            |
| custom_344363        | custom_344363            |
| custom_344372        | custom_344372            |
| custom_344373        | custom_344373            |
| custom_344374        | custom_344374            |
| custom_346502        | custom_346502            |
| custom_346506        | custom_346506            |
| custom_346508        | custom_346508            |
| custom_346509        | custom_346509            |
| custom_346510        | custom_346510            |
| custom_349962        | custom_349962            |
| custom_365440        | custom_365440            |
| custom_367051        | custom_367051            |
| custom_379268        | custom_379268            |
| custom_391555        | custom_391555            |
| custom_418074        | custom_418074            |
| custom_418077        | custom_418077            |
| custom_418650        | custom_418650            |
| custom_418651        | custom_418651            |
| custom_418656        | custom_418656            |
| custom_418657        | custom_418657            |
| custom_435367        | custom_435367            |
| custom_484800        | custom_484800            |
| custom_542838        | custom_542838            |
| custom_554918        | custom_554918            |
| custom_646696        | custom_646696            |
| custom_671286        | custom_671286            |
| custom_73630         | custom_73630             |
| custom_84682         | custom_84682             |
| customer_source_id   | customer_source_id       |
| date_created         | date_created             |
| date_modified        | date_modified            |
| details              | details                  |
| id                   | id                       |
| interaction_count    | interaction_count        |
| loss_reason_id       | loss_reason_id           |
| monetary_unit        | monetary_unit            |
| monetary_value       | monetary_value           |
| name                 | name                     |
| pipeline_id          | pipeline_id              |
| pipeline_stage_id    | pipeline_stage_id        |
| primary_contact_id   | primary_contact_id       |
| priority             | priority                 |
| status               | status                   |
| tags                 | tags                     |
| win_probability      | win_probability          |
|                      | date_last_contacted      |
|                      | leads_converted_from     |
|                      | date_stage_changed       |
|                      | date_lead_created        |
|                      | pipeline_is_revenue      |
|                      | converted_value          |
|                      | pipeline_type            |
|                      | converted_unit           |

---

## Pipedrive

Fields in Data Collection Schema but not in CRM Object Schema:
`{'f833bdcc78798d16f8387238cf42cbc918851ba3_lat', 'a6ba35ef350cd9a2a401482f7267685d5b35edfd_long', '5c62123adff03afe4daf58addea5bb468ea0a915_long', '19941856afdfc9f384b39389c3f4f20c56c7bf6e_long', '19941856afdfc9f384b39389c3f4f20c56c7bf6e_lat', '2213b9a5fdbc89c7f889139cc076b2795432d018_lat', 'ec1202406dfc819cb4f06bf9f31181395a452f12_lat', '1c460f79fbace9ba9df28aade17640a890447929_lat', 'a6ba35ef350cd9a2a401482f7267685d5b35edfd_lat', '533d1bc79102279007bf371611987cdb79dac50e_long', 'ec1202406dfc819cb4f06bf9f31181395a452f12_long', 'f4118fc6c21d1ea9bc78fa52988118ff1c01dcde_long', '2213b9a5fdbc89c7f889139cc076b2795432d018_long', 'org', '533d1bc79102279007bf371611987cdb79dac50e_lat', '1c460f79fbace9ba9df28aade17640a890447929_long', 'f4118fc6c21d1ea9bc78fa52988118ff1c01dcde_lat', 'group_id', 'acae3beb40bf080c3912b625a3b66a0c068ade6c_long', '9be2bc1f2d3922de07c5f738fbc946920ee482b4_long', 'renewal_type', 'acae3beb40bf080c3912b625a3b66a0c068ade6c_lat', 'creator_user', '5c62123adff03afe4daf58addea5bb468ea0a915_lat', '3d806699a95dd5d44c26314a54348f86497c742e_lat', 'group_name', 'd7905cd9d3de6ef22f93367ba37c7d73ebfbe856_long', 'd7905cd9d3de6ef22f93367ba37c7d73ebfbe856_lat', 'user', '9be2bc1f2d3922de07c5f738fbc946920ee482b4_lat', 'f833bdcc78798d16f8387238cf42cbc918851ba3_long', '3d806699a95dd5d44c26314a54348f86497c742e_long', 'person'}`
Fields in CRM Object Schema but not in Data Collection Schema:
`{'deleted', 'local_won_date', 'next_activity', 'org_hidden', 'age', 'followers_count', 'average_stage_progress', 'cc_email', 'stay_in_pipeline_stages', 'average_time_to_won', 'last_activity', 'sequence_enrollment', 'person_hidden', 'local_close_date', 'local_lost_date', 'files_count'}`

| Entity Schema Fields     | Find By ID Object Fields |
|--------------------------|--------------------------|
| active                   | active                   |
| activities_count         | activities_count         |
| acv                      | acv                      |
| acv_currency             | acv_currency             |
| add_time                 | add_time                 |
| archive_time             | archive_time             |
| arr                      | arr                      |
| arr_currency             | arr_currency             |
| channel                  | channel                  |
| channel_id               | channel_id               |
| close_time               | close_time               |
| creator_user             |                          |
| creator_user_id          | creator_user_id          |
| currency                 | currency                 |
| done_activities_count    | done_activities_count    |
| email_messages_count     | email_messages_count     |
| expected_close_date      | expected_close_date      |
| first_won_time           | first_won_time           |
| formatted_value          | formatted_value          |
| formatted_weighted_value | formatted_weighted_value |
| group_id                 |                          |
| group_name               |                          |
| id                       | id                       |
| is_archived              | is_archived              |
| label                    | label                    |
| last_activity_date       | last_activity_date       |
| last_activity_id         | last_activity_id         |
| last_incoming_mail_time  | last_incoming_mail_time  |
| last_outgoing_mail_time  | last_outgoing_mail_time  |
| lost_reason              | lost_reason              |
| lost_time                | lost_time                |
| mrr                      | mrr                      |
| mrr_currency             | mrr_currency             |
| next_activity_date       | next_activity_date       |
| next_activity_duration   | next_activity_duration   |
| next_activity_id         | next_activity_id         |
| next_activity_note       | next_activity_note       |
| next_activity_subject    | next_activity_subject    |
| next_activity_time       | next_activity_time       |
| next_activity_type       | next_activity_type       |
| notes_count              | notes_count              |
| org                      |                          |
| org_id                   | org_id                   |
| org_name                 | org_name                 |
| origin                   | origin                   |
| origin_id                | origin_id                |
| owner_name               | owner_name               |
| participants_count       | participants_count       |
| person                   |                          |
| person_id                | person_id                |
| person_name              | person_name              |
| pipeline_id              | pipeline_id              |
| probability              | probability              |
| products_count           | products_count           |
| renewal_type             |                          |
| rotten_time              | rotten_time              |
| stage_change_time        | stage_change_time        |
| stage_id                 | stage_id                 |
| stage_order_nr           | stage_order_nr           |
| status                   | status                   |
| title                    | title                    |
| undone_activities_count  | undone_activities_count  |
| update_time              | update_time              |
| user                     |                          |
| user_id                  | user_id                  |
| value                    | value                    |
| visible_to               | visible_to               |
| weighted_value           | weighted_value           |
| weighted_value_currency  | weighted_value_currency  |
| won_time                 | won_time                 |
|                          | deleted                  |
|                          | local_won_date           |
|                          | next_activity            |
|                          | org_hidden               |
|                          | age                      |
|                          | followers_count          |
|                          | average_stage_progress   |
|                          | cc_email                 |
|                          | stay_in_pipeline_stages  |
|                          | average_time_to_won      |
|                          | last_activity            |
|                          | sequence_enrollment      |
|                          | person_hidden            |
|                          | local_close_date         |
|                          | local_lost_date          |
|                          | files_count              |

---

## ActiveCampaign

Fields in CRM Object Schema but not in Data Collection Schema: `{'nextTask', 'hash'}`

| Entity Schema Fields | Find By ID Object Fields |
|----------------------|--------------------------|
| account              | account                  |
| activitycount        | activitycount            |
| cdate                | cdate                    |
| contact              | contact                  |
| currency             | currency                 |
| customerAccount      | customerAccount          |
| description          | description              |
| edate                | edate                    |
| group                | group                    |
| id                   | id                       |
| isDisabled           | isDisabled               |
| links                | links                    |
| mdate                | mdate                    |
| nextdate             | nextdate                 |
| nextdealid           | nextdealid               |
| nexttaskid           | nexttaskid               |
| organization         | organization             |
| owner                | owner                    |
| percent              | percent                  |
| stage                | stage                    |
| status               | status                   |
| title                | title                    |
| value                | value                    |
| winProbability       | winProbability           |
| winProbabilityMdate  | winProbabilityMdate      |
|                      | nextTask                 |
|                      | hash                     |

---