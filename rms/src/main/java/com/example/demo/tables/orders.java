package com.example.demo.tables;

import jakarta.persistence.*;
import lombok.Data;

@Data
@Entity
@Table(name = "orders")
public class orders {
    @Id
    private int order_id;
    @OneToOne
    @JoinColumn(name = "item_id")
    private items item;
    @OneToOne
    @JoinColumn(name = "user_id",nullable = false)
    private users user;
}
