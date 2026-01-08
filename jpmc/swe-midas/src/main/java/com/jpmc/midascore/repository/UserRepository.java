package com.jpmc.midascore.repository;

import com.jpmc.midascore.entity.UserRecord;
import org.springframework.data.repository.CrudRepository;

/**
 * Repository interface for UserRecord entities.
 * 
 * Extends Spring Data's CrudRepository to provide standard CRUD operations
 * for UserRecord entities. Additional query methods can be added as needed.
 */
public interface UserRepository extends CrudRepository<UserRecord, Long> {
    /**
     * Finds a user by their ID.
     * 
     * @param id The user ID to search for
     * @return The UserRecord with the specified ID, or null if not found
     */
    UserRecord findById(long id);
}
