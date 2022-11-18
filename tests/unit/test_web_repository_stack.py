import aws_cdk as core
import aws_cdk.assertions as assertions

from web_repository.web_repository_stack import WebRepositoryStack

# example tests. To run these tests, uncomment this file along with the example
# resource in web_repository/web_repository_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = WebRepositoryStack(app, "web-repository")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
