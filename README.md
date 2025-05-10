# PandaDoc Integration Connector Setup Guide

This guide will help you set up and test your PandaDoc Integration Connector in Cursor.

## Project Structure

The Integration Connector follows this folder structure:

```
integration_connector/
├── __init__.py
├── config/
│   ├── config.yaml
│   └── localization.yaml
├── connector.py
├── capabilities/
│   ├── __init__.py
│   ├── info.py
│   ├── localization.py
│   ├── authorize.py
│   ├── entity.py
│   ├── object.py
│   ├── action.py
├── api/
│   ├── __init__.py
│   ├── client.py
├── utils/
│   ├── __init__.py
│   ├── helpers.py
tests/
├── __init__.py
├── test_connector.py
├── test_api_client.py
├── test_action.py
├── test_entity.py
├── test_object.py
├── test_info.py
├── test_localization.py
├── test_authorize.py
run_tests.py
```

## Setup Steps

1. **Create Project Directory Structure**:
   - Create a new directory for your project
   - Create the subdirectories as shown in the structure above

2. **Copy Files**:
   - Copy each file from the provided code into the appropriate location in your project structure
   - Ensure you maintain the correct file paths

3. **Install Required Dependencies**:
   ```bash
   pip install pyyaml requests
   ```

## Testing Your Integration Connector

There are two ways to test your integration connector:

### Method 1: Run All Tests with the Test Runner

1. Navigate to your project directory in the terminal
2. Run the test runner:
   ```bash
   python run_tests.py
   ```
3. This will discover and run all tests in the `tests` directory

### Method 2: Run Individual Test Files

You can also run individual test files if you want to focus on specific capabilities:

1. Navigate to your project directory in the terminal
2. Run a specific test file:
   ```bash
   python -m unittest tests.test_connector
   ```
   
   Or for a specific test case:
   ```bash
   python -m unittest tests.test_connector.TestIntegrationConnector.test_get_info
   ```

## Customizing Your Integration

To customize the integration for your specific external system:

1. **Edit config/config.yaml**:
   - Update metadata in the `info` section
   - Configure authentication method in the `authentication` section
   - Define your entities and actions

2. **Edit config/localization.yaml**:
   - Add translations for your entities and actions
   - Add descriptions for your integration

3. **Customize API Client**:
   - Modify `api/client.py` to communicate with your specific external system
   - Update the API endpoints and request formats

4. **Extend Capability Implementations**:
   - Modify the capability classes to handle your specific data structures
   - Add custom logic for handling entities, objects, and actions

## Next Steps

1. **Test with Real Data**:
   - Update the tests to use real test data from your external system
   - Create more comprehensive test scenarios

2. **Add Additional Capabilities**:
   - Implement additional capabilities as needed for your integration
   - Extend the connector to support custom functionality

3. **Documentation**:
   - Add more detailed documentation about your specific integration
   - Document the API endpoints and data structures

Happy integrating!