# ADR 001: Use AWS Lambda for EC2 Instance Shutdown
## Status
**Accepted**

## ContextS
Our system requires the capability to automatically shut down certain EC2 instances. This task is expected to be executed infrequently - approximately one or two times daily. The goal is to optimize resource usage and administrative overhead in managing this task.

## Decision
We have decided to use an AWS Lambda function to handle the shutdown of EC2 instances.

## Reasons:
- *Minimal Execution Time*: The task of shutting down an instance requires very little processing time, making it a good candidate for a serverless approach.
- *Resource Optimization*: Using a server- based approach would mean either having a dedicated instance for this task or adding this responsibility to an existing server. Both scenarios lead to suboptimal resource utilization, especially considering the infrequency of the task.
- *Reduced Administrative Overhead*: Managing a server, even one dedicated to a small task, requires system administration efforts including patching, monitoring, and security. A serverless approach offloads these responsibilities to AWS, thereby minimizing the tasks for system administrators.
## Alternatives Considered
### Dedicated EC2 Instance:

- *Pros*: Full control over the environment and can handle more complex tasks.
- *Cons*: Higher cost for continuous running; requires regular maintenance and monitoring.
### Scheduled Auto Scaling:

- *Pros*: Can be set up to automatically start and stop instances based on a schedule.
- *Cons*: Less flexibility in handling dynamic conditions; still incurs some costs during idle time.
### Container- based Solution (ECS/EKS):

- *Pros*: Good for complex orchestration tasks; integrates with other AWS services.
- *Cons*: Overkill for simple tasks; involves container management overhead.
### On- demand EC2 Instance with Startup/Shutdown Scripts:

- *Pros*: Runs only when needed; can be fully automated.
- *Cons*: Slower startup times; still requires some form of instance management.
## Consequences
By choosing AWS Lambda, we can efficiently manage the shutdown of EC2 instances in a cost- effective and low- maintenance manner. This decision aligns well with our goal of optimizing resource usage and minimizing administrative tasks. However, it also means we are bound by the constraints of Lambda, such as execution time limits and cold starts, which should be considered in the overall system design.

This ADR provides a clear rationale for the decision to use AWS Lambda, along with considering other alternatives and their trade- offs. It's important to revisit and update ADRs as the context and requirements of your project evolve over time.