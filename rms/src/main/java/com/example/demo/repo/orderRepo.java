package com.example.demo.repo;

import com.example.demo.tables.orders;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.rest.core.annotation.RepositoryRestResource;

@RepositoryRestResource
public interface orderRepo extends JpaRepository<orders,Integer> {
}
