package com.example.demo.repo;

import com.example.demo.tables.discount;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.rest.core.annotation.RepositoryRestResource;

@RepositoryRestResource
public interface discountRepo extends JpaRepository<discount,Integer> {
}
