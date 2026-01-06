package com.jpmc.midascore.component;

import com.jpmc.midascore.entity.UserRecord;
import com.jpmc.midascore.repository.UserRepository;
import org.springframework.stereotype.Component;

/**
 * Component that provides a conduit for database operations.
 * 
 * Wraps the UserRepository to provide a clean interface for persisting
 * UserRecord entities. This abstraction can be extended to include
 * additional database operations as needed.
 */
@Component
public class DatabaseConduit {
    private final UserRepository userRepository;

    public DatabaseConduit(UserRepository userRepository) {
        this.userRepository = userRepository;
    }

    /**
     * Saves a UserRecord entity to the database.
     * 
     * @param userRecord The user record to persist
     */
    public void save(UserRecord userRecord) {
        userRepository.save(userRecord);
    }

}
