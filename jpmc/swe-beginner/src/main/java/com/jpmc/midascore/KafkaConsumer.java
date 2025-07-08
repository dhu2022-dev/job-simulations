package com.jpmc.midascore;

import com.jpmc.midascore.foundation.Transaction;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.kafka.annotation.KafkaListener;
import org.springframework.stereotype.Component;

@Component
public class KafkaConsumer {
    private static final Logger logger = LoggerFactory.getLogger(KafkaConsumer.class);

    @KafkaListener(topics = "${general.kafka-topic}")
    public void handleTransaction(Transaction transaction) {
        logger.info("Received transaction: {}", transaction);
        // TODO: Process the transaction (will be implemented in later tasks)
    }
}
