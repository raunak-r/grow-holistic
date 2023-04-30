package com.example.demo.tables;

import jakarta.persistence.Entity;
import jakarta.persistence.Id;
import jakarta.persistence.Table;
import lombok.Data;

@Data
@Entity
@Table(name = "orders")
public class orders {
    @Id
    private int order_id;

    private int item_id;

    private int res_id;

    private int user_id;
}
