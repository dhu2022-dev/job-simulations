package com.jpmc.midascore.foundation;

import com.fasterxml.jackson.annotation.JsonIgnoreProperties;

/**
 * Represents a user's account balance.
 * 
 * This class is used as the response model for balance query endpoints.
 * It will be used in Task 5 when implementing the REST API for balance queries.
 */
@JsonIgnoreProperties(ignoreUnknown = true)
public class Balance {
    private float amount;

    public Balance() {
    }

    public Balance(float amount) {
        this.amount = amount;
    }

    public float getAmount() {
        return amount;
    }

    public void setAmount(float amount) {
        this.amount = amount;
    }

    @Override
    public String toString() {
        return "Balance {amount=" + amount + "}";
    }
}