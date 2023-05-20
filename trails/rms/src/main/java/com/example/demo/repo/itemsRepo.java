package com.example.demo.repo;

import com.example.demo.tables.items;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.rest.core.annotation.RepositoryRestResource;

@RepositoryRestResource
public interface itemsRepo extends JpaRepository<items,Integer> {
}
