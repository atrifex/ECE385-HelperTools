<div id="table-of-contents">
<h2>Table of Contents</h2>
<div id="text-table-of-contents">
<ul>
<li><a href="#orgc93e559">1. Introduction</a></li>
<li><a href="#org4886a70">2. Documentation Format</a></li>
<li><a href="#orgef7b48e">3. PNG To Hex Converter</a>
<ul>
<li><a href="#orga83cec5">3.1. Motivation</a></li>
<li><a href="#org9defdad">3.2. Contents</a></li>
</ul>
</li>
</ul>
</div>
</div>


<a id="orgc93e559"></a>

# Introduction

-   The purpose of ECE 385 is to give you as sense of modular design and how to apply it to real systems to create complex structures in hardware.
-   This document will walk you through a toolkit developed to help you throughout your final project.
-   We want you to develop complex and interesting hardware and so we believe that it is more productive for you if some of the pure software components of the project are provided to you.
-   Currently, we only have PNG to Hex convert tool for you guys to use. In the future, we hope to develop more tools that will help you create increasing complex projects and show us what you can really do.


<a id="org4886a70"></a>

# Documentation Format

-   Documentation will be provided in subsection
-   You can see below the order in which a given tool will be described:
    1.  Motivation: tells you in what type of projects will this toolkit be useful
    2.  Contents: tells you the contents of a given toolkit
    3.  How To Use: will walk you through a step by step tutorial on how to use the toolkit


<a id="orgef7b48e"></a>

# PNG To Hex Converter


<a id="orga83cec5"></a>

## Motivation

-   This toolkit is mainly useful for those of you who are making a game or something that is graphically intensive.
-   **It allows you to be able to convert an image into a file format that can be used by on-chip memory, SRAM, and SDRAM**
    -   This way you can just focus on designing the hardware and not be worried about how to get an image into memory
-   Some of the python scripts within the toolkit allow you to also compress the size of an image through the use of KDTrees
    -   Since there is a limited amount of memory, this is useful when you have a lot of images or very large images.


<a id="org9defdad"></a>

## Contents

-   On-Chip: if you want to develop on chip memory, the scripts in this folder will be useful.
    -   Folders:
        1.  sprite-originals - You will put your original images in this folder
        2.  sprite-converted - This is where the output `.png` samples will be stored once you have run the scripts.
        3.  sprite-bytes - This is where the output `.txt` files will be stored that can be used by the on-chip memory
    -   Files:
        1)png<sub>to</sub><sub>3</sub><sub>txt.py</sub> -
-   SRAM: if you want to develop using SRAM, the files in this folder will be useful
    1.  SpriteBinaryGenerator.c
        -   This C file generates a `.ram` file.
        -   This .ram file can then be used by the control panel used in lab 6 to load the SRAM

