# JPMC Software Engineering - Beginner: Midas Core

Transaction processing system built with Spring Boot and Apache Kafka, implementing a microservices-style architecture for real-time transaction handling and balance management.

## Project Overview

Midas Core is a transaction processing system that receives financial transactions via Kafka, processes them to update user balances, and provides balance query capabilities. The system demonstrates event-driven architecture principles using Kafka for message queuing and Spring Boot for the application framework.

**Note**: This project was part of a guided virtual experience program. The foundational architecture, entity models, and test infrastructure were provided. This documentation focuses on the implementation work completed within that framework.

## Tech Stack

- **Java 17**
- **Spring Boot 3.2.5**
- **Apache Kafka** (with embedded Kafka for testing)
- **Spring Data JPA** with **H2** in-memory database
- **Maven** for build and dependency management
- **JUnit 5** for testing

## Task Status

### ✅ Task 1: Application Bootstrapping
- **Status**: Completed
- **Objective**: Verify Spring Boot application boots successfully
- **Implementation**: Confirmed application configuration and dependencies are correctly set up
- **Verification**: TaskOneTests passes, demonstrating successful application startup

### ✅ Task 2: Kafka Consumer Setup
- **Status**: Completed
- **Objective**: Configure Kafka consumer to receive and process transaction messages
- **Implementation**: 
  - Kafka consumer configured with JSON deserialization
  - Consumer listens to configured Kafka topic
  - Transaction messages are received and logged
  - Kafka producer utility created for test scenarios
- **Key Components**:
  - `KafkaConsumer`: Listens for Transaction objects from Kafka topics
  - `KafkaConfiguration`: Configures Kafka producer and consumer factories
  - `KafkaProducer`: Helper component for sending test transactions

### 🚧 Task 3: Transaction Processing (In Progress)
- **Status**: Currently working on
- **Objective**: Implement logic to process transactions and update user balances
- **Current State**: 
  - Kafka consumer receives transactions (Task 2)
  - Transaction processing logic needs to be implemented in `KafkaConsumer.handleTransaction()`
  - User entity and repository infrastructure ready (`UserRecord`, `UserRepository`)
  - Database conduit component available for persistence operations

### ⏳ Task 4: Additional Transaction Scenarios
- **Status**: Not started
- **Objective**: Handle additional transaction processing scenarios and edge cases

### ⏳ Task 5: REST API for Balance Queries
- **Status**: Not started
- **Objective**: Create REST endpoint to query user balances
- **Note**: Test infrastructure (`BalanceQuerier`) expects endpoint at `http://localhost:33400/balance?userId={id}`

## Key Implementation Highlights

### Completed Components

- **Kafka Integration**
  - Consumer factory with JSON deserialization
  - Producer factory with JSON serialization
  - Embedded Kafka setup for testing
  - Topic configuration via `application.properties`

- **Database Layer**
  - `UserRecord` entity with JPA annotations
  - `UserRepository` interface extending CrudRepository
  - `DatabaseConduit` component for persistence operations
  - H2 in-memory database configuration

- **Transaction Model**
  - `Transaction` class with sender, recipient, and amount
  - JSON serialization/deserialization support
  - Used for Kafka message payloads

- **Test Infrastructure**
  - Embedded Kafka for integration testing
  - Test utilities: `FileLoader`, `KafkaProducer`, `UserPopulator`
  - Task-specific test classes (TaskOneTests through TaskFiveTests)

### Project Structure

```
src/
├── main/
│   ├── java/com/jpmc/midascore/
│   │   ├── MidasCoreApplication.java       # Spring Boot entry point
│   │   ├── KafkaConsumer.java              # Kafka message consumer (Task 2-3)
│   │   ├── component/
│   │   │   └── DatabaseConduit.java        # Database operations wrapper
│   │   ├── entity/
│   │   │   └── UserRecord.java             # JPA entity for users
│   │   ├── foundation/
│   │   │   ├── Transaction.java            # Transaction model
│   │   │   ├── TransactionRecord.java      # (To be implemented)
│   │   │   └── Balance.java                # Balance response model
│   │   └── repository/
│   │       └── UserRepository.java         # Spring Data repository
│   └── resources/
│       └── application.properties          # Kafka topic configuration
└── test/
    └── java/com/jpmc/midascore/
        ├── KafkaConfiguration.java         # Kafka test configuration
        ├── KafkaProducer.java              # Test producer utility
        ├── UserPopulator.java              # Test data population
        ├── FileLoader.java                 # Test file loading utility
        ├── BalanceQuerier.java             # Balance query utility (for Task 5)
        └── Task*Tests.java                 # Task verification tests
```

## Setup Instructions

### Prerequisites

- **Java 17** or higher
- **Maven 3.6+**
- Optional: IDE with Java support (IntelliJ IDEA, Eclipse, VS Code)

### Building the Project

```bash
cd jpmc/swe-beginner
mvn clean install
```

This will:
- Download all dependencies
- Compile the source code
- Run all tests
- Package the application

### Running Tests

Run all tests:
```bash
mvn test
```

Run a specific task test:
```bash
mvn test -Dtest=TaskOneTests
mvn test -Dtest=TaskTwoTests
# etc.
```

### Running the Application

```bash
mvn spring-boot:run
```

The application will start on the default Spring Boot port (8080). Note that for tasks requiring Kafka, the embedded Kafka in tests handles this automatically.

## Demo Instructions

### Task 1 Demo
```bash
mvn test -Dtest=TaskOneTests
```
Verify the application boots successfully and check the console output for the completion message.

### Task 2 Demo
```bash
mvn test -Dtest=TaskTwoTests
```
The test will send transactions to Kafka. Use a debugger to observe the `KafkaConsumer.handleTransaction()` method receiving and logging transactions. Note: This test contains an infinite loop for debugging purposes.

### Task 3 Demo (In Progress)
When Task 3 is complete, run:
```bash
mvn test -Dtest=TaskThreeTests
```
This will process transactions and update user balances. Use the debugger to verify balance updates in the database.

## Configuration

### Kafka Configuration

The Kafka topic is configured in `src/main/resources/application.properties`:
```properties
general.kafka-topic=test-topic
```

For testing, embedded Kafka is automatically configured in `KafkaConfiguration.java` with:
- Bootstrap server: `localhost:9092`
- Consumer group: `midas-core-group`
- JSON serialization/deserialization for Transaction objects

## Next Steps

1. **Complete Task 3**: Implement transaction processing logic in `KafkaConsumer.handleTransaction()`
   - Retrieve sender and recipient UserRecord entities
   - Update balances (debit sender, credit recipient)
   - Persist changes using DatabaseConduit
   - Handle edge cases (insufficient funds, invalid users, etc.)

2. **Task 4**: Add additional transaction scenarios and validation

3. **Task 5**: Create REST controller with `/balance` endpoint
   - Controller should query UserRepository
   - Return Balance object with user's current balance
   - Ensure endpoint matches expected URL pattern for tests

## Skills Demonstrated

- Event-driven architecture with Kafka
- Spring Boot application development
- Database integration with JPA/H2
- Microservices communication patterns
- Integration testing with embedded services
- Clean code organization and component design

---

*This project is part of the J.P. Morgan Chase Software Engineering Virtual Experience program.*
