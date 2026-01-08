# JPMC Midas Core - Transaction Processing

**Status**: 🚧 In Progress

Transaction processing system built with Spring Boot and Apache Kafka for handling financial transactions and managing user balances.

This is a JPMC Software Engineering virtual experience simulation focused on building a transaction processing system.

## Project Overview

Midas Core is a transaction processing system that demonstrates event-driven architecture in a financial services context. The system:
- Receives financial transactions via Kafka message queues
- Processes transactions to update user account balances
- Provides REST API endpoints for querying user balances

**What This Demonstrates**: This project showcases backend development skills including event-driven architecture, message queue integration, database operations, and REST API design - all critical skills for building scalable financial systems.

**Note**: This project was part of a guided virtual experience program. The foundational architecture, entity models, and test infrastructure were provided. This documentation focuses on what was implemented and how to use it.

## Tech Stack

- **Java 17**
- **Spring Boot 3.2.5**
- **Apache Kafka** (with embedded Kafka for testing)
- **Spring Data JPA** with **H2** in-memory database
- **Maven** for build and dependency management
- **JUnit 5** for testing

## Task Status

**Project Status**: 🚧 In Progress

### ✅ Task 1: Application Setup
- **Status**: Completed
- **Objective**: Set up and verify the Spring Boot application boots successfully
- **Implementation**: Configured application and verified all dependencies are correctly set up

### ✅ Task 2: Interface with Transaction Data Feed
- **Status**: Completed
- **Objective**: Set up a system to interface with the transaction data feed using Kafka
- **Implementation**: 
  - Configured Kafka consumer to listen to the transaction data feed
  - Consumer receives and processes transaction messages from the Kafka topic
  - Handles JSON deserialization of Transaction objects

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
- **Objective**: Handle additional transaction processing scenarios

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

## Quick Start

After cloning this repository, you can get the project running in a few steps:

### Prerequisites

- **Java 17** or higher
- **Maven 3.6+**

### Build and Run

1. **Navigate to the project directory:**
```bash
cd jpmc/swe-beginner
```

2. **Build the project:**
```bash
mvn clean install
```
This downloads dependencies, compiles the code, runs all tests, and packages the application.

3. **Run the application:**
```bash
mvn spring-boot:run
```
The application starts on port 8080. The system uses embedded Kafka for testing, so no separate Kafka server is needed.

### Verify Everything Works

Run the test suite to verify all functionality:
```bash
mvn test
```

Or run individual task tests to see specific functionality:
```bash
mvn test -Dtest=TaskOneTests    # Verifies app bootstrapping
mvn test -Dtest=TaskFiveTests   # Tests the full transaction flow and balance API
```

## How It Works

### System Architecture

The system follows an event-driven architecture:

1. **Transaction Input**: Transactions are sent to Kafka topics as JSON messages
2. **Consumer Processing**: The `KafkaConsumer` receives transactions and processes them
3. **Balance Updates**: User balances are updated in the H2 database
4. **Balance Queries**: REST API endpoints allow querying current balances

### Key Workflow

```
Transaction → Kafka Topic → KafkaConsumer → Database Update → REST API Query
```

### Testing the System

The project includes tests for each task:

- **TaskOneTests**: Verifies the Spring Boot application starts correctly
- **TaskTwoTests**: Tests Kafka consumer setup - sends transactions to Kafka and verifies they're received
- **TaskThreeTests**: (In progress) Will test transaction processing and balance updates
- **TaskFourTests**: (Not started) Will test additional transaction scenarios
- **TaskFiveTests**: (Not started) Will test the complete flow including REST API balance queries

To test what's currently implemented:
```bash
mvn test -Dtest=TaskOneTests  # Verify app boots
mvn test -Dtest=TaskTwoTests  # Test Kafka consumer (Note: contains infinite loop for debugging)
```

Once Tasks 3-5 are complete, TaskFiveTests will demonstrate the full workflow from transaction ingestion to balance queries.

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

## What This Project Demonstrates

This simulation focuses on building core backend engineering skills:

1. **Event-Driven Architecture**: Integrating Kafka for asynchronous message processing
2. **Database Operations**: Working with JPA entities and repositories for data persistence
3. **Transaction Processing**: Building logic to process financial transactions and update balances
4. **REST API Development**: Creating endpoints for querying system state
5. **Integration Testing**: Setting up test infrastructure with embedded services

**Significance**: This project builds skills in production-ready backend systems with event-driven architecture, message queues, and database integration - directly applicable to financial services and trading systems.

## Skills Demonstrated

- Spring Boot application development
- Kafka integration for message processing
- Database integration with JPA/H2
- REST API development
- Integration testing with embedded services
- Component-based software design

---

*This project is part of the J.P. Morgan Chase Software Engineering Virtual Experience program.*
