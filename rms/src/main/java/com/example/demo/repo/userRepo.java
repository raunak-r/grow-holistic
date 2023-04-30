package com.example.demo.repo;

import com.example.demo.tables.users;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.rest.core.annotation.RepositoryRestResource;

@RepositoryRestResource
public interface userRepo extends JpaRepository<users,Integer> {
}
