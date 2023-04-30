package com.example.demo.repo;

import com.example.demo.tables.res;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.rest.core.annotation.RepositoryRestResource;

@RepositoryRestResource
public interface resrepo extends JpaRepository<res,Integer> {
}
