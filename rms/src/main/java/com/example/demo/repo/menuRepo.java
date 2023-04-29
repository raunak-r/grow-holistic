package com.example.demo.repo;

import com.example.demo.tables.menu;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.rest.core.annotation.RepositoryRestResource;

@RepositoryRestResource
public interface menuRepo extends JpaRepository<menu,Integer> {
}