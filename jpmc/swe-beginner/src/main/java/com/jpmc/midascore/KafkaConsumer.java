package com.jpmc.midascore;

import com.jpmc.midascore.foundation.Transaction;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.kafka.annotation.KafkaListener;
import org.springframework.stereotype.Component;

/**
 * Kafka consumer component that listens for transaction messages from Kafka topics.
 * 
 * This component receives Transaction objects from the configured Kafka topic and
 * processes them to update user balances (implementation in progress for Task 3).
 * 
 * The Kafka topic is configured via the {@code general.kafka-topic} property in
 * application.properties.
 */
@Component
public class KafkaConsumer {
    private static final Logger logger = LoggerFactory.getLogger(KafkaConsumer.class);

    /**
     * Handles incoming transaction messages from Kafka.
     * 
     * Currently logs received transactions. Transaction processing logic
     * (updating user balances) will be implemented in Task 3.
     * 
     * @param transaction The transaction message received from Kafka
     */
    @KafkaListener(topics = "${general.kafka-topic}")
    public void handleTransaction(Transaction transaction) {
        logger.info("Received transaction: {}", transaction);
        // TODO: Process the transaction (will be implemented in later tasks)
    }
}
