# import unittest
# import os
# import sys
# from unittest.mock import MagicMock, patch

# # Add the parent directory to the Python path to import the module
# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# from src.connectors.integration_connector.connector import IntegrationConnector

# class TestIntegrationConnector(unittest.TestCase):
#     """Integration test suite for the IntegrationConnector class."""
    
#     def setUp(self):
#         """Set up test fixtures before each test method is run."""
#         # Create patches for external dependencies
#         self.api_client_patcher = patch('src.connectors.integration_connector.api.client.ApiClient')
#         self.load_yaml_patcher = patch('yaml.safe_load')
        
#         # Start the patches
#         self.mock_api_client = self.api_client_patcher.start()
#         self.mock_load_yaml = self.load_yaml_patcher.start()
        
#         # Configure mock config
#         self.mock_config = {
#             'info': {
#                 'name': 'Test Integration',
#                 'description': 'Test Description',
#                 'version': '1.0.0'
#             },
#             'authentication': {
#                 'auth_method': 'credentials',
#                 'auth_params': [
#                     {
#                         'id': 'api_key',
#                         'required': True
#                     }
#                 ]
#             },
#             'entities': [
#                 {
#                     'type': 'deal',
#                     'schema': {
#                         'type': 'object',
#                         'properties': {
#                             'name': {'type': 'string'},
#                             'amount': {'type': 'number'}
#                         }
#                     }
#                 },
#                 {
#                     'type': 'company',
#                     'schema': {
#                         'type': 'object',
#                         'properties': {
#                             'name': {'type': 'string'},
#                             'industry': {'type': 'string'}
#                         }
#                     }
#                 }
#             ],
#             'actions': [
#                 {
#                     'action_id': 'update',
#                     'entities': ['deal', 'company']
#                 },
#                 {
#                     'action_id': 'attach_document',
#                     'entities': ['deal']
#                 },
#                 {
#                     'action_id': 'add_history',
#                     'entities': ['deal']
#                 }
#             ]
#         }
#         self.mock_load_yaml.return_value = self.mock_config
        
#         # Configure mock responses
#         self.mock_api_client.return_value.post = MagicMock(return_value={'success': True, 'token': 'test_token', 'user_id': 'test_user', 'company_id': 'test_company'})
#         self.mock_api_client.return_value.get_deal = MagicMock(return_value={
#             'id': 'deal123',
#             'name': 'Test Deal',
#             'amount': 5000
#         })
#         self.mock_api_client.return_value.get_deals = MagicMock(return_value=[
#             {'id': 'deal123', 'name': 'Test Deal'},
#             {'id': 'deal456', 'name': 'Another Deal'}
#         ])
#         self.mock_api_client.return_value.get_company = MagicMock(return_value={
#             'id': 'company123',
#             'name': 'Test Company',
#             'industry': 'Technology'
#         })
#         self.mock_api_client.return_value.get_companies = MagicMock(return_value=[
#             {'id': 'company123', 'name': 'Test Company'},
#             {'id': 'company456', 'name': 'Another Company'}
#         ])
#         self.mock_api_client.return_value.update_deal = MagicMock(return_value={'success': True})
#         self.mock_api_client.return_value.attach_document = MagicMock(return_value={'success': True})
#         self.mock_api_client.return_value.add_deal_activity = MagicMock(return_value={'success': True})
        
#         # Create an instance of the connector using the factory method
#         self.connector = IntegrationConnector.create('pipedrive')
    
#     def tearDown(self):
#         """Tear down test fixtures after each test method is run."""
#         self.api_client_patcher.stop()
#         self.load_yaml_patcher.stop()
    
#     def test_integration_flow(self):
#         """Test the complete integration flow."""
#         # Step 1: Test authentication
#         auth_result = self.connector.authorize.authorize({'api_key': 'test_key'})
#         self.assertEqual(auth_result.get('status'), 'connected')
        
#         # Step 2: Get and validate entities
#         entities = self.connector.entity.get_entities()
#         self.assertIsInstance(entities, list)
#         self.assertTrue(len(entities) > 0)
        
#         # Step 3: Test each entity
#         for entity in entities:
#             entity_type = entity['type']
            
#             # Get and validate entity schema
#             schema = self.connector.entity.get_entity_schema({'entity_type': entity_type})
#             self.assertIsInstance(schema, dict)
#             self.assertIn('properties', schema)
            
#             # Get and validate objects
#             objects = self.connector.object.get_objects({'entity_type': entity_type})
#             self.assertIsInstance(objects, list)
            
#             if objects:  # If we have any objects
#                 # Get and validate specific object
#                 object_id = objects[0]['id']
#                 object_data = self.connector.object.get_object({
#                     'entity_type': entity_type,
#                     'object_id': object_id
#                 })
#                 self.assertIsInstance(object_data, dict)
#                 self.assertIn('id', object_data)
        
#         # Step 4: Get all actions
#         actions = self.connector.action.get_actions()
#         self.assertIsInstance(actions, list)
#         self.assertTrue(len(actions) > 0)
        
#         # Step 5: Test each action with compatible entities
#         for action in actions:
#             action_id = action['action_id']
#             compatible_entities = action['entities']
            
#             for entity_type in compatible_entities:
#                 # Get objects for this entity type
#                 objects = self.connector.object.get_objects({'entity_type': entity_type})
                
#                 if objects:  # If we have any objects
#                     object_id = objects[0]['id']
                    
#                     # Execute action
#                     if action_id == 'update':
#                         params = {'name': 'Updated Name'}
#                     elif action_id == 'attach_document':
#                         params = {
#                             'document_id': 'doc123',
#                             'document_name': 'Test Doc',
#                             'document_url': 'https://example.com/doc'
#                         }
#                     elif action_id == 'add_history':
#                         params = {
#                             'activity_type': 'note',
#                             'message': 'Test activity'
#                         }
#                     else:
#                         params = {}
                    
#                     result = self.connector.action.execute_action({
#                         'action_id': action_id,
#                         'entity_type': entity_type,
#                         'object_id': object_id,
#                         **params
#                     })
#                     self.assertIsInstance(result, dict)
#                     self.assertTrue(result.get('success'))
        
#         # Step 6: Test localization
#         localization = self.connector.localization.get_localization('en')
#         self.assertIsInstance(localization, dict)
#         self.assertIn('entities', localization)
#         self.assertIn('actions', localization)

# if __name__ == '__main__':
#     unittest.main() 