import serverless_sdk
sdk = serverless_sdk.SDK(
    org_id='mevillepereira10',
    application_name='senti-tweet',
    app_uid='gtYmj3btfgMMc2rC2s',
    org_uid='sq4T6cwPQK2Mh4R8t7',
    deployment_uid='6f072071-6130-4bb9-8161-ab3ea5086052',
    service_name='senti-tweet',
    should_log_meta=True,
    disable_aws_spans=False,
    disable_http_spans=False,
    stage_name='dev',
    plugin_version='3.6.6',
    disable_frameworks_instrumentation=False
)
handler_wrapper_kwargs = {'function_name': 'senti-tweet-dev-get-tweet', 'timeout': 6}
try:
    user_handler = serverless_sdk.get_user_handler('handler.main')
    handler = sdk.handler(user_handler, **handler_wrapper_kwargs)
except Exception as error:
    e = error
    def error_handler(event, context):
        raise e
    handler = sdk.handler(error_handler, **handler_wrapper_kwargs)
