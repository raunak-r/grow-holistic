package com.example.demo.tables;

import jakarta.persistence.Entity;
import jakarta.persistence.Id;
import jakarta.persistence.Table;
import lombok.Data;

@Data
@Entity
@Table(name="discount")
public class discount {
    @Id
    private int dis_id;
    private int dis_price;

    private int item_id;

}
