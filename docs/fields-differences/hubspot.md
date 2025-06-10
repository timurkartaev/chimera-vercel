# Differences between fields in HubSpot

## Deals

| Entity Schema Fields                                             | Entity Schema Types | Find By ID Object Fields                                         | Find By ID Types |
|------------------------------------------------------------------|---------------------|------------------------------------------------------------------|------------------|
| amount                                                           | number              | amount                                                           | str              |
| amount_in_home_currency                                          | number              | amount_in_home_currency                                          | str              |
| billing_email                                                    | string              | billing_email                                                    | null             |
| calculated_property                                              | string              | calculated_property                                              | null             |
| closed_lost_reason                                               | string              | closed_lost_reason                                               | str              |
| closed_won_reason                                                | string              | closed_won_reason                                                | str              |
| closedate                                                        | string              | closedate                                                        | str              |
| company_ids[]                                                    | string              | company_ids[]                                                    | array            |
| contact_ids[]                                                    | string              | contact_ids[]                                                    | array            |
| country_of_residence                                             | string              | country_of_residence                                             | null             |
| createdate                                                       | string              | createdate                                                       | str              |
| custom__                                                         | number              | custom__                                                         | null             |
| custom_boolean                                                   | string              | custom_boolean                                                   | null             |
| custommonetaryfield                                              | number              | custommonetaryfield                                              | null             |
| data_test_2                                                      | string              | data_test_2                                                      | null             |
| days_to_close                                                    | number              | days_to_close                                                    | str              |
| deal_currency_code                                               | string              | deal_currency_code                                               | str              |
| dealname                                                         | string              | dealname                                                         | str              |
| dealstage                                                        | string              | dealstage                                                        | str              |
| dealtype                                                         | string              | dealtype                                                         | null             |
| delivery_date                                                    | string              | delivery_date                                                    | null             |
| delivery_method                                                  | string              | delivery_method                                                  | null             |
| description                                                      | string              | description                                                      | str              |
| dropdowntest_                                                    | string              | dropdowntest_                                                    | null             |
| dropdowntestnew                                                  | string              | dropdowntestnew                                                  | null             |
| engagements_last_meeting_booked                                  | string              | engagements_last_meeting_booked                                  | null             |
| engagements_last_meeting_booked_campaign                         | string              | engagements_last_meeting_booked_campaign                         | null             |
| engagements_last_meeting_booked_medium                           | string              | engagements_last_meeting_booked_medium                           | null             |
| engagements_last_meeting_booked_source                           | string              | engagements_last_meeting_booked_source                           | null             |
| export                                                           | string              | export                                                           | null             |
| hs_acv                                                           | number              | hs_acv                                                           | str              |
| hs_all_accessible_team_ids                                       | string              | hs_all_accessible_team_ids                                       | null             |
| hs_all_deal_split_owner_ids                                      | string              | hs_all_deal_split_owner_ids                                      | null             |
| hs_all_owner_ids                                                 | string              | hs_all_owner_ids                                                 | str              |
| hs_all_team_ids                                                  | string              | hs_all_team_ids                                                  | null             |
| hs_analytics_latest_source                                       | string              | hs_analytics_latest_source                                       | str              |
| hs_analytics_latest_source_company                               | string              | hs_analytics_latest_source_company                               | str              |
| hs_analytics_latest_source_contact                               | string              | hs_analytics_latest_source_contact                               | str              |
| hs_analytics_latest_source_data_1                                | string              | hs_analytics_latest_source_data_1                                | str              |
| hs_analytics_latest_source_data_1_company                        | string              | hs_analytics_latest_source_data_1_company                        | str              |
| hs_analytics_latest_source_data_1_contact                        | string              | hs_analytics_latest_source_data_1_contact                        | str              |
| hs_analytics_latest_source_data_2                                | string              | hs_analytics_latest_source_data_2                                | str              |
| hs_analytics_latest_source_data_2_company                        | string              | hs_analytics_latest_source_data_2_company                        | str              |
| hs_analytics_latest_source_data_2_contact                        | string              | hs_analytics_latest_source_data_2_contact                        | str              |
| hs_analytics_latest_source_timestamp                             | string              | hs_analytics_latest_source_timestamp                             | str              |
| hs_analytics_latest_source_timestamp_company                     | string              | hs_analytics_latest_source_timestamp_company                     | null             |
| hs_analytics_latest_source_timestamp_contact                     | string              | hs_analytics_latest_source_timestamp_contact                     | str              |
| hs_analytics_source                                              | string              | hs_analytics_source                                              | str              |
| hs_analytics_source_data_1                                       | string              | hs_analytics_source_data_1                                       | str              |
| hs_analytics_source_data_2                                       | string              | hs_analytics_source_data_2                                       | str              |
| hs_arr                                                           | number              | hs_arr                                                           | str              |
| hs_associated_deal_registration_deal_type                        | string              | hs_associated_deal_registration_deal_type                        | null             |
| hs_average_call_duration                                         | number              | hs_average_call_duration                                         | null             |
| hs_campaign                                                      | string              | hs_campaign                                                      | null             |
| hs_closed_amount                                                 | number              | hs_closed_amount                                                 | str              |
| hs_closed_amount_in_home_currency                                | number              | hs_closed_amount_in_home_currency                                | str              |
| hs_closed_deal_close_date                                        | number              | hs_closed_deal_close_date                                        | str              |
| hs_closed_deal_create_date                                       | number              | hs_closed_deal_create_date                                       | str              |
| hs_closed_won_count                                              | number              | hs_closed_won_count                                              | str              |
| hs_closed_won_date                                               | string              | hs_closed_won_date                                               | null             |
| hs_created_by_user_id                                            |                     | hs_created_by_user_id                                            | str              |
| hs_createdate                                                    | string              | hs_createdate                                                    | str              |
| hs_date_entered_159448327                                        | string              | hs_date_entered_159448327                                        | null             |
| hs_date_entered_159448328                                        | string              | hs_date_entered_159448328                                        | null             |
| hs_date_entered_159448329                                        | string              | hs_date_entered_159448329                                        | null             |
| hs_date_entered_159448330                                        | string              | hs_date_entered_159448330                                        | null             |
| hs_date_entered_159448331                                        | string              | hs_date_entered_159448331                                        | null             |
| hs_date_entered_159448332                                        | string              | hs_date_entered_159448332                                        | null             |
| hs_date_entered_159448333                                        | string              | hs_date_entered_159448333                                        | null             |
| hs_date_entered_159448334                                        | string              | hs_date_entered_159448334                                        | null             |
| hs_date_entered_241999791                                        | string              | hs_date_entered_241999791                                        | null             |
| hs_date_entered_241999792                                        | string              | hs_date_entered_241999792                                        | null             |
| hs_date_entered_241999793                                        | string              | hs_date_entered_241999793                                        | null             |
| hs_date_entered_241999794                                        | string              | hs_date_entered_241999794                                        | null             |
| hs_date_entered_241999795                                        | string              | hs_date_entered_241999795                                        | null             |
| hs_date_entered_241999796                                        | string              | hs_date_entered_241999796                                        | null             |
| hs_date_entered_241999797                                        | string              | hs_date_entered_241999797                                        | null             |
| hs_date_entered_243792759                                        | string              | hs_date_entered_243792759                                        | null             |
| hs_date_entered_244184403                                        | string              | hs_date_entered_244184403                                        | null             |
| hs_date_entered_252300703                                        | string              | hs_date_entered_252300703                                        | null             |
| hs_date_entered_266848368                                        | string              | hs_date_entered_266848368                                        | null             |
| hs_date_entered_appointmentscheduled                             | string              | hs_date_entered_appointmentscheduled                             | null             |
| hs_date_entered_closedlost                                       | string              | hs_date_entered_closedlost                                       | null             |
| hs_date_entered_closedwon                                        | string              | hs_date_entered_closedwon                                        | null             |
| hs_date_entered_contractsent                                     | string              | hs_date_entered_contractsent                                     | null             |
| hs_date_entered_decisionmakerboughtin                            | string              | hs_date_entered_decisionmakerboughtin                            | null             |
| hs_date_entered_presentationscheduled                            | string              | hs_date_entered_presentationscheduled                            | null             |
| hs_date_entered_qualifiedtobuy                                   | string              | hs_date_entered_qualifiedtobuy                                   | null             |
| hs_date_exited_159448327                                         | string              | hs_date_exited_159448327                                         | null             |
| hs_date_exited_159448328                                         | string              | hs_date_exited_159448328                                         | null             |
| hs_date_exited_159448329                                         | string              | hs_date_exited_159448329                                         | null             |
| hs_date_exited_159448330                                         | string              | hs_date_exited_159448330                                         | null             |
| hs_date_exited_159448331                                         | string              | hs_date_exited_159448331                                         | null             |
| hs_date_exited_159448332                                         | string              | hs_date_exited_159448332                                         | null             |
| hs_date_exited_159448333                                         | string              | hs_date_exited_159448333                                         | null             |
| hs_date_exited_159448334                                         | string              | hs_date_exited_159448334                                         | null             |
| hs_date_exited_241999791                                         | string              | hs_date_exited_241999791                                         | null             |
| hs_date_exited_241999792                                         | string              | hs_date_exited_241999792                                         | null             |
| hs_date_exited_241999793                                         | string              | hs_date_exited_241999793                                         | null             |
| hs_date_exited_241999794                                         | string              | hs_date_exited_241999794                                         | null             |
| hs_date_exited_241999795                                         | string              | hs_date_exited_241999795                                         | null             |
| hs_date_exited_241999796                                         | string              | hs_date_exited_241999796                                         | null             |
| hs_date_exited_241999797                                         | string              | hs_date_exited_241999797                                         | null             |
| hs_date_exited_243792759                                         | string              | hs_date_exited_243792759                                         | null             |
| hs_date_exited_244184403                                         | string              | hs_date_exited_244184403                                         | null             |
| hs_date_exited_252300703                                         | string              | hs_date_exited_252300703                                         | null             |
| hs_date_exited_266848368                                         | string              | hs_date_exited_266848368                                         | null             |
| hs_date_exited_appointmentscheduled                              | string              | hs_date_exited_appointmentscheduled                              | null             |
| hs_date_exited_closedlost                                        | string              | hs_date_exited_closedlost                                        | null             |
| hs_date_exited_closedwon                                         | string              | hs_date_exited_closedwon                                         | null             |
| hs_date_exited_contractsent                                      | string              | hs_date_exited_contractsent                                      | null             |
| hs_date_exited_decisionmakerboughtin                             | string              | hs_date_exited_decisionmakerboughtin                             | null             |
| hs_date_exited_presentationscheduled                             | string              | hs_date_exited_presentationscheduled                             | null             |
| hs_date_exited_qualifiedtobuy                                    | string              | hs_date_exited_qualifiedtobuy                                    | null             |
| hs_days_to_close_raw                                             | number              | hs_days_to_close_raw                                             | str              |
| hs_deal_amount_calculation_preference                            | string              | hs_deal_amount_calculation_preference                            | null             |
| hs_deal_registration_mrr                                         | number              | hs_deal_registration_mrr                                         | null             |
| hs_deal_registration_mrr_currency_code                           | string              | hs_deal_registration_mrr_currency_code                           | null             |
| hs_deal_score                                                    | number              | hs_deal_score                                                    | str              |
| hs_deal_stage_probability                                        | number              | hs_deal_stage_probability                                        | str              |
| hs_deal_stage_probability_shadow                                 | number              | hs_deal_stage_probability_shadow                                 | str              |
| hs_duration                                                      | number              | hs_duration                                                      | null             |
| hs_exchange_rate                                                 | number              | hs_exchange_rate                                                 | str              |
| hs_forecast_amount                                               | number              | hs_forecast_amount                                               | str              |
| hs_forecast_probability                                          | number              | hs_forecast_probability                                          | null             |
| hs_has_empty_conditional_stage_properties                        | boolean             | hs_has_empty_conditional_stage_properties                        | null             |
| hs_is_active_shared_deal                                         | boolean             | hs_is_active_shared_deal                                         | str              |
| hs_is_closed                                                     | boolean             | hs_is_closed                                                     | str              |
| hs_is_closed_count                                               | number              | hs_is_closed_count                                               | str              |
| hs_is_closed_lost                                                | boolean             | hs_is_closed_lost                                                | str              |
| hs_is_closed_won                                                 | boolean             | hs_is_closed_won                                                 | str              |
| hs_is_deal_split                                                 | boolean             | hs_is_deal_split                                                 | str              |
| hs_is_in_first_deal_stage                                        | boolean             | hs_is_in_first_deal_stage                                        | null             |
| hs_is_open_count                                                 | number              | hs_is_open_count                                                 | str              |
| hs_lastmodifieddate                                              | string              | hs_lastmodifieddate                                              | str              |
| hs_latest_approval_status                                        | string              | hs_latest_approval_status                                        | null             |
| hs_latest_approval_status_approval_id                            | number              | hs_latest_approval_status_approval_id                            | null             |
| hs_latest_meeting_activity                                       | string              | hs_latest_meeting_activity                                       | null             |
| hs_likelihood_to_close                                           | number              | hs_likelihood_to_close                                           | null             |
| hs_line_item_global_term_hs_discount_percentage                  | string              | hs_line_item_global_term_hs_discount_percentage                  | null             |
| hs_line_item_global_term_hs_discount_percentage_enabled          | boolean             | hs_line_item_global_term_hs_discount_percentage_enabled          | null             |
| hs_line_item_global_term_hs_recurring_billing_period             | string              | hs_line_item_global_term_hs_recurring_billing_period             | null             |
| hs_line_item_global_term_hs_recurring_billing_period_enabled     | boolean             | hs_line_item_global_term_hs_recurring_billing_period_enabled     | null             |
| hs_line_item_global_term_hs_recurring_billing_start_date         | string              | hs_line_item_global_term_hs_recurring_billing_start_date         | null             |
| hs_line_item_global_term_hs_recurring_billing_start_date_enabled | boolean             | hs_line_item_global_term_hs_recurring_billing_start_date_enabled | null             |
| hs_line_item_global_term_recurringbillingfrequency               | string              | hs_line_item_global_term_recurringbillingfrequency               | null             |
| hs_line_item_global_term_recurringbillingfrequency_enabled       | boolean             | hs_line_item_global_term_recurringbillingfrequency_enabled       | null             |
| hs_manual_campaign_ids                                           | number              | hs_manual_campaign_ids                                           | null             |
| hs_manual_forecast_category                                      | string              | hs_manual_forecast_category                                      | str              |
| hs_mrr                                                           | number              | hs_mrr                                                           | str              |
| hs_net_pipeline_impact                                           | number              | hs_net_pipeline_impact                                           | null             |
| hs_next_meeting_id                                               | number              | hs_next_meeting_id                                               | null             |
| hs_next_meeting_name                                             | string              | hs_next_meeting_name                                             | null             |
| hs_next_meeting_start_time                                       | string              | hs_next_meeting_start_time                                       | null             |
| hs_next_step                                                     | string              | hs_next_step                                                     | str              |
| hs_next_step_updated_at                                          | string              | hs_next_step_updated_at                                          | null             |
| hs_notes_next_activity_type                                      | string              | hs_notes_next_activity_type                                      | null             |
| hs_num_associated_active_deal_registrations                      | number              | hs_num_associated_active_deal_registrations                      | null             |
| hs_num_associated_deal_registrations                             | number              | hs_num_associated_deal_registrations                             | null             |
| hs_num_associated_deal_splits                                    | number              | hs_num_associated_deal_splits                                    | str              |
| hs_num_of_associated_line_items                                  | number              | hs_num_of_associated_line_items                                  | str              |
| hs_num_target_accounts                                           | number              | hs_num_target_accounts                                           | str              |
| hs_number_of_call_engagements                                    | number              | hs_number_of_call_engagements                                    | null             |
| hs_number_of_inbound_calls                                       | number              | hs_number_of_inbound_calls                                       | null             |
| hs_number_of_outbound_calls                                      | number              | hs_number_of_outbound_calls                                      | null             |
| hs_number_of_overdue_tasks                                       | number              | hs_number_of_overdue_tasks                                       | null             |
| hs_number_of_scheduled_meetings                                  | number              | hs_number_of_scheduled_meetings                                  | null             |
| hs_object_id                                                     |                     | hs_object_id                                                     | str              |
| hs_object_source                                                 | string              | hs_object_source                                                 | str              |
| hs_object_source_detail_1                                        | string              | hs_object_source_detail_1                                        | null             |
| hs_object_source_detail_2                                        | string              | hs_object_source_detail_2                                        | null             |
| hs_object_source_detail_3                                        | string              | hs_object_source_detail_3                                        | null             |
| hs_object_source_id                                              | string              | hs_object_source_id                                              | str              |
| hs_object_source_label                                           | string              | hs_object_source_label                                           | str              |
| hs_object_source_user_id                                         | number              | hs_object_source_user_id                                         | str              |
| hs_open_amount_in_home_currency                                  | number              | hs_open_amount_in_home_currency                                  | null             |
| hs_open_deal_create_date                                         | number              | hs_open_deal_create_date                                         | str              |
| hs_pinned_engagement_id                                          | number              | hs_pinned_engagement_id                                          | null             |
| hs_predicted_amount                                              | number              | hs_predicted_amount                                              | null             |
| hs_predicted_amount_in_home_currency                             | number              | hs_predicted_amount_in_home_currency                             | null             |
| hs_primary_associated_company                                    | number              | hs_primary_associated_company                                    | null             |
| hs_priority                                                      | string              | hs_priority                                                      | str              |
| hs_projected_amount                                              | number              | hs_projected_amount                                              | str              |
| hs_projected_amount_in_home_currency                             | number              | hs_projected_amount_in_home_currency                             | str              |
| hs_read_only                                                     | boolean             | hs_read_only                                                     | null             |
| hs_sales_email_last_replied                                      | string              | hs_sales_email_last_replied                                      | null             |
| hs_source_object_id                                              | number              | hs_source_object_id                                              | null             |
| hs_synced_deal_owner_name_and_email                              | string              | hs_synced_deal_owner_name_and_email                              | null             |
| hs_tcv                                                           | number              | hs_tcv                                                           | str              |
| hs_time_in_159448327                                             | number              | hs_time_in_159448327                                             | null             |
| hs_time_in_159448328                                             | number              | hs_time_in_159448328                                             | null             |
| hs_time_in_159448329                                             | number              | hs_time_in_159448329                                             | null             |
| hs_time_in_159448330                                             | number              | hs_time_in_159448330                                             | null             |
| hs_time_in_159448331                                             | number              | hs_time_in_159448331                                             | null             |
| hs_time_in_159448332                                             | number              | hs_time_in_159448332                                             | null             |
| hs_time_in_159448333                                             | number              | hs_time_in_159448333                                             | null             |
| hs_time_in_159448334                                             | number              | hs_time_in_159448334                                             | null             |
| hs_time_in_241999791                                             | number              | hs_time_in_241999791                                             | null             |
| hs_time_in_241999792                                             | number              | hs_time_in_241999792                                             | null             |
| hs_time_in_241999793                                             | number              | hs_time_in_241999793                                             | null             |
| hs_time_in_241999794                                             | number              | hs_time_in_241999794                                             | null             |
| hs_time_in_241999795                                             | number              | hs_time_in_241999795                                             | null             |
| hs_time_in_241999796                                             | number              | hs_time_in_241999796                                             | null             |
| hs_time_in_241999797                                             | number              | hs_time_in_241999797                                             | null             |
| hs_time_in_243792759                                             | number              | hs_time_in_243792759                                             | null             |
| hs_time_in_244184403                                             | number              | hs_time_in_244184403                                             | null             |
| hs_time_in_252300703                                             | number              | hs_time_in_252300703                                             | null             |
| hs_time_in_266848368                                             | number              | hs_time_in_266848368                                             | null             |
| hs_time_in_appointmentscheduled                                  | number              | hs_time_in_appointmentscheduled                                  | null             |
| hs_time_in_closedlost                                            | number              | hs_time_in_closedlost                                            | null             |
| hs_time_in_closedwon                                             | number              | hs_time_in_closedwon                                             | null             |
| hs_time_in_contractsent                                          | number              | hs_time_in_contractsent                                          | null             |
| hs_time_in_decisionmakerboughtin                                 | number              | hs_time_in_decisionmakerboughtin                                 | null             |
| hs_time_in_presentationscheduled                                 | number              | hs_time_in_presentationscheduled                                 | null             |
| hs_time_in_qualifiedtobuy                                        | number              | hs_time_in_qualifiedtobuy                                        | null             |
| hs_unique_creation_key                                           | string              | hs_unique_creation_key                                           | null             |
| hs_updated_by_user_id                                            |                     | hs_updated_by_user_id                                            | str              |
| hs_v2_cumulative_time_in_159448327                               | number              | hs_v2_cumulative_time_in_159448327                               | null             |
| hs_v2_cumulative_time_in_159448328                               | number              | hs_v2_cumulative_time_in_159448328                               | null             |
| hs_v2_cumulative_time_in_159448329                               | number              | hs_v2_cumulative_time_in_159448329                               | null             |
| hs_v2_cumulative_time_in_159448330                               | number              | hs_v2_cumulative_time_in_159448330                               | null             |
| hs_v2_cumulative_time_in_159448331                               | number              | hs_v2_cumulative_time_in_159448331                               | null             |
| hs_v2_cumulative_time_in_159448332                               | number              | hs_v2_cumulative_time_in_159448332                               | null             |
| hs_v2_cumulative_time_in_159448333                               | number              | hs_v2_cumulative_time_in_159448333                               | null             |
| hs_v2_cumulative_time_in_159448334                               | number              | hs_v2_cumulative_time_in_159448334                               | null             |
| hs_v2_cumulative_time_in_241999791                               | number              | hs_v2_cumulative_time_in_241999791                               | null             |
| hs_v2_cumulative_time_in_241999792                               | number              | hs_v2_cumulative_time_in_241999792                               | null             |
| hs_v2_cumulative_time_in_241999793                               | number              | hs_v2_cumulative_time_in_241999793                               | null             |
| hs_v2_cumulative_time_in_241999794                               | number              | hs_v2_cumulative_time_in_241999794                               | null             |
| hs_v2_cumulative_time_in_241999795                               | number              | hs_v2_cumulative_time_in_241999795                               | null             |
| hs_v2_cumulative_time_in_241999796                               | number              | hs_v2_cumulative_time_in_241999796                               | null             |
| hs_v2_cumulative_time_in_241999797                               | number              | hs_v2_cumulative_time_in_241999797                               | null             |
| hs_v2_cumulative_time_in_appointmentscheduled                    | number              | hs_v2_cumulative_time_in_appointmentscheduled                    | str              |
| hs_v2_cumulative_time_in_closedlost                              | number              | hs_v2_cumulative_time_in_closedlost                              | null             |
| hs_v2_cumulative_time_in_closedwon                               | number              | hs_v2_cumulative_time_in_closedwon                               | null             |
| hs_v2_cumulative_time_in_contractsent                            | number              | hs_v2_cumulative_time_in_contractsent                            | str              |
| hs_v2_cumulative_time_in_decisionmakerboughtin                   | number              | hs_v2_cumulative_time_in_decisionmakerboughtin                   | null             |
| hs_v2_cumulative_time_in_presentationscheduled                   | number              | hs_v2_cumulative_time_in_presentationscheduled                   | null             |
| hs_v2_cumulative_time_in_qualifiedtobuy                          | number              | hs_v2_cumulative_time_in_qualifiedtobuy                          | null             |
| hs_v2_date_entered_159448327                                     | string              | hs_v2_date_entered_159448327                                     | null             |
| hs_v2_date_entered_159448328                                     | string              | hs_v2_date_entered_159448328                                     | null             |
| hs_v2_date_entered_159448329                                     | string              | hs_v2_date_entered_159448329                                     | null             |
| hs_v2_date_entered_159448330                                     | string              | hs_v2_date_entered_159448330                                     | null             |
| hs_v2_date_entered_159448331                                     | string              | hs_v2_date_entered_159448331                                     | null             |
| hs_v2_date_entered_159448332                                     | string              | hs_v2_date_entered_159448332                                     | null             |
| hs_v2_date_entered_159448333                                     | string              | hs_v2_date_entered_159448333                                     | null             |
| hs_v2_date_entered_159448334                                     | string              | hs_v2_date_entered_159448334                                     | null             |
| hs_v2_date_entered_241999791                                     | string              | hs_v2_date_entered_241999791                                     | null             |
| hs_v2_date_entered_241999792                                     | string              | hs_v2_date_entered_241999792                                     | null             |
| hs_v2_date_entered_241999793                                     | string              | hs_v2_date_entered_241999793                                     | null             |
| hs_v2_date_entered_241999794                                     | string              | hs_v2_date_entered_241999794                                     | null             |
| hs_v2_date_entered_241999795                                     | string              | hs_v2_date_entered_241999795                                     | null             |
| hs_v2_date_entered_241999796                                     | string              | hs_v2_date_entered_241999796                                     | null             |
| hs_v2_date_entered_241999797                                     | string              | hs_v2_date_entered_241999797                                     | null             |
| hs_v2_date_entered_appointmentscheduled                          | string              | hs_v2_date_entered_appointmentscheduled                          | str              |
| hs_v2_date_entered_closedlost                                    | string              | hs_v2_date_entered_closedlost                                    | null             |
| hs_v2_date_entered_closedwon                                     | string              | hs_v2_date_entered_closedwon                                     | null             |
| hs_v2_date_entered_contractsent                                  | string              | hs_v2_date_entered_contractsent                                  | str              |
| hs_v2_date_entered_current_stage                                 | string              | hs_v2_date_entered_current_stage                                 | str              |
| hs_v2_date_entered_decisionmakerboughtin                         | string              | hs_v2_date_entered_decisionmakerboughtin                         | null             |
| hs_v2_date_entered_presentationscheduled                         | string              | hs_v2_date_entered_presentationscheduled                         | str              |
| hs_v2_date_entered_qualifiedtobuy                                | string              | hs_v2_date_entered_qualifiedtobuy                                | null             |
| hs_v2_date_exited_159448327                                      | string              | hs_v2_date_exited_159448327                                      | null             |
| hs_v2_date_exited_159448328                                      | string              | hs_v2_date_exited_159448328                                      | null             |
| hs_v2_date_exited_159448329                                      | string              | hs_v2_date_exited_159448329                                      | null             |
| hs_v2_date_exited_159448330                                      | string              | hs_v2_date_exited_159448330                                      | null             |
| hs_v2_date_exited_159448331                                      | string              | hs_v2_date_exited_159448331                                      | null             |
| hs_v2_date_exited_159448332                                      | string              | hs_v2_date_exited_159448332                                      | null             |
| hs_v2_date_exited_159448333                                      | string              | hs_v2_date_exited_159448333                                      | null             |
| hs_v2_date_exited_159448334                                      | string              | hs_v2_date_exited_159448334                                      | null             |
| hs_v2_date_exited_241999791                                      | string              | hs_v2_date_exited_241999791                                      | null             |
| hs_v2_date_exited_241999792                                      | string              | hs_v2_date_exited_241999792                                      | null             |
| hs_v2_date_exited_241999793                                      | string              | hs_v2_date_exited_241999793                                      | null             |
| hs_v2_date_exited_241999794                                      | string              | hs_v2_date_exited_241999794                                      | null             |
| hs_v2_date_exited_241999795                                      | string              | hs_v2_date_exited_241999795                                      | null             |
| hs_v2_date_exited_241999796                                      | string              | hs_v2_date_exited_241999796                                      | null             |
| hs_v2_date_exited_241999797                                      | string              | hs_v2_date_exited_241999797                                      | null             |
| hs_v2_date_exited_appointmentscheduled                           | string              | hs_v2_date_exited_appointmentscheduled                           | str              |
| hs_v2_date_exited_closedlost                                     | string              | hs_v2_date_exited_closedlost                                     | null             |
| hs_v2_date_exited_closedwon                                      | string              | hs_v2_date_exited_closedwon                                      | null             |
| hs_v2_date_exited_contractsent                                   | string              | hs_v2_date_exited_contractsent                                   | str              |
| hs_v2_date_exited_decisionmakerboughtin                          | string              | hs_v2_date_exited_decisionmakerboughtin                          | null             |
| hs_v2_date_exited_presentationscheduled                          | string              | hs_v2_date_exited_presentationscheduled                          | null             |
| hs_v2_date_exited_qualifiedtobuy                                 | string              | hs_v2_date_exited_qualifiedtobuy                                 | null             |
| hs_v2_latest_time_in_159448327                                   | number              | hs_v2_latest_time_in_159448327                                   | null             |
| hs_v2_latest_time_in_159448328                                   | number              | hs_v2_latest_time_in_159448328                                   | null             |
| hs_v2_latest_time_in_159448329                                   | number              | hs_v2_latest_time_in_159448329                                   | null             |
| hs_v2_latest_time_in_159448330                                   | number              | hs_v2_latest_time_in_159448330                                   | null             |
| hs_v2_latest_time_in_159448331                                   | number              | hs_v2_latest_time_in_159448331                                   | null             |
| hs_v2_latest_time_in_159448332                                   | number              | hs_v2_latest_time_in_159448332                                   | null             |
| hs_v2_latest_time_in_159448333                                   | number              | hs_v2_latest_time_in_159448333                                   | null             |
| hs_v2_latest_time_in_159448334                                   | number              | hs_v2_latest_time_in_159448334                                   | null             |
| hs_v2_latest_time_in_241999791                                   | number              | hs_v2_latest_time_in_241999791                                   | null             |
| hs_v2_latest_time_in_241999792                                   | number              | hs_v2_latest_time_in_241999792                                   | null             |
| hs_v2_latest_time_in_241999793                                   | number              | hs_v2_latest_time_in_241999793                                   | null             |
| hs_v2_latest_time_in_241999794                                   | number              | hs_v2_latest_time_in_241999794                                   | null             |
| hs_v2_latest_time_in_241999795                                   | number              | hs_v2_latest_time_in_241999795                                   | null             |
| hs_v2_latest_time_in_241999796                                   | number              | hs_v2_latest_time_in_241999796                                   | null             |
| hs_v2_latest_time_in_241999797                                   | number              | hs_v2_latest_time_in_241999797                                   | null             |
| hs_v2_latest_time_in_appointmentscheduled                        | number              | hs_v2_latest_time_in_appointmentscheduled                        | str              |
| hs_v2_latest_time_in_closedlost                                  | number              | hs_v2_latest_time_in_closedlost                                  | null             |
| hs_v2_latest_time_in_closedwon                                   | number              | hs_v2_latest_time_in_closedwon                                   | null             |
| hs_v2_latest_time_in_contractsent                                | number              | hs_v2_latest_time_in_contractsent                                | str              |
| hs_v2_latest_time_in_decisionmakerboughtin                       | number              | hs_v2_latest_time_in_decisionmakerboughtin                       | null             |
| hs_v2_latest_time_in_presentationscheduled                       | number              | hs_v2_latest_time_in_presentationscheduled                       | null             |
| hs_v2_latest_time_in_qualifiedtobuy                              | number              | hs_v2_latest_time_in_qualifiedtobuy                              | null             |
| hs_v2_time_in_current_stage                                      | string              | hs_v2_time_in_current_stage                                      | str              |
| hs_was_imported                                                  | boolean             | hs_was_imported                                                  | null             |
| hubspot_owner_assigneddate                                       | string              | hubspot_owner_assigneddate                                       | str              |
| hubspot_owner_id                                                 | string              | hubspot_owner_id                                                 | str              |
| hubspot_team_id                                                  | string              | hubspot_team_id                                                  | null             |
| lena_custom_prop                                                 | string              | lena_custom_prop                                                 | null             |
| lenas_new_prop                                                   | string              | lenas_new_prop                                                   | null             |
| n1                                                               | string              | n1                                                               | str              |
| nat_checkbox_test                                                | string              | nat_checkbox_test                                                | null             |
| nat_dropdown_test                                                | string              | nat_dropdown_test                                                | null             |
| nat_radiobutton_test                                             | string              | nat_radiobutton_test                                             | null             |
| nat_test___spec__                                                | number              | nat_test___spec__                                                | null             |
| nat_test_date                                                    | string              | nat_test_date                                                    | null             |
| nat_test_phone                                                   | string              | nat_test_phone                                                   | null             |
| nat_test_spec_symbol_                                            | string              | nat_test_spec_symbol_                                            | null             |
| nat_text_test                                                    | string              | nat_text_test                                                    | null             |
| notes_last_contacted                                             | string              | notes_last_contacted                                             | str              |
| notes_last_updated                                               | string              | notes_last_updated                                               | str              |
| notes_next_activity_date                                         | string              | notes_next_activity_date                                         | null             |
| num_associated_contacts                                          | number              | num_associated_contacts                                          | str              |
| num_contacted_notes                                              | number              | num_contacted_notes                                              | str              |
| num_notes                                                        | number              | num_notes                                                        | str              |
| number_of_repro_steps                                            | number              | number_of_repro_steps                                            | null             |
| number_of_rooms                                                  | number              | number_of_rooms                                                  | null             |
| panda_deal_datetime_check                                        | string              | panda_deal_datetime_check                                        | str              |
| pd_55716                                                         | string              | pd_55716                                                         | null             |
| pipeline                                                         | string              | pipeline                                                         | str              |
| present_wrap                                                     | string              | present_wrap                                                     | null             |
| sensitive_field_test                                             | string              | sensitive_field_test                                             | null             |
| single_checkbox                                                  | string              | single_checkbox                                                  | null             |
| super_new                                                        | string              | super_new                                                        | null             |
| tatata                                                           | string              | tatata                                                           | null             |
| test_contact                                                     | enumeration         | test_contact                                                     | null             |
| test_currency                                                    | number              | test_currency                                                    | null             |
| test_date                                                        | string              | test_date                                                        | null             |
| test_date_1                                                      | string              | test_date_1                                                      | null             |
| test_hubspot_property_integration                                | string              | test_hubspot_property_integration                                | null             |
| test_property                                                    | string              | test_property                                                    | null             |
| test_timur_property                                              | string              | test_timur_property                                              | null             |
| this_is_my_property                                              | string              | this_is_my_property                                              | null             |
| truefalse                                                        | string              | truefalse                                                        | null             |
| tytyty                                                           | string              | tytyty                                                           | null             |
| utilisation_rate                                                 | number              | utilisation_rate                                                 | null             |
| utilisation_rate_formateed                                       | string              | utilisation_rate_formateed                                       | null             |
| hs_all_assigned_business_unit_ids[]                              | string              |                                                                  |                  |
| hs_associated_deal_registration_product_interests[]              | string              |                                                                  |                  |
| hs_attributed_team_ids[]                                         | string              |                                                                  |                  |
| hs_merged_object_ids[]                                           | string              |                                                                  |                  |
| hs_owning_teams[]                                                | string              |                                                                  |                  |
| hs_shared_team_ids[]                                             | string              |                                                                  |                  |
| hs_shared_user_ids[]                                             | string              |                                                                  |                  |
| hs_tag_ids[]                                                     | string              |                                                                  |                  |
| hs_user_ids_of_all_notification_followers[]                      | string              |                                                                  |                  |
| hs_user_ids_of_all_notification_unfollowers[]                    | string              |                                                                  |                  |
| hs_user_ids_of_all_owners[]                                      | string              |                                                                  |                  |
| multi_select_field[]                                             | string              |                                                                  |                  |
|                                                                  |                     | hs_all_assigned_business_unit_ids                                | null             |
|                                                                  |                     | hs_all_collaborator_owner_ids                                    | null             |
|                                                                  |                     | hs_associated_deal_registration_product_interests                | null             |
|                                                                  |                     | hs_attributed_team_ids                                           | null             |
|                                                                  |                     | hs_merged_object_ids                                             | null             |
|                                                                  |                     | hs_notes_last_activity                                           | str              |
|                                                                  |                     | hs_notes_next_activity                                           | null             |
|                                                                  |                     | hs_owning_teams                                                  | null             |
|                                                                  |                     | hs_shared_team_ids                                               | null             |
|                                                                  |                     | hs_shared_user_ids                                               | null             |
|                                                                  |                     | hs_tag_ids                                                       | null             |
|                                                                  |                     | hs_user_ids_of_all_notification_followers                        | null             |
|                                                                  |                     | hs_user_ids_of_all_notification_unfollowers                      | null             |
|                                                                  |                     | hs_user_ids_of_all_owners                                        | str              |
|                                                                  |                     | line_item_ids[]                                                  | array            |

## Contacts

| Entity Schema Fields                                    | Entity Schema Types | Find By ID Object Fields                                | Find By ID Types |
|---------------------------------------------------------|---------------------|---------------------------------------------------------|------------------|
| address                                                 | string              | address                                                 | null             |
| annualrevenue                                           | string              | annualrevenue                                           | null             |
| associatedcompanyid                                     |                     | associatedcompanyid                                     | null             |
| associatedcompanylastupdated                            | number              | associatedcompanylastupdated                            | null             |
| city                                                    | string              | city                                                    | null             |
| closedate                                               | string              | closedate                                               | null             |
| company                                                 | string              | company                                                 | null             |
| company_size                                            | string              | company_size                                            | null             |
| country                                                 | string              | country                                                 | null             |
| createdate                                              | string              | createdate                                              | str              |
| currentlyinworkflow                                     | string              | currentlyinworkflow                                     | null             |
| custom_date_of_birth                                    | string              | custom_date_of_birth                                    | null             |
| date_of_birth                                           | string              | date_of_birth                                           | null             |
| days_to_close                                           | number              | days_to_close                                           | null             |
| degree                                                  | string              | degree                                                  | null             |
| email                                                   | string              | email                                                   | str              |
| engagements_last_meeting_booked                         | string              | engagements_last_meeting_booked                         | null             |
| engagements_last_meeting_booked_campaign                | string              | engagements_last_meeting_booked_campaign                | null             |
| engagements_last_meeting_booked_medium                  | string              | engagements_last_meeting_booked_medium                  | null             |
| engagements_last_meeting_booked_source                  | string              | engagements_last_meeting_booked_source                  | null             |
| fax                                                     | string              | fax                                                     | null             |
| field_of_study                                          | string              | field_of_study                                          | null             |
| first_conversion_date                                   | string              | first_conversion_date                                   | null             |
| first_conversion_event_name                             | string              | first_conversion_event_name                             | null             |
| first_deal_created_date                                 | string              | first_deal_created_date                                 | null             |
| firstname                                               | string              | firstname                                               | null             |
| followercount                                           | number              | followercount                                           | null             |
| gender                                                  | string              | gender                                                  | null             |
| graduation_date                                         | string              | graduation_date                                         | null             |
| hs_additional_emails                                    | string              | hs_additional_emails                                    | null             |
| hs_all_accessible_team_ids                              | string              | hs_all_accessible_team_ids                              | null             |
| hs_all_contact_vids                                     | string              | hs_all_contact_vids                                     | str              |
| hs_all_owner_ids                                        | string              | hs_all_owner_ids                                        | null             |
| hs_all_team_ids                                         | string              | hs_all_team_ids                                         | null             |
| hs_analytics_average_page_views                         | number              | hs_analytics_average_page_views                         | str              |
| hs_analytics_first_referrer                             | string              | hs_analytics_first_referrer                             | null             |
| hs_analytics_first_timestamp                            | string              | hs_analytics_first_timestamp                            | str              |
| hs_analytics_first_touch_converting_campaign            | string              | hs_analytics_first_touch_converting_campaign            | null             |
| hs_analytics_first_url                                  | string              | hs_analytics_first_url                                  | null             |
| hs_analytics_first_visit_timestamp                      | string              | hs_analytics_first_visit_timestamp                      | null             |
| hs_analytics_last_referrer                              | string              | hs_analytics_last_referrer                              | null             |
| hs_analytics_last_timestamp                             | string              | hs_analytics_last_timestamp                             | null             |
| hs_analytics_last_touch_converting_campaign             | string              | hs_analytics_last_touch_converting_campaign             | null             |
| hs_analytics_last_url                                   | string              | hs_analytics_last_url                                   | null             |
| hs_analytics_last_visit_timestamp                       | string              | hs_analytics_last_visit_timestamp                       | null             |
| hs_analytics_num_event_completions                      | number              | hs_analytics_num_event_completions                      | str              |
| hs_analytics_num_page_views                             | number              | hs_analytics_num_page_views                             | str              |
| hs_analytics_num_visits                                 | number              | hs_analytics_num_visits                                 | str              |
| hs_analytics_revenue                                    | number              | hs_analytics_revenue                                    | str              |
| hs_analytics_source                                     | string              | hs_analytics_source                                     | str              |
| hs_analytics_source_data_1                              | string              | hs_analytics_source_data_1                              | str              |
| hs_analytics_source_data_2                              | string              | hs_analytics_source_data_2                              | str              |
| hs_associated_target_accounts                           | number              | hs_associated_target_accounts                           | str              |
| hs_avatar_filemanager_key                               | string              | hs_avatar_filemanager_key                               | null             |
| hs_calculated_form_submissions                          | string              | hs_calculated_form_submissions                          | null             |
| hs_calculated_merged_vids                               | string              | hs_calculated_merged_vids                               | null             |
| hs_calculated_mobile_number                             | string              | hs_calculated_mobile_number                             | null             |
| hs_calculated_phone_number                              | string              | hs_calculated_phone_number                              | null             |
| hs_calculated_phone_number_area_code                    | string              | hs_calculated_phone_number_area_code                    | null             |
| hs_calculated_phone_number_country_code                 | string              | hs_calculated_phone_number_country_code                 | null             |
| hs_calculated_phone_number_region_code                  | string              | hs_calculated_phone_number_region_code                  | null             |
| hs_clicked_linkedin_ad                                  | string              | hs_clicked_linkedin_ad                                  | null             |
| hs_contact_enrichment_opt_out                           | boolean             | hs_contact_enrichment_opt_out                           | null             |
| hs_contact_enrichment_opt_out_timestamp                 | string              | hs_contact_enrichment_opt_out_timestamp                 | null             |
| hs_content_membership_email                             | string              | hs_content_membership_email                             | null             |
| hs_content_membership_email_confirmed                   | boolean             | hs_content_membership_email_confirmed                   | null             |
| hs_content_membership_follow_up_enqueued_at             | string              | hs_content_membership_follow_up_enqueued_at             | null             |
| hs_content_membership_notes                             | string              | hs_content_membership_notes                             | null             |
| hs_content_membership_registered_at                     | string              | hs_content_membership_registered_at                     | null             |
| hs_content_membership_registration_domain_sent_to       | string              | hs_content_membership_registration_domain_sent_to       | null             |
| hs_content_membership_registration_email_sent_at        | string              | hs_content_membership_registration_email_sent_at        | null             |
| hs_content_membership_status                            | string              | hs_content_membership_status                            | null             |
| hs_conversations_visitor_email                          | string              | hs_conversations_visitor_email                          | null             |
| hs_count_is_unworked                                    | number              | hs_count_is_unworked                                    | null             |
| hs_count_is_worked                                      | number              | hs_count_is_worked                                      | null             |
| hs_country_region_code                                  | string              | hs_country_region_code                                  | null             |
| hs_created_by_conversations                             | boolean             | hs_created_by_conversations                             | null             |
| hs_created_by_user_id                                   |                     | hs_created_by_user_id                                   | null             |
| hs_createdate                                           | string              | hs_createdate                                           | null             |
| hs_cross_sell_opportunity                               | boolean             | hs_cross_sell_opportunity                               | null             |
| hs_currently_enrolled_in_prospecting_agent              | boolean             | hs_currently_enrolled_in_prospecting_agent              | str              |
| hs_data_privacy_ads_consent                             | boolean             | hs_data_privacy_ads_consent                             | null             |
| hs_date_entered_customer                                | string              | hs_date_entered_customer                                | null             |
| hs_date_entered_evangelist                              | string              | hs_date_entered_evangelist                              | null             |
| hs_date_entered_lead                                    | string              | hs_date_entered_lead                                    | null             |
| hs_date_entered_marketingqualifiedlead                  | string              | hs_date_entered_marketingqualifiedlead                  | null             |
| hs_date_entered_opportunity                             | string              | hs_date_entered_opportunity                             | null             |
| hs_date_entered_other                                   | string              | hs_date_entered_other                                   | null             |
| hs_date_entered_salesqualifiedlead                      | string              | hs_date_entered_salesqualifiedlead                      | null             |
| hs_date_entered_subscriber                              | string              | hs_date_entered_subscriber                              | null             |
| hs_date_exited_customer                                 | string              | hs_date_exited_customer                                 | null             |
| hs_date_exited_evangelist                               | string              | hs_date_exited_evangelist                               | null             |
| hs_date_exited_lead                                     | string              | hs_date_exited_lead                                     | null             |
| hs_date_exited_marketingqualifiedlead                   | string              | hs_date_exited_marketingqualifiedlead                   | null             |
| hs_date_exited_opportunity                              | string              | hs_date_exited_opportunity                              | null             |
| hs_date_exited_other                                    | string              | hs_date_exited_other                                    | null             |
| hs_date_exited_salesqualifiedlead                       | string              | hs_date_exited_salesqualifiedlead                       | null             |
| hs_date_exited_subscriber                               | string              | hs_date_exited_subscriber                               | null             |
| hs_document_last_revisited                              | string              | hs_document_last_revisited                              | null             |
| hs_email_bad_address                                    | boolean             | hs_email_bad_address                                    | null             |
| hs_email_bounce                                         | number              | hs_email_bounce                                         | null             |
| hs_email_click                                          | number              | hs_email_click                                          | null             |
| hs_email_customer_quarantined_reason                    | string              | hs_email_customer_quarantined_reason                    | null             |
| hs_email_delivered                                      | number              | hs_email_delivered                                      | null             |
| hs_email_domain                                         | string              | hs_email_domain                                         | str              |
| hs_email_first_click_date                               | string              | hs_email_first_click_date                               | null             |
| hs_email_first_open_date                                | string              | hs_email_first_open_date                                | null             |
| hs_email_first_reply_date                               | string              | hs_email_first_reply_date                               | null             |
| hs_email_first_send_date                                | string              | hs_email_first_send_date                                | null             |
| hs_email_hard_bounce_reason                             | string              | hs_email_hard_bounce_reason                             | null             |
| hs_email_hard_bounce_reason_enum                        | string              | hs_email_hard_bounce_reason_enum                        | null             |
| hs_email_is_ineligible                                  | boolean             | hs_email_is_ineligible                                  | null             |
| hs_email_last_click_date                                | string              | hs_email_last_click_date                                | null             |
| hs_email_last_email_name                                | string              | hs_email_last_email_name                                | null             |
| hs_email_last_open_date                                 | string              | hs_email_last_open_date                                 | null             |
| hs_email_last_reply_date                                | string              | hs_email_last_reply_date                                | null             |
| hs_email_last_send_date                                 | string              | hs_email_last_send_date                                 | null             |
| hs_email_open                                           | number              | hs_email_open                                           | null             |
| hs_email_optimal_send_day_of_week                       | string              | hs_email_optimal_send_day_of_week                       | null             |
| hs_email_optimal_send_time_of_day                       | string              | hs_email_optimal_send_time_of_day                       | null             |
| hs_email_optout                                         | boolean             | hs_email_optout                                         | null             |
| hs_email_optout_19993558                                | string              | hs_email_optout_19993558                                | null             |
| hs_email_optout_23911077                                | string              | hs_email_optout_23911077                                | null             |
| hs_email_optout_332494355                               | string              | hs_email_optout_332494355                               | null             |
| hs_email_quarantined                                    | boolean             | hs_email_quarantined                                    | null             |
| hs_email_quarantined_reason                             | string              | hs_email_quarantined_reason                             | null             |
| hs_email_recipient_fatigue_recovery_time                | string              | hs_email_recipient_fatigue_recovery_time                | null             |
| hs_email_replied                                        | number              | hs_email_replied                                        | null             |
| hs_email_sends_since_last_engagement                    | number              | hs_email_sends_since_last_engagement                    | null             |
| hs_emailconfirmationstatus                              | string              | hs_emailconfirmationstatus                              | null             |
| hs_employment_change_detected_date                      | string              | hs_employment_change_detected_date                      | null             |
| hs_enriched_email_bounce_detected                       | boolean             | hs_enriched_email_bounce_detected                       | null             |
| hs_facebook_ad_clicked                                  | boolean             | hs_facebook_ad_clicked                                  | null             |
| hs_facebook_click_id                                    | string              | hs_facebook_click_id                                    | null             |
| hs_facebookid                                           | string              | hs_facebookid                                           | null             |
| hs_feedback_last_ces_survey_date                        | string              | hs_feedback_last_ces_survey_date                        | null             |
| hs_feedback_last_ces_survey_follow_up                   | string              | hs_feedback_last_ces_survey_follow_up                   | null             |
| hs_feedback_last_ces_survey_rating                      | number              | hs_feedback_last_ces_survey_rating                      | null             |
| hs_feedback_last_csat_survey_date                       | string              | hs_feedback_last_csat_survey_date                       | null             |
| hs_feedback_last_csat_survey_follow_up                  | string              | hs_feedback_last_csat_survey_follow_up                  | null             |
| hs_feedback_last_csat_survey_rating                     | number              | hs_feedback_last_csat_survey_rating                     | null             |
| hs_feedback_last_nps_follow_up                          | string              | hs_feedback_last_nps_follow_up                          | null             |
| hs_feedback_last_nps_rating                             | string              | hs_feedback_last_nps_rating                             | null             |
| hs_feedback_last_survey_date                            | string              | hs_feedback_last_survey_date                            | null             |
| hs_feedback_show_nps_web_survey                         | boolean             | hs_feedback_show_nps_web_survey                         | null             |
| hs_first_closed_order_id                                | number              | hs_first_closed_order_id                                | null             |
| hs_first_engagement_object_id                           | number              | hs_first_engagement_object_id                           | null             |
| hs_first_order_closed_date                              | string              | hs_first_order_closed_date                              | null             |
| hs_first_outreach_date                                  | string              | hs_first_outreach_date                                  | null             |
| hs_first_subscription_create_date                       | string              | hs_first_subscription_create_date                       | null             |
| hs_full_name_or_email                                   | string              | hs_full_name_or_email                                   | str              |
| hs_google_click_id                                      | string              | hs_google_click_id                                      | null             |
| hs_googleplusid                                         | string              | hs_googleplusid                                         | null             |
| hs_has_active_subscription                              | number              | hs_has_active_subscription                              | null             |
| hs_inferred_language_codes                              | string              | hs_inferred_language_codes                              | null             |
| hs_ip_timezone                                          | string              | hs_ip_timezone                                          | null             |
| hs_is_contact                                           | boolean             | hs_is_contact                                           | str              |
| hs_is_enriched                                          | boolean             | hs_is_enriched                                          | null             |
| hs_is_unworked                                          | boolean             | hs_is_unworked                                          | str              |
| hs_job_change_detected_date                             | string              | hs_job_change_detected_date                             | null             |
| hs_journey_stage                                        | string              | hs_journey_stage                                        | null             |
| hs_language                                             | string              | hs_language                                             | null             |
| hs_last_metered_enrichment_timestamp                    | string              | hs_last_metered_enrichment_timestamp                    | null             |
| hs_last_sales_activity_date                             | string              | hs_last_sales_activity_date                             | null             |
| hs_last_sales_activity_timestamp                        | string              | hs_last_sales_activity_timestamp                        | null             |
| hs_last_sales_activity_type                             | string              | hs_last_sales_activity_type                             | null             |
| hs_last_sms_send_date                                   | string              | hs_last_sms_send_date                                   | null             |
| hs_last_sms_send_name                                   | string              | hs_last_sms_send_name                                   | null             |
| hs_lastmodifieddate                                     | string              | hs_lastmodifieddate                                     | null             |
| hs_latest_disqualified_lead_date                        | string              | hs_latest_disqualified_lead_date                        | null             |
| hs_latest_meeting_activity                              | string              | hs_latest_meeting_activity                              | null             |
| hs_latest_open_lead_date                                | string              | hs_latest_open_lead_date                                | null             |
| hs_latest_qualified_lead_date                           | string              | hs_latest_qualified_lead_date                           | null             |
| hs_latest_sequence_ended_date                           | string              | hs_latest_sequence_ended_date                           | null             |
| hs_latest_sequence_enrolled                             | number              | hs_latest_sequence_enrolled                             | null             |
| hs_latest_sequence_enrolled_date                        | string              | hs_latest_sequence_enrolled_date                        | null             |
| hs_latest_sequence_finished_date                        | string              | hs_latest_sequence_finished_date                        | null             |
| hs_latest_sequence_unenrolled_date                      | string              | hs_latest_sequence_unenrolled_date                      | null             |
| hs_latest_source                                        | string              | hs_latest_source                                        | str              |
| hs_latest_source_data_1                                 | string              | hs_latest_source_data_1                                 | str              |
| hs_latest_source_data_2                                 | string              | hs_latest_source_data_2                                 | str              |
| hs_latest_source_timestamp                              | string              | hs_latest_source_timestamp                              | str              |
| hs_latest_subscription_create_date                      | string              | hs_latest_subscription_create_date                      | null             |
| hs_lead_status                                          | string              | hs_lead_status                                          | null             |
| hs_lifecyclestage_customer_date                         | string              | hs_lifecyclestage_customer_date                         | null             |
| hs_lifecyclestage_evangelist_date                       | string              | hs_lifecyclestage_evangelist_date                       | null             |
| hs_lifecyclestage_lead_date                             | string              | hs_lifecyclestage_lead_date                             | str              |
| hs_lifecyclestage_marketingqualifiedlead_date           | string              | hs_lifecyclestage_marketingqualifiedlead_date           | null             |
| hs_lifecyclestage_opportunity_date                      | string              | hs_lifecyclestage_opportunity_date                      | null             |
| hs_lifecyclestage_other_date                            | string              | hs_lifecyclestage_other_date                            | null             |
| hs_lifecyclestage_salesqualifiedlead_date               | string              | hs_lifecyclestage_salesqualifiedlead_date               | null             |
| hs_lifecyclestage_subscriber_date                       | string              | hs_lifecyclestage_subscriber_date                       | null             |
| hs_linkedin_ad_clicked                                  | string              | hs_linkedin_ad_clicked                                  | null             |
| hs_linkedin_url                                         | string              | hs_linkedin_url                                         | null             |
| hs_linkedinid                                           | string              | hs_linkedinid                                           | null             |
| hs_live_enrichment_deadline                             | string              | hs_live_enrichment_deadline                             | null             |
| hs_marketable_reason_id                                 | string              | hs_marketable_reason_id                                 | null             |
| hs_marketable_reason_type                               | string              | hs_marketable_reason_type                               | null             |
| hs_marketable_status                                    | string              | hs_marketable_status                                    | str              |
| hs_marketable_until_renewal                             | string              | hs_marketable_until_renewal                             | str              |
| hs_membership_has_accessed_private_content              | number              | hs_membership_has_accessed_private_content              | str              |
| hs_membership_last_private_content_access_date          | string              | hs_membership_last_private_content_access_date          | null             |
| hs_messaging_engagement_score                           | number              | hs_messaging_engagement_score                           | null             |
| hs_mobile_sdk_push_tokens                               | string              | hs_mobile_sdk_push_tokens                               | null             |
| hs_notes_last_activity                                  | object_coordinates  | hs_notes_last_activity                                  | str              |
| hs_notes_next_activity                                  | object_coordinates  | hs_notes_next_activity                                  | null             |
| hs_notes_next_activity_type                             | string              | hs_notes_next_activity_type                             | null             |
| hs_object_id                                            |                     | hs_object_id                                            | str              |
| hs_object_source                                        | string              | hs_object_source                                        | str              |
| hs_object_source_detail_1                               | string              | hs_object_source_detail_1                               | str              |
| hs_object_source_detail_2                               | string              | hs_object_source_detail_2                               | null             |
| hs_object_source_detail_3                               | string              | hs_object_source_detail_3                               | null             |
| hs_object_source_id                                     | string              | hs_object_source_id                                     | str              |
| hs_object_source_label                                  | string              | hs_object_source_label                                  | str              |
| hs_object_source_user_id                                | number              | hs_object_source_user_id                                | null             |
| hs_persona                                              | string              | hs_persona                                              | null             |
| hs_pinned_engagement_id                                 | number              | hs_pinned_engagement_id                                 | null             |
| hs_pipeline                                             | string              | hs_pipeline                                             | str              |
| hs_predictivecontactscore                               | number              | hs_predictivecontactscore                               | null             |
| hs_predictivecontactscore_v2                            | number              | hs_predictivecontactscore_v2                            | str              |
| hs_predictivecontactscorebucket                         | string              | hs_predictivecontactscorebucket                         | null             |
| hs_predictivescoringtier                                | string              | hs_predictivescoringtier                                | str              |
| hs_prospecting_agent_actively_enrolled_count            | number              | hs_prospecting_agent_actively_enrolled_count            | str              |
| hs_quarantined_emails                                   | string              | hs_quarantined_emails                                   | null             |
| hs_read_only                                            | boolean             | hs_read_only                                            | null             |
| hs_recent_closed_order_date                             | string              | hs_recent_closed_order_date                             | null             |
| hs_registered_member                                    | number              | hs_registered_member                                    | str              |
| hs_registration_method                                  | string              | hs_registration_method                                  | null             |
| hs_returning_to_office_detected_date                    | string              | hs_returning_to_office_detected_date                    | null             |
| hs_role                                                 | string              | hs_role                                                 | null             |
| hs_sa_first_engagement_date                             | string              | hs_sa_first_engagement_date                             | null             |
| hs_sa_first_engagement_descr                            | string              | hs_sa_first_engagement_descr                            | null             |
| hs_sa_first_engagement_object_type                      | string              | hs_sa_first_engagement_object_type                      | null             |
| hs_sales_email_last_clicked                             | string              | hs_sales_email_last_clicked                             | null             |
| hs_sales_email_last_opened                              | string              | hs_sales_email_last_opened                              | null             |
| hs_sales_email_last_replied                             | string              | hs_sales_email_last_replied                             | null             |
| hs_searchable_calculated_international_mobile_number    | phone_number        | hs_searchable_calculated_international_mobile_number    | null             |
| hs_searchable_calculated_international_phone_number     | phone_number        | hs_searchable_calculated_international_phone_number     | null             |
| hs_searchable_calculated_mobile_number                  | phone_number        | hs_searchable_calculated_mobile_number                  | null             |
| hs_searchable_calculated_phone_number                   | phone_number        | hs_searchable_calculated_phone_number                   | null             |
| hs_seniority                                            | string              | hs_seniority                                            | null             |
| hs_sequences_actively_enrolled_count                    | number              | hs_sequences_actively_enrolled_count                    | str              |
| hs_sequences_enrolled_count                             | number              | hs_sequences_enrolled_count                             | null             |
| hs_sequences_is_enrolled                                | boolean             | hs_sequences_is_enrolled                                | null             |
| hs_social_facebook_clicks                               | number              | hs_social_facebook_clicks                               | str              |
| hs_social_google_plus_clicks                            | number              | hs_social_google_plus_clicks                            | str              |
| hs_social_last_engagement                               | string              | hs_social_last_engagement                               | null             |
| hs_social_linkedin_clicks                               | number              | hs_social_linkedin_clicks                               | str              |
| hs_social_num_broadcast_clicks                          | number              | hs_social_num_broadcast_clicks                          | str              |
| hs_social_twitter_clicks                                | number              | hs_social_twitter_clicks                                | str              |
| hs_source_object_id                                     | number              | hs_source_object_id                                     | null             |
| hs_source_portal_id                                     | number              | hs_source_portal_id                                     | null             |
| hs_state_code                                           | string              | hs_state_code                                           | null             |
| hs_sub_role                                             | string              | hs_sub_role                                             | null             |
| hs_testpurge                                            | string              | hs_testpurge                                            | null             |
| hs_testrollback                                         | string              | hs_testrollback                                         | null             |
| hs_time_between_contact_creation_and_deal_close         | number              | hs_time_between_contact_creation_and_deal_close         | null             |
| hs_time_between_contact_creation_and_deal_creation      | number              | hs_time_between_contact_creation_and_deal_creation      | null             |
| hs_time_in_customer                                     | number              | hs_time_in_customer                                     | null             |
| hs_time_in_evangelist                                   | number              | hs_time_in_evangelist                                   | null             |
| hs_time_in_lead                                         | number              | hs_time_in_lead                                         | null             |
| hs_time_in_marketingqualifiedlead                       | number              | hs_time_in_marketingqualifiedlead                       | null             |
| hs_time_in_opportunity                                  | number              | hs_time_in_opportunity                                  | null             |
| hs_time_in_other                                        | number              | hs_time_in_other                                        | null             |
| hs_time_in_salesqualifiedlead                           | number              | hs_time_in_salesqualifiedlead                           | null             |
| hs_time_in_subscriber                                   | number              | hs_time_in_subscriber                                   | null             |
| hs_time_to_first_engagement                             | number              | hs_time_to_first_engagement                             | null             |
| hs_time_to_move_from_lead_to_customer                   | number              | hs_time_to_move_from_lead_to_customer                   | null             |
| hs_time_to_move_from_marketingqualifiedlead_to_customer | number              | hs_time_to_move_from_marketingqualifiedlead_to_customer | null             |
| hs_time_to_move_from_opportunity_to_customer            | number              | hs_time_to_move_from_opportunity_to_customer            | null             |
| hs_time_to_move_from_salesqualifiedlead_to_customer     | number              | hs_time_to_move_from_salesqualifiedlead_to_customer     | null             |
| hs_time_to_move_from_subscriber_to_customer             | number              | hs_time_to_move_from_subscriber_to_customer             | null             |
| hs_timezone                                             | string              | hs_timezone                                             | null             |
| hs_twitterid                                            | string              | hs_twitterid                                            | null             |
| hs_unique_creation_key                                  | string              | hs_unique_creation_key                                  | null             |
| hs_updated_by_user_id                                   |                     | hs_updated_by_user_id                                   | null             |
| hs_v2_cumulative_time_in_customer                       | number              | hs_v2_cumulative_time_in_customer                       | null             |
| hs_v2_cumulative_time_in_evangelist                     | number              | hs_v2_cumulative_time_in_evangelist                     | null             |
| hs_v2_cumulative_time_in_lead                           | number              | hs_v2_cumulative_time_in_lead                           | null             |
| hs_v2_cumulative_time_in_marketingqualifiedlead         | number              | hs_v2_cumulative_time_in_marketingqualifiedlead         | null             |
| hs_v2_cumulative_time_in_opportunity                    | number              | hs_v2_cumulative_time_in_opportunity                    | null             |
| hs_v2_cumulative_time_in_other                          | number              | hs_v2_cumulative_time_in_other                          | null             |
| hs_v2_cumulative_time_in_salesqualifiedlead             | number              | hs_v2_cumulative_time_in_salesqualifiedlead             | null             |
| hs_v2_cumulative_time_in_subscriber                     | number              | hs_v2_cumulative_time_in_subscriber                     | null             |
| hs_v2_date_entered_customer                             | string              | hs_v2_date_entered_customer                             | null             |
| hs_v2_date_entered_evangelist                           | string              | hs_v2_date_entered_evangelist                           | null             |
| hs_v2_date_entered_lead                                 | string              | hs_v2_date_entered_lead                                 | str              |
| hs_v2_date_entered_marketingqualifiedlead               | string              | hs_v2_date_entered_marketingqualifiedlead               | null             |
| hs_v2_date_entered_opportunity                          | string              | hs_v2_date_entered_opportunity                          | null             |
| hs_v2_date_entered_other                                | string              | hs_v2_date_entered_other                                | null             |
| hs_v2_date_entered_salesqualifiedlead                   | string              | hs_v2_date_entered_salesqualifiedlead                   | null             |
| hs_v2_date_entered_subscriber                           | string              | hs_v2_date_entered_subscriber                           | null             |
| hs_v2_date_exited_customer                              | string              | hs_v2_date_exited_customer                              | null             |
| hs_v2_date_exited_evangelist                            | string              | hs_v2_date_exited_evangelist                            | null             |
| hs_v2_date_exited_lead                                  | string              | hs_v2_date_exited_lead                                  | null             |
| hs_v2_date_exited_marketingqualifiedlead                | string              | hs_v2_date_exited_marketingqualifiedlead                | null             |
| hs_v2_date_exited_opportunity                           | string              | hs_v2_date_exited_opportunity                           | null             |
| hs_v2_date_exited_other                                 | string              | hs_v2_date_exited_other                                 | null             |
| hs_v2_date_exited_salesqualifiedlead                    | string              | hs_v2_date_exited_salesqualifiedlead                    | null             |
| hs_v2_date_exited_subscriber                            | string              | hs_v2_date_exited_subscriber                            | null             |
| hs_v2_latest_time_in_customer                           | number              | hs_v2_latest_time_in_customer                           | null             |
| hs_v2_latest_time_in_evangelist                         | number              | hs_v2_latest_time_in_evangelist                         | null             |
| hs_v2_latest_time_in_lead                               | number              | hs_v2_latest_time_in_lead                               | null             |
| hs_v2_latest_time_in_marketingqualifiedlead             | number              | hs_v2_latest_time_in_marketingqualifiedlead             | null             |
| hs_v2_latest_time_in_opportunity                        | number              | hs_v2_latest_time_in_opportunity                        | null             |
| hs_v2_latest_time_in_other                              | number              | hs_v2_latest_time_in_other                              | null             |
| hs_v2_latest_time_in_salesqualifiedlead                 | number              | hs_v2_latest_time_in_salesqualifiedlead                 | null             |
| hs_v2_latest_time_in_subscriber                         | number              | hs_v2_latest_time_in_subscriber                         | null             |
| hs_was_imported                                         | boolean             | hs_was_imported                                         | null             |
| hs_whatsapp_phone_number                                | string              | hs_whatsapp_phone_number                                | null             |
| hubspot_owner_assigneddate                              | string              | hubspot_owner_assigneddate                              | null             |
| hubspot_owner_id                                        | string              | hubspot_owner_id                                        | null             |
| hubspot_team_id                                         | string              | hubspot_team_id                                         | null             |
| hubspotscore                                            | number              | hubspotscore                                            | null             |
| industry                                                | string              | industry                                                | null             |
| ip_city                                                 | string              | ip_city                                                 | null             |
| ip_country                                              | string              | ip_country                                              | null             |
| ip_country_code                                         | string              | ip_country_code                                         | null             |
| ip_latlon                                               | string              | ip_latlon                                               | null             |
| ip_state                                                | string              | ip_state                                                | null             |
| ip_state_code                                           | string              | ip_state_code                                           | null             |
| ip_zipcode                                              | string              | ip_zipcode                                              | null             |
| job_function                                            | string              | job_function                                            | null             |
| jobtitle                                                | string              | jobtitle                                                | null             |
| kloutscoregeneral                                       | number              | kloutscoregeneral                                       | null             |
| lastmodifieddate                                        | string              | lastmodifieddate                                        | str              |
| lastname                                                | string              | lastname                                                | null             |
| lifecyclestage                                          | string              | lifecyclestage                                          | str              |
| linkedinbio                                             | string              | linkedinbio                                             | null             |
| linkedinconnections                                     | number              | linkedinconnections                                     | null             |
| marital_status                                          | string              | marital_status                                          | null             |
| message                                                 | string              | message                                                 | null             |
| military_status                                         | string              | military_status                                         | null             |
| mobilephone                                             | string              | mobilephone                                             | null             |
| notes_last_contacted                                    | string              | notes_last_contacted                                    | null             |
| notes_last_updated                                      | string              | notes_last_updated                                      | str              |
| notes_next_activity_date                                | string              | notes_next_activity_date                                | null             |
| num_associated_deals                                    | number              | num_associated_deals                                    | null             |
| num_contacted_notes                                     | number              | num_contacted_notes                                     | null             |
| num_conversion_events                                   | number              | num_conversion_events                                   | str              |
| num_notes                                               | number              | num_notes                                               | str              |
| num_unique_conversion_events                            | number              | num_unique_conversion_events                            | str              |
| number_of_custom_smth                                   | number              | number_of_custom_smth                                   | null             |
| numemployees                                            | string              | numemployees                                            | null             |
| owneremail                                              | string              | owneremail                                              | null             |
| ownername                                               | string              | ownername                                               | null             |
| phone                                                   | string              | phone                                                   | null             |
| phone_number                                            | string              | phone_number                                            | null             |
| photo                                                   | string              | photo                                                   | null             |
| recent_conversion_date                                  | string              | recent_conversion_date                                  | null             |
| recent_conversion_event_name                            | string              | recent_conversion_event_name                            | null             |
| recent_deal_amount                                      | number              | recent_deal_amount                                      | null             |
| recent_deal_close_date                                  | string              | recent_deal_close_date                                  | null             |
| relationship_status                                     | string              | relationship_status                                     | null             |
| salutation                                              | string              | salutation                                              | null             |
| school                                                  | string              | school                                                  | null             |
| seniority                                               | string              | seniority                                               | null             |
| start_date                                              | string              | start_date                                              | null             |
| state                                                   | string              | state                                                   | null             |
| surveymonkeyeventlastupdated                            | number              | surveymonkeyeventlastupdated                            | null             |
| total_revenue                                           | number              | total_revenue                                           | null             |
| twitterbio                                              | string              | twitterbio                                              | null             |
| twitterhandle                                           | string              | twitterhandle                                           | null             |
| twitterprofilephoto                                     | string              | twitterprofilephoto                                     | null             |
| webinareventlastupdated                                 | number              | webinareventlastupdated                                 | null             |
| website                                                 | string              | website                                                 | null             |
| work_email                                              | string              | work_email                                              | null             |
| zip                                                     | string              | zip                                                     | null             |
| company_ids[]                                           | string              |                                                         |                  |
| deal_ids[]                                              | string              |                                                         |                  |
| hs_all_assigned_business_unit_ids[]                     | string              |                                                         |                  |
| hs_buying_role[]                                        | string              |                                                         |                  |
| hs_legal_basis[]                                        | string              |                                                         |                  |
| hs_merged_object_ids[]                                  | string              |                                                         |                  |
| hs_owning_teams[]                                       | string              |                                                         |                  |
| hs_shared_team_ids[]                                    | string              |                                                         |                  |
| hs_shared_user_ids[]                                    | string              |                                                         |                  |
| hs_user_ids_of_all_notification_followers[]             | string              |                                                         |                  |
| hs_user_ids_of_all_notification_unfollowers[]           | string              |                                                         |                  |
| hs_user_ids_of_all_owners[]                             | string              |                                                         |                  |
|                                                         |                     | hs_all_assigned_business_unit_ids                       | null             |
|                                                         |                     | hs_buying_role                                          | null             |
|                                                         |                     | hs_legal_basis                                          | null             |
|                                                         |                     | hs_merged_object_ids                                    | null             |
|                                                         |                     | hs_owning_teams                                         | null             |
|                                                         |                     | hs_shared_team_ids                                      | null             |
|                                                         |                     | hs_shared_user_ids                                      | null             |
|                                                         |                     | hs_user_ids_of_all_notification_followers               | null             |
|                                                         |                     | hs_user_ids_of_all_notification_unfollowers             | null             |
|                                                         |                     | hs_user_ids_of_all_owners                               | null             |

## Companies

| Entity Schema Fields                                                        | Entity Schema Types | Find By ID Object Fields                                                    | Find By ID Types |
|-----------------------------------------------------------------------------|---------------------|-----------------------------------------------------------------------------|------------------|
| about_us                                                                    | string              | about_us                                                                    | null             |
| address                                                                     | string              | address                                                                     | null             |
| address2                                                                    | string              | address2                                                                    | null             |
| annualrevenue                                                               | number              | annualrevenue                                                               | null             |
| city                                                                        | string              | city                                                                        | str              |
| closedate                                                                   | string              | closedate                                                                   | null             |
| country                                                                     | string              | country                                                                     | null             |
| createdate                                                                  | string              | createdate                                                                  | str              |
| days_to_close                                                               | number              | days_to_close                                                               | null             |
| description                                                                 | string              | description                                                                 | null             |
| domain                                                                      | string              | domain                                                                      | str              |
| engagements_last_meeting_booked                                             | string              | engagements_last_meeting_booked                                             | null             |
| engagements_last_meeting_booked_campaign                                    | string              | engagements_last_meeting_booked_campaign                                    | null             |
| engagements_last_meeting_booked_medium                                      | string              | engagements_last_meeting_booked_medium                                      | null             |
| engagements_last_meeting_booked_source                                      | string              | engagements_last_meeting_booked_source                                      | null             |
| export                                                                      | string              | export                                                                      | null             |
| facebook_company_page                                                       | string              | facebook_company_page                                                       | null             |
| facebookfans                                                                | number              | facebookfans                                                                | null             |
| first_contact_createdate                                                    | string              | first_contact_createdate                                                    | null             |
| first_contact_createdate_timestamp_earliest_value_78b50eea                  | string              | first_contact_createdate_timestamp_earliest_value_78b50eea                  | null             |
| first_conversion_date                                                       | string              | first_conversion_date                                                       | null             |
| first_conversion_event_name                                                 | string              | first_conversion_event_name                                                 | null             |
| first_deal_created_date                                                     | string              | first_deal_created_date                                                     | str              |
| founded_year                                                                | string              | founded_year                                                                | null             |
| googleplus_page                                                             | string              | googleplus_page                                                             | null             |
| hs_all_accessible_team_ids                                                  | string              | hs_all_accessible_team_ids                                                  | null             |
| hs_all_owner_ids                                                            | string              | hs_all_owner_ids                                                            | str              |
| hs_all_team_ids                                                             | string              | hs_all_team_ids                                                             | null             |
| hs_analytics_first_timestamp                                                | string              | hs_analytics_first_timestamp                                                | null             |
| hs_analytics_first_touch_converting_campaign                                | string              | hs_analytics_first_touch_converting_campaign                                | null             |
| hs_analytics_first_visit_timestamp                                          | string              | hs_analytics_first_visit_timestamp                                          | null             |
| hs_analytics_last_timestamp                                                 | string              | hs_analytics_last_timestamp                                                 | null             |
| hs_analytics_last_timestamp_timestamp_latest_value_4e16365a                 | string              | hs_analytics_last_timestamp_timestamp_latest_value_4e16365a                 | null             |
| hs_analytics_last_touch_converting_campaign                                 | string              | hs_analytics_last_touch_converting_campaign                                 | null             |
| hs_analytics_last_touch_converting_campaign_timestamp_latest_value_81a64e30 | string              | hs_analytics_last_touch_converting_campaign_timestamp_latest_value_81a64e30 | null             |
| hs_analytics_last_visit_timestamp                                           | string              | hs_analytics_last_visit_timestamp                                           | null             |
| hs_analytics_last_visit_timestamp_timestamp_latest_value_999a0fce           | string              | hs_analytics_last_visit_timestamp_timestamp_latest_value_999a0fce           | null             |
| hs_analytics_latest_source                                                  | string              | hs_analytics_latest_source                                                  | null             |
| hs_analytics_latest_source_data_1                                           | string              | hs_analytics_latest_source_data_1                                           | null             |
| hs_analytics_latest_source_data_2                                           | string              | hs_analytics_latest_source_data_2                                           | null             |
| hs_analytics_latest_source_timestamp                                        | string              | hs_analytics_latest_source_timestamp                                        | null             |
| hs_analytics_num_page_views                                                 | number              | hs_analytics_num_page_views                                                 | null             |
| hs_analytics_num_page_views_cardinality_sum_e46e85b0                        | number              | hs_analytics_num_page_views_cardinality_sum_e46e85b0                        | null             |
| hs_analytics_num_visits                                                     | number              | hs_analytics_num_visits                                                     | null             |
| hs_analytics_num_visits_cardinality_sum_53d952a6                            | number              | hs_analytics_num_visits_cardinality_sum_53d952a6                            | null             |
| hs_analytics_source                                                         | string              | hs_analytics_source                                                         | null             |
| hs_analytics_source_data_1                                                  | string              | hs_analytics_source_data_1                                                  | null             |
| hs_analytics_source_data_2                                                  | string              | hs_analytics_source_data_2                                                  | null             |
| hs_annual_revenue_currency_code                                             | string              | hs_annual_revenue_currency_code                                             | str              |
| hs_avatar_filemanager_key                                                   | string              | hs_avatar_filemanager_key                                                   | str              |
| hs_country_code                                                             | string              | hs_country_code                                                             | null             |
| hs_created_by_user_id                                                       |                     | hs_created_by_user_id                                                       | str              |
| hs_createdate                                                               | string              | hs_createdate                                                               | null             |
| hs_csm_sentiment                                                            | string              | hs_csm_sentiment                                                            | null             |
| hs_customer_success_ticket_sentiment                                        | number              | hs_customer_success_ticket_sentiment                                        | null             |
| hs_date_entered_customer                                                    | string              | hs_date_entered_customer                                                    | null             |
| hs_date_entered_evangelist                                                  | string              | hs_date_entered_evangelist                                                  | null             |
| hs_date_entered_lead                                                        | string              | hs_date_entered_lead                                                        | str              |
| hs_date_entered_marketingqualifiedlead                                      | string              | hs_date_entered_marketingqualifiedlead                                      | null             |
| hs_date_entered_opportunity                                                 | string              | hs_date_entered_opportunity                                                 | str              |
| hs_date_entered_other                                                       | string              | hs_date_entered_other                                                       | null             |
| hs_date_entered_salesqualifiedlead                                          | string              | hs_date_entered_salesqualifiedlead                                          | null             |
| hs_date_entered_subscriber                                                  | string              | hs_date_entered_subscriber                                                  | null             |
| hs_date_exited_customer                                                     | string              | hs_date_exited_customer                                                     | null             |
| hs_date_exited_evangelist                                                   | string              | hs_date_exited_evangelist                                                   | null             |
| hs_date_exited_lead                                                         | string              | hs_date_exited_lead                                                         | str              |
| hs_date_exited_marketingqualifiedlead                                       | string              | hs_date_exited_marketingqualifiedlead                                       | null             |
| hs_date_exited_opportunity                                                  | string              | hs_date_exited_opportunity                                                  | null             |
| hs_date_exited_other                                                        | string              | hs_date_exited_other                                                        | null             |
| hs_date_exited_salesqualifiedlead                                           | string              | hs_date_exited_salesqualifiedlead                                           | null             |
| hs_date_exited_subscriber                                                   | string              | hs_date_exited_subscriber                                                   | null             |
| hs_employee_range                                                           | string              | hs_employee_range                                                           | null             |
| hs_gps_coordinates                                                          | string              | hs_gps_coordinates                                                          | null             |
| hs_gps_error                                                                | string              | hs_gps_error                                                                | null             |
| hs_ideal_customer_profile                                                   | string              | hs_ideal_customer_profile                                                   | null             |
| hs_industry_group                                                           | string              | hs_industry_group                                                           | null             |
| hs_intent_page_views_last_30_days                                           | number              | hs_intent_page_views_last_30_days                                           | null             |
| hs_intent_visitors_last_30_days                                             | number              | hs_intent_visitors_last_30_days                                             | null             |
| hs_is_enriched                                                              | boolean             | hs_is_enriched                                                              | null             |
| hs_is_intent_monitored                                                      | boolean             | hs_is_intent_monitored                                                      | null             |
| hs_is_target_account                                                        | boolean             | hs_is_target_account                                                        | null             |
| hs_last_booked_meeting_date                                                 | string              | hs_last_booked_meeting_date                                                 | null             |
| hs_last_logged_call_date                                                    | string              | hs_last_logged_call_date                                                    | null             |
| hs_last_logged_outgoing_email_date                                          | string              | hs_last_logged_outgoing_email_date                                          | null             |
| hs_last_metered_enrichment_timestamp                                        | string              | hs_last_metered_enrichment_timestamp                                        | null             |
| hs_last_open_task_date                                                      | string              | hs_last_open_task_date                                                      | null             |
| hs_last_sales_activity_date                                                 | string              | hs_last_sales_activity_date                                                 | null             |
| hs_last_sales_activity_timestamp                                            | string              | hs_last_sales_activity_timestamp                                            | null             |
| hs_last_sales_activity_type                                                 | string              | hs_last_sales_activity_type                                                 | null             |
| hs_lastmodifieddate                                                         | string              | hs_lastmodifieddate                                                         | str              |
| hs_latest_createdate_of_active_subscriptions                                | string              | hs_latest_createdate_of_active_subscriptions                                | null             |
| hs_latest_meeting_activity                                                  | string              | hs_latest_meeting_activity                                                  | null             |
| hs_lead_status                                                              | string              | hs_lead_status                                                              | null             |
| hs_linkedin_handle                                                          | string              | hs_linkedin_handle                                                          | null             |
| hs_live_enrichment_deadline                                                 | string              | hs_live_enrichment_deadline                                                 | null             |
| hs_logo_url                                                                 | string              | hs_logo_url                                                                 | null             |
| hs_most_recent_de_anonymized_visit                                          | string              | hs_most_recent_de_anonymized_visit                                          | null             |
| hs_notes_last_activity                                                      | object_coordinates  | hs_notes_last_activity                                                      | str              |
| hs_notes_next_activity                                                      | object_coordinates  | hs_notes_next_activity                                                      | null             |
| hs_notes_next_activity_type                                                 | string              | hs_notes_next_activity_type                                                 | null             |
| hs_num_blockers                                                             | number              | hs_num_blockers                                                             | str              |
| hs_num_child_companies                                                      | number              | hs_num_child_companies                                                      | str              |
| hs_num_contacts_with_buying_roles                                           | number              | hs_num_contacts_with_buying_roles                                           | str              |
| hs_num_decision_makers                                                      | number              | hs_num_decision_makers                                                      | str              |
| hs_num_open_deals                                                           | number              | hs_num_open_deals                                                           | str              |
| hs_object_id                                                                |                     | hs_object_id                                                                | str              |
| hs_object_source                                                            | string              | hs_object_source                                                            | str              |
| hs_object_source_detail_1                                                   | string              | hs_object_source_detail_1                                                   | null             |
| hs_object_source_detail_2                                                   | string              | hs_object_source_detail_2                                                   | null             |
| hs_object_source_detail_3                                                   | string              | hs_object_source_detail_3                                                   | null             |
| hs_object_source_id                                                         | string              | hs_object_source_id                                                         | str              |
| hs_object_source_label                                                      | string              | hs_object_source_label                                                      | str              |
| hs_object_source_user_id                                                    | number              | hs_object_source_user_id                                                    | str              |
| hs_parent_company_id                                                        | number              | hs_parent_company_id                                                        | null             |
| hs_pinned_engagement_id                                                     | number              | hs_pinned_engagement_id                                                     | null             |
| hs_pipeline                                                                 | string              | hs_pipeline                                                                 | str              |
| hs_predictivecontactscore_v2                                                | number              | hs_predictivecontactscore_v2                                                | null             |
| hs_predictivecontactscore_v2_next_max_max_d4e58c1e                          | number              | hs_predictivecontactscore_v2_next_max_max_d4e58c1e                          | null             |
| hs_quick_context                                                            | string              | hs_quick_context                                                            | null             |
| hs_read_only                                                                | boolean             | hs_read_only                                                                | null             |
| hs_revenue_range                                                            | string              | hs_revenue_range                                                            | null             |
| hs_sales_email_last_replied                                                 | string              | hs_sales_email_last_replied                                                 | null             |
| hs_source_object_id                                                         | number              | hs_source_object_id                                                         | null             |
| hs_state_code                                                               | string              | hs_state_code                                                               | null             |
| hs_target_account                                                           | string              | hs_target_account                                                           | null             |
| hs_target_account_probability                                               | number              | hs_target_account_probability                                               | str              |
| hs_target_account_recommendation_snooze_time                                | string              | hs_target_account_recommendation_snooze_time                                | null             |
| hs_target_account_recommendation_state                                      | string              | hs_target_account_recommendation_state                                      | null             |
| hs_task_label                                                               | string              | hs_task_label                                                               | str              |
| hs_time_in_customer                                                         | number              | hs_time_in_customer                                                         | null             |
| hs_time_in_evangelist                                                       | number              | hs_time_in_evangelist                                                       | null             |
| hs_time_in_lead                                                             | number              | hs_time_in_lead                                                             | str              |
| hs_time_in_marketingqualifiedlead                                           | number              | hs_time_in_marketingqualifiedlead                                           | null             |
| hs_time_in_opportunity                                                      | number              | hs_time_in_opportunity                                                      | str              |
| hs_time_in_other                                                            | number              | hs_time_in_other                                                            | null             |
| hs_time_in_salesqualifiedlead                                               | number              | hs_time_in_salesqualifiedlead                                               | null             |
| hs_time_in_subscriber                                                       | number              | hs_time_in_subscriber                                                       | null             |
| hs_total_deal_value                                                         | number              | hs_total_deal_value                                                         | str              |
| hs_unique_creation_key                                                      | string              | hs_unique_creation_key                                                      | null             |
| hs_updated_by_user_id                                                       |                     | hs_updated_by_user_id                                                       | str              |
| hs_was_imported                                                             | boolean             | hs_was_imported                                                             | null             |
| hubspot_owner_assigneddate                                                  | string              | hubspot_owner_assigneddate                                                  | str              |
| hubspot_owner_id                                                            | string              | hubspot_owner_id                                                            | str              |
| hubspot_team_id                                                             | string              | hubspot_team_id                                                             | null             |
| hubspotscore                                                                | number              | hubspotscore                                                                | null             |
| industry                                                                    | string              | industry                                                                    | str              |
| is_public                                                                   | boolean             | is_public                                                                   | null             |
| lifecyclestage                                                              | string              | lifecyclestage                                                              | str              |
| linkedin_company_page                                                       | string              | linkedin_company_page                                                       | null             |
| linkedinbio                                                                 | string              | linkedinbio                                                                 | null             |
| name                                                                        | string              | name                                                                        | str              |
| natphone                                                                    | string              | natphone                                                                    | null             |
| notes_last_contacted                                                        | string              | notes_last_contacted                                                        | null             |
| notes_last_updated                                                          | string              | notes_last_updated                                                          | str              |
| notes_next_activity_date                                                    | string              | notes_next_activity_date                                                    | null             |
| num_associated_contacts                                                     | number              | num_associated_contacts                                                     | str              |
| num_associated_deals                                                        | number              | num_associated_deals                                                        | str              |
| num_contacted_notes                                                         | number              | num_contacted_notes                                                         | null             |
| num_conversion_events                                                       | number              | num_conversion_events                                                       | null             |
| num_conversion_events_cardinality_sum_d095f14b                              | number              | num_conversion_events_cardinality_sum_d095f14b                              | null             |
| num_notes                                                                   | number              | num_notes                                                                   | str              |
| numberofemployees                                                           | number              | numberofemployees                                                           | null             |
| owneremail                                                                  | string              | owneremail                                                                  | null             |
| ownername                                                                   | string              | ownername                                                                   | null             |
| phone                                                                       | string              | phone                                                                       | null             |
| recent_conversion_date                                                      | string              | recent_conversion_date                                                      | null             |
| recent_conversion_date_timestamp_latest_value_72856da1                      | string              | recent_conversion_date_timestamp_latest_value_72856da1                      | null             |
| recent_conversion_event_name                                                | string              | recent_conversion_event_name                                                | null             |
| recent_conversion_event_name_timestamp_latest_value_66c820bf                | string              | recent_conversion_event_name_timestamp_latest_value_66c820bf                | null             |
| recent_deal_amount                                                          | number              | recent_deal_amount                                                          | null             |
| recent_deal_close_date                                                      | string              | recent_deal_close_date                                                      | null             |
| state                                                                       | string              | state                                                                       | str              |
| timezone                                                                    | string              | timezone                                                                    | null             |
| total_money_raised                                                          | string              | total_money_raised                                                          | null             |
| total_revenue                                                               | number              | total_revenue                                                               | null             |
| twitterbio                                                                  | string              | twitterbio                                                                  | null             |
| twitterfollowers                                                            | number              | twitterfollowers                                                            | null             |
| twitterhandle                                                               | string              | twitterhandle                                                               | null             |
| type                                                                        | string              | type                                                                        | str              |
| website                                                                     | string              | website                                                                     | str              |
| zip                                                                         | string              | zip                                                                         | str              |
| closedate_timestamp_earliest_value_a2a17e6e                                 | string              |                                                                             |                  |
| hs_additional_domains[]                                                     | string              |                                                                             |                  |
| hs_all_assigned_business_unit_ids[]                                         | string              |                                                                             |                  |
| hs_keywords[]                                                               | string              |                                                                             |                  |
| hs_merged_object_ids[]                                                      | string              |                                                                             |                  |
| hs_owning_teams[]                                                           | string              |                                                                             |                  |
| hs_shared_team_ids[]                                                        | string              |                                                                             |                  |
| hs_shared_user_ids[]                                                        | string              |                                                                             |                  |
| hs_user_ids_of_all_notification_followers[]                                 | string              |                                                                             |                  |
| hs_user_ids_of_all_notification_unfollowers[]                               | string              |                                                                             |                  |
| hs_user_ids_of_all_owners[]                                                 | string              |                                                                             |                  |
| id                                                                          | string              |                                                                             |                  |
| web_technologies[]                                                          | string              |                                                                             |                  |
|                                                                             |                     | hs_additional_domains                                                       | null             |
|                                                                             |                     | hs_all_assigned_business_unit_ids                                           | str              |
|                                                                             |                     | hs_keywords                                                                 | null             |
|                                                                             |                     | hs_merged_object_ids                                                        | null             |
|                                                                             |                     | hs_owning_teams                                                             | null             |
|                                                                             |                     | hs_shared_team_ids                                                          | null             |
|                                                                             |                     | hs_shared_user_ids                                                          | null             |
|                                                                             |                     | hs_user_ids_of_all_notification_followers                                   | null             |
|                                                                             |                     | hs_user_ids_of_all_notification_unfollowers                                 | null             |
|                                                                             |                     | hs_user_ids_of_all_owners                                                   | str              |
|                                                                             |                     | web_technologies                                                            | null             |